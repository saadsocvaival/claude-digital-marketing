# KPI Dictionary — CostSage.ai

> Every metric has: name, formal definition, formula, data source, freshness target, owner, dashboard tab. Grouped by AARRR funnel stage.

## A. Acquisition (Top of funnel)

| # | KPI | Definition | Formula | Source | Freshness | Owner | Dashboard tab |
|---|-----|------------|---------|--------|-----------|-------|----------------|
| 1 | Sessions | Unique browsing sessions on costsage.ai | GA4 sessions | GA4 | Hourly | SEO Lead | Acquisition |
| 2 | Users | Distinct users (cookied) | GA4 users | GA4 | Hourly | SEO Lead | Acquisition |
| 3 | New users % | New / total users | new_users / users | GA4 | Daily | SEO Lead | Acquisition |
| 4 | Organic sessions | Sessions with `medium=organic` | GA4 filter | GA4 | Hourly | SEO Lead | Acquisition |
| 5 | Paid clicks | Clicks from paid channels | sum(paid platforms clicks) | Ad APIs | Daily | Paid Media | Acquisition |
| 6 | Paid impressions | Impressions paid | sum(paid platforms imp) | Ad APIs | Daily | Paid Media | Acquisition |
| 7 | Paid CTR | Clicks / impressions | clicks/imp | Ad APIs | Daily | Paid Media | Acquisition |
| 8 | Paid CPC | Avg cost per click | spend/clicks | Ad APIs | Daily | Paid Media | Acquisition |
| 9 | Branded search clicks | Search Console clicks for brand queries | GSC | GSC | Daily | SEO Lead | Acquisition |
| 10 | Non-branded organic clicks | GSC clicks - branded clicks | GSC | GSC | Daily | SEO Lead | Acquisition |
| 11 | Channel mix | % sessions by channel | GA4 channel grouping | GA4 | Daily | CMO | CMO |

## B. Activation (Engaged → Lead)

| # | KPI | Definition | Formula | Source | Freshness | Owner | Tab |
|---|-----|------------|---------|--------|-----------|-------|-----|
| 12 | Engaged session rate | GA4-defined engaged session % | engaged/total | GA4 | Daily | Web Lead | Web/CRO |
| 13 | Scroll-75 rate | scroll_75 events / page_views | events ratio | GA4 | Daily | Web Lead | Web/CRO |
| 14 | CTA click rate (per CTA) | cta_click / page_view (per cta_id) | ratio | GA4 | Daily | Web Lead | Web/CRO |
| 15 | Form-start rate | form_start / form-page sessions | ratio | GA4 | Daily | Web Lead | Web/CRO |
| 16 | Form-completion rate | form_submit / form_start | ratio | GA4 | Daily | Web Lead | Web/CRO |
| 17 | LP CVR (paid) | demo_request / paid LP sessions | ratio | GA4+UTMs | Daily | Paid Media | Acquisition |
| 18 | Newsletter signups | form_submit where form_id=newsletter | count | GA4/ESP | Daily | Content Lead | Acquisition |
| 19 | Demo requests (count) | demo_request events | count | GA4 | Hourly | RevOps | Pipeline |
| 20 | Demo-show rate | demos held / demos requested | held/req | CRM | Weekly | RevOps | Pipeline |

## C. Revenue (Lead → Customer → $)

| # | KPI | Definition | Formula | Source | Freshness | Owner | Tab |
|---|-----|------------|---------|--------|-----------|-------|-----|
| 21 | SQLs | demo_request leads marked SQL | count | CRM | Daily | RevOps | Pipeline |
| 22 | SQL rate | SQLs / demo_requests | ratio | CRM | Daily | RevOps | Pipeline |
| 23 | Opportunities | Open opps | count | CRM | Daily | RevOps | Pipeline |
| 24 | Opp creation rate | Opps / SQLs | ratio | CRM | Weekly | RevOps | Pipeline |
| 25 | Pipeline $ | sum(opp ARR) | sum | CRM | Daily | RevOps | Pipeline |
| 26 | Pipeline coverage | Pipeline $ / quarterly target | ratio | CRM | Weekly | CMO | CMO |
| 27 | Win rate | closed_won / (closed_won + closed_lost) | ratio | CRM | Monthly | RevOps | Pipeline |
| 28 | Avg deal size (ACV) | sum(arr)/count(closed_won) | mean | CRM | Monthly | RevOps | CMO |
| 29 | New ARR ($) | sum ARR closed_won this period | sum | CRM | Daily | RevOps | CMO |
| 30 | Sales-cycle length (days) | mean days(opp_create → closed) | mean | CRM | Weekly | RevOps | Pipeline |
| 31 | CAC (paid) | paid spend / new customers acquired (paid-attributed) | ratio | Ad APIs + CRM | Monthly | CMO | CMO |
| 32 | LTV (margin-adjusted) | gross margin × ARR × avg lifetime | calc | Finance | Quarterly | CFO | CMO |
| 33 | LTV:CAC | LTV / CAC | ratio | Finance | Monthly | CFO | CMO |
| 34 | Payback period (months) | CAC / (monthly margin contribution) | ratio | Finance | Monthly | CFO | CMO |

## D. Retention & Lifecycle

| # | KPI | Definition | Formula | Source | Freshness | Owner | Tab |
|---|-----|------------|---------|--------|-----------|-------|-----|
| 35 | Trial-to-paid conversion | paid_after_trial / trial_start | ratio | App + CRM | Weekly | PM/Growth | Lifecycle |
| 36 | Activation rate | trial_complete / trial_start | ratio | App | Weekly | PM | Lifecycle |
| 37 | Time-to-activation (days) | median days trial_start → trial_complete | median | App | Weekly | PM | Lifecycle |
| 38 | Logo retention (12mo) | retained / starting cohort | ratio | CRM | Monthly | CS | Lifecycle |
| 39 | NRR (Net Revenue Retention) | (start ARR + expansion − churn − contraction) / start ARR | calc | Finance | Monthly | CFO | CMO |
| 40 | GRR (Gross Revenue Retention) | (start − churn − contraction)/start | calc | Finance | Monthly | CFO | Lifecycle |
| 41 | Churned ARR ($) | sum lost ARR | sum | CRM | Monthly | CS | Lifecycle |
| 42 | Newsletter open rate | opens/sent | ratio | ESP | Per send | Email Lead | Lifecycle |
| 43 | Newsletter CTR | clicks/sent | ratio | ESP | Per send | Email Lead | Lifecycle |

## E. Referral / Expansion

| # | KPI | Definition | Formula | Source | Freshness | Owner | Tab |
|---|-----|------------|---------|--------|-----------|-------|-----|
| 44 | Expansion ARR ($) | upsell + cross-sell ARR | sum | CRM | Monthly | CS | Lifecycle |
| 45 | Referral leads | leads w/ source=referral | count | CRM | Weekly | RevOps | Pipeline |
| 46 | NPS | (% promoters − % detractors) | NPS | Survey | Quarterly | CS | Lifecycle |
| 47 | G2/Capterra review velocity | new reviews / month | count | Review platforms | Monthly | CS | CMO |

## F. Web / CRO Health

| # | KPI | Definition | Formula | Source | Freshness | Owner | Tab |
|---|-----|------------|---------|--------|-----------|-------|-----|
| 48 | Lighthouse perf score (median) | median across 18 URLs | median | Lighthouse CI | Daily | Web Lead | Web/CRO |
| 49 | LCP (median) | Largest Contentful Paint median | ms | Lighthouse CI / CrUX | Daily | Web Lead | Web/CRO |
| 50 | INP (median) | Interaction to Next Paint median | ms | CrUX | Weekly | Web Lead | Web/CRO |
| 51 | CLS (median) | Cumulative Layout Shift | unitless | CrUX | Weekly | Web Lead | Web/CRO |
| 52 | 4xx/5xx rate | error responses / total | ratio | Server logs | Hourly | Web Lead | Web/CRO |
| 53 | Search impressions (GSC) | total impressions | count | GSC | Daily | SEO Lead | Web/CRO |

## G. Operational / Cost-of-Marketing

| # | KPI | Definition | Formula | Source | Freshness | Owner | Tab |
|---|-----|------------|---------|--------|-----------|-------|-----|
| 54 | Total marketing spend | sum paid + tools + headcount | sum | Finance | Monthly | CMO | CMO |
| 55 | Spend pacing % | actual / planned (MTD) | ratio | Finance | Daily | CMO | CMO |
| 56 | Cost per demo (blended) | total spend / demo_requests | ratio | mixed | Weekly | CMO | CMO |
| 57 | Cost per SQL (blended) | total spend / SQLs | ratio | mixed | Weekly | CMO | CMO |

**Total entries: 57.**
