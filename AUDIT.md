# Coverage Audit — Autonomous Digital Marketing OS

> Maps playbook policy → artifact (this PR) → rubric → eval harness. Gaps are called out honestly.
> **v1.1.1** — Now reflects gap-fill (6 workflows, 8 connectors, 5 rubrics, costsage scaffold, 7 vertical READMEs filled) **plus v1.1 SME-hardened additions** (motion overlay, head-of-revops, adversarial-critic, metric-tree, triangulated attribution, two-phase lead scoring, real GEO/AEO methodology, unit-economics, distribution-map, experiment-program, creative-ops, incrementality-test, rubric-calibration). See CHANGELOG.md and ROADMAP.md.

## Legend
- ✅ shipped + rubric-gated
- ⚠️ shipped, rubric pending
- 🔲 not in this PR (Stage 3+)

## Coverage matrix

| Domain | Policy ref (playbook §) | Artifact in this PR | Rubric | Eval | Status |
|---|---|---|---|---|---|
| Operating protocol | CLAUDE.md | `/CLAUDE.md` | n/a (protocol) | n/a | ✅ |
| Orchestrator | 02-agents/tier-1 | `.claude/agents/cmo-orchestrator.md` | `rubrics/agent.yaml` | manual | ✅ |
| 8 Department Heads | 02-agents/tier-2 | `.claude/agents/head-of-*.md` | `rubrics/agent.yaml` | manual | ✅ |
| Onboarding | 01-playbook §2 | `skills/orchestration/onboarding.skill.md` | `rubrics/skill.yaml` + `rubrics/client-ledger.yaml` | yes | ✅ |
| Goal decomposition | 01-playbook §3 | `skills/orchestration/goal-decomposer.skill.md` | `rubrics/skill.yaml` + `rubrics/90-day-plan.yaml` | yes | ✅ |
| Weekly tick | 04-workflows | `skills/orchestration/weekly-tick.skill.md` | `rubrics/skill.yaml` + `rubrics/weekly-digest.yaml` | yes | ✅ |
| HITL protocol | 11-approvals/gates | `skills/orchestration/hitl-request.skill.md` | `rubrics/hitl-request.yaml` | yes | ✅ |
| ICP | 01-playbook §4.1 | `templates/icp.md` + fixture `icp.md` | `rubrics/icp.yaml` | yes | ✅ |
| Positioning | 01-playbook §4.2 | `templates/positioning.md` + fixture `positioning.md` | `rubrics/positioning.yaml` | yes | ✅ |
| Brand voice | 01-playbook §4.3 | `templates/brand-voice.md` + fixture `brand-voice.md` | `rubrics/brand-voice.yaml` | yes | ✅ |
| Messaging | 01-playbook §4.4 | `templates/messaging.md` + fixture `messaging.md` | `rubrics/messaging.yaml` | yes | ✅ |
| Offer | 01-playbook §4.5 | `templates/offer.md` + fixture `offer.md` | `rubrics/offer.yaml` | manual | ✅ |
| UTM taxonomy | 01-playbook §6.2 | `templates/utm-taxonomy.md` + fixture | `rubrics/utm.yaml` | manual | ✅ |
| Lead scoring | 01-playbook §6.3 | `templates/lead-scoring.md` + fixture | `rubrics/lead-scoring.yaml` | yes | ✅ |
| Battlecards | 01-playbook §4.6 | `templates/battlecard.md` + 3 fixture cards | `rubrics/battlecard.yaml` | yes | ✅ |
| 90-day plan | 01-playbook §3 | fixture `plan.md` | `rubrics/90-day-plan.yaml` | yes | ✅ |
| OKRs per Head | 01-playbook §3.2 | fixture `okrs/2026-q2.md` | `rubrics/okr.yaml` | manual | ✅ |
| Editorial calendar | 01-playbook §5.1 | `templates/editorial-calendar.md` + fixture | `rubrics/editorial-calendar.yaml` | manual | ✅ |
| Campaign brief | 01-playbook §5.2 | `templates/campaign-brief.md` + 3 fixture briefs | `rubrics/campaign-brief.yaml` | yes | ✅ |
| Ad copy | 01-playbook §5.3 | 5 fixture ad sets | `rubrics/ad-copy.yaml` | yes | ✅ |
| Landing page | 01-playbook §5.4 | `templates/landing-page-brief.md` + fixture | `rubrics/landing-page.yaml` | yes | ✅ |
| Email (single) | 01-playbook §5.5 | `templates/email-sequence.md` + 3 fixture sequences | `rubrics/email-sequence.yaml` + `rubrics/email.yaml` | yes | ✅ |
| SEO content brief | 01-playbook §5.6 | `templates/seo-content-brief.md` + 9-piece cluster | `rubrics/seo-brief.yaml` | yes | ✅ |
| Weekly KPI snapshot | 01-playbook §7.1 | `templates/weekly-kpi-snapshot.md` + fixture | `rubrics/weekly-kpi-snapshot.yaml` | yes | ✅ |
| Weekly digest | 01-playbook §7.2 | digest format inside CMO agent | `rubrics/weekly-digest.yaml` | manual | ✅ |
| Monthly exec report | 01-playbook §7.3 | `templates/monthly-exec-report.md` | `rubrics/monthly-exec.yaml` | manual | ✅ |
| Attribution | 01-playbook §6.4 | fixture `attribution-model.md` | `rubrics/attribution.yaml` | manual | ✅ |
| Security / secrets | 11-approvals | `SECURITY.md` + `.gitignore` + pre-commit hook | — | manual scan | ✅ |
| Multi-tenant scaffold | (new) | `clients/_template/` tree | — | — | ✅ |
| Dogfood fixture client | (new) | `clients/_fixture_devtools_saas/` (~40 artifacts) | per-artifact self-rubric | yes | ✅ |
| MCP tool-calling (GA4, Ads, HubSpot, LinkedIn, Webflow, WordPress, SendGrid, Resend, Mailgun, Trello, Microsoft Ads, Segment, BigQuery) | 06-connectors | connector specs expanded (+8 in gap-fill PR); runtime pending | — | — | 🔲 specs expanded; runtime pending (Stage 3) |
| Autonomous scheduler | (new) | — | — | — | 🔲 Stage 4 |
| Real client pilot | (new) | — | — | — | 🔲 Stage 5 |

## Known gaps (honest)
- ✅ Closed: 6 rubrics added in gap-fill PR — `offer.yaml`, `editorial-calendar.yaml`, `okr.yaml`, `attribution.yaml`, `utm.yaml`, `monthly-exec.yaml`.
- ✅ 6 new workflows added in gap-fill PR — `client-onboarding`, `daily-stop-loss`, `kpi-snapshot-pipeline`, `digest-delivery`, `learning-loop`, `secrets-vault-setup`.
- ✅ 8 connector specs added — SendGrid, Resend, Mailgun, Trello, WordPress App Password, Microsoft Ads, Segment, BigQuery.
- ✅ 7 vertical playbook READMEs filled (charter / KPIs / cadence / workflows / tools / policies / refusal triggers / artifacts / rubrics).
- ✅ CostSage client scaffolded (`clients/costsage/`) — pending-onboarding.
- MCP tool-calling: specs expanded; runtime not wired. Stage 3 — needs sandbox creds.
- Autonomous scheduler: the weekly-tick skill assumes operator-triggered. A real cron/scheduler with credential vault lives in Stage 4.
- External CMO review not performed; artifacts are self-rubric-graded. Stage 2.5 in ROADMAP.
- Fixture is an archetype, not a real company. Real-client pilot in Stage 5.

## v1.1 SME-hardened layer (PR #7) — addressable inside repo

| Domain | Artifact | Rubric | Status |
|---|---|---|---|
| Metric-tree decomposition | `skills/orchestration/goal-decomposer.skill.md` v2.0 | `rubrics/metric-tree.yaml` | ✅ |
| Triangulated attribution (MTA + MMM + incrementality) | `clients/_fixture_devtools_saas/attribution-model.md` v2 + `skills/analytics/incrementality-test.skill.md` | `rubrics/attribution.yaml` (v1.1) | ✅ methodology; empirical fit Stage 3.5 |
| Two-phase lead scoring | `clients/_fixture_devtools_saas/lead-scoring.md` v2 | `rubrics/lead-scoring.yaml` (phase_discipline) | ✅ |
| Motion-based overlay | `.claude/agents/motion-{acquisition,activation,retention}.md` | `rubrics/agent.yaml` | ✅ |
| Head of RevOps | `.claude/agents/head-of-revops.md` | `rubrics/revops-hygiene.yaml` | ✅ |
| Adversarial-critic gate | `.claude/agents/adversarial-critic.md` | `rubrics/agent.yaml` | ✅ |
| Real GEO/AEO methodology | `skills/seo/aeo-citation-audit.skill.md`, `skills/seo/answer-engine-brief.skill.md` | `rubrics/seo-brief.yaml` + skill rubric | ✅ |
| Unit economics standing section | `skills/analytics/unit-economics.skill.md` + `templates/cac-ltv-ledger.md` | `rubrics/unit-economics.yaml` | ✅ |
| Content distribution model | `skills/content/distribution-map.skill.md` | `rubrics/skill.yaml` | ✅ |
| Experiment program | `skills/growth/experiment-program.skill.md` + `clients/_template/learning-ledger.jsonl` | `rubrics/skill.yaml` | ✅ |
| Creative ops | `skills/performance/creative-ops.skill.md` + `templates/creative-test-matrix.md` | `rubrics/skill.yaml` | ✅ |
| PLG / pricing CRO scope | `templates/pricing-page-brief.md` + `templates/plg-conversion-audit.md` | `rubrics/landing-page.yaml` | ✅ |
| Lifecycle/expansion programs | `templates/lifecycle-map.md`, `templates/behavioral-trigger-catalog.md`, `templates/retention-cohort-program.md` | `rubrics/skill.yaml` | ✅ |
| Category design / narrative | `templates/category-design.md`, `templates/narrative-thesis.md` + Loopgate fixture | `rubrics/category-design.yaml` | ✅ |
| Rubric calibration loop | `skills/quality/rubric-calibration.skill.md` | `rubrics/skill.yaml` | ✅ methodology; empirical Stage 3.5 |
| Skill I/O composability | I/O JSON-Schema blocks in skills + manifest `skill_edges` | `rubrics/skill.yaml` (io_contract) | ✅ |
