---
name: rubric-calibration
description: Closes the outcome→rubric feedback loop. On every 30/90-day artifact review, emits a rubric-calibration-event proposing weight adjustments when rubric scores diverge from real pipeline outcomes. Quarterly rubric-version bumps.
invoked_by: cmo-orchestrator, adversarial-critic
frameworks:
  - Calibration curves (Platt/Isotonic)
  - Brier score for forecast quality
  - Goodhart-resistant metric design
---

## Why

A rubric that scores everything 9/10 but produces mediocre pipeline is broken. Without a calibration loop, rubrics drift into self-congratulation. This skill forces rubrics to be tested against outcomes, not just applied to artifacts.

## Inputs

```json
{
  "lookback_window_days": 30,
  "artifacts_to_review": ["paths"],
  "outcome_metrics": {
    "artifact_id": { "self_score": "float", "critic_score": "float", "actual_outcome": "float (normalized 0-10)", "metric_used": "string" }
  }
}
```

## Outputs

```json
{
  "calibration_table": [
    { "rubric": "string", "avg_self_score": "float", "avg_critic_score": "float", "avg_outcome": "float", "divergence": "float" }
  ],
  "brier_score_per_rubric": "float",
  "proposed_weight_adjustments": [
    { "rubric": "string", "criterion": "string", "current_weight": "float", "proposed_weight": "float", "rationale": "string" }
  ],
  "criteria_to_retire": ["string (no signal vs outcome)"],
  "criteria_to_add": ["string (outcome pattern not captured by any criterion)"],
  "rubric_version_bump": "semver"
}
```

## Protocol

1. **Join scores to outcomes.** For each artifact scored ≥30 days ago, retrieve the downstream outcome it influenced (pipeline $, conversion lift, test-learning shipped).
2. **Compute divergence.** |avg_score − normalized_outcome| per rubric. Divergence >2.0 = mis-calibrated.
3. **Criterion-level correlation.** Correlate each individual criterion's score with the outcome. Criteria with |r|<0.1 across ≥15 artifacts = candidates for retirement.
4. **Spot uncovered patterns.** Artifacts where outcome was great but score was average (or vice versa) — what feature of the artifact explains it? Propose new criterion.
5. **Propose adjustments.** Weight shifts ≤0.15 per quarter (avoid whiplash). Retirements need ≥2 quarters of evidence.
6. **HITL approval.** Rubric changes are policy. Require operator sign-off before version bump.
7. **Version bump.** Semantic: patch = threshold tweak, minor = weight adjustment, major = criterion add/remove. Old scores preserved with old version tag; no retrodoctoring.

## Anti-patterns

- **Goodhart capture.** If teams start writing to the rubric and scores rise without outcomes, the rubric has become the metric. Rotate criteria.
- **n-too-small retirement.** Killing a criterion after 3 artifacts is noise, not signal.
- **Silent version drift.** Every score must carry its rubric version; otherwise trend analysis is meaningless.
- **Outcome-washing.** Picking the outcome metric *after* seeing scores, to justify a conclusion.

## Failure modes

- **Outcome lag > review cadence.** If the real outcome (e.g. pipeline $) takes 120 days, 30-day calibration uses leading proxies — label them as such.
- **Survivor bias.** Only shipped artifacts get outcomes; killed ones don't. Include kill-decision quality as an outcome.
- **Confounded outcome.** A great plan that failed due to market shift shouldn't demote the planning rubric. Qualitative gate before weight changes.

## Rubric gate

`rubrics/skill.yaml` + criteria: statistical rigor (0–10), adjustment conservatism (0–10), versioning discipline (0–10). Pass bar 8.

## Output file

`rubrics/_calibration/{yyyy-mm-dd}-event.md` + updated `rubrics/{name}.yaml` with bumped `version:` field
