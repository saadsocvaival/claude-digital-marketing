# Newsletter Issue 03 — The Hidden Cost of Bad Tagging

**Subject A:** "Other" is your biggest AWS cost center
**Subject B:** Tagging is the most boring high-ROI work in FinOps
**Preview text:** Why tagging is the only FinOps work where ROI is asymmetric and effort is one sprint.
**UTM campaign slug:** `nl-issue-03-tagging`

---

## Block 1 — Hook

If your AWS Cost Explorer's largest cost center is called "Other" — or worse, "Untagged" — you don't have a cost problem. You have an *allocation* problem. And you can't optimize what you can't allocate.

This issue: why tagging is the highest-ROI engineering work nobody schedules, the four-tag minimum, and how to drop your allocation gap from 40% to <5% in three weeks.

---

## Block 2 — Deep dive

Tagging gets postponed for the same reason flossing does: it's tedious, the cost is upfront, and the benefit is invisible until something breaks.

But the math on tagging is asymmetric in a way no other FinOps work is. Cost: roughly one engineering sprint to get a Terraform module + SCP in place. Benefit: every cost decision from that point forward is *informed*. Without tags, every "is this team's spend going up?" question is a wild guess; every chargeback model is fiction; every product unit-economics number has a margin of error wider than the gross margin itself.

**The four-tag minimum.** The minimum useful tag schema:

- `env` — prod / staging / dev / test
- `owner` — team email or Slack handle (a *human-resolvable* address, not a person's name)
- `service` — the application or microservice
- `cost-center` — finance's allocation bucket

That's it. More tags can be useful (`compliance`, `lifecycle`, `pii`), but adding them before the four foundational ones are universally enforced is premature optimization.

**Why audit-only fails.** Most teams "tag" via quarterly audits: spreadsheet, who owns this resource, fill in the blanks. This works for ~6 weeks and decays. The structural fix is enforcement at *create time*: an AWS Service Control Policy that denies resource creation without the four required tags + a Terraform module that ships them by default. Untagged resources literally can't exist.

**The 3-week migration.** Realistic shape:
- Week 1: define schema, get sign-off, write SCP in dry-run mode (logs only). Audit existing resources, identify untagged.
- Week 2: enforce SCP. New resources comply or fail. Backfill tags on existing resources via Resource Groups Tag Editor — 80/20 rule, prioritize the top 20 cost contributors.
- Week 3: enable tags as cost-allocation tags in Billing. Wait 24h. Allocation gap is now visible — should drop to <10% if backfill was thorough, <5% within another month as long-tail resources cycle.

**What it unlocks.** Once allocation is real: chargeback works, unit economics math works, anomaly detection works (a service whose cost doubles is suddenly *findable*), and every other piece of FinOps tooling stops lying to you.

For the engineering pattern (Terraform module + SCP example), our /aws page covers the implementation: costsage.ai/aws?utm_source=email&utm_medium=newsletter&utm_campaign=nl-issue-03-tagging&utm_content=block2

---

## Block 3 — Tactical tip

**Tip: turn on AWS-generated cost allocation tags this week.**

In Billing → Cost Allocation Tags → enable AWS-generated tags (`aws:createdBy`, etc.). Free. Takes 60 seconds. They'll start populating within 24 hours and give you a *partial* allocation view immediately, while you build out the proper schema. Not a substitute for user-defined tags, but a useful diagnostic in the meantime.

---

## Block 4 — Community

The FinOps Foundation maintains a tagging best-practices working group; their reference schemas are a useful starting point ([TBD-OPERATOR — link]).

Counter-take we found credible (paraphrased): *"Don't enforce tags via SCP — it breaks emergency provisioning."* Fair concern; the answer is a break-glass IAM role with a short audit trail, not abandoning enforcement. The trade-off is real but manageable.

---

## Block 5 — CTA

If your allocation gap is >10%, you're flying half-blind on cost. We built CostSage to flag tag drift the moment it happens and recommend the SCP changes that would have caught it.

→ Run the audit: costsage.ai/aws?utm_source=email&utm_medium=newsletter&utm_campaign=nl-issue-03-tagging&utm_content=cta

— {{sender_first}}
Founder, CostSage

---

[Footer per compliance-footers.md]
