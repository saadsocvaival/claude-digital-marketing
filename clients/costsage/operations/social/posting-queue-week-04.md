# Posting Queue — Week 04

Theme: **Comparisons + customer-shaped narrative** — anchor on /compare/* + /pricing.
Campaign = `w04-compare-proof`.

---

## LinkedIn Company Posts (5)

### LI-CO-W4-01 (Mon) — "Tagging is the highest-ROI engineering work nobody schedules"
**Hook:** Tagging is the only FinOps work where the ROI is asymmetric and the cost is one sprint.
**Body:** Untagged spend can't be allocated. Unallocatable spend can't be optimized — you'd be guessing. We've seen teams cut allocation gaps from 40% to 5% in 3 weeks by enforcing 4 tags at create time via a Terraform module + SCP. The work is unglamorous and the savings show up in someone else's column. Schedule it anyway.
**CTA:** Newsletter issue 3 deep dive → [TBD-OPERATOR URL]
**Hashtags:** #FinOps #AWS #Tagging
**Media:** Allocation gap before/after.

### LI-CO-W4-02 (Tue) — "When CloudZero is the right answer (not us)"
**Hook:** A vendor that tells you when you shouldn't buy them is more useful than one that doesn't.
**Body:** CloudZero is the right call when: (a) you're a >$5M/yr cloud spend company with a dedicated FinOps team, (b) unit economics is your primary FinOps story, (c) you have eng capacity to translate insights into action. CostSage is the right call when: (a) $10K–$500K/mo spend, (b) small/no FinOps team, (c) you want the actions auto-drafted.
**CTA:** Side by side → costsage.ai/compare/cloudzero-vs-costsage
**Hashtags:** #FinOps #SaaS
**Media:** Decision matrix.
**Repurpose source:** /compare/cloudzero-vs-costsage

### LI-CO-W4-03 (Wed) — Carousel: "Anatomy of a CostSage PR"
**Hook:** What does an "agent-drafted savings PR" actually look like? Walking through one, panel by panel.
**CTA:** costsage.ai/finops-agent-vs-dashboard
**Hashtags:** #FinOps #AgenticAI
**Media:** 5-panel carousel.

### LI-CO-W4-04 (Thu) — "Pricing usage-based, not seat-based — here's why"
**Hook:** Seat-based pricing on a FinOps tool incentivizes the wrong thing.
**Body:** If your FinOps vendor charges by user, they want more users on the platform. We charge as a small % of optimized spend, so we win when you save. The structure determines the behavior. Watch the pricing page; it tells you what the company is actually optimizing.
**CTA:** costsage.ai/pricing
**Hashtags:** #SaaS #Pricing #FinOps
**Media:** Pricing model comparison.
**Repurpose source:** /pricing

### LI-CO-W4-05 (Fri) — "Month 1 wrap + what we're shipping next"
**Hook:** A month of FinOps writing in one post, plus what's next.
**Body:** Recap: AWS cost foundations, RI vs SP math, agentic FinOps definition, Azure parity, AI workload economics, tagging ROI. Next month we're going deeper on (1) FinOps for K8s, (2) cost in CI/CD pipelines, (3) the unit-economics handoff to product. If there's something you want covered, reply.
**CTA:** Subscribe to the newsletter → [TBD-OPERATOR newsletter URL]
**Hashtags:** #FinOps
**Media:** Month-1 roundup graphic.

---

## Founder Amplification Posts (5)

### LI-F-W4-01 (Mon) "Tagging is unglamorous. So is brushing your teeth. Both are highest-ROI activities in their domain ↓"

### LI-F-W4-02 (Tue) "Wrote out, honestly, when CloudZero is the right call instead of us. ↓"

### LI-F-W4-03 (Wed) "Walking through what a real CostSage-drafted PR looks like. Carousel ↓"

### LI-F-W4-04 (Thu) "Pricing structure tells you what a vendor optimizes for. Why we went usage-based ↓"

### LI-F-W4-05 (Fri) "First month of public writing wrapped. What's next ↓ — reply with topic requests."

---

## X Posts (14)

### X-W4-01 (Mon 9am) — single
Tagging is the only FinOps work where ROI is asymmetric and cost is one sprint. Schedule it.

### X-W4-02 (Mon 2pm) — single
Three required tags at minimum: env, owner, service.
Enforce at create time via SCP.
Don't try to audit your way out of an untagged account.

### X-W4-03 (Tue 9am) — THREAD (5 tweets)
1/ Honest take: when CloudZero is the right call vs CostSage.
2/ CloudZero: $5M+/yr spend, dedicated FinOps team, unit economics is the story.
3/ CostSage: $10K–$500K/mo, small/no FinOps team, want actions drafted for you.
4/ More often a complement than a competitor.
5/ Side-by-side: costsage.ai/compare/cloudzero-vs-costsage
**Source:** /compare/cloudzero-vs-costsage

### X-W4-04 (Tue 2pm) — single
Vendor that tells you when not to buy them > vendor that doesn't.

### X-W4-05 (Wed 9am) — single (carousel driver)
What does an "agent-drafted savings PR" actually look like?
We walked through a real one. Carousel on LinkedIn → [TBD-OPERATOR]

### X-W4-06 (Wed 2pm) — single
PR description fields we standardized:
- Recommendation
- Confidence
- Estimated $/mo savings
- Rollback steps
Make it impossible to merge without context.

### X-W4-07 (Thu 9am) — THREAD (4 tweets)
1/ Seat-based pricing on a FinOps tool incentivizes the wrong thing.
2/ Vendor wants more users on platform.
3/ Usage-based (% of optimized spend) → vendor wins when you save.
4/ Pricing structure tells you what the company optimizes for. Ours: costsage.ai/pricing

### X-W4-08 (Thu 2pm) — single
"Contact us" pricing on a tool whose job is making cost legible is its own punchline.

### X-W4-09 (Fri 9am) — single
Month 1 wrap (links in replies):
- AWS foundations
- RI vs SP math
- Agentic FinOps definition
- Azure parity
- AI workload economics
- Tagging ROI

### X-W4-10 (Fri 2pm) — single
Coming in month 2: FinOps for K8s, cost in CI/CD, unit-economics handoff to product. Reply with what else you want.

### X-W4-11 (Sat 10am) — single
Cheapest K8s optimization: rightsize requests/limits. Most teams pad by 3–5x. Pad by 1.3x.

### X-W4-12 (Sat 3pm) — single
Spot for stateless. Reserved for stateful. Don't let it get more complicated than that on day 1.

### X-W4-13 (Sun 11am) — single (community)
Reply with the most expensive AWS lesson you've learned. We'll round them up next week (anonymized if you want).

### X-W4-14 (Sun 4pm) — single
Subscribe to our FinOps newsletter — twice a month, no fluff: [TBD-OPERATOR signup URL].

---

## Carousel Storyboard — "Anatomy of a CostSage PR"

5 panels.
**Panel 1 — Cover:** "Anatomy of a CostSage savings PR."
**Panel 2 — Title + summary:** "Right-size m5.4xlarge → m6i.2xlarge on prod-ingest. Est. $1,840/mo. Confidence: 0.92."
**Panel 3 — Evidence section:** 14-day CPU/mem chart, p95 utilization.
**Panel 4 — Rollback steps:** Terraform diff + revert command.
**Panel 5 — CTA:** "See it on real infra → costsage.ai/finops-agent-vs-dashboard"

**Week 4 totals:** LI co 5, founder 5, X singles 12, X threads 2 (9 tweets), 1 carousel.

---

## 4-Week Aggregate

- LinkedIn company posts: 20
- LinkedIn founder posts: 20
- X singles: 48
- X threads: 8 (36 tweets total in threads)
- X total tweets: 84
- Carousels: 4 (20 panels)
