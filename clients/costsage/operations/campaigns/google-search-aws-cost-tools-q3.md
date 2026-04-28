# Google Search — AWS Cost Tools — Q3

> Launch-ready brief. Builds on `_templates/campaign-brief-template.md`.

## 1. Meta
- **Campaign name:** GS_AWS_CostTools_Q3
- **Channel:** Google Ads — Search Network only (no Display, no Search Partners at launch)
- **Owner:** Paid Media DRI
- **Status:** draft (awaits operator account provisioning) — `[TBD-OPERATOR: Google Ads MCC link]`
- **Launch date:** within 5 business days of account approval
- **Linked OKR:** Q3 acquisition — pipeline created from paid

## 2. Objective
- **Primary:** `demo_request` conversions on `/aws`, `/compare/cloudzero-vs-costsage`, `/pricing`.
- **Secondary:** `trial_start`; branded-search lift (track via Search Terms report).

## 3. ICP & Audience
- See `_audiences/icp-master.md` (AWS-first SaaS, 50–500 employees, $10K–$500K/mo cloud spend).
- **Geographies:** US, CA, UK, IE, AU, NZ — English. Bid +20% on US.
- **Audience signals layered (observation, not narrowing):** in-market "Enterprise software", "Cloud computing"; affinity "Tech early adopters"; **Customer Match seed** = `seed_customers_paying.csv`, `seed_demo_requested_90d.csv` (uploaded as observation + bid +25%).
- **Excluded audiences:** `suppress_current_customers.csv`, `suppress_competitors.csv`.
- **Device bid mods:** desktop +10%, tablet 0%, mobile −10% (B2B intent skews desktop).

## 4. Hypothesis
> AWS-first SaaS leaders searching "aws cost optimization tool" / "aws cost management software" / "cloudzero alternative" will convert on `/aws` + `/compare/cloudzero-vs-costsage` at ≥ 5% LP→`demo_request`, with CPA ≤ $250 by month 2.

## 5. Budget & Pacing
- **Monthly seed:** $1,500 ($50/day across the campaign).
- **Bid strategy:** start "Maximize Conversions" (no tCPA) for 14 days to gather data; switch to **tCPA $250** at ≥ 30 conversions.
- **Daily cap rule:** auto-pause via script if 7-day spend > $400 with 0 conversions.

## 6. Ad-Group Structure (5 ad groups)

### AG-1 — Exact: AWS Cost Optimization (LP: `/aws`)
**Exact match keywords (tier — high intent, brand-adjacent):**
1. [aws cost optimization tool]
2. [aws cost optimization software]
3. [aws cost optimization platform]
4. [aws cost management tool]
5. [aws cost management software]
6. [aws cost management platform]
7. [aws cloud cost optimization]
8. [aws bill optimization]
9. [aws bill optimization tool]
10. [aws cost reduction tool]
11. [aws cost reduction software]
12. [aws spend optimization]
13. [reduce aws costs]
14. [reduce aws bill]
15. [aws cost analysis tool]
16. [aws cost monitoring tool]
17. [aws cost monitoring software]
18. [aws cost visibility]
19. [aws cost allocation tool]
20. [aws finops tool]
21. [aws finops platform]
22. [aws finops software]
23. [aws cost saving tool]
24. [aws rightsizing tool]
25. [aws rightsizing software]
26. [aws cost optimization service]
27. [aws cost dashboard]
28. [aws cost analytics]
29. [aws cost intelligence]
30. [optimize aws spend]
31. [aws cost governance]

### AG-2 — Phrase: AWS Cost Variants (LP: `/aws`)
**Phrase match (tier — broader intent within AWS):**
1. "aws cost optimization"
2. "aws cost management"
3. "aws cost reduction"
4. "aws bill too high"
5. "lower aws costs"
6. "aws spend management"
7. "aws cost control"
8. "aws cost cutting"
9. "aws cloud cost tool"
10. "aws cloud cost management"
11. "amazon web services cost optimization"
12. "amazon web services cost management"
13. "ec2 cost optimization"
14. "rds cost optimization"
15. "s3 cost optimization"
16. "aws savings plan optimization"
17. "aws reserved instance optimization"
18. "aws cost anomaly detection"
19. "aws cost forecasting"
20. "aws cost allocation"
21. "aws tag governance"
22. "aws unit economics"
23. "aws cost showback"
24. "aws cost chargeback"
25. "kubernetes aws cost"
26. "eks cost optimization"
27. "fargate cost optimization"
28. "aws auto scaling cost"
29. "aws cost per customer"
30. "aws cost per team"

### AG-3 — Broad (smart match) with audience guardrails: AWS FinOps (LP: `/aws`)
**Broad match (must be paired with Customer Match audience targeting and aggressive negatives):**
1. aws finops
2. cloud finops aws
3. aws cost engineering
4. aws cost discipline
5. aws margin
6. cloud cost optimization aws
7. aws cost best practices
8. aws cost guardrails
9. aws billing optimization
10. aws cost ops
…(plus 20 more variants — auto-expanded by Google. Strict negatives in section 8.)

### AG-4 — Phrase: Switch / Competitor-aware (LP: `/compare/cloudzero-vs-costsage`)
1. "cloudzero alternative"
2. "cloudzero competitor"
3. "cloudzero vs"
4. "cloudzero pricing"
5. "cloudzero review"
6. "vantage alternative"
7. "vantage.sh alternative"
8. "nops alternative"
9. "nops competitor"
10. "spot.io alternative"
11. "harness ccm alternative"
12. "kubecost alternative aws"
13. "apptio cloudability alternative"
14. "ibm turbonomic alternative"
15. "densify alternative"
16. "cloudhealth alternative"
17. "vmware cloudhealth alternative"
18. "finout alternative"
19. "yotascale alternative"
20. "zesty alternative"
21. "usage ai alternative"
22. "cast.ai alternative"
23. "best aws cost optimization tool"
24. "top aws cost optimization tools"
25. "aws cost tool comparison"
26. "cloudzero pricing comparison"
27. "switching from cloudzero"
28. "switching from nops"
29. "cloudzero discount"
30. "cloudzero limitations"

### AG-5 — Exact: Pricing-intent (LP: `/pricing`)
1. [aws cost tool pricing]
2. [cloudzero pricing]
3. [nops pricing]
4. [vantage pricing]
5. [aws finops platform pricing]
6. [aws cost optimization tool pricing]
7. [aws cost management pricing]
8. [costsage pricing]
9. [costsage cost]
10. [costsage demo]
11. [costsage trial]
12. [aws cost software cost]
13. [finops tool cost]
14. [finops platform cost]
15. [aws cost tool free trial]
… (extend to 30 with ID-style permutations as data arrives)

## 7. Negative Keyword List (campaign-level)

```
-free
-open source
-tutorial
-course
-certification
-jobs
-salary
-resume
-aws training
-aws exam
-aws calculator (only Amazon's calculator term)
-pricing calculator
-aws certification cost
-aws course cost
-amazon shopping
-amazon prime
-aws lambda free
-student
-bootcamp
-internship
-india
-pakistan
-bangladesh
-philippines (geo-handled, but as keyword negative for outsourced-services queries)
-azure only
-gcp only
-google cloud only
-on premise
-on-prem
-pdf
-cheat sheet
-meaning
-definition
-what is
-vs azure
-vs gcp
-amazon stock
-amazon shares
-amazon shop
-aws cli
-aws cdk
-terraform
-cloudformation
```

Add a **shared negative list** `Brand-Safety_Universal` applied to every CostSage paid search campaign (job/training/student terms).

## 8. RSA Ad Variants (3 per ad group)

### AG-1 RSAs (LP `/aws?utm_*`)

**RSA-1**
- Headlines (15): H02 "Your AWS Bill, Decoded" | H08 "Right-Size AWS Automatically" | H06 "The Agentic FinOps Platform" | H17 "Built On AWS Well-Architected" | H03 "FinOps Without The Spreadsheets" | H29 "Get The CostSage AWS Audit" | H09 "AWS Bill Surprises? End Them." | "AWS-First FinOps Platform" | "Cut AWS Waste Today" | "RIs, SPs, Rightsizing — One Tool" | "For 50–500 Person SaaS" | "Read-Only AWS Setup" | "SOC 2-Aligned" | "Free 14-Day Trial" | "Book A 20-Min Demo"
- Descriptions (4): D02 | D04 | D07 | D09
- Pinned: H02 to position 1; CTA "Book A 20-Min Demo" to position 3.

**RSA-2 (proof-led)**
- Headlines: H30 "LTV:CAC Loves A 30% Cloud Cut" | H13 "Cut AWS Waste In 24 Hours" | "Find Waste In Your AWS Account" | "Quantify Savings Before You Commit" | "ROI In Weeks, Not Quarters" | H17 | H08 | "Engineers Free To Build" | "Anomaly Alerts To The Right Team" | "Multi-Account, AWS Org Aware" | "Available On AWS Marketplace" | "Talk To A FinOps Engineer" | "See A Live Account Demo" | "Start Your Free Trial" | "Book Your AWS Audit"
- Descriptions: D08 | D13 | D17 | D19

**RSA-3 (problem-frame)**
- Headlines: H05 "Stop Paying For Idle Cloud" | H07 "Engineers Build. We Save." | H03 | "End AWS Bill Surprises" | "AWS Costs Eating Margin?" | "Idle Resources Drain Budgets" | "Tag Hygiene On Autopilot" | "Showback Without The Spreadsheets" | "Cost Allocation Without Disputes" | "Forecasts You Can Defend" | "Built For AWS-First SaaS" | H06 | H08 | "See Your Savings In One Demo" | "Get Started Free"
- Descriptions: D01 | D05 | D11 | D18

(Same pattern duplicated, persona-tuned, for AG-2 to AG-5. AG-4 uses comparison angle copy and Description D10 prominently. AG-5 uses pricing-anchored copy + D14, D19.)

## 9. Sitelinks (campaign-level, 8)
1. AWS Cost Optimization → `/aws`
2. Pricing & Plans → `/pricing`
3. CloudZero vs CostSage → `/compare/cloudzero-vs-costsage`
4. nOps vs CostSage → `/compare/nops-vs-costsage`
5. AWS Best Practices Guide → `/blog/aws-cost-optimisation-best-practices`
6. RIs vs Savings Plans → `/blog/ri-vs-savings-plans`
7. Book A Demo → `/aws#demo`
8. Start Free Trial → `/pricing#trial`

## 10. Callouts (10)
- Read-only AWS access
- SOC 2-aligned
- Available on AWS Marketplace `[TBD-OPERATOR-URL]`
- Free 14-day trial
- Multi-account, AWS Organization-aware
- Cuts 20–30% AWS waste (typical) `[TBD-OPERATOR-CLAIM]`
- 24-hour audit
- For AWS-first SaaS
- Engineering-friendly setup
- No credit card to start

## 11. Structured Snippets
- **Header: Services** — Rightsizing, Anomaly Detection, RI Optimization, Savings Plans, Forecasting, Tag Governance.
- **Header: Featured** — AWS-First, SOC 2-aligned, AWS Marketplace, Multi-account, Read-only, Self-serve.

## 12. Conversion Tracking
- **Primary conversion:** `demo_request` (Google Ads conversion ID `[TBD-OPERATOR]`, conversion action "Demo Request — Web", count once per click).
- **Secondary:** `trial_start`, `cta_click[cta_id=cta_book_demo]`, `form_start`.
- **Enhanced Conversions:** ON, hashed email + name from form submit.
- **Imported conversions from CRM (offline):** `sql_qualified`, `opportunity_created`, `closed_won` — 90-day attribution window. `[TBD-OPERATOR: CRM connector]`.
- **GTM trigger map:** see `analytics/tag-plan.md`.
- **UTM template:** `?utm_source=google&utm_medium=cpc&utm_campaign=gs_aws_cost_tools_q3&utm_content={ad_id}&utm_term={keyword}` per `analytics/utm-convention.md`.

## 13. KPIs / Targets
| Metric | Month 1 | Month 2 | Month 3 |
|--------|---------|---------|---------|
| Spend | $1,500 | $1,500 | $1,500–$2,500 (scale if hitting tCPA) |
| Impressions | 25K | 35K | 45K |
| Clicks | 750 | 1,000 | 1,400 |
| CTR | 3.0% | 4.0% | 5.0% |
| Avg CPC | $2.00 | $1.80 | $1.60 |
| LP→demo_request CVR | 3% | 4% | 5% |
| Demo requests | 22 | 40 | 70 |
| CPA | $68 | $37 | $21 (blended; tCPA $250 caps) |
| SQL rate | 25% | 30% | 35% |
| Pipeline created ($) | `[TBD: CRM live]` | | |

## 14. Kill-Switch
Pause campaign if any holds for 7 consecutive days:
- CPA > $400 with ≥ $750 spent.
- CTR < 1.2% across campaign with ≥ 10K impressions.
- LP CVR < 1% with ≥ 200 LP visits.
- 0 conversions in 14 days post-launch.
- Search Terms report shows > 25% spend on irrelevant queries (add as negatives, then assess).

## 15. Operator dependencies
- `[TBD-OPERATOR]` Google Ads account creation + MCC link.
- `[TBD-OPERATOR]` Conversion actions created with IDs.
- `[TBD-OPERATOR]` AWS Marketplace URL for sitelink.
- `[TBD-OPERATOR-CLAIM]` Approval of "20–30% waste" range copy.
- `[TBD-OPERATOR]` CRM offline-conversion import (Zapier or native).
