# PLG Conversion Audit — {Client}

## 1. Funnel spine
| Stage | Definition | Current rate | Benchmark | Gap |
|---|---|---|---|---|
| Visit → signup | ... | ...% | 3–8% (LP) | ... |
| Signup → activation | reached aha-event | ...% | 25–40% | ... |
| Activation → habit | 3+ sessions wk2 | ...% | 40–60% | ... |
| Habit → paid | self-serve upgrade | ...% | 3–8% (PLG SaaS) | ... |
| Paid → expansion | seat / usage growth | ...% | 15%+ MoM (NRR >120%) | ... |

## 2. Aha-event definition
- **Event:** {exact product action — e.g., "created first feature flag and toggled in production"}
- **Time-to-aha p50:** target ≤5 min, current ...
- **Time-to-aha p90:** target ≤24 h, current ...
- **Aha-correlation with wk4 retention:** r = ...

## 3. Friction diagnostic (per stage)
For each stage below benchmark, complete:
- **Drop-off step:** specific screen / event
- **Hypothesized cause:** {technical | cognitive | motivational | trust}
- **Data evidence:** session replay count, error rate, time-on-step
- **Proposed fix:** specific change
- **MDE-feasibility:** do we have traffic to test this? (see `experiment-program.skill.md`)

## 4. In-product conversion surfaces
| Surface | Owner | Current conversion | Test queue |
|---|---|---|---|
| Empty-state CTAs | ... | ... | ... |
| Paywall modals | ... | ... | ... |
| Usage-limit banners | ... | ... | ... |
| Upgrade page (in-app) | ... | ... | ... |
| Trial-ending emails + in-app | ... | ... | ... |
| Feature-gate peeks | ... | ... | ... |

## 5. Pricing-page handoff
- **% of in-app upgrade clicks landing on pricing page:** ...
- **% of those converting within 7 days:** ...
- **Drop point:** ...

## 6. Onboarding checklist health
- Completion rate: ...%  (target ≥60%)
- Avg items completed: ... / ...
- Correlation between checklist completion and wk4 retention: r = ...
- Items with <30% completion = candidates for deletion (over-scoped checklist hurts more than helps).

## 7. Sales-assist triggers (PLG+SLG)
- **Trigger 1:** workspace adds 3+ users in 7 days → AE outreach within 48h
- **Trigger 2:** usage >80% of plan cap → upgrade flow + AE for Mid-Market+
- **Trigger 3:** domain matches target-account list → AE assigned at signup

## 8. Instrumentation audit
- [ ] All funnel events defined and firing consistently
- [ ] Aha-event landed in warehouse and joined to user/account
- [ ] Session replay sampled ≥1% per stage
- [ ] Activation cohort dashboard exists and is loved (used weekly by ≥2 stakeholders)

## 9. Top-5 remediation (ranked by expected lift × reach)
1. ...
2. ...
3. ...
4. ...
5. ...
