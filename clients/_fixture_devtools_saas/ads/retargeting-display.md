# Ads — Retargeting + Display (Q2)

## Segments
| Segment | Definition | Primary offer |
|---|---|---|
| R1 — Pricing visitors | Visited /pricing in last 30d, no form | Book a migration walkthrough |
| R2 — TCO-calc starters | Opened TCO calc, didn't complete | "Finish your TCO — 90s left" |
| R3 — Docs readers | Visited docs ≥3 pages, not signed up | Start free tier — 3 users, 5 flags |
| R4 — Comparison page | Visited /vs-launchdarkly | "Here's the case study of a team that did it" |
| R5 — Blog readers (pillar) | Read pillar TCO post | Download the ebook + calc |

## Creative rules
- ≥3 variants per segment.
- Frequency cap 3/day, 10/week.
- Hard refresh at 14 days; performance review at 7.

## Stop-loss
- Any segment ROAS <0.8 for 14d → pause.
- R3 not converting signups at >2% in 21d → re-brief.

## UTMs
`utm_medium=retargeting&utm_campaign=2026-q2-retarget-{segment}`

## Platform compliance
- GDPR: consent-based retargeting; EU audiences excluded if consent missing.
- CCPA: honor DNT / opt-out signals.
