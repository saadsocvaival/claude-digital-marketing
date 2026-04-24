# Eval Harness — Golden Cases

Each eval = input fixture + expected output shape + rubric gate (≥8).

## Cases
1. `01-icp-builder.md` — Given ledger excerpt, produce ICP that scores ≥8 on `rubrics/icp.yaml`.
2. `02-positioning.md` — Given ICP + product notes, produce Moore positioning statement ≥8 on `rubrics/positioning.yaml`.
3. `03-messaging.md` — From positioning, produce 3 pillars + 10 objections ≥8.
4. `04-seo-brief.md` — From a target query + SERP paste, produce SEO brief ≥8.
5. `05-keyword-research.md` — Query + business context → cluster with primary + 5–15 secondaries + intent classification.
6. `06-ad-copy.md` — From messaging + offer, produce 3 ad variants ≥8 on `rubrics/ad-copy.yaml`.
7. `07-email-sequence.md` — From goal (activation / nurture / winback), produce 5–7 email sequence ≥8.
8. `08-lp-brief.md` — From ad promise, produce LP brief with message-match ≥8.
9. `09-battlecard.md` — From competitor name + ICP, produce battlecard ≥8.
10. `10-campaign-brief.md` — From objective + budget, produce campaign brief with stop-loss, launch gate, UTMs ≥8.

## Run

Manual (today): open a Claude Code session, paste the input fixture from a case file, run the skill, then grade the output with its rubric.

Automated (Stage 2.5 follow-up): spawn quality-assurance subagent with input + rubric; assert score ≥8; fail the run on regression.

## Acceptance
All 10 cases pass (≥8) on at least 3 independent runs before declaring the skill "golden". Any regression to <8 blocks the change.
