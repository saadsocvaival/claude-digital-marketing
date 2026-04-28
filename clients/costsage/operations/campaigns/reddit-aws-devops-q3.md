# Reddit Ads — AWS / DevOps / SRE / FinOps — Q3

> Reddit users resist hard-sell; lead with content + community-native voice. Promote a guide, not a demo.

## 1. Meta
- **Campaign name:** RDT_AWS_DevOps_Q3.
- **Platform:** Reddit Ads (Reddit Ads Manager).
- **Owner:** Paid Media DRI.
- **Status:** draft. `[TBD-OPERATOR: Reddit Ads account; Reddit Pixel installed via GTM]`.

## 2. Objective
- **Objective:** Traffic + Conversions (`cta_click[cta_aws_best]` and newsletter `form_submit` on `/blog/aws-cost-optimisation-best-practices`).
- **Secondary:** `demo_request` from longer-arc retargeting (handled in another campaign).

## 3. Audience
- **Subreddit targeting (community targeting — primary):**
  - r/aws
  - r/devops
  - r/sre
  - r/FinOps
  - r/kubernetes
  - r/Terraform
  - r/awscertifications (light; informational visitors)
  - r/sysadmin (filtered via interest)
  - r/programming (broad — bid lower)
  - r/ExperiencedDevs (engineering leaders)
- **Interest targeting (layer):** Cloud Computing, DevOps, Software Development, Information Technology.
- **Geos:** US, CA, UK, IE, AU, NZ.
- **Devices:** all; mobile bid −10%.
- **Excluded:** subreddits unrelated to professional infra (r/jokes, r/funny, etc. — Reddit auto-handles via the "Conversation/Community" mode but explicit block list applies).

## 4. Hypothesis
> Reddit users in infra-pro subreddits engage with native-tone, content-led ads at 2–3× CTR of branded ads; the funnel is content read → newsletter → demo over 30–60 days, not direct demo.

## 5. Budget
- **Monthly seed:** $500 ($16/day).
- **Bid:** CPC manual $0.50–$1.50; Reddit Ads Manager auto-bidding once 50 conv recorded.

## 6. Creative (4 variants)

### Ad-1 — Image post (native voice)
- Headline: "We wrote the playbook we wished existed for cutting AWS waste at SaaS scale."
- Body: "Posting our AWS cost-optimization best-practices guide. 0 fluff, real RI/SP math, real rightsizing flow. Free, no email gate to read; we save the demo for if you're curious." (Native, low-pitch tone.)
- Image: clean diagram preview from the guide.
- CTA: "View Link" → `/blog/aws-cost-optimisation-best-practices`.
- `cta_id=rdt_ad1_guide`.

### Ad-2 — Image post (RI/SP focus)
- Headline: "RIs vs Savings Plans — when each one beats the other (with the math)."
- CTA → `/blog/ri-vs-savings-plans`.
- `cta_id=rdt_ad2_risp`.

### Ad-3 — Image post (BOFU, demo for curious)
- Headline: "Built CostSage because we got tired of the CUR. Demo if interested."
- Body: tone like an HN comment, not a marketing pitch. Names the product once.
- CTA → `/aws`.
- `cta_id=rdt_ad3_aws`.

### Ad-4 — Conversation Placement (text-only, in-feed)
- Headline: "If you've ever spent a Friday hunting an AWS cost spike, you'll get this."
- Body: 2-line empathy + link to blog.
- CTA → `/blog/aws-cost-optimisation-best-practices`.
- `cta_id=rdt_ad4_text`.

## 7. Landing Pages
- Primary: `/blog/aws-cost-optimisation-best-practices`.
- Secondary: `/blog/ri-vs-savings-plans`, `/aws` (BOFU only).
- LP must have content-upgrade form (newsletter) and inline `/aws` CTA — see `_creative/landing-page-suitability.md`.

## 8. Conversion Tracking
- Reddit Pixel via GTM.
- Conversion events:
  - `RDT_blog_view` (`page_view` on `/blog/*`).
  - `RDT_newsletter_signup` (`form_submit` with `form_id=newsletter`).
  - `RDT_cta_click` (any `cta_click`).
  - `RDT_demo_request` (BOFU, low volume expected).
- Attribution: 30-day click + 1-day view.
- UTM: `utm_source=reddit&utm_medium=paid_social&utm_campaign=rdt_aws_devops_q3&utm_content={ad_id}&utm_term={subreddit}`.

## 9. KPIs
| Metric | M1 | M2 | M3 |
|--------|----|----|----|
| Spend | $500 | $500 | $500 |
| Impressions | 200K | 250K | 300K |
| CTR | 0.4% | 0.6% | 0.8% |
| Clicks | 800 | 1,500 | 2,400 |
| Newsletter signups | 12 | 30 | 60 |
| Demo requests (assist) | 1 | 4 | 9 |
| Cost per blog read | $0.62 | $0.33 | $0.21 |

## 10. Kill-switch
- CTR < 0.15% across campaign with ≥ 50K imp.
- 0 newsletter signups in 30 days.
- Brand-safety: any negative comment-section incident on r/aws or r/devops triggers 24-hour pause and review (Reddit comment ecosystem is reputational).

## 11. Operator deps
- `[TBD-OPERATOR]` Reddit Ads account + Pixel.
- `[TBD-OPERATOR]` Newsletter ESP integrated with form `id=newsletter`.
- `[TBD-OPERATOR]` On-call comment-moderation policy for ad threads.
