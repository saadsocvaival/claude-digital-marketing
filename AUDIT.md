# Coverage Audit — Autonomous Digital Marketing OS

> Maps playbook policy → artifact (this PR) → rubric → eval harness. Gaps are called out honestly.

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
| Offer | 01-playbook §4.5 | `templates/offer.md` + fixture `offer.md` | — | — | ⚠️ |
| UTM taxonomy | 01-playbook §6.2 | `templates/utm-taxonomy.md` + fixture | — | manual | ⚠️ |
| Lead scoring | 01-playbook §6.3 | `templates/lead-scoring.md` + fixture | `rubrics/lead-scoring.yaml` | yes | ✅ |
| Battlecards | 01-playbook §4.6 | `templates/battlecard.md` + 3 fixture cards | `rubrics/battlecard.yaml` | yes | ✅ |
| 90-day plan | 01-playbook §3 | fixture `plan.md` | `rubrics/90-day-plan.yaml` | yes | ✅ |
| OKRs per Head | 01-playbook §3.2 | fixture `okrs/2026-q2.md` | — | — | ⚠️ |
| Editorial calendar | 01-playbook §5.1 | `templates/editorial-calendar.md` + fixture | — | — | ⚠️ |
| Campaign brief | 01-playbook §5.2 | `templates/campaign-brief.md` + 3 fixture briefs | `rubrics/campaign-brief.yaml` | yes | ✅ |
| Ad copy | 01-playbook §5.3 | 5 fixture ad sets | `rubrics/ad-copy.yaml` | yes | ✅ |
| Landing page | 01-playbook §5.4 | `templates/landing-page-brief.md` + fixture | `rubrics/landing-page.yaml` | yes | ✅ |
| Email (single) | 01-playbook §5.5 | `templates/email-sequence.md` + 3 fixture sequences | `rubrics/email-sequence.yaml` + `rubrics/email.yaml` | yes | ✅ |
| SEO content brief | 01-playbook §5.6 | `templates/seo-content-brief.md` + 9-piece cluster | `rubrics/seo-brief.yaml` | yes | ✅ |
| Weekly KPI snapshot | 01-playbook §7.1 | `templates/weekly-kpi-snapshot.md` + fixture | `rubrics/weekly-kpi-snapshot.yaml` | yes | ✅ |
| Weekly digest | 01-playbook §7.2 | digest format inside CMO agent | `rubrics/weekly-digest.yaml` | manual | ✅ |
| Monthly exec report | 01-playbook §7.3 | `templates/monthly-exec-report.md` | — | — | ⚠️ |
| Attribution | 01-playbook §6.4 | fixture `attribution-model.md` | — | manual | ⚠️ |
| Security / secrets | 11-approvals | `SECURITY.md` + `.gitignore` + pre-commit hook | — | manual scan | ✅ |
| Multi-tenant scaffold | (new) | `clients/_template/` tree | — | — | ✅ |
| Dogfood fixture client | (new) | `clients/_fixture_devtools_saas/` (~40 artifacts) | per-artifact self-rubric | yes | ✅ |
| MCP tool-calling (GA4, Ads, HubSpot, LinkedIn, Webflow) | 06-connectors | connector specs present (pre-existing) | — | — | 🔲 Stage 3 |
| Autonomous scheduler | (new) | — | — | — | 🔲 Stage 4 |
| Real client pilot | (new) | — | — | — | 🔲 Stage 5 |

## Known gaps (honest)
- Missing rubrics: offer.yaml, editorial-calendar.yaml, okr.yaml, attribution.yaml, utm.yaml, monthly-exec.yaml. (~6 additional rubrics planned — worth adding in a follow-up PR before external review.)
- MCP tool-calling: connectors describe interfaces but no runtime tool definitions are wired. This is deliberately Stage 3 — needs sandbox creds.
- Autonomous scheduler: the weekly-tick skill assumes operator-triggered. A real cron/scheduler with credential vault lives in Stage 4.
- External CMO review not performed; artifacts are self-rubric-graded. Stage 2.5 in ROADMAP.
- Fixture is an archetype, not a real company. Real-client pilot in Stage 5.
