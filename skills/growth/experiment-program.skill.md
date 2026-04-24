---
name: experiment-program
description: Defines the experimentation program (not a single test) — velocity target, learning-rate metric, MDE policy, power-analysis defaults, stop-loss rules, and a learning-ledger distinct from the event-ledger.
invoked_by: head-of-growth, head-of-cro, motion-acquisition, motion-activation
frameworks:
  - Sean Ellis / GrowthHackers ICE
  - Reforge experimentation maturity model
  - Evan Miller / Optimizely power-analysis conventions
---

## Why a *program*, not a test

One-off tests produce one-off wins that don't compound. A program produces a learning rate — wins per unit time — that compounds. The difference between a 10%/year growth team and a 40%/year growth team is not test quality; it's test velocity × decision quality × memory.

## Inputs

```json
{
  "team_size_experiment_capable": "int",
  "traffic_per_surface": { "lp": "int/week", "signup": "int/week", "in_app": "int/week" },
  "current_conversion_rates": { "surface": "float" },
  "strategic_bets": ["string (themes the program should concentrate on)"],
  "risk_tolerance": "conservative | balanced | aggressive"
}
```

## Outputs

```json
{
  "velocity_target": "experiments/quarter (by surface)",
  "learning_rate_target": "decisions shipped from experiments / quarter",
  "mde_policy": { "surface": "min detectable effect % (based on traffic)" },
  "power_analysis_defaults": { "alpha": 0.05, "beta": 0.2, "one_tailed": false },
  "sample_size_formulas": "string (reference)",
  "stop_loss_rules": [ { "trigger": "string", "action": "kill | extend | pivot" } ],
  "test_types_allowed": ["A/B", "A/B/n", "MAB", "holdout", "sequential"],
  "learning_ledger_schema": "jsonl (see below)",
  "review_cadence": "weekly triage + monthly program review"
}
```

## Protocol

1. **Compute MDE per surface.** Given weekly traffic T and baseline conversion p, MDE ≈ 2.8·√(2p(1−p)/(T·w)) for a w-week test. If MDE > 20% relative, don't test on that surface — change the mechanic instead.
2. **Set velocity target.** Experiment-capable headcount × 1.5–3 experiments/person/quarter depending on surface complexity. Reforge benchmark: elite teams run 4–6/person/quarter.
3. **Set learning rate.** Of shipped experiments, ≥60% should result in a decision (ship, kill, or iterate). <60% = low learning rate — tests are unfocused or under-powered.
4. **Pre-register every test.** Hypothesis, primary metric, guardrails, MDE, sample size, stop criteria — written *before* traffic starts.
5. **Stop-loss rules.**
   - Primary metric moves >2σ negative early → kill immediately.
   - Guardrail (e.g. latency, support volume) breaches → kill regardless of primary.
   - Time-boxed: no test runs >6 weeks without program-lead review.
6. **Record in learning-ledger** (separate from event-ledger):

```jsonl
{"date":"YYYY-MM-DD","surface":"lp","hypothesis":"...","primary_metric":"...","result":"ship|kill|inconclusive","lift":"-x.x% to +x.x%","learning":"what we now believe","confidence":"high|med|low"}
```

7. **Monthly program review.** Velocity vs target, learning rate, bet-concentration (are we testing the strategic themes?), dead-zones (surfaces with zero tests).

## Anti-patterns

- **Sample-size mathlaundering.** Running under-powered tests and calling inconclusive results "flat."
- **Theme drift.** Tests scattered across 12 themes produce no compounding knowledge.
- **Memory-less program.** No learning ledger → same hypothesis retested every 18 months.
- **Novelty chasing.** MAB / sequential / Bayesian when basic A/B would settle it. Complexity is a cost.

## Failure modes

- **High velocity, low learning rate.** Team is shipping tests but not decisions — usually unclear success criteria or missing pre-registration.
- **Low velocity, high learning rate per test.** Probably over-thinking; not enough shots on goal.
- **Strategic bets uncovered.** If no tests touched the CEO's top-3 bets this quarter, the program is misaligned.

## Rubric gate

`rubrics/skill.yaml` + criteria: velocity realism (0–10), MDE defensibility (0–10), learning-ledger discipline (0–10). Pass bar 8.

## Output file

`clients/{id}/experiments/program-{quarter}.md` + `clients/{id}/experiments/learning-ledger.jsonl` (append-only)
