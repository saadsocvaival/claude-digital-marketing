# Repurposing Engine — One Long-Form into Ten Assets

> Owner: Content Lead • v1.0 • 2026-04-28
> Goal: every pillar piece, in addition to the long form, ships as **5 LinkedIn posts + 3 X threads + 1 newsletter section + 1 sales card** within 14 days of publication.

---

## 1. The recipe (per pillar piece)

| # | Asset | Source extract | Cadence after publication |
|---|-------|----------------|---------------------------|
| 1 | LinkedIn post — main argument | The thesis paragraph + one number | Day 0 |
| 2 | LinkedIn post — counter-intuitive claim | The most contrarian H2 | Day 2 |
| 3 | LinkedIn carousel — playbook steps | The numbered list section | Day 4 |
| 4 | LinkedIn post — micro-case | The example or paragraph with a $ figure | Day 7 |
| 5 | LinkedIn post — author POV | The conclusion's category claim, in first person | Day 11 |
| 6 | X thread — the playbook | The numbered list, 1 step per post | Day 1 |
| 7 | X thread — the contrarian take | The single H2 that breaks consensus | Day 5 |
| 8 | X thread — the FAQ | The FAQ block, repackaged | Day 9 |
| 9 | Newsletter section — Block 2 of an issue | The teardown paragraph + 1 link | Next issue |
| 10 | Sales card — 1-page PDF for AEs | TL;DR + 3 stats + CTA | Day 0 |

## 2. Voice rules (all platforms inherit `voice-guidelines.md`)

- LinkedIn: 80–220 words, plain text or single image, no emoji-spam, lead with a number.
- X: 6–10 posts per thread, 220–280 chars each, one number per post, one image (chart) max in post 1.
- Newsletter: respect the 5-block template.
- Sales card: ≤350 words, brand-locked design.

## 3. Concrete worked example — `/blog/aws-cost-optimisation-best-practices`

The article: "10 AWS Cost Optimisation Best Practices Every SaaS Company Should Follow in 2026."

### LinkedIn Post 1 — Main argument (Day 0)
> The thing about AWS cost optimisation in 2026: a $500K/mo bill is hiding $120K–$170K of recoverable waste, and ten specific practices recover ~80% of it.
>
> Here's the part that's changed:
> Most of those ten practices are now automatable. The bottleneck isn't the analysis anymore. It's the execution.
>
> The teams keeping cloud bills flat while ARR doubles are running the same ten-step playbook. They're just running it continuously, not quarterly.
>
> Full playbook: [link]

### LinkedIn Post 2 — Counter-intuitive claim (Day 2)
> Unpopular opinion: most "rightsizing" projects fail not because the recommendations are wrong, but because nobody had time to act on them.
>
> The recommendation engine isn't the constraint. The Jira backlog is.
>
> Until you close the loop between "this should be `m6i.large`" and the actual `terraform apply` — with a human approval — your FinOps program is theater.
>
> Closing the loop is step 10 of the playbook for a reason. It's the step that makes the other nine matter.

### LinkedIn Carousel — 10 practices (Day 4)
- Slide 1: cover, "10 AWS cost practices that actually move the bill in 2026."
- Slides 2–11: one practice per slide, each with: one-line claim + typical recovery % + one-line mechanism.
- Slide 12: CTA — read the full piece + connect AWS in 60 seconds.

### LinkedIn Post 4 — Micro-case (Day 7)
> A $500K/mo AWS bill walks into a quarterly review.
> Compute is 60%. Idle resources are ~7% of compute. Untagged spend is ~32%. Commitment coverage is 22%. On-demand premium on the un-covered baseline is ~38%.
>
> The recoverable ceiling, before anyone touches an architecture decision, is $120K–$170K/mo. Inside 90 days. With the existing engineering team, if and only if the work isn't tickets.
>
> If the work is tickets, it's a year. If the work is an agent, it's a quarter.

### LinkedIn Post 5 — Author POV (Day 11)
> I keep saying this and I'll keep saying it: visibility is not the product. Action is.
>
> The dashboard era of FinOps showed engineering and finance the waste. Twelve years later, we still have the waste. The job was never to look at the chart. The job was to ship the change.
>
> Agentic FinOps is not "AI on top of a dashboard." It's the entire posture flipped. Read → reason → plan → approve → execute → audit → rollback. The dashboard is a side effect, not the product.

### X Thread A — The playbook (Day 1)
- Post 1: "A $500K/mo AWS bill is hiding $120K–$170K of recoverable waste. 10 practices recover ~80% of it. Thread:"
- Post 2: "1/ Rightsize EC2/RDS. Typical recovery: 15–22% of EC2 spend. Most line items run 2–3 sizes too big."
- Post 3: "2/ Commitment coverage. On-demand pricing is 28–60% over commitment pricing on stable workloads. Recovery: 18–34% of covered spend."
- Post 4: "3/ Idle resource cleanup. Sounds basic. Recovery: 6–10% of total bill. The boring step that pays for the rest."
- Post 5: "4/ Tag enforcement. Until you can allocate 75%+ of spend by service, you can't intelligently rightsize or commit."
- Post 6: "5/ S3 lifecycle. 30–55% recovery on S3 spend on first pass. Lifecycle policies, not point-in-time deletes."
- Post 7: "6/ NAT/networking diet. Variable. $5–20K/mo on a $200K bill is common. Inter-AZ traffic is the silent killer."
- Post 8: "7–9/ AI workload guardrails, RDS rightsize, EBS gp2→gp3. Each worth a thread. Linked below."
- Post 9: "10/ Close the loop. The first 9 practices are useless if your team doesn't have time to act on them. This is what 'agentic FinOps' means."
- Post 10: "Full piece: [link]. Connect AWS in 60 seconds: [trial]."

### X Thread B — Contrarian take (Day 5)
- Post 1: "Hot take: rightsizing recommendations don't fail because they're wrong. They fail because no engineer has time to act on them. The constraint isn't analysis. It's execution."
- Posts 2–7: build the argument out — Jira backlog math, dashboard era critique, action loop, agent's role, what HITL really means.
- Post 8: link.

### X Thread C — FAQ (Day 9)
- 1 post per FAQ. Drives long-tail.

### Newsletter — Block 2 (next issue)
- Sharpen the thesis paragraph + the most-shareable practice + 1 chart.
- See `newsletter-issues/issue-XX-*.md` for shape.

### Sales Card (Day 0, design + content)
- Page 1, top: "10 practices. $120K–$170K/mo recoverable on a $500K/mo bill. 90 days."
- Page 1, middle: 3 highest-leverage practices with mechanisms.
- Page 1, bottom: "Connect AWS in under 60 seconds. The agent runs all 10."
- Used by AEs in late-stage pursuits and at events.

## 4. Process & ownership

- Content Lead drafts repurposing in the same week as the long-form ships.
- LinkedIn: scheduled via [TBD-OPERATOR] tool (Buffer / native).
- X: scheduled via [TBD-OPERATOR] (Typefully / native).
- Sales card: Brand designer applies template; PMM owns final.
- All assets cross-link to the long-form using consistent UTMs: `?utm_source=linkedin|x|salescard&utm_medium=organic&utm_campaign=<slug>`.

## 5. Quality gate

Before any repurposed asset ships, run the same 5-question voice check from `voice-guidelines.md` §9. If the asset reads as a teaser ("read more!") rather than a complete-thought-with-link, kill it and rewrite. The repurposed asset must be useful even if the reader never clicks through.
