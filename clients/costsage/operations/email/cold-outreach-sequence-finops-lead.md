# Cold Outreach Sequence — FinOps Practitioner

**Persona:** FinOps lead / FinOps engineer / Cloud Economics manager. Already practitioner-aware. Less convincing on "FinOps matters", more skeptical of vendor pitches. Cares about depth, integrations, accuracy of recommendations.
**Sequence length:** 5 touches (4 emails + 1 LinkedIn) over ~14 business days.
**Sender:** Founder or [TBD-OPERATOR — FinOps-credible team member]. From: founder@costsage.ai.
**UTM:** `?utm_source=email&utm_medium=cold&utm_campaign=finops-lead-q1&utm_content=<email#>-<variant>`
**Exit conditions:** same as AWS-SaaS sequence (replied, booked, unsubscribed, bounced, spam).

---

## Email 1 — Day 0 — Problem (peer-to-peer framing)

**Subject A:** {{first_name}} — SP utilization tracking at {{company}}?
**Subject B:** A FinOps question for you

**Body:**

{{first_name}},

Peer question, not a pitch.

When you re-check Savings Plan utilization at {{company}} — is it weekly, monthly, or "at renewal"?

Asking because the median we see across audits is monthly, and it's where most of the slow-bleed waste lives. Curious how you're handling it.

(Disclosure: I run CostSage. Genuinely interested in how practitioners handle this — happy to share what we see across our customer base in return.)

— {{sender_first}}
costsage.ai/blog/ri-vs-savings-plans?utm_source=email&utm_medium=cold&utm_campaign=finops-lead-q1&utm_content=e1-A

---

## Email 2 — Day 3 — Proof / depth

**Subject A:** Re: SP utilization — sharing the math
**Subject B:** {{first_name}} — the 90% threshold

**Body:**

{{first_name}},

Following up — wrote down why ~90% is the threshold and what falls off below it:

→ costsage.ai/blog/ri-vs-savings-plans?utm_source=email&utm_medium=cold&utm_campaign=finops-lead-q1&utm_content=e2-A

The short version: SP discount averages ~28% on Compute. At 80% utilization the *effective* discount is closer to 12% — barely above 1-yr no-upfront RI. Below ~76% you're net-negative vs on-demand.

Curious if {{company}}'s thresholds line up, or if you've got better numbers — would update the post if so.

— {{sender_first}}

---

## Touch 3 — Day 6 — LinkedIn

**Connection request note:**
> Hi {{first_name}} — emailed you a peer question on SP utilization thresholds. No reply needed. Adding here for an easier channel. Following your work in FinOps Foundation [TBD-OPERATOR — replace with actual signal].

---

## Email 3 — Day 9 — Case-shape (technical)

**Subject A:** How one team cut SP waste 23%
**Subject B:** {{first_name}} — three SP failure modes

**Body:**

{{first_name}},

The three SP failure modes that show up in every audit:

1. Committed to peak not trough — guaranteed waste on every below-peak hour.
2. Region drift — workload migrated, SP didn't follow.
3. Family drift on non-convertible commits — m5 → m6i without coverage path.

We took an anonymized $1.2M annual SP and decomposed where the 23% waste came from — full breakdown in the carousel here: [TBD-OPERATOR LinkedIn URL].

If you want, I'll run the same decomposition on your live data — read-only role, ~45 min. No pitch, just the report.

— {{sender_first}}

---

## Email 4 — Day 12 — Resource share

**Subject A:** Tagging governance — what works
**Subject B:** {{first_name}} — allocation gap audit

**Body:**

{{first_name}},

You probably already know this stuff, but in case useful for a teammate:

- Tagging governance pattern that drops allocation gap from ~40% to <5% in 3 weeks: enforce tags at create time via Terraform module + SCP. Audit-only approaches don't get there.
- Write-up on agentic vs dashboard FinOps (closer to your domain, hopefully not preachy): costsage.ai/finops-agent-vs-dashboard?utm_source=email&utm_medium=cold&utm_campaign=finops-lead-q1&utm_content=e4-A

Always interested in how other practitioners are handling this.

— {{sender_first}}

---

## Email 5 — Day 14 — Break-up

**Subject A:** Closing the loop
**Subject B:** Last note from me, {{first_name}}

**Body:**

{{first_name}},

Closing the loop on my outreach.

If a FinOps tooling refresh is on {{company}}'s plate later this year, easiest entry is a self-serve audit: costsage.ai?utm_source=email&utm_medium=cold&utm_campaign=finops-lead-q1&utm_content=e5-A

If we're not the right fit, a one-line "not for us, here's why" reply is genuinely the most useful thing — helps me get sharper. No follow-up either way.

Thanks for the time.

— {{sender_first}}

---

## Operational notes

- Tone: peer-to-peer, never patronizing. FinOps practitioners detect hype instantly.
- Always offer reciprocal value (data sharing, sharper post update) before any ask.
- Hard suppress on any reply containing "not interested", "remove", "stop".
- Compliance footer per `compliance-footers.md`.
