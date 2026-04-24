# Battlecard — Loopgate vs Statsig

> Last reviewed: 2026-04-23.

## Cheat Card
- **They are:** experimentation-first platform, strong stats, generous free tier.
- **When we win:** platform teams where flagging discipline matters more than experiment-stats depth; audit-regulated buyers; teams already running homegrown flags who want a unified platform.
- **When they win:** product-analytics-first buyers, experimentation-heavy orgs with small eng teams, teams where Product (not Platform) owns the tool.
- **3 discovery Qs:**
  1. "Who's the primary buyer — Platform/DevEx or Product?"
  2. "Do flagging and experimentation share an audit trail today?"
  3. "What's your compliance posture? SOC2? SOX?"
- **Top rebuttal:** "Statsig is great for experimentation-first teams with Product driving. For Platform-driven orgs with audit + SOC2 needs, unified flags+experiments on one trail is our wedge — not experimentation depth."

## Full Card

### Who they are
Experimentation + flagging platform. Strong stats engine. Free tier is generous (up to 1M events/mo in places). Primarily adopted by PM/growth orgs.

### Why they win
1. **Stats engine depth.** CUPED, sequential testing, bandits — well-known team.
2. **Free tier.** Low adoption friction.
3. **Product-led buyer.** Sells well where PMs drive tool selection.

### Why we win
1. **Audit + compliance posture.** SOC2 Type II, SOX-grade change log, SSO/SCIM in Business — Statsig's enterprise governance is younger.
2. **Platform-team fit.** We are tuned to DevEx/Platform priorities (SDK perf, self-host, trunk-based flagging discipline).
3. **Unified source of truth.** Flags and experiments share permission model + audit trail — Statsig's architecture is experimentation-first with flagging as an add-on.

### Trap-setting discovery questions
1. "Who adjudicates when experiment results disagree with feature-flag state?"
2. "When SOC2 asks about feature-flag change approval, what do you show them?"
3. "What's your p95 SDK eval requirement?"
4. "How important is self-host to your security team?"

### Objection library
| They say | Rebuttal |
|---|---|
| "Statsig has better stats" | We OSS'd our stats engine; reviewed by [named statistician]; CUPED + sequential + SRM checks standard |
| "Statsig is cheaper (free tier)" | At our ICP scale (50–500 eng) Statsig's paid tiers arrive; compare at scale, not at zero |
| "We already use Statsig for experimentation" | Co-exist or consolidate — we plug in below for flags, above for unified audit. 3 case studies |
| "Switching is painful" | Migrator for flag definitions; experiments can be re-pointed without re-wiring |

### Switch playbook
Map experiment definitions to Loopgate; re-instrument SDK (10-min); parallel-run for 2 weeks; cut over.

### Landmines
- Product-led org where PM is buyer and experimentation depth is the only need: Statsig wins.
- Pre-Series-A startup: Statsig free tier is fine.
