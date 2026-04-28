# Campaign Brief Template — CostSage.ai

> Single source of truth for a paid campaign. Copy this file, rename to `<channel>-<theme>-<quarter>.md`, and fill in every section before launch. No section may be left blank — use `[TBD-OPERATOR]` if a value depends on operator action (budget approval, ad-account, AWS Marketplace URL, etc.).

---

## 1. Meta
- **Campaign name:**
- **Channel / platform:**
- **Owner (DRI):**
- **Status:** draft / approved / live / paused / archived
- **Launch date:**
- **Review cadence:** weekly (Mon 10:00 GMT)
- **Linked OKR:** (link to `clients/costsage/okrs/`)

## 2. Objective
- **Primary:** (e.g., demo_request conversions on /aws)
- **Secondary:** (e.g., trial_start, branded-search lift)
- **North-star metric tied to this campaign:**

## 3. ICP & Audience
- **Persona(s):** (CTO / VP Eng / Head of Platform / FinOps lead) — link to `_audiences/icp-master.md`
- **Firmographics:** (AWS-first SaaS, 50–500 employees, $10K–$500K/mo cloud spend)
- **Geographies:** (US, CA, UK, EU-W, AU-NZ — tier 1 English)
- **Exclusions / anti-personas:** (students, agencies < 10 employees, individual hobbyists, current customers)
- **Audience spec (platform-native targeting JSON-equivalent):**

## 4. Hypothesis
> "We believe that <audience> with <pain point> will respond to <message> on <channel> and convert at <rate>, producing <CAC> within <LTV:CAC> of 3:1."

- **Disconfirming evidence we are watching for:**

## 5. Budget & Pacing
- **Monthly seed budget (USD):**
- **Daily cap:**
- **Bid strategy:** (Max conversions w/ tCPA / Manual CPC / etc.)
- **tCPA / tROAS target:**
- **Pacing rule:** spend ≤ 110% of daily cap; pause if 7-day spend > 130% w/o conversion lift.

## 6. Creative Spec
- **Ad formats:**
- **Headline bank ref:** `_creative/ad-copy-bank.md#<persona-stage>`
- **Description bank ref:**
- **CTA(s):**
- **Visual / video assets:** (path or "[TBD-DESIGN]")
- **Variant count at launch:** (min 3 per ad group)
- **Brand check passed:** y/n (link to `brand/` review)

## 7. Landing Page
- **Primary URL:**
- **Secondary URL (alt-test):**
- **CRO uplift required pre-launch?** y/n (see `_creative/landing-page-suitability.md`)
- **Above-the-fold message-match check:** y/n
- **Form fields captured:** (work email, company, role, monthly cloud spend)

## 8. Conversion Tracking
- **Primary event:** (e.g., `demo_request`) — full spec in `conversion-tracking-spec.md`
- **Secondary events:** (`form_start`, `trial_start`, `cta_click`)
- **Pixel / tag IDs:** (Google Ads conv ID, LinkedIn Insight Tag partner ID, Microsoft UET tag, Reddit Pixel, Meta Pixel) — `[TBD-OPERATOR]`
- **GTM trigger reference:** `analytics/tag-plan.md#<event>`
- **UTM template:** see `analytics/utm-convention.md`

## 9. KPIs & Success Criteria
| Tier | Metric | 30-day target | 60-day target | 90-day target |
|------|--------|---------------|---------------|---------------|
| Volume | Impressions | | | |
| Engagement | CTR | | | |
| Cost | CPC | | | |
| Conversion | CVR (LP→demo_request) | | | |
| Efficiency | CPA (per demo_request) | | | |
| Quality | SQL rate from leads | | | |
| Revenue | Pipeline $ created | | | |
| Efficiency | LTV:CAC (rolling 90) | ≥ 3:1 | ≥ 3:1 | ≥ 3:1 |

## 10. Kill-Switch / Pause Criteria
Pause and escalate if **any** of the following hold for 7 consecutive days:
1. CPA > 1.5× target with ≥ $500 spent.
2. CTR < 0.4× channel baseline with > 10K impressions.
3. CVR (LP→demo_request) < 0.3× site average with > 200 LP visits.
4. Lead quality: SQL rate < 10% across ≥ 25 leads.
5. Brand-safety incident (placement on excluded site, comment-section problem).

## 11. Decision Log
| Date | Decision | Rationale | Author |
|------|----------|-----------|--------|

## 12. Post-Mortem (fill at month 1, 2, 3)
- **What worked:**
- **What didn't:**
- **Hypothesis update:**
- **Decision:** scale / iterate / kill
- **Reusable creative / audience artifact created:**
- **Cross-pollination to other channels:**
