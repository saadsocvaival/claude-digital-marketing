# CostSage — Client README

> Brand: **CostSage** · Domain: **costsage.ai** · CMS: **WordPress** · Vertical: AI cost optimization SaaS · Status: **pending-onboarding**.

This client was scaffolded from `clients/_template/` and has not yet completed onboarding. No live tool calls or autonomous activity is enabled until onboarding + secrets-vault setup are complete.

## Onboarding Checklist
- [ ] Run `vaival-agentic-marketing-engine/04-workflows/client-onboarding.workflow.md` (12 leverage Qs).
- [ ] Populate `ledger.md` §1–§9 from intake.
- [ ] Decompose goal: 4 NSMs + quarterly OKRs + 90-day plan via `skills/orchestration/goal-decomposer.skill.md`.
- [ ] Run `vaival-agentic-marketing-engine/04-workflows/secrets-vault-setup.workflow.md` — migrate cleartext sheet to vault, revoke source.
- [ ] Confirm `secrets.pointer.md` rows all have non-placeholder vault paths.
- [ ] Verify per-platform read access (least-privilege) for each connector.
- [ ] Rubric-grade `ledger.md` ≥8 (`rubrics/client-ledger.yaml`).
- [ ] Rubric-grade OKRs ≥8 (`rubrics/okr.yaml`).
- [ ] Rubric-grade 90-day plan ≥8 (`rubrics/90-day-plan.yaml`).
- [ ] Produce activation digest; rubric-grade ≥8 (`rubrics/weekly-digest.yaml`).
- [ ] Flip `ledger.md` `status: active` once all of the above pass.

## Key Links
- Onboarding workflow: `../../vaival-agentic-marketing-engine/04-workflows/client-onboarding.workflow.md`
- Onboarding skill: `../../skills/orchestration/onboarding.skill.md`
- Goal decomposer: `../../skills/orchestration/goal-decomposer.skill.md`
- Secrets-vault workflow: `../../vaival-agentic-marketing-engine/04-workflows/secrets-vault-setup.workflow.md`
- KPI snapshot pipeline: `../../vaival-agentic-marketing-engine/04-workflows/kpi-snapshot-pipeline.workflow.md`
- Digest delivery: `../../vaival-agentic-marketing-engine/04-workflows/digest-delivery.workflow.md`
- Daily stop-loss: `../../vaival-agentic-marketing-engine/04-workflows/daily-stop-loss.workflow.md`
- Learning loop: `../../vaival-agentic-marketing-engine/04-workflows/learning-loop.workflow.md`
- WordPress App Password sub-spec: `../../vaival-agentic-marketing-engine/06-connectors/web-dev/wordpress-application-password.connector.md`

## Directory Layout
```
costsage/
├── README.md            (this file)
├── ledger.md            (status: pending-onboarding)
├── secrets.pointer.md   (vault paths only — NO raw creds)
├── okrs/                (per-quarter OKRs; .gitkeep)
├── feeds/               (weekly KPI snapshots; .gitkeep)
├── memory/
│   ├── long-term/       (.gitkeep)
│   └── short-term/      (.gitkeep)
└── ledger-events/       (append-only events; .gitkeep)
```

## Notes for Operator
- The `ledger.md` carries known facts (brand, domain, CMS) and inferred ICP (AI cost optimization SaaS). All other fields are TBD until intake.
- Do NOT paste credentials into any file in this directory. Use the secrets-vault workflow.
- HITL is required before any spend, brand-departing claim, legal-sensitive copy, or external publishing.
