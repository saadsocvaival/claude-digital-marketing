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

## 🚧 Stage 2.5 — External CMO Review (pre-pilot)
**Gate to Stage 3.** Send the fixture and 3 artifacts (90-day plan, SEO cluster pillar, paid campaign brief) to 2 senior marketing operators for adversarial critique. Incorporate corrections before pilot.

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
