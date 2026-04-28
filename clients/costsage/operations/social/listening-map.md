# Social Listening Map

Tooling: [TBD-OPERATOR — recommend Brand24, Mention, or free combo of Google Alerts + TweetDeck/X Pro + Reddit RSS].

---

## Brand-mention queries

Run on X, LinkedIn, Reddit, Hacker News, Google Alerts.

- `"costsage"`
- `"cost sage"` (likely typo variant)
- `costsage.ai`
- `"@costsage"` (X)
- `site:reddit.com costsage`
- `site:news.ycombinator.com costsage`

Alert response SLA: <4 business hours.

---

## Category / topic keywords (always-on)

For sourcing engagement opportunities, not for direct response.

- `"AWS cost optimization"`
- `"cloud cost optimization"`
- `"FinOps tool"` / `"FinOps tooling"`
- `"savings plans" AWS`
- `"reserved instances" optimize`
- `"cloud bill" surprised OR shocked OR huge`
- `"AWS bill" review`
- `"Kubernetes cost"`
- `"GPU cost" AWS`
- `"agentic AI" FinOps OR cost`
- `"untagged" AWS spend`
- `"unit economics" cloud`

---

## Competitor-mention queries

Listen, don't intercept. Use for positioning intel and to spot dissatisfaction (which is engagement gold for *content*, not for hijacking).

- `"cloudzero"` cost OR finops
- `"nops"` aws OR finops
- `"vantage"` cost
- `"cloudability"`
- `"apptio"` finops
- `"finout"`
- `"prosperops"`
- `"cudos"` (open-source) — relevant for build-vs-buy threads

Rule: never reply to a competitor-mention thread to push CostSage. Use for content ideation only.

---

## Influencer / practitioner list (10) — follow + engage

| # | Name / Handle | Why follow | Engagement style |
|---|---|---|---|
| 1 | J.R. Storment ([TBD-OPERATOR confirm handle]) | Co-author "Cloud FinOps", FinOps Foundation co-founder | Thoughtful comment on FinOps posts; never link CostSage |
| 2 | Mike Fuller (FinOps Foundation) | Industry voice | Helpful comment on technical posts |
| 3 | Corey Quinn / @QuinnyPig | Snark + AWS pricing expertise; huge audience | Light engagement, never pitch |
| 4 | Forrest Brazeal / @forrestbrazeal | AWS cloud cartoonist + writer; resharable | Comment + occasional reshare |
| 5 | Jeremy Daly / @jeremy_daly | Serverless cost expertise | Substantive technical comments |
| 6 | Eoin Shanaghy ([TBD-OPERATOR]) | AWS cost speaker | Engage on talks |
| 7 | Sebastian Stadil | FinOps practitioner | DM-worthy for community building |
| 8 | Erik Peterson (CTO, CloudZero) | Competitor founder, valuable POV | Polite engagement only, never antagonistic |
| 9 | Aran Khanna | Cloud cost-economics writer | Engage on long-form |
| 10 | Pavlos Mitsoulis-Ntompos | FinOps practitioner | Comment on practical posts |

[TBD-OPERATOR]: refresh quarterly; replace any handle that goes inactive.

---

## Hashtags to monitor (X + LinkedIn)

- #FinOps
- #AWSCost
- #CloudCost
- #SavingsPlans
- #ReservedInstances
- #AgenticAI (rising)
- #CloudEconomics
- #AWSReInvent (event spikes)

---

## Subreddit feeds

Pull RSS for:
- reddit.com/r/aws/.rss
- reddit.com/r/FinOps/.rss
- reddit.com/r/devops/.rss
- reddit.com/r/sre/.rss
- reddit.com/r/kubernetes/.rss

Feed → daily digest → operator triage 10 min/day.

---

## Response decision tree

```
Mention detected
├── Is it our brand? 
│   ├── Positive → reply with thanks, no pitch
│   ├── Question → answer publicly, fast
│   └── Negative/complaint → reply ack + DM offer to make it right
├── Is it a category keyword?
│   ├── Genuine question we can answer → comment with value, mention CostSage only if perfectly on-topic + disclose
│   └── Vendor-shopping thread → wait for organic mention; don't volunteer
└── Is it a competitor mention?
    └── Don't engage. Note for content ideation.
```

---

## Weekly listening review (15 min, Monday)

1. Volume: total brand mentions vs last week.
2. Sentiment: any negative threads needing follow-up.
3. Category opportunities missed: any high-engagement threads we didn't comment on?
4. Influencer interactions logged.
5. One content idea pulled from listening.

[TBD-OPERATOR]: ESP/listening tool selection determines exact alert delivery.
