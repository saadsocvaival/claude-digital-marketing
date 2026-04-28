# Cold Outreach Sequence — AWS-First SaaS (CTO / Head of Eng / FinOps Lead)

**Persona:** Engineering leader at a SaaS company spending $10K–$500K/mo on AWS. Owns the cloud bill or is the technical decision maker for FinOps tooling.
**Sequence length:** 5 touches (4 emails + 1 LinkedIn) over ~14 business days.
**Sender:** Founder ([TBD-OPERATOR — name + title]). From-address: founder@costsage.ai [TBD-OPERATOR confirm].
**UTM convention:** `?utm_source=email&utm_medium=cold&utm_campaign=aws-saas-q1&utm_content=<email#>-<variant>`
**Exit conditions (any single trigger removes from sequence):**
- Replied (any reply, including OOO with future date — pause + resume)
- Booked a meeting
- Unsubscribed / opted out
- Hard bounced (remove permanently from list)
- Clicked unsubscribe in footer
- Marked spam (auto-remove + suppress domain)

---

## Email 1 — Day 0 — Problem

**Subject A:** Quick question on {{company}}'s AWS bill
**Subject B:** {{first_name}}, idle EC2 at {{company}}?

**Preview text:** Two-minute read. No deck.

**Body:**

Hi {{first_name}},

I run CostSage, an agentic FinOps tool for AWS-first SaaS teams.

Across the ~50 SaaS accounts we've audited, two patterns show up almost every time:

1. 12–18% of EC2 spend on workloads averaging <5% CPU
2. Savings Plan utilization that drifted below 90% and nobody caught it until renewal

Wanted to ask — does that match what you're seeing at {{company}}, or are you tracking it tightly already?

If it's interesting, I can share the 4-question audit checklist we use ourselves.

— {{sender_first}}
{{sender_title}}, CostSage
costsage.ai/aws?utm_source=email&utm_medium=cold&utm_campaign=aws-saas-q1&utm_content=e1-A

---

## Email 2 — Day 3 — Proof

**Subject A:** Re: AWS at {{company}} — small follow up
**Subject B:** {{first_name}} — the RI vs SP decision tree

**Preview text:** One asset, then I'll be quiet.

**Body:**

{{first_name}},

Following up briefly. Wrote down the RI-vs-Savings-Plans decision tree we walk every customer through:

→ costsage.ai/blog/ri-vs-savings-plans?utm_source=email&utm_medium=cold&utm_campaign=aws-saas-q1&utm_content=e2-A

If it's useful, I'd love to swap notes on what {{company}} is running on. If not, no worries — just trying to be helpful, not annoying.

— {{sender_first}}

---

## Touch 3 — Day 6 — LinkedIn

**Action:** Connection request from sender's LinkedIn to {{first_name}}.
**Note (300 char):**
> Hi {{first_name}} — sent a couple notes on AWS cost at {{company}}. No reply needed. Adding here in case it's an easier place to chat. I run CostSage (agentic FinOps for AWS SaaS). Following your work on [TBD-OPERATOR — relevant signal: blog, talk, etc.].

**Exit:** if accepts and replies → mark replied, exit email sequence.

---

## Email 3 — Day 9 — Case-shape

**Subject A:** How a {{ICP_descriptor}} cut AWS by 22% in one quarter
**Subject B:** {{first_name}} — one customer story (anonymized)

**Preview text:** Specific, no fluff.

**Body:**

{{first_name}},

Quick one — anonymized customer profile in case it resonates:

- B2B SaaS, ~$180K/mo on AWS, ~70 engineers
- Top 3 issues we found: (1) idle dev EC2 + RDS, (2) Compute SP committed to peak not trough, (3) NAT gateway in a deprecated VPC routing nothing
- Outcome: 22% reduction in 90 days, all changes shipped as PRs the team reviewed and merged

Full structure (no customer names): costsage.ai/aws?utm_source=email&utm_medium=cold&utm_campaign=aws-saas-q1&utm_content=e3-A

If you want me to run the same audit shape on {{company}}'s account (read-only role, ~30 min), happy to.

— {{sender_first}}

---

## Email 4 — Day 12 — Resource share

**Subject A:** Comparing FinOps tools? (no pitch)
**Subject B:** {{first_name}} — CloudZero / nOps / CostSage in one page

**Preview text:** Honest comparison, including when not to pick us.

**Body:**

{{first_name}},

If you're (or someone on your team is) shopping FinOps tooling, two pages that might save you a meeting:

- CostSage vs CloudZero (including when to pick CloudZero): costsage.ai/compare/cloudzero-vs-costsage?utm_source=email&utm_medium=cold&utm_campaign=aws-saas-q1&utm_content=e4-A
- CostSage vs nOps: costsage.ai/compare/nops-vs-costsage?utm_source=email&utm_medium=cold&utm_campaign=aws-saas-q1&utm_content=e4-A2

Sharing because they're useful regardless of whether we end up talking.

— {{sender_first}}

---

## Email 5 — Day 14 — Break-up

**Subject A:** Closing the loop, {{first_name}}
**Subject B:** Last note from me

**Preview text:** Closing the loop, no follow-up.

**Body:**

{{first_name}},

I won't keep emailing — closing the loop on this thread.

If FinOps for {{company}} is on the roadmap later this year, the easiest place to start is a 10-min self-serve audit: costsage.ai?utm_source=email&utm_medium=cold&utm_campaign=aws-saas-q1&utm_content=e5-A

And if FinOps is *never* a fit, a one-line "not for us" reply is the most useful thing you could do for me — helps me sharpen who I should be reaching out to.

Thanks for your time either way.

— {{sender_first}}

---

## Operational notes

- All emails plain-text rendered; no images, no tracking pixels by default (privacy-first; deliverability boost). [TBD-OPERATOR — confirm tracking policy.]
- Sender warmup: see `deliverability-runbook.md` before this sequence runs.
- Daily send cap during warmup: 30/day → 100/day.
- A/B split: 50/50 on subject lines, fixed body. Pick winner after 200 sent per arm.
- Compliance footer: see `compliance-footers.md` — must be appended to every email automatically.
- Suppression list: any unsubscribe, bounce, or "not for us" reply → permanent suppress.
