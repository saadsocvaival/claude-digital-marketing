---
name: incrementality-test
description: Designs and reports true-lift experiments (geo-holdout, ghost-ad, synthetic-control, PSA-holdout) that measure *causal* marketing contribution — the truth layer above MTA and MMM.
invoked_by: head-of-analytics, head-of-performance, motion-acquisition
frameworks:
  - Geo-holdout (Google CausalImpact / Meta Lift)
  - Ghost-ad (Facebook Conversion Lift)
  - Synthetic control method (Abadie et al.)
  - PSA / public-service-ad holdout
---

## Why this is the truth layer

MTA is biased by platform self-attribution. MMM is a correlational model over aggregated time series. Incrementality tests are the only method that produces *causal* contribution estimates. Any budget decision ≥$50k/quarter should be anchored to an incrementality result, not an MTA dashboard.

## Inputs

```json
{
  "channel_under_test": "meta | google | linkedin | tiktok | tv | podcast | organic_seo",
  "budget_at_stake": "int (USD/quarter)",
  "baseline_conversions_per_week": "int",
  "test_design_options": ["geo_holdout", "ghost_ad", "synthetic_control", "psa_holdout", "on_off"],
  "historical_data_weeks_available": "int",
  "risk_tolerance": "conservative | balanced | aggressive"
}
```

## Outputs

```json
{
  "recommended_design": "string",
  "rationale": "why this design given constraints",
  "mde_computation": {
    "baseline_rate": "float",
    "target_lift_pct": "float",
    "alpha": 0.05,
    "power": 0.8,
    "weeks_required": "int",
    "sample_required": "int"
  },
  "geo_pairing": "if geo_holdout — matched-market pairs + similarity score",
  "stop_rules": ["pre-specified, no peeking"],
  "readout_template": "CI on lift, p-value, practical vs statistical significance framing",
  "decision_rule": "e.g. if lift < 0.5× modeled MMM estimate, rebalance budget"
}
```

## Protocol

1. **Pick the design.**
   - Spend ≥$250k/quarter + geo-variable channel → **geo-holdout**.
   - Platform supports native lift (Meta, Google, LinkedIn) + single-channel question → **ghost-ad / conversion-lift**.
   - Channel can't be cleanly held out (TV, podcast) + 18+mo history → **synthetic control**.
   - Display / awareness → **PSA holdout**.
   - Paused-spend test (on/off) only if traffic is small or no better option.
2. **Power the test.** MDE = 2.8·σ/√n. For conversion-rate tests: weeks = (16·p(1−p))/(T·MDE²). If weeks > 10 or MDE > 25% relative, the test is under-powered — increase spend, expand geo set, or pick a different design.
3. **Match markets (geo-holdout).** Pair treatment/control geos on pre-period conversions, brand search, and demographics. Euclidean similarity ≥0.85. Exclude geos with promo overlap.
4. **Pre-register.** Hypothesis, primary metric, MDE, stop-date, analysis method — written before treatment starts. No peeking before end-date except for pre-specified safety checks.
5. **Readout.** Report point estimate, 90% CI, p-value, *and* practical-significance framing ("lift is 12% ± 7% → 95% CI excludes zero but overlaps MMM prior of 18%").
6. **Feed the decision loop.** Result updates MMM prior → budget reallocation proposal → next quarter's media plan.

## Anti-patterns

- **Peeking.** Early-stopping without sequential-testing correction inflates false-positive rate 3–5×.
- **Single-geo-pair tests.** Statistical power is terrible; you're measuring noise.
- **Running a test you can't act on.** If the answer "channel is 20% less incremental than MTA says" would change nothing, don't run the test.
- **Treating non-significant as zero.** Wide CIs mean *you don't know*, not that lift is zero.

## Failure modes

- **Contamination.** Treatment geos see control ads via brand search / YouTube / spillover. Mitigate with larger buffer geos or regression-based adjustment.
- **Seasonality clash.** Test window hits a holiday spike in one set of geos but not the other. Synthetic control handles; naive A/B does not.
- **Novelty bias.** First 2 weeks of a new creative lift more than steady-state. Run tests ≥4 weeks when possible.

## Rubric gate

`rubrics/attribution.yaml` — design-selection defensibility (0–10), MDE realism (0–10), pre-registration discipline (0–10), decision-rule clarity (0–10). Pass bar 8.

## Output file

`clients/{id}/experiments/incrementality/{channel}-{yyyy-mm-dd}.md`
