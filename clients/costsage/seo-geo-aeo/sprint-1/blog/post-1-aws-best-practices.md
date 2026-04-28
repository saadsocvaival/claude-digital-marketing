---
slug: aws-cost-optimisation-best-practices
url: https://costsage.ai/blog/aws-cost-optimisation-best-practices
title: 10 AWS Cost Optimisation Best Practices Every SaaS Company Should Follow in 2026
description: A 2026 playbook for AWS cost optimisation across rightsizing, Savings Plans, idle resources, storage, and tagging — written for SaaS teams already past visibility.
canonical: https://costsage.ai/blog/aws-cost-optimisation-best-practices
publish_date: 2026-04-28
author: CostSage Engineering
schema_type: Article
internal_links:
  - /finops-agent-vs-dashboard
  - /aws
  - /features
  - /pricing
  - /blog/ri-vs-savings-plans
word_count_target: 2400
status: draft-for-review
---

# 10 AWS Cost Optimisation Best Practices Every SaaS Company Should Follow in 2026

> **TL;DR.** AWS cost optimisation in 2026 is no longer a quarterly tagging
> exercise. The teams keeping cloud bills flat while ARR doubles are doing ten
> specific things — most of them automatable. This guide walks through each
> one, with the underlying mechanics, the typical waste percentage it
> recovers, and how an agentic FinOps tool changes the work.

## Why this list looks different in 2026

The AWS cost-optimisation literature from 2019–2023 boils down to: see your
spend, find your waste, file a ticket, hope someone fixes it. That loop fails
because the gap between *finding* waste and *fixing* it is where money dies.
Modern practice closes that loop. Every recommendation below is paired with
how it gets executed — not just observed. For the broader argument see
[FinOps agent vs dashboard](/finops-agent-vs-dashboard).

---

## 1. Right-size every EC2 and RDS instance against 14 days of CloudWatch

**Why it matters.** The single largest line item in most AWS bills is compute
that's two to three sizes larger than it needs to be. Spec sheets are written
optimistically; CPU and memory utilisation rarely cross 35%.

**The mechanic.** Pull 14 days of CloudWatch utilisation per instance.
Compute p95 CPU + memory + network. Map to the smallest instance class with
≥99.9% headroom guarantee. Apply during a maintenance window or — for
stateless workloads — during a rolling restart.

**Typical recovery.** 15–22% of the EC2 line.

**Agent-driven.** [CostSage on AWS](/aws) computes the recommendation, opens
the change ticket pre-filled, and (after approval) executes the resize inside
a scoped IAM role with rollback if CloudWatch alarms fire.

---

## 2. Hold ≥80% Savings Plan or RI coverage on stable baseline

**Why it matters.** On-demand pricing on stable workloads is a 28–60% premium
over commitment pricing. The penalty grows with utilisation.

**The mechanic.** Identify your stable baseline (the always-on subset of
compute over the last 90 days). Cover it with a 1- or 3-year Savings Plan or
RI. Don't cover beyond the baseline — the residual is what spot, scaled
elastically, or simply paid on-demand.

**Typical recovery.** 18–34% of the covered compute spend.

**Pitfall.** Over-committing during growth periods. Re-evaluate quarterly.
See [Reserved Instances vs Savings Plans](/blog/ri-vs-savings-plans) for the
choice between them.

---

## 3. Kill idle compute on weekends and holidays

**Why it matters.** Non-production workloads (dev, staging, QA, integration)
typically run 24/7 even though humans use them ~50 hours/week. That's a
67%-utilisation upper bound.

**The mechanic.** Tag every non-prod resource with `Schedule=mon-fri-09-19`
(or similar). A scheduler stops them outside the window and starts them on
schedule. Stateful resources need DB-snapshot-and-restore patterns; stateless
just stop.

**Typical recovery.** 40–60% of non-prod compute spend.

**Agent-driven.** The agent enforces tag policy, generates the schedule
proposal per environment, and applies stop/start once approved.

---

## 4. Delete orphaned EBS volumes and stale snapshots

**Why it matters.** EBS volumes detached from EC2, and snapshots older than
your retention policy, are a quiet 2–4% storage tax.

**The mechanic.** List EBS volumes where `AttachmentState != attached` for
≥7 days. List snapshots where `StartTime < retention_threshold`. Confirm
ownership. Delete (with a one-week archive in S3 if recovery insurance
matters).

**Typical recovery.** 1–4% of total AWS spend.

**Pitfall.** Don't delete production-retention snapshots required by
compliance (SOC 2, HIPAA, GDPR backups). Tag retention requirements
explicitly.

---

## 5. Move infrequently-accessed S3 to Intelligent-Tiering or Glacier

**Why it matters.** Standard S3 is overpriced for objects accessed less than
once per month. The bulk of S3 spend in mature SaaS is logs, backups, and
historical analytics — none of which need Standard.

**The mechanic.** Enable S3 Intelligent-Tiering with archive access
configurations on every bucket where access patterns are mixed or unknown.
For purely-archival prefixes, move to Glacier Instant Retrieval or Glacier
Deep Archive directly.

**Typical recovery.** 30–60% of S3 storage spend on the migrated prefixes.

---

## 6. Right-size and consolidate NAT Gateways

**Why it matters.** NAT Gateways at $0.045/hour + $0.045/GB processed are a
hidden line item that scales with traffic, not with engineering effort.
Multi-AZ deployments often run a NAT per AZ when one would do.

**The mechanic.** Audit NAT-Gateway data-processed by AZ for 14 days.
Consolidate where cross-AZ traffic costs are smaller than the saved
NAT-hours. Switch to VPC endpoints for S3, DynamoDB, and other supported
services to bypass NAT entirely for those flows.

**Typical recovery.** 30–70% of NAT Gateway spend; 1–3% of total AWS spend.

---

## 7. Enforce tagging policy at the account boundary

**Why it matters.** Untagged resources block cost allocation. You can't
optimise what you can't attribute. A 95%+ tag-compliance rate is the price
of meaningful cost reporting.

**The mechanic.** Define a minimum tag set (`Owner`, `Environment`,
`CostCentre`, `Application`). Enforce via Service Control Policies at the AWS
Organization level — non-compliant `RunInstances`/`CreateBucket` calls fail.
For pre-existing resources, run a tagger that enriches via reference data
(account → owner; VPC → environment).

**Typical recovery.** Indirect — but unlocks the visibility for everything
else on this list. Cost-allocation accuracy moves from <50% to >95%.

---

## 8. Catch anomalies the same day they start

**Why it matters.** A misconfigured EMR cluster left running over a weekend
can add five figures to a single day's bill. Discovering it on the monthly
invoice is too late.

**The mechanic.** Use AWS Cost Anomaly Detection (free) plus your own
threshold rules per account/service/tag. Route alerts to Slack/PagerDuty
with the 3 likely culprits attached. Time-to-detect target: <24 hours.
Time-to-remediate target: <72 hours.

**Typical recovery.** Variable — but a single missed weekend leak can dwarf
a quarter's structural savings.

---

## 9. Track unit economics: cost per 1,000 API calls / GB processed / active customer

**Why it matters.** Total spend in isolation is meaningless during growth.
The right number is *cost per unit of value delivered*. If cost per 1K API
calls is flat as you scale, you're winning.

**The mechanic.** Tag spend to a *unit*. Compute the ratio monthly. Track
the trend, not the absolute. Investigate any month with >10% unit-cost
inflation. (For the full unit-economics methodology see CostSage's
[unit-economics skill spec](/features#unit-economics).)

**Typical recovery.** Indirect — but exposes structural cost diseases that
rightsizing alone won't catch.

---

## 10. Close the loop: every recommendation becomes an executed action

**Why it matters.** The previous nine practices are useless if your team
doesn't have time to act on the recommendations. This is the failure mode
that buried the dashboard era.

**The mechanic.** Either staff a FinOps team that ships changes weekly, or
run an agent that converts each recommendation into a pre-approved change
request inside guardrails. Both work; the latter scales without headcount.

**Typical recovery.** The full theoretical recovery from 1–9 only realises
when this step happens. Without it, "potential savings" stays a slide.

---

## Putting it together

A SaaS company on $500K/month AWS spend that follows the first eight
practices typically books $120K–$170K/month in waste reduction inside the
first 90 days. The exact number depends on your starting baseline and how
much of it you can execute against. The agent-driven path closes the
execution gap — see how it works on [CostSage on AWS](/aws), or
[start a free trial](/pricing).

---

## FAQ

**How long does it take to implement these 10 practices?**
A dedicated engineer can implement #1–#7 inside a quarter. Practice #10
(closing the loop) is the multi-quarter discipline. An agent compresses the
first quarter to roughly two weeks of approval cycles.

**Which practice has the biggest ROI?**
Almost always #2 (Savings Plan / RI coverage) followed by #1 (rightsizing).
Together they routinely cover 30%+ of the bill in committed-and-rightsized
spend.

**Can these practices be applied to Azure too?**
Yes — the analogues are reservations, VM rightsizing, idle-VM scheduling,
managed-disk cleanup, and Storage tier optimisation. See
[CostSage on Azure](/azure).

**Where does an agent fit in?**
Practices #1–#9 produce recommendations. Practice #10 turns recommendations
into executed change. An agent — like CostSage — runs the recommendation
loop continuously and executes after one human approval, eliminating the
backlog where most savings die. See
[FinOps agent vs dashboard](/finops-agent-vs-dashboard) for the architectural
difference.

---

## Article JSON-LD (drop into `<head>`)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "10 AWS Cost Optimisation Best Practices Every SaaS Company Should Follow in 2026",
  "description": "A 2026 playbook for AWS cost optimisation across rightsizing, Savings Plans, idle resources, storage, and tagging.",
  "image": "https://costsage.ai/assets/blog/aws-best-practices-cover.png",
  "datePublished": "2026-04-28",
  "dateModified": "2026-04-28",
  "author": {"@type": "Organization", "name": "CostSage", "url": "https://costsage.ai"},
  "publisher": {
    "@type": "Organization",
    "name": "CostSage",
    "logo": {"@type": "ImageObject", "url": "https://costsage.ai/assets/costsage_ai_project_logos_cost-sage-logo-dark-01-300x65.png"}
  },
  "mainEntityOfPage": "https://costsage.ai/blog/aws-cost-optimisation-best-practices",
  "keywords": "aws cost optimisation, finops, savings plans, reserved instances, ec2 rightsizing, s3 intelligent tiering, ebs cleanup"
}
```
