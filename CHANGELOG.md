# Changelog

## v1.1.0 — SME-Hardened (2026-04-24)

**Theme:** close the methodology gaps flagged in senior SME adversarial review of v1.0. 15 of 17 gaps addressed as authored artifacts; 2 blocked by empirical-data requirements and documented as Stage 3.5 gating.

### Added — agents
- `.claude/agents/head-of-revops.md` — pipeline hygiene, funnel diagnostic, stage velocity, SDR→AE handoff SLA, CRM data quality.
- `.claude/agents/motion-acquisition.md` — outcome owner for new-ARR, CAC, payback; pulls from 6 Heads.
- `.claude/agents/motion-activation.md` — outcome owner for activation rate, TTFV, wk2-retention, activation→SQL.
- `.claude/agents/motion-retention.md` — outcome owner for NRR, GRR, expansion ACV, logo churn.
- `.claude/agents/adversarial-critic.md` — independent reviewer; reads artifact + rubric cold; produces critic-score independent of self-score; gate `min(self, critic) ≥ 8`.

### Added — skills
- `skills/seo/aeo-citation-audit.skill.md` — LLM-citation share across ChatGPT/Claude/Gemini/Perplexity/Google AIO; BMI-LLM metric; 4-class query set; n≥3 sampling.
- `skills/seo/answer-engine-brief.skill.md` — canonical-answer-block content brief; entity grounding; schema.org markup; factual-density targets.
- `skills/content/distribution-map.skill.md` — per-asset distribution plan; dark-social instrumentation; sales-enablement routing.
- `skills/growth/experiment-program.skill.md` — velocity target, learning-rate metric, MDE policy, learning-ledger distinct from event-ledger.
- `skills/performance/creative-ops.skill.md` — hook × angle × format matrix, creative-velocity KPI, fatigue thresholds, AI-creative pipeline.
- `skills/analytics/incrementality-test.skill.md` — geo-holdout / ghost-ad / synthetic-control / PSA-holdout design + readout methodology.
- `skills/analytics/unit-economics.skill.md` — segmented CAC / LTV / payback / burn-multiple / magic-number; fully-loaded CAC discipline.
- `skills/quality/rubric-calibration.skill.md` — outcome→rubric feedback loop with criterion-level correlation, calibration events, quarterly version bumps.

### Added — templates
- `templates/category-design.md` — Play Bigger + Dunford hybrid with honest gating.
- `templates/narrative-thesis.md` — Raskin strategic-narrative structure.
- `templates/creative-test-matrix.md` — explore/exploit/moonshot budget split + tag-level roll-up.
- `templates/pricing-page-brief.md` — tier architecture, anchoring, instrumentation, testing queue.
- `templates/plg-conversion-audit.md` — funnel spine, aha-event, in-product conversion surfaces.
- `templates/lifecycle-map.md` — stages × triggers × messages × goals with holdout discipline.
- `templates/behavioral-trigger-catalog.md` — versioned, reusable trigger IDs.
- `templates/retention-cohort-program.md` — cohort curves, leading indicators, program portfolio.
- `templates/cac-ltv-ledger.md` — monthly unit-economics ledger (CMO digest feeder).

### Added — rubrics
- `rubrics/metric-tree.yaml`
- `rubrics/attribution.yaml`
- `rubrics/revops-hygiene.yaml`
- `rubrics/category-design.yaml`
- `rubrics/unit-economics.yaml`

### Added — other
- `clients/_template/learning-ledger.jsonl` — schema + append-only convention.
- `clients/_fixture_devtools_saas/category-design.md` — Loopgate "Runtime Product Policy" category.
- `clients/_fixture_devtools_saas/narrative-thesis.md` — shift/stakes/insight structure.
- `clients/_fixture_devtools_saas/lifecycle-map.md` — 8-stage map + trigger table.
- `clients/_fixture_devtools_saas/cac-ltv-ledger.md` — synthetic unit-economics snapshot.

### Rewritten
- `skills/orchestration/goal-decomposer.skill.md` → **v2.0**: outputs a metric tree (NSM → L1 inputs → L2 levers) per Reforge model; motion OKRs; Head OKRs; 90-day plan. JSON schemas for inputs/outputs.
- `clients/_fixture_devtools_saas/attribution-model.md` → **v2**: triangulated MTA + MMM + incrementality with explicit decision hierarchy, MDE policy, instrumentation checklist. Self 92 / Critic 88.
- `clients/_fixture_devtools_saas/lead-scoring.md` → **v2 two-phase**: Phase-1 fit-only firmographic + behavioral routing; Phase-2 composite gated on n≥2000 closed-won + data-quality + HITL. Self 98 / Critic 91.

### Updated — agents
- `.claude/agents/cmo-orchestrator.md` — Motion Summary section; Unit Economics standing section; RevOps line in vertical assignments; adversarial-critic gate rule in non-negotiables.

### Updated — rubrics
- `rubrics/skill.yaml` — added `io_contract` criterion for composability.
- `rubrics/lead-scoring.yaml` — added `phase_discipline` criterion; demoted composite dimensions to Phase-2.

### Updated — other
- `.claude/skills.manifest.json` → **v1.1.0**: `motions` block; `skill_edges` (producer→consumer); RevOps Head; category-design & narrative-thesis under Brand.
- `ROADMAP.md` — Stage 2.5 marked ✅ SME-Hardened; new Stage 2.6 (external CMO review); new Stage 3.5 (empirical attribution validation).
- `README.md` — v1.1 note with honest diff vs v1.0.

### Known unaddressed (gated to Stage 3.5)
- MMM empirical coefficient fit (needs 18+ months real spend/outcome data).
- Incrementality empirical proof (needs live geo-holdout or ghost-ad test).
- LLM-citation benchmarking against real engine outputs (methodology + instrumentation shipped; collection needs live API access).
- External CMO validation of upgraded rubrics (Stage 2.6).

---

## v1.0.0 — Initial Public Release
Stages 0–2 as described in ROADMAP.md: foundation skills, fixture, eval harness skeleton.
