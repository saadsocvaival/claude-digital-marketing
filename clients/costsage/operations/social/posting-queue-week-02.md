# Posting Queue — Week 02

Theme: **RIs vs Savings Plans deep week** — anchor on /blog/ri-vs-savings-plans + /pricing.
Cadence and UTM convention as Week 1, campaign = `w02-ri-vs-sp`.

---

## LinkedIn Company Posts (5)

### LI-CO-W2-01 (Mon) — "The 90% rule for Savings Plans"
**Hook:** If your Savings Plan utilization is below 90%, you're losing money on the commitment itself. Here's the math.
**Body:** SP discount averages ~28% on Compute. If utilization drops to 80%, your effective discount falls to ~12% — barely better than a 1-yr no-upfront RI. We re-calc utilization weekly, not monthly. Below 90%, we recommend either (a) right-sizing the commit downward at renewal or (b) shifting workloads back onto the SP via instance-family normalization. Don't wait until renewal to find out.
**CTA:** Full math → costsage.ai/blog/ri-vs-savings-plans
**Hashtags:** #AWS #FinOps #SavingsPlans
**Media:** Utilization curve graphic.
**Repurpose source:** /blog/ri-vs-savings-plans

### LI-CO-W2-02 (Tue) — "Why FinOps lives in engineering, not finance"
**Hook:** FinOps that lives in finance produces reports. FinOps that lives in engineering produces savings.
**Body:** The handoff cost is everything. When the team that owns the workload also owns the cost number, decisions happen in PRs and design reviews instead of QBRs. Best teams we work with: cost is a column in the engineering scorecard, not a separate dashboard. Finance still owns the budget envelope; engineering owns the burn rate.
**CTA:** How we ship savings into eng workflow → costsage.ai/finops-agent-vs-dashboard
**Hashtags:** #FinOps #Engineering
**Media:** Org-diagram graphic.
**Repurpose source:** /finops-agent-vs-dashboard

### LI-CO-W2-03 (Wed) — Carousel: "Anatomy of a wasted Savings Plan"
**Hook:** We took an anonymized customer SP commit and broke down where the 23% waste came from.
**CTA:** costsage.ai/blog/ri-vs-savings-plans
**Hashtags:** #AWS #FinOps
**Media:** 5-panel carousel.
**Repurpose source:** /blog/ri-vs-savings-plans

### LI-CO-W2-04 (Thu) — "Pricing transparency is a FinOps signal"
**Hook:** If a FinOps vendor's pricing isn't on their site, ask why.
**Body:** Cost-optimization tools should have transparent cost themselves. We publish pricing because we sell to people who can spot a non-linear "Contact us" model from a mile away. Three things to check on any FinOps vendor's pricing page: (1) is it usage-based or seat-based? (2) does it scale with your AWS spend? (3) is there a real free trial?
**CTA:** Our pricing → costsage.ai/pricing
**Hashtags:** #FinOps #SaaS
**Media:** Pricing page screenshot.
**Repurpose source:** /pricing

### LI-CO-W2-05 (Fri) — "nOps vs CostSage — when each wins"
**Hook:** "Should we use nOps or CostSage?" The honest answer depends on team size.
**Body:** nOps is a strong fit when you want a managed-services overlay and a vendor-led optimization motion. CostSage fits when you want an agent that ships changes into your engineering workflow and your team is doing the merging. Side-by-side comparison breaks down where each wins.
**CTA:** costsage.ai/compare/nops-vs-costsage
**Hashtags:** #FinOps #AWS
**Media:** Comparison table.
**Repurpose source:** /compare/nops-vs-costsage

---

## Founder Amplification Posts (5)

### LI-F-W2-01 (Mon) "We watched a customer leak $40K/yr because their SP utilization had drifted to 76% and nobody caught it until renewal. Below-90% should be a P1 alert. Wrote it up ↓"

### LI-F-W2-02 (Tue) "Every successful FinOps program I've seen has cost as an engineering metric, not a finance one. The ones that don't, fail. ↓"

### LI-F-W2-03 (Wed) "Took a real (anonymized) Savings Plan and broke down the 23% that was wasted. Carousel ↓"

### LI-F-W2-04 (Thu) "If you're shopping FinOps tools and the pricing page says ‘Contact us’ — ask why. We publish ours. ↓"

### LI-F-W2-05 (Fri) "Get the nOps question almost weekly. Here's where each tool wins, honestly. ↓"

---

## X Posts (14)

### X-W2-01 (Mon 9am) — single
SP utilization below 90% = your effective discount is ~12%, not 28%.
You're paying for coverage you're not using.
Re-check utilization weekly, not at renewal.

### X-W2-02 (Mon 2pm) — single
FinOps anti-pattern: monthly SP review.
By the time the report lands, you're 30 days into the waste.

### X-W2-03 (Tue 9am) — THREAD (5 tweets)
1/ FinOps that lives in finance produces reports.
FinOps that lives in engineering produces savings.
2/ Difference is the handoff cost.
3/ Best teams: cost is a column in the eng scorecard, not a separate dashboard.
4/ Finance owns the budget envelope. Engineering owns the burn rate.
5/ How to ship savings into eng workflow: costsage.ai/finops-agent-vs-dashboard
**Source:** /finops-agent-vs-dashboard

### X-W2-04 (Tue 2pm) — single
Cost should appear in a PR description.
"This change adds ~$340/mo on RDS storage."
Make it impossible to merge in the dark.

### X-W2-05 (Wed 9am) — single (carousel driver)
Took a real (anonymized) Savings Plan and broke down the 23% waste line by line.
Carousel on LinkedIn → [TBD-OPERATOR LI URL]

### X-W2-06 (Wed 2pm) — single
Three SP traps:
1) Committing to peak
2) Committing to a region you're migrating away from
3) 3-yr term on a workload that's <12 mo old
Don't.

### X-W2-07 (Thu 9am) — THREAD (4 tweets)
1/ Quick test for any FinOps vendor:
2/ Is pricing on the site?
3/ Does it scale with your AWS spend, not your seat count?
4/ Is the trial real?
Ours: costsage.ai/pricing

### X-W2-08 (Thu 2pm) — single
"Contact us for pricing" on a FinOps tool is its own kind of irony.

### X-W2-09 (Fri 9am) — single
nOps vs CostSage in one line:
nOps = managed services overlay.
CostSage = agent that ships PRs into your engineering flow.
costsage.ai/compare/nops-vs-costsage

### X-W2-10 (Fri 2pm) — single
The cheapest cost optimization is the one your engineers ship without thinking about it.
Make the action one-click. Make the savings visible. Repeat.

### X-W2-11 (Sat 10am) — single (evergreen)
Tag everything at create time.
Three required tags minimum: env, owner, service.
Enforce via SCP. Don't audit your way out of an untagged account, you'll lose.

### X-W2-12 (Sat 3pm) — single
Reserved Instance hack: convertible RIs let you change instance family mid-term. Discount is smaller (~5–10% less) but you regain flexibility lost on standard RIs.

### X-W2-13 (Sun 11am) — single (community)
Question for the FinOps practitioners: what's the most useful single chart in your monthly review? Replies welcome.

### X-W2-14 (Sun 4pm) — single
Weekend reading from costsage.ai:
- /blog/ri-vs-savings-plans
- /finops-agent-vs-dashboard
- /pricing (yes, transparent)

---

## Carousel Storyboard — "Anatomy of a wasted Savings Plan"

5 panels, 1080x1350 px.
**Panel 1 — Cover:** "Anatomy of a wasted Savings Plan." Subtext: "Real, anonymized — $1.2M annual SP commit."
**Panel 2 — Layer 1, peak commit:** "Committed to peak: 11% wasted on under-utilization."
**Panel 3 — Layer 2, region drift:** "Migrated workload to us-west-2; SP stuck in us-east-1: 6% wasted."
**Panel 4 — Layer 3, family drift:** "Workload moved m5 → m6i; non-convertible SP: 6% wasted."
**Panel 5 — Total + CTA:** "23% of $1.2M = $276K/yr wasted. Audit yours → costsage.ai/blog/ri-vs-savings-plans"
**Repurpose source:** /blog/ri-vs-savings-plans

**Week 2 totals:** LI co 5, founder 5, X singles 12, X threads 2 (9 tweets), 1 carousel.
