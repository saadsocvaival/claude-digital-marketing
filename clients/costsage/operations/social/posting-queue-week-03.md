# Posting Queue — Week 03

Theme: **Agentic FinOps + multi-cloud (Azure)** — anchor on /finops-agent-vs-dashboard + /azure.
Campaign = `w03-agentic-azure`.

---

## LinkedIn Company Posts (5)

### LI-CO-W3-01 (Mon) — "What ‘agentic’ actually means in FinOps"
**Hook:** "Agentic AI" is the most overloaded word in SaaS this year. Here's the working definition we use internally.
**Body:** An agentic FinOps tool: (1) observes the system continuously, (2) decides on a recommended action with a confidence score, (3) writes the action — PR, ticket, scheduled job — into a system you already use, and (4) closes the loop by tracking whether it merged and what the realized savings were. Anything missing one of those four isn't agentic; it's a chart with a button.
**CTA:** costsage.ai/finops-agent-vs-dashboard
**Hashtags:** #AgenticAI #FinOps
**Media:** 4-step diagram.
**Repurpose source:** /finops-agent-vs-dashboard

### LI-CO-W3-02 (Tue) — "Azure cost is AWS cost with different vocabulary"
**Hook:** Azure cost optimization isn't a different sport. It's the same sport with relabeled equipment.
**Body:** AWS Reserved Instances ↔ Azure Reservations. AWS Savings Plans ↔ Azure Savings Plans (yes, same name, slightly different rules). AWS Cost Explorer ↔ Azure Cost Management. The mistake teams make is treating the two as separate cultures. Same FinOps fundamentals — commit to the floor, kill the idle, tag everything — different APIs.
**CTA:** Azure-specific guide → costsage.ai/azure
**Hashtags:** #Azure #FinOps
**Media:** Cross-cloud terminology table.
**Repurpose source:** /azure

### LI-CO-W3-03 (Wed) — Carousel: "AWS → Azure FinOps glossary in one page"
**Hook:** If you do AWS cost optimization and just inherited Azure, here's the cheat sheet.
**CTA:** costsage.ai/azure
**Hashtags:** #Azure #AWS #FinOps
**Media:** 5-panel carousel.
**Repurpose source:** /azure

### LI-CO-W3-04 (Thu) — "Three things an agent should never auto-execute"
**Hook:** Agentic FinOps means the agent ships work into your workflow. It does not mean the agent ships changes into prod without you.
**Body:** Things our agent will never execute without human review: (1) deletion of any resource >7 days old, (2) Savings Plan / Reservation purchases, (3) anything that crosses an account/subscription boundary. These create PRs and tickets, never silent kills. Agentic ≠ autonomous. Agentic = drafts the change with full context, you press merge.
**CTA:** costsage.ai/finops-agent-vs-dashboard
**Hashtags:** #AgenticAI #FinOps #Engineering
**Media:** "PR, never prod" graphic.
**Repurpose source:** /finops-agent-vs-dashboard

### LI-CO-W3-05 (Fri) — "FinOps for AI workloads is the next chapter"
**Hook:** Most FinOps tools were built before GPU spend was material. The next chapter is here, and it's expensive.
**Body:** GPU instance pricing breaks the assumptions of classic FinOps: (1) RIs/SPs cover G/P-series differently than M/C; (2) idle GPUs cost 8–15x idle CPUs; (3) inference vs training have totally different commit profiles. Teams running >$30K/mo on AI compute should treat it as its own cost center, not a line item under "EC2."
**CTA:** Newsletter issue 1 covers this in depth → [TBD-OPERATOR newsletter URL]
**Hashtags:** #AI #FinOps #GPU
**Media:** GPU vs CPU idle-cost comparison.
**Repurpose source:** Newsletter issue 1 (FinOps for AI workloads).

---

## Founder Amplification Posts (5)

### LI-F-W3-01 (Mon) "‘Agentic’ is overloaded. Here's the 4-part test we apply to ourselves before using the word ↓"

### LI-F-W3-02 (Tue) "Watched a team treat AWS and Azure as separate FinOps universes. They're not. Same sport, different jerseys ↓"

### LI-F-W3-03 (Wed) "Cheat sheet: AWS terminology → Azure equivalent. Saved me a month onboarding the first time ↓"

### LI-F-W3-04 (Thu) "Important boundary for agentic systems: the agent drafts; you merge. Three things ours will never auto-execute ↓"

### LI-F-W3-05 (Fri) "GPU spend breaks classic FinOps. We're publishing a newsletter on it next week. Preview ↓"

---

## X Posts (14)

### X-W3-01 (Mon 9am) — single
"Agentic" test:
1) observes continuously
2) decides with confidence score
3) writes the action into a real system (PR/ticket)
4) closes the loop on realized savings
Miss one = chart with a button.

### X-W3-02 (Mon 2pm) — single
A confidence score on a recommendation is a forcing function. It makes the model commit. Demand it from any AI tool you adopt.

### X-W3-03 (Tue 9am) — THREAD (5 tweets)
1/ Azure cost optimization isn't a different sport. Same sport, different jerseys.
2/ AWS RI ↔ Azure Reservation
3/ AWS Savings Plan ↔ Azure Savings Plan (yes, same name)
4/ AWS Cost Explorer ↔ Azure Cost Management
5/ Same fundamentals: commit to floor, kill idle, tag everything. costsage.ai/azure
**Source:** /azure

### X-W3-04 (Tue 2pm) — single
Multi-cloud FinOps is mostly a vocabulary problem until it's a tagging problem.

### X-W3-05 (Wed 9am) — single (carousel driver)
AWS → Azure terminology cheat sheet, in one carousel.
LinkedIn → [TBD-OPERATOR LI URL]

### X-W3-06 (Wed 2pm) — single
Tag schema that survives multi-cloud:
- env
- owner (team email)
- service
- cost-center
Same names on AWS and Azure. Future-you says thanks.

### X-W3-07 (Thu 9am) — THREAD (4 tweets)
1/ Things our agent will never auto-execute:
2/ Resource deletion >7 days old
3/ SP / Reservation purchases
4/ Cross-account/subscription changes
PR, never prod. Agentic ≠ autonomous.

### X-W3-08 (Thu 2pm) — single
Best mental model for an AI agent in your infra: a thoughtful junior engineer who never sleeps and always opens a PR.

### X-W3-09 (Fri 9am) — single
GPU FinOps fact: an idle G5 instance costs ~10x an idle M5.
If you have GPUs and you're not scheduling them like batch jobs, you're burning.

### X-W3-10 (Fri 2pm) — single
Inference vs training have different commit profiles.
Inference = predictable → reservation candidate.
Training = bursty → spot or short-term commit.
Don't lump them.

### X-W3-11 (Sat 10am) — single (evergreen)
Cheapest GPU optimization: shut down notebook instances overnight. Data scientists don't ssh in at 2am.

### X-W3-12 (Sat 3pm) — single
Spot instances for stateless workers. Still works. Still 70%+ savings. Underused.

### X-W3-13 (Sun 11am) — single (community)
What's your team's policy on GPU instance shutdown? Reply — collecting patterns for the newsletter.

### X-W3-14 (Sun 4pm) — single
Reading list:
- /finops-agent-vs-dashboard
- /azure
- /aws
All on costsage.ai.

---

## Carousel Storyboard — "AWS → Azure FinOps glossary"

5 panels.
**Panel 1 — Cover:** "AWS → Azure FinOps glossary."
**Panel 2 — Compute commits:** RI → Reservation. SP → Azure SP for Compute.
**Panel 3 — Visibility:** Cost Explorer → Cost Management. CUR → Exports to Storage.
**Panel 4 — Tagging:** Tags → Tags (case-sensitive on Azure! gotcha).
**Panel 5 — CTA:** "Full Azure guide → costsage.ai/azure"
**Repurpose source:** /azure

**Week 3 totals:** LI co 5, founder 5, X singles 12, X threads 2 (9 tweets), 1 carousel.
