---
name: learning-loop.workflow
owner_tier: cross-cutting
owner_vertical: cross-vertical
primary_agent: recursive-optimizer
playbook_source: §13.5 (calibration), §14.3 (data governance), CLAUDE.md Phase 6
skills: [orchestration/weekly-tick, performance-reporter, hitl-request]
status: active
phase: 2
---

# Learning Loop Workflow

Monthly recursive optimizer pass: read ledger-events → propose SOP / rubric / threshold updates → HITL approval → apply.

## Trigger
- Monthly first business day, 10:00 client-local.
- On-demand after major incident or quarterly review.

## Actors
- **Owner**: `recursive-optimizer` agent (cross-cutting).
- **Approvers**: CMO Orchestrator + relevant Department Head(s) per change scope.
- **Reviewer**: human operator (final HITL).

## Inputs
- 30 days of `clients/{id}/ledger-events/`.
- Last 4 weekly digests + KPI snapshots.
- Outcomes vs OKR targets.
- Failure / refusal events.
- Rubric scores trending below 9 across artifacts.

## Steps
1. **Aggregate** events into pattern buckets: refusals, HITL escalations, rubric near-misses, stop-loss actions, attribution discrepancies, deliverability incidents, content underperformers.
2. **Diagnose**: identify systemic patterns (vs one-off). E.g. "60% of paid HITLs are spend-spike on launches >$1k — threshold may be too low."
3. **Propose**: draft change-list — SOP edits, rubric criterion weight changes, threshold tweaks, new refusal triggers, connector budget changes. Each proposal includes evidence link to events + expected effect + rollback plan.
4. **Rubric grade**: proposals graded as `agent.skill.yaml`-style outputs ≥8.
5. **HITL**: package via `skills/orchestration/hitl-request.skill.md`. CMO approves cross-cutting changes; vertical Heads approve vertical-scoped ones.
6. **Apply**: on approval, the change is committed to the relevant SOP / rubric / config file with a `learning-loop:{yyyy-mm}` tag in the commit message; original file diff captured in ledger.
7. **Re-baseline**: new rubric / threshold becomes the gate for the next cycle. Schedule a 60-day post-change review event.

## Outputs
- Change-list document in `clients/{id}/memory/long-term/learning-loop-{yyyy-mm}.md`.
- Approved changes applied to `rubrics/`, `skills/`, `04-workflows/`, vertical READMEs as scoped.
- Post-change review scheduled in 60 days.

## Rubric
`rubrics/agent.yaml` for the optimizer's run; `rubrics/hitl-request.yaml` for the change package.

## HITL Gates
- Any rubric pass-bar change → HITL CMO + originating vertical Head.
- Refusal-trigger removal → HITL CMO + Legal review where applicable.
- Threshold loosening that increases blast radius (spend, audience, brand) → HITL CMO.
- Tightening that creates >20% additional HITL volume → HITL Head of Marketing.

## Failure Modes
- Sample size too small (<10 events of a kind) → recommend "monitor more cycles," don't change.
- Recommendation contradicts playbook → refuse; escalate as a playbook-amendment proposal (separate path).
- Drift detected (post-change KPI worsens) → auto-rollback within next loop iteration.

## Ledger Events Emitted
`learning_loop.started` · `learning_loop.patterns.detected` · `learning_loop.proposals.drafted` · `learning_loop.hitl.requested` · `learning_loop.applied.{rubric|sop|threshold}` · `learning_loop.rollback.{reason}` · `learning_loop.review.scheduled`.
