---
name: decision-boundary-layer
owner_tier: tier-2
status: draft
phase: 1
---

# Decision-Boundary Layer

A thin, orchestrator-enforced policy layer whose sole purpose is to prevent runaway, circular, or unbounded agent activity. It is not a decision-maker — it is a gatekeeper sitting in front of every delegation and tool call.

## Rules (Invariant)

1. **No specialist-to-specialist calls.** A Tier-4 specialist MAY NOT invoke another specialist. If a specialist needs work outside its scope, it returns control to its Lead.
2. **No lead-to-lead direct calls.** Tier-3 Vertical Leads MAY NOT directly invoke peers. All cross-vertical coordination MUST route through the CMO Orchestrator.
3. **CMO is the only cross-vertical delegator.** Fan-out across verticals originates at Tier-2 and nowhere else.
4. **Max delegation depth = 4.** Founder (1) → CMO (2) → Lead (3) → Specialist (4). Any attempt to create a depth-5 chain is refused and ledger-logged as `refusal:depth-cap`.
5. **Max fan-out per node = 12.** A single delegating agent may not emit more than 12 concurrent child tasks in one decision. Larger batches must be decomposed into phased waves.
6. **Circular-dependency detection.** The Orchestrator maintains a DAG of live task dependencies. Any proposed edge that would close a cycle is refused.
7. **Cross-cutting agents are invoked, not delegated to.** Resource Discovery, Feasibility Validator, QA, Compliance, and Recursive Optimizer are consulted — they do not become parents in the delegation tree and do not count toward depth.

## Responsibilities

- **Orchestrator (enforcer).** Intercepts every delegation request. Validates against rules 1–7 before the ledger event is written. Refusals are terminal for the attempted call and are logged with reason code.
- **Leads (declarants).** When receiving a task, declare `expected_subtasks` and `expected_depth`. If actual execution would exceed the declared envelope, return to CMO for re-decomposition instead of proceeding.
- **Specialists (silent enforcers).** Reject any incoming invocation whose `actor_tier` is not `tier-3` (own Lead) or `tier-2` (CMO, rare pass-through for audit).

## Circular-Dependency Detection

The Orchestrator holds a live dependency graph `G` keyed by `decision_id`. Before writing a new delegation edge `A → B`, it runs a DFS from `B`; if `A` is reachable, the edge is refused. All decisions are included, including those pending approval, so pre-approval queuing cannot be used to hide a cycle.

## Timeout & Fallback

- **Per-task timeout** is declared at delegation time (`deadline` field). Default: 60 min for specialists, 4h for Leads, 24h for CMO-level decompositions.
- **On timeout**: the Orchestrator marks the task `timed_out`, cancels any still-running children, and invokes the fallback path declared on the parent decision. Fallback options, in order of preference: (a) retry with degraded scope, (b) escalate to next tier, (c) refuse upward with partial-results report.
- **No silent retry.** Every retry is a new `event_id` with `retry_of` pointing to the original. Retry counts are bounded at 3 per logical task.

## Observable Signals

The decision-boundary layer emits these ledger event types for monitoring:

- `refusal:depth-cap`, `refusal:fan-out-cap`, `refusal:cycle`, `refusal:cross-tier`, `refusal:unknown-credential`
- `timeout:specialist`, `timeout:lead`, `timeout:orchestrator`
- `fallback:degraded`, `fallback:escalated`, `fallback:partial`

Sustained refusals of any one type are a strong signal for the Recursive Optimizer to adjust SOPs or delegation templates.
