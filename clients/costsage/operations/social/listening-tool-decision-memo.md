---
artifact: listening-tool-decision-memo
date: 2026-04-30
recommendation: Google Alerts (free) + Mention free tier; upgrade to Brand24 at >50 mentions/wk
---

# Social Listening — Decision Memo

## Tier 1 (free, ship today)
**Google Alerts** — already provisioned per credential bundle.

Alerts to set up:
- `"CostSage"` (exact match)
- `costsage.ai` (domain)
- `"agentic finops"` (category claim)
- `"AWS cost optimization tool"` (high-intent category)
- `"FinOps platform"` (broader category)
- Competitor mentions: CloudZero, nOps, Vantage, ProsperOps, Cast AI, Finout

Frequency: as-it-happens for first 4; daily digest for category + competitors.

## Tier 2 (cheap, ship in week 2)
**Mention free tier** — 1 alert + 250 mentions/month.
Use case: real-time Twitter/X + Reddit + News mentions of "CostSage" with sentiment analysis Google Alerts doesn't have.

## Tier 3 (paid, ship at >50 mentions/week)
**Brand24** Mini plan ($69/mo): unlimited mentions, sentiment, source diversity, automated reporting.
Trigger to upgrade: when free Mention tier caps out or when we have meaningful mention volume to triage daily.

## Tier 4 (enterprise — defer)
Sprinklr, Brandwatch, Meltwater. $5K-50K/year. Not us at this stage.

## Recommendation summary

| Stage | Tool | Cost | Trigger |
|---|---|---|---|
| **Today** | Google Alerts | $0 | Already have it |
| **Week 2** | + Mention (free tier) | $0 | After 1st post goes live |
| **Q3/Q4** | Upgrade to Brand24 Mini | $69/mo | When mentions >50/week |
| **2027+** | Enterprise (Brandwatch / Sprinklr) | $$$$ | Only if mentions >5k/month |

## Daily ops once tools are wired

Each morning (~10 min):
1. Triage Google Alerts inbox → archive irrelevant, flag negative-sentiment for response
2. Review Mention dashboard for any mention requiring same-day response
3. Cross-reference against the V6 community-management SLA

## Operator confirmations

- [ ] Google account email for alerts (provisioned: "Saad Ahmed Vaival Account Email Account")
- [ ] Mention sign-up email (recommend: same)
- [ ] Brand24 plan budget approval (when tier-3 triggers)
