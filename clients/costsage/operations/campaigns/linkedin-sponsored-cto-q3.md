# LinkedIn Sponsored — CTO Audience — Q3

> Launch-ready LinkedIn Campaign Manager brief.

## 1. Meta
- **Campaign name:** LI_CTO_Q3
- **Platform:** LinkedIn Campaign Manager (LCM).
- **Owner:** Paid Media DRI.
- **Status:** draft. `[TBD-OPERATOR: LinkedIn Ad Account, Insight Tag verified on costsage.ai]`.

## 2. Objective
- **Campaign Manager objective:** Website Conversions.
- **Primary event:** `demo_request` on `/aws`.
- **Secondary:** `cta_click[cta_book_demo]`, video views (for video creative).

## 3. Audience Spec (LCM filters)
**Locations (AND):**
- United States, Canada, United Kingdom, Ireland, Australia, New Zealand, Netherlands, Germany, France.

**Job Titles (OR — primary targeting attribute):**
- CTO
- Chief Technology Officer
- Co-founder, CTO
- Chief Architect
- Chief Engineering Officer
- VP, Technology

**Job Function (OR — alt audience):**
- Engineering
- Information Technology

**Seniority (OR):**
- CXO
- VP
- Director (only when paired with Function = Engineering AND Title contains "Engineering" or "Platform")

**Company Size (OR):**
- 51–200 employees
- 201–500 employees

**Industries (OR):**
- Software Development
- Internet Publishing
- IT Services and IT Consulting
- Technology, Information and Internet
- Computer & Network Security (filtered to SaaS)
- Financial Services (only when Member Skills include AWS)

**Member Skills (must include at least one — narrow audience):**
- Amazon Web Services (AWS)
- Cloud Computing
- DevOps
- FinOps
- Site Reliability Engineering
- Cloud Architecture

**Excluded audiences:**
- Matched audience: `suppress_current_customers.csv`.
- Matched audience: `suppress_competitors.csv`.
- Job titles: Recruiter, Talent, Sales Development Representative, Account Executive (these crowd CTO-titled feeds).

**Audience expansion:** OFF (we want precision).
**LinkedIn Audience Network:** OFF at launch; revisit at 60 days.
**Targeted audience size at save:** confirm 80K–500K members. If < 80K, drop the Member Skills constraint to OR-of-three. If > 500K, add seniority constraint or restrict industries.

## 4. Hypothesis
> CTOs at 50–500 employee AWS-first SaaS will engage with margin/runway-framed creative more than feature-led creative; conversation ads outperform single-image for demo bookings at this seniority.

## 5. Budget & Pacing
- **Monthly seed:** $2,000.
- **Bid type:** Maximum Delivery (auto) for 14 days; switch to **Manual CPC** at $8–$12 once CTR baseline established.
- **Daily cap:** $70.
- **Schedule:** Mon–Fri, 06:00–20:00 destination time zones.

## 6. Creative Spec (5 ads in rotation)

### Ad-1 — Single Image #1 (CTO TOFU, margin frame)
- Visual: clean 1200×627, dark teal brand, headline overlay.
- Intro text (≤ 150 chars): "Your AWS bill is 30% waste — and it's eating gross margin. CostSage finds it in 24 hours."
- Headline (≤ 70): "Your AWS bill, decoded."
- Description (≤ 100): "Agentic FinOps for AWS-first SaaS, 50–500 employees."
- CTA button: "Request Demo" → `/aws?utm_source=linkedin&utm_medium=paid_social&utm_campaign=li_cto_q3&utm_content=ad1_si_margin`.
- `cta_id=li_cto_ad1`.

### Ad-2 — Single Image #2 (CTO MOFU, eng time)
- Intro: "Your engineers shouldn't moonlight as FinOps analysts. CostSage handles the cost work in the background."
- Headline: "Engineers build. We save."
- Description: "RIs, Savings Plans, rightsizing — automated, AWS-first."
- CTA: "Learn More" → `/aws`.
- `cta_id=li_cto_ad2`.

### Ad-3 — Single Image #3 (CTO BOFU, audit offer)
- Intro: "We'll quantify your AWS waste in 24 hours — free, read-only access. No commitment."
- Headline: "Get the CostSage AWS audit."
- Description: "20–30% waste typical. SOC 2-aligned. Read-only setup." `[TBD-OPERATOR-CLAIM]`
- CTA: "Sign Up" → `/aws#audit`.
- `cta_id=li_cto_ad3`.

### Ad-4 — Carousel (5 cards), MOFU
**Storyboard:**
1. **Card 1 — Hook:** "Your AWS bill is a black box." Visual: cluttered Cost Explorer screenshot, blurred.
2. **Card 2 — Pain:** "Tag hygiene, RI math, anomaly triage — engineers' time, not their job." Visual: tired engineer at terminal (stock).
3. **Card 3 — Reframe:** "What if FinOps ran in the background?" Visual: clean dashboard.
4. **Card 4 — Proof:** "20–30% waste typically eliminated in 90 days." `[TBD-CLAIM]` Visual: chart down-and-to-right.
5. **Card 5 — CTA:** "Get a free 24-hour AWS audit." Button "Request Demo" → `/aws`.
- `cta_id=li_cto_ad4_carousel`.

### Ad-5 — Video, 60s (CTO TOFU/MOFU)
**Script:**
```
[0–3s — bold text on dark bg]
"Your AWS bill is 30% waste."

[3–10s — voiceover, brand visual]
"At 50 to 500 employee SaaS companies, cloud cost is one of the top three line items —
and one of the least understood."

[10–25s — product demo b-roll]
"CostSage is an agentic FinOps platform. It connects to AWS read-only,
finds rightsizing opportunities, optimizes RIs and Savings Plans,
and routes anomalies to the team that owns the spike."

[25–40s — claim block, footnoted]
"Customers typically eliminate 20 to 30 percent of waste in the first 90 days." [TBD-CLAIM]
"Engineers stop firefighting. Margins go up. Forecasts hold."

[40–55s — CTO direct]
"If you're a CTO defending the AWS line item, give us 20 minutes.
We'll show you waste in your own account."

[55–60s — end card]
"costsage.ai/aws — Book a demo."
```
- Subtitles: burned-in, OpenSans bold, brand-safe.
- Aspect: 1:1 primary; 16:9 alt.
- CTA: "Learn More" → `/aws`.
- `cta_id=li_cto_ad5_video`.

### Ad-6 — Conversation Ad
**Flow:**
```
Sender: [SDR persona name + photo, "Head of FinOps Engineering, CostSage"]

Opening:
"Hi {first_name} — quick one. Most CTOs at 50–500 person SaaS we talk to are losing
20–30% of their AWS spend to waste they can't see in Cost Explorer.
Two questions to figure out if CostSage can help:"

Button A: "How much do you spend on AWS each month?"
  → Reply: "Got it. Roughly: under $25K / $25–100K / $100–500K / $500K+?"
     Buttons: [< $25K] [$25–100K] [$100–500K] [$500K+]
     - <$25K → "We're built for $10K+. Send you our blog instead?" → CTA: blog.
     - $25–100K → "Sweet spot. Want a 24-hour free audit?" → CTA: /aws#audit.
     - $100–500K → "Very common range. Demo would land best." → CTA: /aws.
     - $500K+ → "We have a senior FinOps eng for that range." → CTA: /aws.

Button B: "What does CostSage do, in one paragraph?"
  → Reply: 60-word product blurb with link to /aws.

Button C: "Send me the comparison vs CloudZero."
  → CTA: /compare/cloudzero-vs-costsage.

Button D: "Not now."
  → Reply: "Totally fair. I'll send our RI vs Savings Plans guide if useful." → CTA: /blog/ri-vs-savings-plans.
```
- `cta_id=li_cto_ad6_convo` (each button suffixed `_a`/`_b`/`_c`/`_d`).

## 7. Landing Page
- Primary: `/aws`.
- CRO uplift required: see `_creative/landing-page-suitability.md` (medium priority — inline form, social proof bar).

## 8. Conversion Tracking
- LinkedIn Insight Tag installed site-wide via GTM (`analytics/tag-plan.md`).
- Conversions defined in LCM:
  - `LI_demo_request` → fires on `demo_request` event.
  - `LI_cta_book_demo` → fires on `cta_click` with `cta_id` starting `li_cto_`.
  - `LI_form_start` (engagement, not conversion).
- Attribution: 30-day click + 1-day view.
- Offline conversion upload via CRM connector for `sql_qualified` and `closed_won` (90-day window). `[TBD-OPERATOR]`.

## 9. KPIs
| Metric | M1 | M2 | M3 |
|--------|----|----|----|
| Spend | $2,000 | $2,000 | $2,000–$3,500 |
| Impressions | 200K | 250K | 300K |
| CTR | 0.5% | 0.7% | 0.9% |
| Clicks | 1,000 | 1,750 | 2,700 |
| CPC | $2.00 | $1.15 | $0.75 |
| LP CVR | 2% | 3% | 4% |
| Demo requests | 20 | 52 | 108 |
| CPA | $100 | $38 | $19 |
| SQL rate | 30% | 35% | 40% |
| Conv-ad open rate | 50% | 55% | 60% |
| Conv-ad click rate | 6% | 8% | 10% |

## 10. Kill-Switch
- CPA > $400 with ≥ $1,000 spent (7-day rolling).
- CTR < 0.25% with ≥ 50K impressions on any ad — pause that ad.
- Conv-ad open rate < 30% — rewrite opener.
- 0 conversions in 21 days post-launch.
- LP CVR < 1% with ≥ 300 visits — escalate to CRO uplift before scaling.

## 11. Operator deps
- `[TBD-OPERATOR]` LinkedIn ad account + Insight Tag verification.
- `[TBD-OPERATOR]` Sender persona for conversation ad (real employee LinkedIn profile required).
- `[TBD-OPERATOR-CLAIM]` "20–30% waste" copy approval.
- `[TBD-OPERATOR]` SDR coverage for conversation-ad replies (LinkedIn requires human handling within 24h SLA).
