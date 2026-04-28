# Posting Queue — Week 01

Theme: **AWS cost foundations** — anchor on /aws and /blog/aws-cost-optimisation-best-practices.
Cadence: LinkedIn company 5/wk (Mon–Fri 9:00 ET), founder amplifies same day +2hr. X 14/wk (2/day, 9:00 + 14:00 ET). 1 carousel (Wed). All UTMs: `?utm_source=<channel>&utm_medium=organic&utm_campaign=w01-aws-foundations`.

---

## LinkedIn Company Posts (5)

### LI-CO-W1-01 (Mon) — "The AWS bill question nobody asks first"
**Hook:** Most AWS cost reviews start with "what's expensive?" The better question: "what's running and shouldn't be?"
**Body:** Idle resources don't show up in dashboards because dashboards report cost, not utilization. We see 12–18% of AWS spend on workloads averaging <5% CPU across a 14-day window. Three places to look first: dev/staging EC2 left on overnight, RDS instances behind deprecated services, NAT gateways routing nothing. Each has a different fix pattern — schedule, decommission, route consolidation.
**CTA:** Full breakdown → costsage.ai/blog/aws-cost-optimisation-best-practices
**Hashtags:** #AWS #FinOps #CloudCost
**Media:** Screenshot of utilization heatmap (idle resources highlighted). [TBD-OPERATOR: brand-approved asset]
**Repurpose source:** /blog/aws-cost-optimisation-best-practices

### LI-CO-W1-02 (Tue) — "RIs vs Savings Plans, the actual decision tree"
**Hook:** "Should we buy RIs or Savings Plans?" is the wrong framing. The real question: how predictable is your compute mix?
**Body:** Decision tree we use: (1) Workload locked to a family for 12+ mo → RI. (2) Mix shifts across families/regions → Compute SP. (3) Fargate or Lambda dominant → Compute SP, never RIs. (4) Spiky? Buy a base layer, leave the peak on-demand. Most teams over-buy SPs by 8–15% because they commit to peak instead of trough. Commit to your floor.
**CTA:** Full guide → costsage.ai/blog/ri-vs-savings-plans
**Hashtags:** #AWS #FinOps #SavingsPlans
**Media:** Decision-tree graphic.
**Repurpose source:** /blog/ri-vs-savings-plans

### LI-CO-W1-03 (Wed) — Carousel post (see storyboard below)
**Hook:** 5 AWS cost mistakes we see in every audit.
**CTA:** Audit your account → costsage.ai/aws
**Hashtags:** #AWS #CloudCost #FinOps
**Media:** 5-panel carousel.
**Repurpose source:** /aws + /blog/aws-cost-optimisation-best-practices

### LI-CO-W1-04 (Thu) — "Dashboards don't ship savings"
**Hook:** A dashboard that tells you "you're spending too much on EC2" is not FinOps. It's a receipt.
**Body:** The gap between "we know" and "we fixed it" is where 80% of cloud savings die. FinOps tools that stop at visibility leave engineering to translate insight into PRs. Agentic FinOps closes the loop: detect → recommend → ship the change as a PR/ticket your team can review and merge.
**CTA:** What agentic FinOps means → costsage.ai/finops-agent-vs-dashboard
**Hashtags:** #FinOps #AgenticAI #CloudCost
**Media:** Side-by-side: dashboard view vs PR view.
**Repurpose source:** /finops-agent-vs-dashboard

### LI-CO-W1-05 (Fri) — "How we think about CloudZero vs CostSage"
**Hook:** Asked 3x this week: how is CostSage different from CloudZero?
**Body:** Short version: CloudZero is excellent at unit economics reporting. CostSage is built to *act* — generate the PR, schedule the SP buy, decommission the idle resource. They're complements more often than competitors, but if you only have budget for one and your team is small, the agentic actor wins on time-to-savings.
**CTA:** Side-by-side → costsage.ai/compare/cloudzero-vs-costsage
**Hashtags:** #FinOps #CloudCost
**Media:** Comparison table screenshot.
**Repurpose source:** /compare/cloudzero-vs-costsage

---

## Founder Amplification Posts (5) — same day, +2hr

### LI-F-W1-01 (Mon) — quote-amplify LI-CO-W1-01
"This one bites every team I talk to. We had a customer last month with $14K/mo on a NAT gateway that hadn't routed business traffic in 6 weeks. Posted the deeper write-up on the company page ↓"

### LI-F-W1-02 (Tue) — quote-amplify LI-CO-W1-02
"The trough-vs-peak commit mistake is the most expensive default in FinOps. Wrote up the actual decision tree we use with customers ↓"

### LI-F-W1-03 (Wed) — carousel reshare
"5 mistakes I'd bet money are in your AWS account right now. Carousel ↓"

### LI-F-W1-04 (Thu) — POV
"FinOps tools that stop at the dashboard are SaaS receipts. The interesting work is closing the loop. Why we built CostSage as an agent, not a chart ↓"

### LI-F-W1-05 (Fri) — comparison
"We get the CloudZero question every week. Honest take ↓ — they're great at what they do; we built for a different job."

---

## X Posts (14)

### X-W1-01 (Mon 9am) — single
Most AWS cost reviews start with "what's expensive?" Better question: "what's running and shouldn't be?"
12–18% of AWS spend, on average, sits on workloads under 5% CPU.
costsage.ai/blog/aws-cost-optimisation-best-practices
**CTA:** read • **Hashtags:** #AWS #FinOps • **Media:** none • **Source:** /blog/aws-cost-optimisation-best-practices

### X-W1-02 (Mon 2pm) — single
NAT gateways that route nothing are the most expensive "ghost" line item in AWS.
$0.045/GB processing + $0.045/hr × 24 × 30 = $32.40/mo *idle*.
Multiply by every region you forgot about.
**Source:** /blog/aws-cost-optimisation-best-practices

### X-W1-03 (Tue 9am) — THREAD start (5 tweets)
1/ "Should we buy RIs or Savings Plans?" is the wrong question.
The real one: how predictable is your compute mix over 12 months?
2/ Locked to one instance family for 12+ mo → RI. Best discount, least flexibility.
3/ Mix shifts across families or regions → Compute Savings Plan. Worse discount, much more flex.
4/ Fargate / Lambda heavy → Compute SP. RIs don't apply.
5/ Spiky workload? Commit to your floor, not your peak. Most teams over-buy by 8–15%.
Full decision tree → costsage.ai/blog/ri-vs-savings-plans
**Source:** /blog/ri-vs-savings-plans

### X-W1-04 (Tue 2pm) — single
Rule of thumb: never commit Savings Plans to peak. Commit to trough.
Peak commit = guaranteed waste on the days you're below.
Trough commit = guaranteed coverage; on-demand handles the spikes.

### X-W1-05 (Wed 9am) — single (carousel-LI driver)
We listed the 5 AWS cost mistakes that show up in literally every audit we run.
Posted on LinkedIn this morning → [TBD-OPERATOR: paste LI URL]

### X-W1-06 (Wed 2pm) — single
Untagged resources are the silent killer. You can't allocate what you can't identify, and "Other" is the largest cost center in most AWS accounts. Tag at create time, not at audit time.

### X-W1-07 (Thu 9am) — THREAD start (4 tweets)
1/ A dashboard that tells you "EC2 is expensive" isn't FinOps. It's a receipt.
2/ The gap between "we see the problem" and "we shipped the fix" is where 80% of savings die.
3/ Agentic FinOps closes that loop: detect → recommend → open the PR.
4/ Why we built CostSage as an agent, not a chart → costsage.ai/finops-agent-vs-dashboard
**Source:** /finops-agent-vs-dashboard

### X-W1-08 (Thu 2pm) — single
"We'll fix it next sprint" is the most expensive sentence in FinOps.

### X-W1-09 (Fri 9am) — single
CloudZero vs CostSage — short version:
CloudZero: best-in-class unit economics reporting.
CostSage: built to *act* — PR, ticket, scheduled action.
They complement more often than they compete.
costsage.ai/compare/cloudzero-vs-costsage

### X-W1-10 (Fri 2pm) — single
nOps vs CostSage in one line:
nOps is a managed-services overlay; CostSage is an agent that ships changes into your existing engineering workflow.
costsage.ai/compare/nops-vs-costsage
**Source:** /compare/nops-vs-costsage

### X-W1-11 (Sat 10am) — single (evergreen)
Cheapest AWS optimization: turn off dev/staging on weekends. 48 hours × ~30% of fleet = real money. Costs you nothing to ship.

### X-W1-12 (Sat 3pm) — single
Reserved Instance marketplace is underused. If your needs change mid-term, you can sell standard RIs. Not all teams know.

### X-W1-13 (Sun 11am) — single (community)
Reading list this week:
- /blog/aws-cost-optimisation-best-practices
- /blog/ri-vs-savings-plans
- /finops-agent-vs-dashboard
All on costsage.ai.

### X-W1-14 (Sun 4pm) — single
What's the most surprising line item you've found in an AWS bill? Reply — we'll share the wildest ones (anonymized) next week.

---

## Carousel Storyboard — "5 AWS cost mistakes we see in every audit"

**Format:** 5 panels, 1080x1350 px, brand template.

**Panel 1 — Cover:** "5 AWS cost mistakes we see in every audit." Subtext: "From 50+ FinOps engagements." CostSage mark bottom-right.

**Panel 2 — Mistake #1: Idle dev/staging:** Headline "Dev/staging running 24/7." Body: 12–18% of fleet under 5% CPU. Fix: scheduler tags + automated nightly stop. Visual: utilization heatmap, weekend gap absent.

**Panel 3 — Mistake #2: Peak-committed Savings Plans:** Headline "Committing to peak, not trough." Body: every hour below your commit is waste. Fix: commit to floor; let on-demand handle spikes.

**Panel 4 — Mistake #3: Untagged spend:** Headline "‘Other’ is your biggest cost center." Body: untagged = unallocatable. Fix: enforce tags at create-time via SCP + Terraform module.

**Panel 5 — Mistake #4 + #5 + CTA:** "#4 Idle NAT gateways. #5 Oversized RDS read replicas." CTA: "Audit your account in 10 min → costsage.ai/aws"

**CTA:** costsage.ai/aws
**Hashtags (post body):** #AWS #FinOps #CloudCost
**Media note:** brand template [TBD-OPERATOR confirm]
**Repurpose source:** /aws + /blog/aws-cost-optimisation-best-practices

---

**Week 1 totals:** LI company 5, founder 5, X singles 12, X threads 2 (9 tweets in threads), 1 carousel.
