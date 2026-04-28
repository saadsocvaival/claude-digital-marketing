# CRO Test 001 — Pricing Page Hero

**Status:** Drafted, awaiting operator approval to ship
**Page:** /pricing
**Hypothesis:** Replacing the generic "Choose your plan" hero with an outcome-anchored claim ("Stop paying for idle cloud — typical CostSage customers cut waste by [TBD-OPERATOR]% in week one") will increase the click-through rate to /contact and trial signup CTAs.

---

## 1. Background

Pricing page is the highest-intent page on the site after /contact. Current hero copy is descriptive ("Choose your plan") rather than outcome-anchored. Comparable benchmarks (Vantage, CloudZero pricing pages indexed by SimilarWeb) lead with savings-oriented claims.

## 2. Variants

- **Control (A):** Current hero — "Pricing" + sub "Choose the plan that fits your team."
- **Variant B:** Outcome hero — "Stop paying for idle cloud" + sub "Typical CostSage customers cut waste by `[TBD-OPERATOR]%` in week one. Plans below."
- **Variant C:** Risk-reversal hero — "Try CostSage free. Pay only after you've seen the savings." + sub "30-day trial. No credit card. AWS Marketplace billing available."

## 3. Primary metric

Click-through rate from /pricing → /contact OR "Start free trial" button click.

Secondary: pricing-page bounce rate, scroll depth past pricing-table fold.

## 4. Sample size + duration

- Baseline CTR: estimated 3-5% (`[TBD-OPERATOR]` confirm from analytics)
- MDE: +30% relative lift
- Required sample size per variant: ~3,200 sessions (3-arm test)
- At current /pricing traffic of `[TBD-OPERATOR]` sessions/week, expect 3-4 weeks
- Stop early if 95% confidence reached, never before 1 full business cycle

## 5. Implementation

When A/B engine is selected (see `ab-engine-decision-memo.md`), implement client-side via JS variant injection on `/pricing`. Until then, run **sequential** test: ship Variant B for 2 weeks, then Variant C for 2 weeks, compare to control baseline. Mark this as lower confidence (sequential ≠ randomised).

## 6. Risks

- "Typical customers cut waste by X%" requires operator-confirmed data — if no real number, do not ship Variant B. Use Variant C (risk-reversal) which doesn't require fabricated stats.
- Trademark / claim review — `[TBD-OPERATOR]` legal sign-off if quantitative claim is used.

## 7. Decision log

| Date | Decision | Owner |
|---|---|---|
| `[TBD-OPERATOR]` | Approve / reject Variant B claim source | Founder |
| `[TBD-OPERATOR]` | Variant C copy approved | Marketing |
| `[TBD-OPERATOR]` | Test launched | CRO operator |
