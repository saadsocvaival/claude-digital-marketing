---
slug: ri-vs-savings-plans
url: https://costsage.ai/blog/ri-vs-savings-plans
title: Reserved Instances vs Savings Plans — How to Choose (and How an Agent Decides for You)
description: A practical 2026 guide to choosing between AWS Reserved Instances and Savings Plans, with the math, the trade-offs, and how an agent automates the decision.
canonical: https://costsage.ai/blog/ri-vs-savings-plans
publish_date: 2026-04-29
author: CostSage Engineering
schema_type: Article
internal_links:
  - /aws
  - /features
  - /finops-agent-vs-dashboard
  - /blog/aws-cost-optimisation-best-practices
word_count_target: 2200
status: draft-for-review
---

# Reserved Instances vs Savings Plans: How to Choose (and How an Agent Decides for You)

> **TL;DR.** Use Compute Savings Plans as the default for almost all stable
> compute. Use Standard Reserved Instances only for RDS, ElastiCache,
> Redshift, and where Convertible RIs offer specific exchange flexibility
> that matters. EC2 Instance Savings Plans are a niche middle ground. The
> right mix depends on your forecast confidence and the share of your spend
> that's mutable.

## Why this question keeps coming back

AWS commitments are the single biggest lever in your bill. They also
introduce risk: if you over-commit, you pay for capacity you don't use; if
you under-commit, you forfeit ~30%+ in discount. The choice between RIs and
Savings Plans isn't academic — it shapes every quarterly invoice for the
next one to three years.

This post lays out the decision the way a FinOps engineer or an agent would
make it: by service, by stability of forecast, and by mutability of spend.

---

## The four commitment instruments, briefly

### 1. Compute Savings Plans
- **Discount range:** up to 66% vs On-Demand.
- **Coverage:** EC2, Fargate, Lambda — across instance family, size, region,
  OS, tenancy.
- **Term:** 1 or 3 years.
- **Payment:** All-Upfront / Partial / No-Upfront.
- **Flexibility:** maximum. Survives almost any architectural change.

### 2. EC2 Instance Savings Plans
- **Discount range:** up to 72% vs On-Demand.
- **Coverage:** EC2 only, locked to a specific instance family in a region.
- **Term/payment:** as above.
- **Flexibility:** moderate. Works for committed family but not across
  family changes.

### 3. Standard Reserved Instances (Standard RI)
- **Discount range:** up to 72% vs On-Demand.
- **Coverage:** EC2, RDS, ElastiCache, Redshift, OpenSearch, MemoryDB,
  DynamoDB.
- **Term/payment:** as above.
- **Flexibility:** poor for EC2 (locked to family/region/OS). Mandatory for
  RDS et al — Savings Plans don't cover those services.

### 4. Convertible Reserved Instances (Convertible RI)
- **Discount range:** up to 54% vs On-Demand.
- **Coverage:** EC2 only.
- **Flexibility:** can be exchanged into different families / sizes / OS.
- **Use case:** retired in most modern stacks; Compute Savings Plans give
  more flexibility for similar discount.

---

## The decision tree

```
Is the workload EC2 / Fargate / Lambda?
├── Yes
│   └── Is there >12-month forecast confidence?
│       ├── Yes → 3-year Compute Savings Plan, Partial-Upfront
│       └── No  → 1-year Compute Savings Plan, No-Upfront
├── No, it's RDS / ElastiCache / Redshift / OpenSearch / MemoryDB
│   └── Standard Reserved Instance, term matching forecast confidence
└── It's something else (DynamoDB, etc.)
    └── Standard RI if available, else On-Demand
```

In practice the answer is "Compute Savings Plans" for ~70% of typical SaaS
spend, and Standard RI for the database tier.

---

## Picking the coverage ratio

The mistake teams make is committing for everything. The mistake they make
*next* is committing for nothing because they got burned once.

The right answer is: **commit for the stable baseline, and only the stable
baseline.**

To find your baseline:
1. Pull 90 days of hourly compute spend across the relevant services.
2. Compute the rolling p10 over that window — the floor your spend never
   drops below.
3. That's your baseline. Commit ≤95% of it.
4. The remaining (variable + headroom + experimentation) compute stays
   On-Demand or Spot.

This typically lands a coverage ratio between 65% and 85% of total spend.
Lower than 60% and you're leaving discount on the table. Higher than 85%
and a single architectural shift can leave you paying for unused capacity.

---

## How an agent makes this decision

Manually, the analysis above is a half-day spreadsheet exercise per quarter.
An agent does it continuously:

1. **Forecast.** It builds a 90-day rolling p10/p50/p90 forecast per
   compute family + per database engine.
2. **Risk model.** It scores forecast confidence (variance / regime change
   detection / planned-architecture-change inputs from the team's planning
   doc).
3. **Recommend.** It outputs a recommended commitment package: term,
   payment option, hourly commitment per service, expected discount,
   expected payback.
4. **Approve.** A human (FinOps lead, engineering lead) signs off.
5. **Execute.** Inside a scoped IAM role, the agent purchases the package.
6. **Re-evaluate.** Coverage is re-modelled monthly; if utilisation drifts
   below threshold the agent flags an exchange or sale on the AWS RI
   Marketplace.

[CostSage on AWS](/aws) runs this loop. The agent's commitment recommendation
typically captures 90%+ of the theoretically-available discount — versus 60–
70% for teams running quarterly manual reviews. See the broader argument in
[FinOps agent vs dashboard](/finops-agent-vs-dashboard).

---

## Common traps

**Trap 1 — Committing during a growth spike.** If your spend is growing
30%/quarter, a 3-year commitment locks in a baseline that will be way
under-coverage in 18 months. Use 1-year terms or stick to a smaller share.

**Trap 2 — Buying RIs when Savings Plans would do.** Convertible RIs and
EC2 Instance Savings Plans both lose to Compute Savings Plans for almost
every modern workload. Default to CSP unless you have a specific reason.

**Trap 3 — Ignoring the database tier.** RDS reservations alone cover 18%
of the typical SaaS bill. Many teams over-rotate on EC2 commitments and
leave RDS at On-Demand.

**Trap 4 — Letting Savings Plans expire silently.** A SP rolling off
without a replacement is a 30%+ overnight bill jump. Put expiry in your
calendar or — more reliably — let the agent watch for it.

---

## A worked example

Mid-size SaaS, $250K/month AWS spend pre-commitment.

| Service | Monthly On-Demand | Stable baseline (p10) | Recommended commit | Discount | Monthly saving |
|---|---|---|---|---|---|
| EC2 + Fargate | $130K | $95K | 3-yr CSP, Partial-Upfront | 47% | $44.7K |
| Lambda | $8K | $6K | 1-yr CSP, No-Upfront | 17% | $1.0K |
| RDS | $40K | $34K | 3-yr Standard RI, No-Upfront | 41% | $13.9K |
| ElastiCache | $9K | $7K | 1-yr Standard RI, No-Upfront | 30% | $2.1K |
| **Total** | **$187K** | **$142K** | **mixed** | **avg 43% on baseline** | **$61.7K** |

Total monthly saving on the same workload: ~$61.7K, or ~25% of the AWS
bill. Add idle-resource cleanup and rightsizing (covered in
[10 best practices](/blog/aws-cost-optimisation-best-practices)) and 35%+
total reduction is realistic.

---

## FAQ

**Should I default to 1-year or 3-year terms?**
Default to 1-year unless your business and architecture have stable
multi-year visibility. The discount uplift from 1-yr to 3-yr is real
(~10–15 percentage points) but the lock-in risk is bigger for most growing
companies.

**Partial-Upfront, All-Upfront, or No-Upfront?**
All-Upfront has the highest absolute discount but the worst capital
efficiency. Partial-Upfront is the typical sweet spot. No-Upfront is correct
when you're cash-constrained or when treasury yields exceed the AWS
upfront-discount premium.

**Can I exchange a Savings Plan if my workload changes?**
No — Savings Plans are not exchangeable. They flex automatically across
instance family / size / region within their type, but you can't swap a
3-year for a 1-year. This is why baseline-only commitment matters.

**Does CostSage handle the purchase?**
Yes — after your approval, the agent purchases inside a scoped IAM role
limited to commitment APIs. It also monitors utilisation and recommends
exchanges or RI Marketplace sales when coverage drifts. See
[/features](/features#commitment-management).

---

## Article JSON-LD

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Reserved Instances vs Savings Plans: How to Choose (and How an Agent Decides for You)",
  "description": "A practical 2026 guide to choosing between AWS Reserved Instances and Savings Plans.",
  "image": "https://costsage.ai/assets/blog/ri-vs-sp-cover.png",
  "datePublished": "2026-04-29",
  "dateModified": "2026-04-29",
  "author": {"@type": "Organization", "name": "CostSage", "url": "https://costsage.ai"},
  "publisher": {
    "@type": "Organization",
    "name": "CostSage",
    "logo": {"@type": "ImageObject", "url": "https://costsage.ai/assets/costsage_ai_project_logos_cost-sage-logo-dark-01-300x65.png"}
  },
  "mainEntityOfPage": "https://costsage.ai/blog/ri-vs-savings-plans",
  "keywords": "reserved instances, savings plans, aws commitment, finops, compute savings plans, ec2 instance savings plans"
}
```
