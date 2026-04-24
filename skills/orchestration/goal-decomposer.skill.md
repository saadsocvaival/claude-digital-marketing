---
name: goal-decomposer
description: Decomposes a top-level growth goal into 4 North-Star metrics, quarterly OKRs (objectives + key results per vertical), and a 90-day execution plan with vertical assignments. Invoke after onboarding completes, or when operator gives a fresh goal against an existing client.
invoked_by: cmo-orchestrator
inputs:
  - clients/{id}/ledger.md
  - clients/{id}/icp.md
  - clients/{id}/positioning.md (if exists)
  - goal_statement: string
outputs:
  - clients/{id}/okrs/{quarter}.md
  - clients/{id}/plan.md
  - clients/{id}/vertical-assignments.md
rubric: rubrics/90-day-plan.yaml
---

# Goal Decomposer Skill

## Purpose
Translate a fuzzy goal ("Achieve 50% growth") into a rigorous, Playbook-compliant NSM → OKR → 90-day plan with explicit vertical ownership and measurable KRs.

## Frameworks applied (non-negotiable)

1. **North Star Framework** (Sean Ellis / Amplitude) — pick the single metric that best predicts long-term success, plus 3 supporting NSMs.
2. **AARRR / Pirate Metrics** (Dave McClure) — categorize KRs across Acquisition, Activation, Retention, Referral, Revenue.
3. **OKR methodology** (Andy Grove / John Doerr) — Objectives are qualitative and ambitious; KRs are quantitative and time-bound.
4. **SiriusDecisions Demand Waterfall** (for B2B) — inquiry → MQL → SQL → opp → closed-won conversion ratios drive capacity plan.
5. **RICE** (Reach × Impact × Confidence / Effort) — for initiative prioritization within the 90-day plan.

## Protocol

### Step 1 — Ground the goal
Read:
- `clients/{id}/ledger.md` §1 (revenue stage), §4 (channels, motion), §5 (budget).
- `clients/{id}/icp.md`.
- Operator goal statement.

Classify the goal type:
- **Top-line** (ARR, MRR, revenue) → work backward through funnel.
- **Pipeline** (MQLs, SQLs, opps) → focus on demand stages.
- **Efficiency** (CAC, payback, LTV:CAC) → focus on optimization + retention.
- **Retention** (churn, NDR) → focus on onboarding + lifecycle.
- **Brand** (awareness, SOV) → focus on Brand + Content + PR mix.

### Step 2 — Select NSMs (max 4, min 3)

Use this template (pick ONE primary + 3 supporting per applicable motion):

| Motion | Primary NSM candidates | Supporting |
|---|---|---|
| PLG SaaS | Weekly Active Teams / Activated Accounts | Signups, Activation Rate, D30 Retention, Paid Conversion |
| Sales-led SaaS | Qualified Pipeline Generated ($) | MQLs, SQL-to-Opp, Win Rate, ACV |
| Hybrid | Weighted Pipeline + Activated Accounts | Same supporting as motion dominants |
| DTC / e-com | Net New Customers / month | Sessions, CVR, AOV, Repeat-Purchase Rate |
| Marketplace | Successful Transactions / Active Participant | Supply liquidity, demand liquidity, take rate |
| Content/Media | Weekly Active Readers / Paid Subs | Sessions, Time, Email List, Paid Conversion |

Document your choice + the 3 alternatives you rejected with reasons (audit trail).

### Step 3 — Work the funnel backward

Given the 90-day NSM target and historical conversion rates (from ledger or assumptions), compute the required inputs at each stage. Template:

```
Goal:                 +X NSM units in 90 days
Current run rate:     Y / 90 days → gap = X - Y
Stage conversion:     {stage 1 → 2}%, {2 → 3}%, ...
Required top-of-funnel: Z (with 10–20% buffer for risk)
Required daily/weekly cadence: …
```

If any conversion rate is unknown, flag as assumption with citation to industry benchmark (cite source; if unavailable use conservative lower bound).

### Step 4 — Set Q-level OKRs (per vertical)

For each of the 8 Heads, write:
- **1 qualitative Objective** aligned to the NSM and 90-day plan theme.
- **3 quantitative Key Results** — measurable, with baseline + target + deadline.

Objective template:
> "{Verb} {thing} so that we {outcome linked to NSM}."

KR template:
> "Move {metric} from {baseline} to {target} by {date}."

Every KR must have a named owner (the Head), a measurement source (from Analytics' kpi-dictionary), and a cadence (weekly/bi-weekly check).

### Step 5 — 90-day plan

Build a 12-week plan with three phases:

- **Weeks 1–3: Foundation & Quick Wins.** Measurement in place, audit baseline, kill obvious waste, ship one visible win per vertical.
- **Weeks 4–8: Programs & Optimization.** Launch flagship programs per vertical, begin experiments, accumulate data.
- **Weeks 9–12: Compound & Reallocate.** Double down on winners, retire losers, publish outcomes, set Q+1 direction.

For each week, list:
- Cross-vertical dependencies (e.g., Analytics must publish tracking plan before Performance launches).
- Critical-path milestones.
- Decision gates + HITL flags.

### Step 6 — Vertical assignments

One brief per Head, written to `clients/{id}/vertical-assignments.md`:

```markdown
## Head of {Vertical}
- **Objective**: ...
- **Key Results**: KR1 / KR2 / KR3
- **Budget envelope**: $...
- **Dependencies (from)**: {other Heads / upstream}
- **Feeds to publish**: {list}
- **Feeds to consume**: {list}
- **First-week deliverable**: ...
- **Stop-loss criteria**: ...
```

### Step 7 — Risk register + assumptions log

List:
- Top 5 risks with likelihood × impact × mitigation.
- Every assumption made (conversion rates, market growth, competitive moves).
- External dependencies (tools, creds, legal).

### Step 8 — Self-eval against rubric

Score the produced plan against `rubrics/90-day-plan.yaml`. If < 8/10, iterate before returning to Orchestrator.

## Anti-patterns to reject

- "Increase brand awareness" as an OKR (not measurable).
- KRs without a baseline (can't evaluate progress).
- More than 5 objectives per vertical (focus collapse).
- OKRs that sum to more than the capacity plan supports (fantasy).
- Skipping the backward-from-NSM math (goals detached from math = wishful).

## Output files

All three files below must be produced; plan is not complete until all three validate.

1. `clients/{id}/okrs/{YYYY-Q}.md` — OKR table, NSM math, alternatives considered.
2. `clients/{id}/plan.md` — 12-week plan, phases, cross-vertical deps, risks.
3. `clients/{id}/vertical-assignments.md` — 8 briefs for the 8 Heads.

Self-rubric ≥ 8/10 is required to ship.
