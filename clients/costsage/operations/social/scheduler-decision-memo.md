---
artifact: scheduler-decision-memo
date: 2026-04-30
recommendation: Buffer (Essentials, ~$15/month per channel)
---

# Social Scheduler — Decision Memo

## Comparison

| Tool | Monthly cost | Channels | Scheduling | Analytics | Content library | Team collab | Notes |
|---|---|---|---|---|---|---|---|
| **Buffer Essentials** | $15/channel | LinkedIn / X / IG / FB / TikTok / Pinterest / YouTube | ✅ | Light | ✅ | $10/user add-on | Best fit at our scale |
| Hootsuite Professional | $99/mo | 10 channels | ✅ | Strong | ✅ | ✅ | Pricey for 1-channel start |
| Later | $25/mo | LinkedIn + 5 others | ✅ | Strong (visual) | ✅ | $25/user | Best for IG-heavy; not us |
| Sprout Social Standard | $249/user/mo | 5 channels | ✅ | Best in class | ✅ | $249/user | Enterprise — overkill |
| Native LinkedIn API | Free + dev time | LinkedIn only | ✅ (custom) | API-driven | DIY | Code-managed | Build it yourself; not staff-cheap |
| Publer | $12/mo | LinkedIn / X / FB / IG | ✅ | Medium | ✅ | $5/user | Closest Buffer alternative |

## Recommendation: **Buffer Essentials**

At our current scale (1-2 founders + 1 marketing operator + LinkedIn + X = 2 channels):
- Buffer Essentials covers it: ~$30/month for 2 channels
- Free trial available; no card required to test
- Mobile + desktop apps mature
- API-friendly if we want automation later
- Migration path to Hootsuite or Sprout when team grows past 5

## Why not native LinkedIn API
We could write our own scheduler against the LinkedIn API. We won't, because the engineering hours cost > 10 months of Buffer subscription, and we'd build a worse version of what already exists.

## Why not "free" options (e.g., LinkedIn's native scheduler)
LinkedIn's native scheduling exists but is feature-poor: no team collaboration, no draft pipeline, no cross-channel coordination. Buffer adds ~$30/month for substantially better workflow.

## What this unblocks
Once Buffer is provisioned (operator OD11), V6 becomes operational:
- Posting queue weeks 1-12 (200+ items already drafted) can schedule
- Listening map + analytics auto-populate Buffer's dashboard
- Founder amplification kit triggers based on company-page posts

## Operator action

1. Sign up at buffer.com (Essentials tier, 2 channels)
2. Connect LinkedIn company page + X account [TBD-OPERATOR]
3. Generate API access token (Settings → Apps & Integrations → API Access)
4. Vault as `vault://costsage/buffer/api-token`
5. Confirm channel limits (we'll alert if approaching)

ETA after operator action: 24h to first scheduled post.
