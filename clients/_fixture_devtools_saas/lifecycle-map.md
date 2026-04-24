# Loopgate — Lifecycle Map

## 1. Lifecycle stages
| Stage | Entry | Exit | Goal |
|---|---|---|---|
| Lead | form fill on pricing / demo / content | signup completed or 30d no action | complete signup |
| New | workspace created | first-flag-toggled-in-prod (aha) | aha within 7d |
| Activated | aha fired | 3+ sessions wk2 | form habit |
| Habit | engaged wk2 | upgrade or decay | monetize |
| Paid | paid plan or annual contract | expansion signal or downgrade | retain |
| Expansion | +3 editors in 30d OR usage >80% cap | renewal / next tier | grow ARR |
| At-Risk | flag-creation <40% cohort p50 over 30d | re-engage or churn | save |
| Churned | cancel | win-back at d60 | win-back |

## 2. Trigger→message table (abbreviated; full catalog in `behavioral-trigger-catalog.md`)
| Trigger ID | Stage | Message | Channel | KPI | Holdout |
|---|---|---|---|---|---|
| T-001 | New | "2 minutes to your first flag in prod" | email+in-app | TTFV-p50 | 10% |
| T-002 | New | AE-personal email (ICP-A only, aha not fired in 72h) | email | activation-assist rate | 10% |
| T-003 | Activated | re-engage digest | email+push | wk2 retention | 10% |
| T-004 | Habit | upgrade banner (usage >80% cap) | in-app+email | PLG→paid conv | 10% |
| T-005 | Habit | expansion AE outreach (+3 editors in 30d) | AE email | expansion ACV | 10% |
| T-006 | Paid | CS alert + usage-dip email | email | GRR | 10% |
| T-009 | Paid | advocacy invite (NPS≥9 + 90d) | email | references count | — |
| T-010 | Churned | win-back (d60) | email | reactivation % | 10% |

## 3. Suppression
- 3 marketing emails/week cap; 1 sales/week.
- Pause marketing during open sev-1/2 ticket.
- No upgrade CTA within 7d of downgrade.
- Time-zone aware send.

## 4. Measurement
- Every program has 10% holdout, assigned at first-eligible.
- 60-day lift vs holdout = program retention criterion (≥2% primary metric lift).
- Dashboard owner: Head of Automation; review monthly with Motion leads.

## 5. Ownership
- Map owner: Head of Automation
- Stage reviews: Motion-Acquisition (Lead→New), Motion-Activation (New→Habit), Motion-Retention (Paid→Churned)

---
**Self-score:** 84/100 — concrete triggers, holdout discipline. Loses points on: 30-day correlations still TBD with real data; T-007/T-008/T-011 not instantiated in this fixture slice (in full catalog).
**Critic-score:** TBD.
