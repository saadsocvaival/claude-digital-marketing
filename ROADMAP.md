# Roadmap — Autonomous Digital Marketing OS

This PR delivers **Stages 0–2**. Stages 3–5 require credentials, time, and/or external review.

## ✅ Stage 0 — Foundation (this PR)
- Skill library dedup (146 canonical skills).
- Rubric library (19 YAMLs, pass bar 8).
- `CLAUDE.md` runtime entrypoint + `.claude/` wiring.
- 8 Department Head agents.
- 4 orchestration skills (onboarding / goal-decomposer / weekly-tick / hitl-request).
- 15 artifact templates.
- Multi-tenant `clients/_template/` scaffold.
- Security hygiene: `.gitignore`, pre-commit secret scan, SECURITY.md.

## ✅ Stage 1 — Dogfood Fixture (this PR)
- `clients/_fixture_devtools_saas/` populated end-to-end (~40 rubric-graded artifacts).
- Every strategic artifact scores ≥94/100 on its rubric.
- Orchestrator dry-run supported: "Achieve 50% ARR growth for the fixture client" traces through ledger → plan → OKRs → per-Head action lists.

## ✅ Stage 2 — Eval Harness Skeleton (this PR)
- 10 golden eval cases covering top skills (ICP, positioning, messaging, keyword/SEO brief, copywriting, email sequence, content brief, LP, competitor battlecard, paid-ads).
- Each eval: input fixture + expected-shape output + rubric gate (≥8).
- `run-evals.md` explains how to execute.

## ✅ Stage 2.5 — SME-Hardened v1.1 (this PR)
Senior SME adversarial review flagged 17 methodology gaps in v1.0. v1.1 addresses 15 of 17 as authored artifacts (2 blocked by need for real pipeline data — see Stage 3.5).

**Delivered:**
- Metric-tree methodology (NSM → L1 input metrics → L2 levers) in rewritten `goal-decomposer`.
- Triangulated attribution (MTA + MMM + incrementality with decision hierarchy) in `attribution-model.md` + new `incrementality-test.skill.md` with geo-holdout, ghost-ad, synthetic-control designs.
- Two-phase lead scoring: Phase-1 fit-only, Phase-2 composite gated on n≥2000 closed-won + HITL.
- Motion-based overlay: `motion-acquisition`, `motion-activation`, `motion-retention` agents owning outcomes across Heads.
- New `head-of-revops` agent (pipeline hygiene, funnel diagnostic, SLA, CRM data quality).
- Adversarial-critic pattern: separate critic agent reads artifact + rubric cold; ship gate `min(self, critic) ≥ 8`.
- Real GEO/AEO methodology: `aeo-citation-audit` + `answer-engine-brief` skills with BMI-LLM metric, entity grounding, canonical answer blocks, schema.org markup.
- New skills: `distribution-map`, `experiment-program`, `creative-ops`, `unit-economics`, `rubric-calibration`.
- New templates: category-design, narrative-thesis, creative-test-matrix, pricing-page-brief, plg-conversion-audit, lifecycle-map, behavioral-trigger-catalog, retention-cohort-program, cac-ltv-ledger.
- New rubrics: metric-tree, attribution, revops-hygiene, category-design, unit-economics. Updated: skill (I/O contract criterion), lead-scoring (phase discipline).
- CMO digest v1.1: Motion Summary section + Unit Economics standing section + adversarial-critic gate in non-negotiables.
- Skill manifest v1.1: producer→consumer edges; motion definitions.
- Fixture regrade: authored `category-design.md`, `narrative-thesis.md`, `lifecycle-map.md`, `cac-ltv-ledger.md` for Loopgate.

## 🚧 Stage 2.6 — External CMO Review (pre-pilot)
**Gate to Stage 3.** Send v1.1 fixture + 5 strategic artifacts to ≥2 senior marketing operators for truly-external adversarial critique. Incorporate corrections before pilot.

## 🚧 Stage 3.5 — Empirical Attribution Validation
**Needs: live pilot client + ≥18 months of spend/outcome history OR a running geo-holdout.**
- MMM coefficient estimation with real priors, adstock, saturation (methodology shipped in v1.1; empirical fit awaits data).
- Incrementality empirical proof (design shipped; execution needs live traffic).
- LLM-citation benchmarking against actual engine outputs (methodology + instrumentation shipped; running collection needs live API access).
- Rubric-calibration first feedback loop (`rubric-calibration.skill.md`) with 90-day outcome data.

## 🚧 Stage 3 — Real Tool-Calling
**Needs: sandbox credentials + integration tests.**
- Upgrade `06-connectors/` specs to runtime MCP tools (GA4, Google Ads, LinkedIn, HubSpot, Webflow, Customer.io, Amplitude).
- Each connector: read/write contract, rate-limit discipline, idempotency, error retry, audit trail.
- Per-connector integration test + sandbox harness.
- Credential vault pattern (e.g., 1Password CLI, doppler) wired via `secrets.pointer.md`.

## 🚧 Stage 4 — Autonomous Scheduler
**Needs: Stage 3 complete + operator acceptance of autonomy boundaries.**
- Weekly tick on cron (or equivalent) + digest delivery to Slack/email.
- Auto-paused operations on stop-loss (paid ROAS, CAC, frequency).
- HITL queue with deadline escalation.
- Reallocation executor under policy.
- Full audit event log with replay.

## 🚧 Stage 5 — Real Client Pilot
**Needs: Stage 4 complete + signed pilot agreement + legal/privacy review.**
- 1 paying design-partner client onboarded.
- 90-day outcome tracked vs plan; weekly digest delivered; KPI lift measured.
- Post-pilot retrospective + open-sourced learnings.

## Non-goals (explicit)
- Not a SaaS product — this is an open operating system meant to be forked per operator.
- Not a replacement for senior marketing judgment — it is a force-multiplier with rubric-gated quality.
- Not a content farm — every artifact is graded and cut if <8/10.
