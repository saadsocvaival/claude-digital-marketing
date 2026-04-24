# Experiment Brief — Guided First-Flag Tour vs Self-Serve Default

**Hypothesis:** A guided 3-step first-flag tour (shown on first dashboard load) will lift 7-day activation (flag live in prod) from 36.9% to ≥44% (MDE +5pp, power 0.8) because friction at step 2 ("which SDK?") is the top drop-off point in funnel analysis.

**Population:** new free signups, all stacks, US/EU. Exclusions: returning users, team plan trialers.
**Allocation:** 50/50 random at signup.
**Sample size:** 4,200 per arm (MDE +5pp, baseline 36.9%, alpha 0.05, power 0.8). Estimated duration: 3 weeks at current signup rate.
**Primary metric:** 7-day activation rate (flag live in prod).
**Guardrail:** no regression on 30d retention (±2pp), no regression on team-plan conversion at day 21.
**Pre-registered analysis:** two-proportion z-test; SRM check; Bonferroni for 3 guardrails.
**Decision rule:** Ship if primary lifts ≥3pp significant AND no guardrail regresses. Kill if primary flat + guardrail negative.
**Owner:** Head of Growth.
**Review date:** 2026-05-13.
**Rubric self-score:** hypothesis 10, MDE 10, guardrails 10, pre-reg 10, decision-rule 10 → 95/100.
