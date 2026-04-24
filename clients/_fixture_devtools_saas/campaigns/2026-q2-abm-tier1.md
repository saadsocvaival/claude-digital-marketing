# Campaign Brief — Q2 ABM Tier-1 (20 accounts)

**Objective:** Demand generation at named enterprise accounts; book discovery with Platform EB.
**ICP:** 20 target accounts matching ideal enterprise pattern (fintech/marketplace/health, 200–500 eng, on LD or homegrown, SOC2/SOX in-scope). List maintained in `memory/shared/abm-tier1.yaml`.
**Budget:** $24k over 10 weeks.

## Creative plays (3)
| Variant | Channel | Offer | Proof |
|---|---|---|---|
| A — LinkedIn IP-targeted | LinkedIn paid (company targeting) | Custom TCO calc for their eng-count | "We'll run the numbers for you — reply or message" |
| B — Handwritten direct mail | Mail (addressed to Head of Platform) | Printed compliance-audit checklist + gift card | "Audit's coming. We'll buy you coffee while you read this." |
| C — Personalized microsite | Email (SDR) → per-account LP | Pre-filled comparison calculator + case-study matched by vertical | — |

## SDR playbook
- 5-touch sequence (email → LinkedIn DM → email → call → LinkedIn video) over 14 days.
- Trap-setting questions from `battlecards/launchdarkly.md`.
- Meeting → handoff to AE within 4h.

## Measurement
- Primary: meetings booked at Tier-1 accounts (target 6/20 in 10 weeks).
- Secondary: engaged accounts (website + content engagement ≥3 touches), pipeline $ opened.
- Attribution: account-level (not lead-level) — BigQuery model required.

## Stop-loss / gate
- Budget burn >50% at week 5 with <3 meetings → restructure message.
- Creative fatigue: LinkedIn frequency >5 on any account → rotate.

## UTMs
`utm_campaign=2026-q2-abm-tier1&utm_content=account-{acct-id}`

## Launch gate
- [ ] Account list approved (VP Marketing + CEO)
- [ ] Legal sign-off on direct-mail copy
- [ ] CRM account-based reporting view built
- [ ] SDR playbook + training complete
