---
artifact: stop-loss-rules
date: 2026-04-30
purpose: prevent runaway spend or worthless impressions across all paid channels
---

# Stop-Loss + Budget Caps

## Per-channel daily / weekly / monthly caps

| Channel | Daily cap | Weekly cap | Monthly cap | CPL ceiling | Auto-pause if |
|---|---|---|---|---|---|
| Google Search AWS Cost Tools | $50/day | $300 | $1,500 | $400 | CTR <1% over 200 impressions |
| Google Search FinOps Platform | $40/day | $250 | $1,000 | $400 | CTR <1% over 200 impressions |
| LinkedIn CTO | $67/day | $400 | $2,000 | $1,200 | CPC >$15 over 50 clicks |
| LinkedIn FinOps Lead | $67/day | $400 | $2,000 | $900 | CPC >$10 over 50 clicks |
| Microsoft Bing | $25/day | $150 | $750 | $400 | CTR <0.8% over 200 impressions |
| Reddit (when launched) | $17/day | $100 | $500 | $250 | CTR <0.4% over 500 impressions |
| Capterra/G2 (when launched) | varies | $250 | $1,000 | $500 | CPL >$500 |

**Total month-1 spend cap: $5,000.** This matches the controlled budget pacing model.

## CTR / CPC / CVR floors and ceilings

For each channel + ad group, the system pauses if any of these breach:
- **CTR < 0.5× target** for 72 hours: **PAUSE creative**, swap to next variant
- **CPC > 2× target** for 72 hours: **PAUSE keyword**, increase negative-keyword list
- **Conv rate < 0.5× target** over 100 clicks: **PAUSE landing page**, route to fallback URL
- **No conversion** after $500 spent: **PAUSE campaign**, manual review

## Daily QA checklist (per active campaign)

Run every 09:00 UTC + every 17:00 UTC:
- [ ] Yesterday's spend within daily cap?
- [ ] Yesterday's CTR within target range?
- [ ] Yesterday's conversions tracked correctly (no pixel fires missing)?
- [ ] Any 4xx / 5xx errors on landing pages?
- [ ] Any negative-sentiment comments on the ad?
- [ ] Any anomalies on competitor bidding (sudden spike from CloudZero/nOps/Vantage)?

If anything flags red: pause + investigate; resume once root cause identified.

## Auto-pause script logic

A simple cron-driven check (`/opt/costsage-sprint1/paid-stop-loss.sh`) runs every 4 hours:

```bash
#!/bin/bash
# Pseudo-code — actual implementation requires platform APIs
# For each (channel, campaign):
#   metric = pull_metrics(channel, campaign, last_72h)
#   if metric.spend > daily_cap: pause; alert founder
#   if metric.ctr < target.ctr * 0.5: pause; alert
#   if metric.cpl > target.cpl_ceiling: pause; alert
#   if metric.cpc > target.cpc_ceiling: pause; alert
```

Implementation requires:
- Google Ads API token
- LinkedIn Ads API token
- Microsoft Advertising API token
- Slack webhook (V3 dependency)

## Stop-loss escalation

When auto-pause triggers:
1. Slack notification to `#paid-alerts` (channel TBD-OPERATOR)
2. Email to performance lead + founder
3. Auto-pause stays in effect until human resumes
4. Post-mortem within 48h: what triggered + what to change

## Resume rules

After a pause, before resume:
- [ ] Root cause identified (audience? creative? landing page? keyword?)
- [ ] Fix shipped (new creative, new keywords, LP change)
- [ ] Test budget (50% of original cap for 72h) before full resume
- [ ] If second pause within 14 days on same campaign: kill the campaign

## Operator confirmations

- [ ] Daily budget approval per channel (matrix above)
- [ ] CPL ceilings approved (these are working assumptions)
- [ ] Slack channel for #paid-alerts
- [ ] On-call rotation for after-hours pauses
- [ ] CRO budget for landing-page experiments when LP itself is the issue
