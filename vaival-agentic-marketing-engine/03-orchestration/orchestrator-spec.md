---
name: orchestrator-spec
owner_tier: tier-2
status: draft
phase: 1
---

# CMO Orchestrator — Specification

The CMO Orchestrator is the single point of cross-vertical coordination. It is the only agent permitted to fan work out across verticals, the only agent that writes top-level entries to the execution ledger, and the enforcer of the decision-boundary layer.

## Inputs

- **Founder directive** — structured strategic input (ICP, priorities, budget envelope, timeframe, success criteria).
- **Feedback-loop signals** — emitted by the Recursive Optimizer (`13-feedback-loop/`): performance deltas, MQL-quality trends, attribution shifts, SOP updates, founder feedback.
- **Vertical Lead reports** — status + escalations from the 7 Tier-3 leads.
- **Cross-cutting agent findings** — Feasibility pre-flight results, QA validations, Compliance reviews, Resource Discovery readiness signals.
- **Approval-queue state** — pending/approved/rejected/needs-revision events from `11-approvals/`.

## Outputs

- **Delegated tasks** to Vertical Leads, each with: `task_id`, `parent_decision_id`, `scope`, `success_criteria`, `budget_envelope`, `deadline`, `required_schema`, `gates_applicable`.
- **Ledger events** for every decision (decomposition, delegation, gate trigger, rejection, re-plan).
- **Escalations upward** to Founder when an approval gate or strategy-change is triggered.
- **Policy updates** pushed to Leads when the Recursive Optimizer ships a framework change.

## Delegation Rules

1. **Only the CMO delegates cross-vertical.** A Lead that needs work from another vertical MUST request it from the CMO; direct lead-to-lead delegation is refused.
2. **Leads delegate within their vertical.** SEO Manager → SEO specialists, etc. No Lead can invoke a specialist outside its own vertical.
3. **Specialists do not delegate.** They either execute or escalate.
4. **Max delegation depth = 4.** Founder → CMO → Lead → Specialist. Any chain attempting depth 5 is refused.
5. **Every delegation is ledger-logged** with `parent_decision_id` set to the delegating agent's decision.

## Escalation Triggers

The Orchestrator MUST escalate to Founder when:

- An approval-matrix row requires Founder sign-off (see `00-governance/approval-matrix.md`).
- Two or more Leads return conflicting plans for the same objective and conflict cannot be resolved within defined policy.
- Feasibility Validator returns `fail` on a directive Founder issued (directive is not currently executable).
- Recursive Optimizer proposes a strategy-change.

The Orchestrator MUST NOT escalate trivial questions, timeline slips within envelope, or issues resolvable by Leads.

## Refusal Conditions

The Orchestrator MUST refuse (and log refusal) when:

- Delegation depth cap is exceeded.
- A circular dependency is detected in the proposed DAG of tasks.
- The request lacks a valid `parent_decision_id` (other than a Founder directive, which is the root).
- Compliance has flagged the action in a prior review and no superseding approval exists.
- Resource Discovery reports that a required credential is unavailable or unapproved.

## Audit Fields (Per Decision)

Each Orchestrator decision logs the following to the execution ledger:

- `event_id`, `timestamp`, `actor_agent = cmo-orchestrator`, `actor_tier = tier-2`
- `parent_decision_id`, `triggering_input` (pointer to Founder directive, signal, or lead report)
- `decision_framework_used` (pointer to `00-governance/decision-frameworks/…`)
- `confidence_score` (0.0–1.0)
- `required_approvals` + `approval_status`
- `output_ref` (delegation task IDs emitted)
- `expected_business_impact` (structured)
- `rollback_path` (how to undo if downstream fails)
- `audit_hash` (chained with previous event)
