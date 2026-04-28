# Ad Copy Bank — CostSage.ai

> Reusable, on-brand copy. Tagged by persona (CTO / VPE / PLAT / FINOPS) and funnel stage (TOFU / MOFU / BOFU). Pull from here into briefs; do not invent fresh copy per campaign without a reason. Update only via PR-style review with brand owner.

Token rules:
- All claims must trace to product copy on costsage.ai or be marked `[TBD-OPERATOR-CLAIM-APPROVAL]`.
- Specific savings percentages (e.g., "30%") are illustrative ranges — confirm before paid use.
- Never use competitor logos in headlines/descriptions.

---

## A. Headlines (30) — character counts targeted at Google RSA (≤ 30) where noted

### TOFU — awareness, problem-frame
| ID | Headline | Persona | Char |
|----|----------|---------|------|
| H01 | Cut AWS Waste In 24 Hours | All | 26 |
| H02 | Your AWS Bill, Decoded | CTO/FINOPS | 22 |
| H03 | FinOps Without The Spreadsheets | FINOPS | 31 |
| H04 | Cloud Cost On Autopilot | CTO/PLAT | 23 |
| H05 | Stop Paying For Idle Cloud | PLAT/FINOPS | 27 |
| H06 | The Agentic FinOps Platform | All | 28 |
| H07 | Engineers Build. We Save. | VPE/CTO | 25 |
| H08 | Right-Size AWS Automatically | PLAT | 29 |
| H09 | AWS Bill Surprises? End Them. | CTO | 29 |
| H10 | Margin-Safe Cloud Engineering | VPE/CTO | 29 |

### MOFU — solution-aware, capability-led
| ID | Headline | Persona | Char |
|----|----------|---------|------|
| H11 | RIs vs Savings Plans, Solved | FINOPS/PLAT | 28 |
| H12 | Continuous Commitment Optimization | FINOPS | 35 |
| H13 | Anomaly Alerts That Reach The Right Team | FINOPS | 41 |
| H14 | Tag Hygiene, On Autopilot | PLAT/FINOPS | 25 |
| H15 | Showback In Hours, Not Sprints | FINOPS/VPE | 30 |
| H16 | Cost Allocation Without Disputes | FINOPS | 31 |
| H17 | Built On AWS Well-Architected | PLAT/CTO | 29 |
| H18 | One Dashboard. Every Account. | PLAT/FINOPS | 28 |
| H19 | From CUR To Decisions, In Minutes | FINOPS | 33 |
| H20 | Forecast Cloud Spend With Confidence | CTO/FINOPS | 36 |

### BOFU — comparison, proof, urgency
| ID | Headline | Persona | Char |
|----|----------|---------|------|
| H21 | CloudZero Alternative, Engineered For AWS-First SaaS | FINOPS | 53 |
| H22 | Switching From nOps? Read This. | FINOPS/PLAT | 31 |
| H23 | Try CostSage Free For 14 Days | All | 30 |
| H24 | Book A 20-Minute Demo | All | 21 |
| H25 | See Your Waste In One Call | FINOPS/CTO | 27 |
| H26 | Pricing Built For 50–500 Employee SaaS | All | 39 |
| H27 | AWS Marketplace Ready | CTO/PROC | 21 |
| H28 | SOC 2-Aligned, Read-Only Setup | CTO/PLAT | 30 |
| H29 | Get The CostSage AWS Audit | FINOPS | 27 |
| H30 | LTV:CAC Loves A 30% Cloud Cut | CTO | 30 |

## B. Descriptions (20) — Google RSA ≤ 90 chars; LinkedIn intro ≤ 150 chars

| ID | Description | Stage | Char |
|----|-------------|-------|------|
| D01 | Agentic AI watches your AWS bill 24/7 and fixes waste before it hits the invoice. | TOFU | 80 |
| D02 | RIs, Savings Plans, rightsizing, anomaly alerts — one platform, AWS-first. | MOFU | 76 |
| D03 | For 50–500 employee SaaS spending $10K–$500K/mo on AWS. | TOFU | 56 |
| D04 | See where every dollar goes — by team, service, environment — without tag hell. | MOFU | 80 |
| D05 | Replace spreadsheets and CUR queries with a live FinOps dashboard. | MOFU | 65 |
| D06 | Engineers ship. CostSage handles the cost optimization in the background. | TOFU | 73 |
| D07 | Read-only AWS access. Recommendations approved by you. No surprise changes. | BOFU | 76 |
| D08 | Get a free 24-hour AWS waste audit — see your savings before you commit. | BOFU | 71 |
| D09 | Book a 20-minute demo. We'll show you waste in your own account. | BOFU | 64 |
| D10 | CloudZero, Vantage, nOps users: see how AWS-first design changes the math. | BOFU | 75 |
| D11 | FinOps Foundation framework, applied automatically to your stack. | MOFU | 65 |
| D12 | Forecasts you can put in a board deck. | TOFU | 39 |
| D13 | Cut 20–30% of AWS waste in the first 90 days — typical CostSage range. | BOFU | 71 |
| D14 | Pricing scales with the savings, not the seats. | TOFU | 49 |
| D15 | Tag hygiene that updates itself. Allocation that holds up in audit. | MOFU | 67 |
| D16 | Anomaly alerts to the team that owns the spike — with the why and the fix. | MOFU | 75 |
| D17 | Multi-account, cross-region, AWS Organization-aware. | MOFU | 51 |
| D18 | Built for the eng leader who has to defend the AWS line item. | TOFU | 60 |
| D19 | Try CostSage free for 14 days. No credit card. SOC 2-aligned. | BOFU | 60 |
| D20 | Available on AWS Marketplace — bill against your committed spend. | BOFU | 65 |

## C. CTAs (10)

| ID | CTA text | Where | cta_id (analytics) |
|----|----------|-------|--------------------|
| C01 | Book a demo | site primary, all BOFU ads | `cta_book_demo` |
| C02 | Start free trial | /pricing, BOFU ads | `cta_start_trial` |
| C03 | Get the AWS audit | LinkedIn, BOFU | `cta_aws_audit` |
| C04 | See your savings | LP hero | `cta_see_savings` |
| C05 | Compare to CloudZero | /compare/cloudzero-vs-costsage | `cta_cmp_cloudzero` |
| C06 | Compare to nOps | /compare/nops-vs-costsage | `cta_cmp_nops` |
| C07 | Read the RI vs SP guide | /blog/ri-vs-savings-plans | `cta_ri_sp_guide` |
| C08 | Read AWS best practices | /blog/aws-cost-optimisation-best-practices | `cta_aws_best` |
| C09 | View pricing | /pricing | `cta_view_pricing` |
| C10 | Talk to a FinOps engineer | LI conversation ad | `cta_talk_finops` |

## D. Persona / stage / LP suggested combinations
- CTO TOFU → H01/H02/H07 + D01/D03/D18 + C01 → /
- VPE MOFU → H07/H10/H15 + D04/D05/D11 + C01 → /aws
- PLAT MOFU → H08/H14/H17/H18 + D04/D15/D17 + C03 → /aws
- FINOPS BOFU → H11/H21/H22/H29 + D02/D10/D13 + C03/C05 → /compare/cloudzero-vs-costsage, /blog/ri-vs-savings-plans
- All BOFU → H23/H24/H26 + D08/D09/D19 + C01/C02 → /pricing
