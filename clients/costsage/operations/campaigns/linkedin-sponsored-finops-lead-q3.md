# LinkedIn Sponsored — FinOps Lead / Practitioner — Q3

> Mirror of `linkedin-sponsored-cto-q3.md`, retuned for FinOps practitioner audience (champion, day-to-day user).

## 1. Meta
- **Campaign name:** LI_FinOps_Q3
- **Platform:** LinkedIn Campaign Manager.
- **Owner:** Paid Media DRI.
- **Status:** draft.

## 2. Objective
- **Objective:** Website Conversions.
- **Primary event:** `demo_request` on `/aws`; secondary `cta_click[cta_ri_sp_guide]`, `cta_click[cta_cmp_cloudzero]`.

## 3. Audience

**Locations (AND):** US, CA, UK, IE, AU, NZ, NL, DE, FR.

**Job Titles (OR):**
- FinOps Lead
- FinOps Manager
- FinOps Practitioner
- Cloud FinOps
- Cloud FinOps Manager
- Cloud FinOps Engineer
- Cloud Economist
- Cloud Cost Analyst
- Cloud Cost Manager
- Cloud Financial Management
- Manager, Cloud Operations
- Director, Cloud Operations
- Head of Cloud
- Director of Platform Engineering
- Principal SRE (where Skills include AWS + FinOps)

**Member Skills (must include ≥ 1):**
- FinOps
- Amazon Web Services (AWS)
- Cloud Cost Management
- Cloud Cost Optimization
- AWS Cost Management
- Reserved Instances
- Savings Plans

**Member Groups (boosted via interest):**
- FinOps Foundation
- AWS User Group (various)

**Seniority:** Manager, Senior, Director, VP. (Exclude Entry, Owner unless company > 50.)

**Company Size:** 51–200, 201–500, 501–1,000 (top end, since FinOps role often emerges later).

**Industries:** Software Development, Internet, IT Services, Financial Services, Computer Software, Technology Information & Internet.

**Excluded:**
- `suppress_current_customers.csv`, `suppress_competitors.csv`.
- Title contains "Recruiter", "Sales", "Marketing", "Student".
- Companies with < 50 employees.

**Audience expansion:** OFF.
**Audience size target at save:** 30K–150K members.

## 4. Hypothesis
> FinOps practitioners are practitioner-buyers — they respond to depth, not pitches. Comparison + technical-proof creative outperforms ROI-claim creative; content (RI/SP guide) is the highest-throughput entry point.

## 5. Budget & Pacing
- **Monthly seed:** $2,000.
- **Bid:** Max Delivery 14 days, then Manual CPC ~ $7.

## 6. Creative

### Ad-1 — Single Image #1 (BOFU, comparison)
- Intro: "Evaluating CloudZero, nOps, Vantage? See where AWS-first design changes the math."
- Headline: "CloudZero alternative, engineered for AWS-first SaaS."
- CTA: "Learn More" → `/compare/cloudzero-vs-costsage`.
- `cta_id=li_finops_ad1`.

### Ad-2 — Single Image #2 (MOFU, depth)
- Intro: "Continuous commitment optimization across RIs + Savings Plans, AWS-Org-wide. Stop spreadsheeting it."
- Headline: "Tag hygiene + commitment portfolio, on autopilot."
- CTA: "Request Demo" → `/aws`.
- `cta_id=li_finops_ad2`.

### Ad-3 — Single Image #3 (TOFU, content)
- Intro: "RIs vs Savings Plans, decided automatically. Read our practitioner guide."
- Headline: "RIs vs Savings Plans, solved."
- CTA: "Download" → `/blog/ri-vs-savings-plans`.
- `cta_id=li_finops_ad3`.

### Ad-4 — Carousel (4 cards)
1. "Your CUR has 600 columns. Your CFO has 6 questions." (visual: spreadsheet collapse).
2. "Allocation that holds up in audit." (visual: tag tree).
3. "Anomalies routed to the team that owns the spike." (visual: alert → Slack).
4. "Get the CostSage demo — see your account live." → `/aws`.
- `cta_id=li_finops_ad4_carousel`.

### Ad-5 — Video, 60s (FinOps practitioner)
**Script:**
```
[0–5s] "If you're a FinOps lead at an AWS-first SaaS, you spend most of your day in three places."
[5–20s] "Cost Explorer, the CUR in Athena, and a Slack channel arguing about tags."
[20–35s] "CostSage is the agentic FinOps platform that replaces all three.
Read-only AWS access. Live allocation. Anomaly routing. Commitment optimization. AWS-Org aware."
[35–50s] "Engineers don't fight you on tags. Finance doesn't fight you on showback.
You stop being the human glue."
[50–60s] "Demo at costsage.ai/aws — 20 minutes."
```
- `cta_id=li_finops_ad5_video`.

### Ad-6 — Conversation ad
- Sender: "FinOps Engineer, CostSage."
- Opening: "Hi {first_name} — saw your role at {company}. Quick one for fellow FinOps folks: which of these is eating your week?"
- Buttons: [Tag/allocation] [RI/SP commitment math] [Anomaly triage] [Showback / chargeback reporting] [None of the above].
- Each branches to a depth reply + relevant LP (`/aws`, `/blog/ri-vs-savings-plans`, `/compare/cloudzero-vs-costsage`).

## 7. Landing pages
- Primary: `/aws`.
- Secondary: `/compare/cloudzero-vs-costsage`, `/blog/ri-vs-savings-plans`.

## 8. Conversion Tracking
Same as LI_CTO_Q3, plus:
- `LI_cta_ri_sp_guide` (engagement) → fires on `cta_click[cta_id=cta_ri_sp_guide]`.

UTM: `utm_source=linkedin&utm_medium=paid_social&utm_campaign=li_finops_q3&utm_content={ad_id}`.

## 9. KPIs
| Metric | M1 | M2 | M3 |
|--------|----|----|----|
| Spend | $2,000 | $2,000 | $2,000–$3,000 |
| Impressions | 250K | 320K | 400K |
| CTR | 0.6% | 0.8% | 1.0% |
| LP CVR | 2.5% | 3.5% | 4.5% |
| Demo requests | 35 | 75 | 130 |
| CPA | $57 | $27 | $15 |
| Newsletter / RI-SP downloads | 60 | 100 | 175 |

## 10. Kill-switch
Same shape as LI_CTO_Q3.

## 11. Operator deps
Same as LI_CTO_Q3 + `[TBD-OPERATOR]` SME for conversation-ad responses (FinOps depth).
