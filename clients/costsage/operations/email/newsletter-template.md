# Newsletter Template — "The CostSage Note"

**Cadence:** bi-weekly (twice/month). [TBD-OPERATOR confirm.]
**Length target:** 600–900 words.
**Sender name:** "{{sender_first}} from CostSage"
**From:** newsletter@costsage.ai [TBD-OPERATOR]
**Reply-to:** founder@costsage.ai (real human reads replies)
**UTM:** `?utm_source=email&utm_medium=newsletter&utm_campaign=<issue-slug>&utm_content=<block>`

**Single-CTA rule:** every issue has exactly one primary CTA. Internal links inside blocks are *navigation*, not CTAs.

---

## Block 1 — Hook (50–100w)

Open with a surprising fact, contrarian claim, or sharp question. No "Hi all, hope your week is going well." Cold open.

Format options:
- "[Number] [thing] [unexpected outcome]." — e.g., "23% of a $1.2M SP commit was waste — here's where it went."
- "I used to think [common belief]. I was wrong because [reason]."
- "Three things you can ignore in FinOps. One thing you can't."

End the block with a one-line preview of what the issue covers.

---

## Block 2 — Deep dive (250–400w)

The substance. One topic, well-developed, with at least one of:
- Concrete numbers (verifiable; cite source if external)
- A diagram, table, or decision tree (ASCII fine in email)
- A story (anonymized customer, your own infra, public case)

Structure:
- 1 paragraph — frame the problem
- 1 paragraph — why the obvious answer is wrong / incomplete
- 1 paragraph — the better mental model or pattern
- 1 paragraph — concrete example or numbers
- 1 paragraph — what to do tomorrow morning

Embed 1–2 *navigation* links to relevant pages on costsage.ai (`/aws`, `/blog/...`). These are not the CTA.

---

## Block 3 — Tactical tip (100–150w)

One thing the reader can do this week. Specific. Less than 30 minutes of work.

Format:
- "**Tip:** [one-line action]"
- 2–3 sentences of why
- 2–3 lines of *how* (commands, links, exact steps)

---

## Block 4 — Community / curated (75–125w)

One or two of:
- Useful third-party resource (someone else's blog, talk, doc — be generous, link out)
- A reader question + answer
- A FinOps Foundation / community update worth knowing
- A counter-take we found credible (showing intellectual honesty)

Helps the issue feel like a *letter*, not a brochure.

---

## Block 5 — CTA (40–80w)

One primary CTA. Examples:
- "Run a 10-min audit of your AWS account → costsage.ai/aws"
- "Reply to this email with your worst SP story — I'll feature the most surprising in issue X."
- "Forward this to one teammate who'd find it useful."

Then sign-off:

> — {{sender_first}}
> Founder, CostSage
> [Reply works — I read everything]

---

## Footer

Per `compliance-footers.md`. Includes:
- Physical mailing address
- One-click unsubscribe
- "You're getting this because [reason]"
- Manage preferences link

---

## Pre-send checklist

- [ ] Single CTA confirmed
- [ ] All links UTM'd
- [ ] All claims are verifiable / [TBD-OPERATOR] tagged if not
- [ ] Subject line A/B set
- [ ] Plain-text version generated
- [ ] Preview text set (≤90 char)
- [ ] Send time: Tuesday or Thursday, 10am ET [TBD-OPERATOR test]
- [ ] Suppression list synced
- [ ] Footer renders correctly on iOS Mail + Gmail web
