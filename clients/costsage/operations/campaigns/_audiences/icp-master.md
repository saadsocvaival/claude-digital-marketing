# ICP Master — CostSage.ai

> Cross-platform reusable. All paid campaigns reference this file for personas, firmographics, behaviors, JTBD, anti-personas. Update quarterly with sales-call learnings.

## 1. Firmographic envelope (the "who")
| Dimension | Tier-1 sweet spot | Tier-2 acceptable | Out of scope |
|-----------|-------------------|-------------------|--------------|
| Industry | SaaS, B2B software, consumer software with cloud backend | Fintech, healthtech with AWS workloads | Pure brick-and-mortar, regulated on-prem-only |
| Cloud provider | AWS-first | AWS + Azure / AWS + GCP | Pure Azure-only, pure GCP-only |
| Employee count | 50–500 | 25–50 (early), 500–1,000 (late) | < 25, > 1,000 |
| Monthly cloud spend | $10K–$500K | $5K–$10K, $500K–$1M | < $5K, > $1M (enterprise sales motion) |
| Geography | US, CA, UK, IE, AU, NZ, NL, DE, FR (English-first ops) | Nordics, Singapore | LATAM, India, MENA (later) |
| Funding stage | Seed → Series C | Bootstrapped profitable, Series D | Pre-seed, late public |
| Buying motion | Self-serve trial → sales-assisted | Procurement-led | Pure RFP / 12-month-cycle enterprise |

## 2. Personas

### 2.1 Persona A — CTO (champion, sometimes economic buyer)
- Title variants: CTO, Co-founder/CTO, Chief Architect.
- Reports to: CEO.
- Top JTBD: "Keep the platform reliable while costs stay predictable so we don't burn runway."
- Pains: Cloud-bill surprise, board pressure on gross margin, eng time spent on cost vs feature work.
- Wins: Predictable cloud unit economics; engineers freed up; cost visibility into board reporting.
- Trigger events: missed quarterly margin target, fundraising due-diligence, layoff-driven margin push, AWS bill > 25% of COGS.
- Where they hang out: LinkedIn, Hacker News, AWS re:Invent, podcasts (Software Engineering Daily, The CTO Show).
- Disqualifiers: companies < 25 employees (CTO is solo, no FinOps appetite).

### 2.2 Persona B — VP Engineering / Head of Engineering
- Title variants: VP Eng, Head of Engineering, Director of Engineering.
- JTBD: "Ship features fast without engineers sidetracked by cost firefights."
- Pains: Engineers chasing rogue spend, no clean ownership of cost, cost reviews eat sprint cycles.
- Wins: Cost-aware engineering culture without process overhead; auto-attributed cost to teams/services.
- Triggers: cost-allocation project kicked off, scaling-pains incidents, new CFO onboard.
- Channels: LinkedIn, engineering Slack communities, Rands Leadership.

### 2.3 Persona C — Head of Platform / Infrastructure / SRE Lead
- Title variants: Head of Platform, Director of Infrastructure, Principal SRE, Staff Platform Engineer.
- JTBD: "Run an efficient platform — right-sized, automated, observable — without becoming a FinOps shop."
- Pains: Manual right-sizing, RI/SP commitment math, tag hygiene, cross-account visibility.
- Wins: Automation that proposes/executes safe rightsizing; commitment portfolio managed continuously.
- Triggers: AWS Enterprise Discount Program negotiation, multi-account migration, FinOps Foundation certification push.
- Channels: r/aws, r/devops, r/sre, AWS user groups, KubeCon, SREcon.

### 2.4 Persona D — FinOps Lead / Practitioner (champion + day-to-day user)
- Title variants: FinOps Lead, Cloud FinOps Manager, Cloud Economist, Cloud Cost Analyst.
- JTBD: "Make cloud cost a shared, accountable number across eng + finance, on a credible cadence."
- Pains: Spreadsheets, Cost & Usage Report wrangling, allocation disputes, slow showback.
- Wins: Shared dashboards, automated allocation, anomaly alerts that reach the right team.
- Triggers: FinOps Foundation framework adoption, new finance partner, audit / SOX prep.
- Channels: FinOps Foundation Slack, r/FinOps, LinkedIn FinOps groups.

## 3. Buying-committee map
| Role | Champion likelihood | Veto power | Primary objection |
|------|--------------------|-----------|-------------------|
| CTO | High | High | "Can we build this internally in 2 weeks?" |
| VP Eng | High | Medium | "Will my team actually use it?" |
| Head of Platform | High | Medium | "Will it touch prod safely?" |
| FinOps Lead | Highest | Low | "Does it integrate with our CUR/tags?" |
| CFO / Finance | Medium | High | "What's payback in months?" |
| Procurement / Security | Low | High (late) | SOC 2, DPA, SSO |

## 4. Behavioral signals (intent / fit signals to feed audiences)
- Visited /aws, /pricing, /compare/* in last 30 days.
- Downloaded RI vs. Savings Plans guide.
- Searched: "aws cost optimization tool", "aws bill too high", "finops platform", "cloudzero alternative", "rightsizing automation".
- Job-change to FinOps role in last 90 days (LinkedIn).
- Hiring for FinOps / Platform Eng (job posts).
- Engaged with FinOps Foundation content.
- AWS Marketplace browsing of cost-management category.

## 5. Jobs-to-be-done (functional / emotional / social)
- **Functional:** cut waste; forecast cloud spend; attribute cost to teams/products; manage RI/SP commitment.
- **Emotional:** confidence going into board / finance reviews; relief from "bill shock".
- **Social:** be seen as a cost-disciplined eng leader; FinOps practitioner peer recognition.

## 6. Anti-personas (do NOT target)
- Students, bootcampers, individual side-projects.
- Pure Azure-only or pure GCP-only shops (CostSage is AWS-first today).
- Agencies with < 10 employees reselling cloud (low LTV, high churn).
- Current paying customers (suppress via CRM-match exclusion lists on every platform).
- Free-tier-only AWS accounts (< $5K/mo).
- Roles: students, recruiters, marketing, sales (unless founder-titled at < 50 ppl).

## 7. Cross-platform translation cheatsheet
| Concept | LinkedIn | Google | Bing | Reddit | Meta |
|---------|----------|--------|------|--------|------|
| AWS-first SaaS | Industry: Software Dev + Internet + IT&Services; Skills: AWS | Audience signals: "AWS", "Amazon Web Services" custom intent | In-market: Cloud computing | r/aws, r/devops | Interest: AWS, DevOps |
| FinOps lead | Job title contains "FinOps" OR "Cloud Cost" OR "Cloud Economist" | Custom segment + keywords | Profession: IT | r/FinOps | Interest: FinOps Foundation |
| 50–500 employees | Company size 51–200, 201–500 | Company-size signal (limited) | Company-size signal | n/a (use creative gating) | n/a |
| Out: current customers | Match-list exclusion | Customer-match exclusion | Customer list exclusion | Pixel exclusion (purchasers) | Custom audience exclusion |

## 8. Source-of-truth rituals
- Updated by: Marketing DRI, monthly.
- Inputs: Won-deal interviews, lost-deal post-mortems, AE call recordings, CS expansion notes.
- Anti-persona list reviewed each month vs. unqualified-lead pipeline.
