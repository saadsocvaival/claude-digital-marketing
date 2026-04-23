---
name: approval-matrix
owner_tier: governance
status: draft
phase: 1
---

# Approval Matrix

Canonical table of action types × required approvers × thresholds. Any action matching a row here MUST trigger the corresponding gate in `11-approvals/gates/` and be recorded in the execution ledger with `approval_status` fields populated.

## Matrix

| Action Type | Threshold / Condition | Required Approver(s) | Gate | SLA |
|---|---|---|---|---|
| Paid-media spend commitment (single campaign) | > $5,000 | Founder | budget-threshold | 24h |
| Paid-media spend commitment (aggregate monthly) | > $20,000 | Founder | budget-threshold | 24h |
| Paid-media spend commitment (single campaign) | $1,000 – $5,000 | CMO Orchestrator | budget-threshold | 12h |
| Paid-media spend commitment (single campaign) | < $1,000 | Paid Media Manager (self-approve, logged) | — | — |
| External publishing — paid ads (new creative) | Any | CMO + Compliance | external-publishing | 24h |
| External publishing — owned blog / longform | Any | Content Marketing Manager + QA pass | external-publishing | 12h |
| External publishing — guest post / PR / syndication | Any | CMO + Compliance | external-publishing | 48h |
| External publishing — organic social post | Standard cadence | Social Media Manager (self-approve, QA pass) | — | — |
| External publishing — organic social post | Reactive / crisis / topical | CMO | external-publishing | 4h |
| External publishing — email broadcast > 10k recipients | Any | CRM/Email Manager + Compliance | external-publishing | 12h |
| Strategy change — ICP modification | Any | Founder | strategy-change | 72h |
| Strategy change — positioning / messaging pillars | Any | Founder | strategy-change | 72h |
| Strategy change — channel-mix reallocation > 20% | Any | Founder | strategy-change | 48h |
| Strategy change — pricing narrative | Any | Founder | strategy-change | 72h |
| New credential onboarding — marketing platform | Any | Founder + Compliance | new-credential | 48h |
| New credential onboarding — data source / analytics | Any | Founder + Compliance | new-credential | 48h |
| New credential onboarding — CRM or email provider | Any | Founder + Compliance | new-credential | 48h |
| Production deploy — website | Any | Web Lead + QA pass; CMO notified | external-publishing | 12h |
| Production deploy — schema/tracking change | Any | Marketing Ops Manager + Web Lead | external-publishing | 12h |
| Experiment launch (A/B test) | Standard traffic split | Originating Lead + QA | — | — |
| Experiment launch (A/B test) | > 50% traffic or pricing-related | CMO | strategy-change | 24h |

## Rules

1. **Default deny.** If an action type is not listed here, it is out-of-scope for autonomous execution and MUST escalate to CMO for classification.
2. **Thresholds are inclusive at the lower bound.** `> $5,000` means strictly above; `$1,000 – $5,000` is inclusive.
3. **Aggregate windows are rolling.** Monthly spend is evaluated on a rolling 30-day window, not calendar month.
4. **All approvals are logged** with approver identity, timestamp, decision_id, and link to the triggering event.
5. **Rejection is terminal for that request.** A rejected item must be re-proposed as a new decision_id; it cannot be silently re-submitted.
6. **SLA breach escalates upward.** If an approver does not respond within SLA, the request escalates to the next tier automatically (CMO → Founder) and is flagged in the human-review queue.
