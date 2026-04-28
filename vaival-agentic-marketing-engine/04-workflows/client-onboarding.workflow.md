---
name: client-onboarding.workflow
owner_tier: orchestrator
owner_vertical: cross-vertical
primary_agent: cmo-orchestrator
playbook_source: §2 (Vision/Mission/Purpose), §3 (Department Structure), §6 (Goals & KPIs)
skills: [orchestration/onboarding, orchestration/goal-decomposer, orchestration/weekly-tick, orchestration/hitl-request]
status: active
phase: 2
---

# Client Onboarding Workflow

End-to-end zero-knowledge onboarding for a new client. Maps to `skills/orchestration/onboarding.skill.md`.

## Trigger
- Operator command: `New client: {id}. Goal: {SMART goal}.`
- OR cold scaffold: `clients/{id}/` cloned from `_template/` with `ledger.md` status `pending-onboarding`.

## Actors
- **Owner**: CMO Orchestrator (Tier 1).
- **HITL**: Human operator (12 leverage Qs).
- **Downstream**: 8 Department Heads.

## Inputs
- Client identifier (`{id}`).
- High-level SMART goal (timeframe + outcome).
- Operator availability for 12-question intake.

## Steps
1. **Scaffold**: copy `clients/_template/` → `clients/{id}/`. Stamp `ledger.md` frontmatter with `status: pending-onboarding`, `created_at`, `operator`.
2. **Leverage Q&A** (12 questions): invoke `skills/orchestration/onboarding.skill.md`. Capture company, goal, current state, constraints, ICP seed, competitors, cadence, secrets pointer, open questions. NO fabrication — unknowns marked.
3. **Ledger write**: persist answers into `ledger.md` §1–§9. Append event `onboarding.completed` to `ledger-events/`.
4. **Goal decompose**: invoke `skills/orchestration/goal-decomposer.skill.md`. Produce: 4 NSMs, quarterly OKRs (per vertical), 90-day plan, vertical assignments. Write to `clients/{id}/okrs/` and `clients/{id}/plan.md`.
5. **Rubric gates**: ledger ≥8 (`rubrics/client-ledger.yaml`), OKRs ≥8 (`rubrics/okr.yaml`), plan ≥8 (`rubrics/90-day-plan.yaml`). Below 8 → iterate, do not proceed to Step 6.
6. **Activation digest**: produce first weekly digest (per CMO digest format) covering NSM baselines, OKR scoreboard, top 7-day actions per Head, HITL items.
7. **Secrets bootstrap**: confirm `secrets.pointer.md` complete; if any vault path empty, trigger `secrets-vault-setup.workflow.md`. Set `ledger.status: active` only after secrets are in vault, not in cleartext.

## Outputs
- `clients/{id}/ledger.md` (rubric-graded ≥8).
- `clients/{id}/okrs/{yyyy-qN}.md` (rubric-graded ≥8).
- `clients/{id}/plan.md` (rubric-graded ≥8).
- `clients/{id}/secrets.pointer.md` (no raw creds).
- First weekly digest in `clients/{id}/feeds/`.
- Ledger events: `onboarding.completed`, `okrs.created`, `plan.created`, `digest.delivered`.

## Rubrics
- `rubrics/client-ledger.yaml`, `rubrics/okr.yaml`, `rubrics/90-day-plan.yaml`, `rubrics/weekly-digest.yaml`.

## HITL Gates
- 12-question intake itself (operator-driven).
- Ambition recalibration if any KR confidence is <30% or >85%.
- Brand-voice / messaging conflicts surfaced during intake.
- Secrets migration completion before `status: active`.

## Failure Modes
- Operator skips questions → workflow refuses to write OKRs; flags missing context.
- Source-of-truth conflicts (e.g. CRM says one ICP, operator says another) → escalate as HITL.
- Vault unavailable → block status flip, raise HITL.

## Ledger Events Emitted
`client.scaffolded` · `onboarding.qna.completed` · `ledger.written` · `nsms.set` · `okrs.created` · `plan.created` · `secrets.pointer.linked` · `activation.digest.delivered` · `client.status.active`.
