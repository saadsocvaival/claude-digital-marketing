---
name: approval-workflow
owner_tier: governance
status: draft
phase: 1
---

# Approval Workflow

State machine and routing for every approval gate in the system. Any ledger event whose `required_approvals` is non-empty enters this workflow; nothing downstream of it executes until the workflow reaches a terminal state.

## State Machine

```
                    ┌─────────┐
     enqueue ──────▶│ pending │
                    └────┬────┘
                         │ reviewer picks up
                         ▼
                  ┌──────────────┐
                  │ under-review │
                  └──┬───┬───┬───┘
          approve    │   │   │    request-changes
     ┌──────────────┘    │   └─────────────┐
     ▼                   │ reject          ▼
 ┌──────────┐            ▼           ┌──────────────────┐
 │ approved │       ┌──────────┐     │ needs-revision   │
 └──────────┘       │ rejected │     └────────┬─────────┘
   (terminal)       └──────────┘              │ requester resubmits as new event
                     (terminal)               ▼
                                         (new decision_id,
                                          workflow restarts)
```

Terminal states: `approved`, `rejected`. `needs-revision` is not terminal for the business intent, but the specific `decision_id` does not proceed — a new decision_id must be submitted.

## Queue Routing

| Gate | Queue | Primary Reviewer | Secondary (SLA breach) |
|---|---|---|---|
| budget-threshold ($1k–$5k) | cmo-review | CMO Orchestrator | Founder |
| budget-threshold (> $5k) | founder-review | Founder | — (blocks until reviewed) |
| external-publishing (owned) | lead-review | Originating Vertical Lead | CMO |
| external-publishing (paid / PR / syndication) | cmo+compliance | CMO + Compliance (both required) | Founder |
| strategy-change | founder-review | Founder | — |
| new-credential | founder+compliance | Founder + Compliance (both required) | — |

"Both required" means the request is `approved` only when both reviewers approve; any single rejection → `rejected`.

## SLA Per Gate

| Gate | SLA | Breach Behavior |
|---|---|---|
| budget-threshold ($1k–$5k) | 12h | Auto-escalate to Founder; flag in human-review queue |
| budget-threshold (> $5k) | 24h | Flag in human-review queue; notify Founder via `16-human-review/` channel |
| external-publishing (owned) | 12h | Auto-escalate to CMO |
| external-publishing (paid / PR) | 24h | Flag in human-review queue |
| external-publishing (crisis / reactive social) | 4h | Page CMO via priority channel |
| strategy-change | 72h | Flag in human-review queue; request dropped if unaddressed at 7d |
| new-credential | 48h | Flag in human-review queue |

## Escalation If Unaddressed

The workflow runs a continuous SLA monitor. On breach:

1. Add a ledger event `escalation:sla-breach` linking to the original `decision_id`.
2. Notify the secondary reviewer per the routing table.
3. Mark the queue item `priority: high`.
4. If no action after 2× SLA, notify Founder regardless of original routing.
5. If no action after 5× SLA on non-strategy gates, the request auto-transitions to `rejected` with reason `sla-timeout` and must be re-proposed.

## Human-In-The-Loop Interface

All queue state is exposed through the review interface defined in `16-human-review/review-interface-spec.md`. Reviewers see: the originating directive chain (via ledger lineage), the proposed action, feasibility-check results, compliance findings, expected business impact, and the rollback path. Reviewers act via an affirmative decision (approve / reject / request-changes with structured feedback) — passive silence is not an approval and breaches SLA.

## Invariants

- An event with pending/unapproved gates MUST NOT execute downstream.
- An approval decision is itself a ledger event with full audit fields.
- Re-proposing a rejected request requires a new `decision_id`; the prior rejection remains in the ledger.
- Approvals are scoped to a single `decision_id` — they do not generalize to future similar requests.
