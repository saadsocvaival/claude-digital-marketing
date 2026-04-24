---
name: goal-decomposer
description: Decomposes a top-level business goal into a metric tree (North Star → L1 input metrics → L2 levers), motion-based OKRs (acquisition / activation / retention), and a 90-day execution plan with per-motion + per-Head assignments. Invoke after onboarding completes, or when operator gives a fresh goal against an existing client.
invoked_by: cmo-orchestrator
version: 2.0
frameworks:
  - Reforge metric-tree methodology (Amplitude/Brian Balfour)
  - Elena Verna separate-loop NSM model (acquisition / monetization / retention)
  - April Dunford positioning inputs
  - SiriusDecisions demand waterfall (funnel math)
  - OKR (Doerr) — objectives qualitative, KRs quantitative + time-bound
---

## Why v2 (metric tree, not flat NSM)

Flat NSM + 3-supporting is 2018-era. Modern practice: the business runs **multiple loops** (acquisition, activation, retention/expansion) that compete for resources and cannot share one NSM without distorting decisions. The metric tree decomposes the top-of-tree business goal (revenue / ARR / contribution margin) into **input metrics** (what drives it) and **levers** (what we can move this week). Every KR ladders to an input; every experiment ladders to a lever.

## Inputs (schema)

```json
{
  "client_id": "string",
  "business_goal": {
    "metric": "ARR | revenue | contribution_margin | signups",
    "start_value": "number",
    "target_value": "number",
    "horizon_days": "integer",
    "constraint_budget_usd": "number",
    "constraint_headcount_fte": "integer"
  },
  "client_ledger_path": "string"
}
```

## Outputs (schema)

```json
{
  "metric_tree": {
    "north_star": { "name": "string", "definition": "string", "current": "number", "target": "number" },
    "l1_inputs": [
      { "name": "string", "formula": "string (how it rolls up)", "current": "number", "target": "number", "owner_motion": "acquisition | activation | retention" }
    ],
    "l2_levers": [
      { "name": "string", "rolls_up_to_l1": "string", "owner_head": "string", "baseline": "number", "target": "number", "mechanism": "string (how we move it)" }
    ]
  },
  "motion_okrs": {
    "acquisition": { "objective": "string", "key_results": [] },
    "activation":  { "objective": "string", "key_results": [] },
    "retention":   { "objective": "string", "key_results": [] }
  },
  "head_okrs": [ { "head": "string", "objective": "string", "key_results": [] } ],
  "ninety_day_plan": {
    "phases": [ { "name": "string", "weeks": "string", "exit_criteria": [] } ],
    "critical_path": [],
    "risk_register": [],
    "hitl_preflags": []
  },
  "rejected_alternatives": [ { "candidate": "string", "reason": "string" } ]
}
```

## Protocol (7 steps)

1. **Read the ledger.** Extract: business model (PLG vs SLG vs hybrid), stage (pre-PMF / post-PMF / scale), constraints, motion-mix today.
2. **Pick the North Star.** Rule: must correlate with revenue, must be leading (not lagging), must be movable by marketing+product within the horizon. Log 2–3 rejected candidates with reasons (usually lagging revenue metrics get rejected in favor of their leading indicator).
3. **Decompose to L1 inputs.** For each, write the explicit formula (e.g., `ARR = new_ARR + expansion_ARR − churned_ARR`). Assign each L1 to a motion (acquisition / activation / retention). Cover the whole revenue equation — gaps mean hidden goals.
4. **Decompose L1 → L2 levers.** Each lever is something a Head can directly move in ≤90 days (e.g., "paid LinkedIn CPL" rolls up to "qualified-lead volume" rolls up to "new-ARR"). Each lever names an owner Head and a mechanism.
5. **Funnel math with 1.3× buffer.** Back-solve lever targets from the North Star target. Inflate by 1.3× to absorb shortfall variance. If the math requires >3× current lever performance, flag as implausible and loop back to Step 2 with reduced target or longer horizon.
6. **Motion OKRs.** Per motion: one Objective (qualitative, inspirational), 3 KRs (quantitative, matching L1 inputs). Then per-Head OKRs that cascade from motion OKRs to Head-owned levers.
7. **90-day plan.** Phase into `Foundation (wks 1–4) → Scale (wks 5–9) → Compound (wks 10–13)` with exit criteria per phase. Produce risk register (≥5), HITL pre-flags, critical path.

## Failure modes to check for

- **NSM = revenue.** Lagging. Reject; find the leading input (e.g., qualified pipeline, activated accounts, weekly-active teams).
- **Gaps in coverage.** If no L1 owns retention/expansion, marketing will over-invest in acquisition. Reject and add.
- **Lever with no mechanism.** "Increase demo requests" is a metric, not a lever. The lever is "LP conversion rate" or "paid-search CTR." Reject and decompose further.
- **Funnel math requires >3× lever lift.** Implausible in a quarter. Flag + reset target.
- **All KRs owned by one motion.** Indicates poor decomposition. Force coverage.

## Invocation example

```
Input: { client_id: "loopgate", business_goal: { metric: "ARR", start_value: 2100000, target_value: 4000000, horizon_days: 240, constraint_budget_usd: 600000, constraint_headcount_fte: 8 } }

Output (abbreviated):
  north_star: weekly_active_teams (leading indicator of net-new + retained ARR)
  l1_inputs:
    - new_ARR (acquisition) = deals_won × ACV
    - expansion_ARR (retention) = expand_accounts × avg_expand_ACV
    - churned_ARR (retention, negative) = churn_rate × last_quarter_ARR
  l2_levers (selected):
    - paid_LinkedIn_MQLs  → Head of Performance, mechanism: ABM audience + creative iteration
    - PLG_sandbox_activation_rate → Head of CRO + Product, mechanism: guided tour + aha-event
    - net_revenue_retention → Head of Automation, mechanism: expansion-trigger lifecycle program
  motion_okrs:
    acquisition: O=Build repeatable SQL engine; KR1=600 SQLs/qtr, KR2=CPL ≤$180, KR3=paid pipeline $3M
    activation:  O=Halve time-to-first-value; KR1=TTFV ≤7d, KR2=wk2_retention ≥45%, KR3=activation→SQL ≥8%
    retention:   O=Expansion > churn; KR1=NRR ≥115%, KR2=gross_churn ≤8%, KR3=expansion_ACV $400k
```

## Rubric gate
Output gated by `rubrics/metric-tree.yaml` AND `rubrics/90-day-plan.yaml`. Both must score ≥8 on self-rubric AND ≥8 on adversarial-critic pass before plan.md ships.

## Output file mapping
- Metric tree → `clients/{id}/metric-tree.md`
- Motion OKRs → `clients/{id}/okrs/motion-{qtr}.md`
- Head OKRs → `clients/{id}/okrs/{head}-{qtr}.md` (per Head)
- 90-day plan → `clients/{id}/plan.md`
- Rejected alternatives → appended to `plan.md §Appendix`
