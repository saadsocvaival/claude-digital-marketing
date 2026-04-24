# Retention Cohort Program — {Client}

## 1. Cohort definition
- **Cohort unit:** account (B2B) vs user (B2C/PLG) — pick and justify.
- **Cohort grain:** weekly signup cohort (PLG) or monthly close-won cohort (SLG).
- **Segmentation axes:** ICP segment, acquisition channel, plan tier, vertical.

## 2. Retention curves
| Cohort | W1 | W2 | W4 | W8 | W12 | W26 | W52 | Flattening point |
|---|---|---|---|---|---|---|---|---|
| ... | ...% | ...% | ...% | ...% | ...% | ...% | ...% | ... |

**Smile curve check:** if curve flattens with re-engagement, marketing has a job. If it flattens at zero, product-market fit is the real problem and retention programs are lipstick.

## 3. Leading indicators of retention (measured in wk1–wk2)
| Indicator | Threshold | Lift vs non-crossers (r with w12 retention) |
|---|---|---|
| aha-event fired in d0 | yes | r = ... |
| ≥3 sessions wk1 | yes | r = ... |
| 2nd user invited | yes | r = ... |
| Integration connected | yes | r = ... |

Top 2 correlated indicators → set as activation goals (see `plg-conversion-audit.md`).

## 4. Program portfolio
| Program | Stage targeted | Trigger (from `behavioral-trigger-catalog.md`) | Primary metric | Holdout | Status |
|---|---|---|---|---|---|
| Activation nurture | New | T-001, T-002 | TTFV-p50 | 10% | live |
| Wk2 re-engage | Activated | T-003 | wk2 retention | 10% | live |
| Usage-dip save | Paid | T-006 | GRR | 10% | pilot |
| Expansion trigger | Habit | T-005 | expansion ACV | 10% | live |
| Advocacy | Paid | T-009 | NPS + reviews | — | live |
| Win-back | Churned | T-010 | reactivation % | 10% | pilot |

## 5. Measurement
- **Program-level:** lift on primary metric vs holdout over 60 days.
- **Portfolio-level:** NRR and GRR by segment vs plan target.
- **Attribution:** incrementality-first (see `skills/analytics/incrementality-test.skill.md`); don't over-credit last-touch email.

## 6. Kill rules
- Individual program: <2% lift on primary metric after 90 days → retire or redesign.
- Portfolio: if NRR drops >5pp quarter-over-quarter with no external shock → full-portfolio review + CS+Product joint diagnostic.

## 7. Quarterly ritual
- Redraw retention curves with new cohort data.
- Re-estimate leading-indicator correlations (behavior shifts as product/ICP evolves).
- Retire programs that underperform their holdout; birth new programs for uncovered stages.
