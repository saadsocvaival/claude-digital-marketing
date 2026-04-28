---
client_id: costsage
artifact: customer-review-request-email
purpose: short, low-friction emails to existing happy customers asking for a public review on G2 / Capterra / TrustRadius
audience: V6 (Email) + V1 (GEO/authority graph)
priority: P0 once first 10 customers exist; ship via personal email or once ESP lands
date: 2026-04-28
---

# Customer review-request email — 3 sequence variants

> Goal: turn happy customers into G2 / Capterra / TrustRadius reviews. These directly lift V1 GEO scoring (Track 4: 17.5/50 → ~25 once 5+ reviews land per platform). Each email is 80–120 words, single CTA, plain-text-friendly. **Don't batch-send to all customers at once** — stagger to 3-5/day to avoid spam-flag risk.

## Variant 1 — "first review" cold ask (warm customer, no review pressure yet)

**From:** [Founder name TBD] <[founder email TBD]>
**To:** [Customer name]
**Subject:** Quick favor — 3-min G2 review?

Hi [first-name],

Hope CostSage is still saving your AWS bill the way we promised. (If it's not — please reply and tell me what's broken; we'll fix it before the next ask.)

If it IS working: would you write us a 3-minute G2 review? Honest take, good or bad. We're a young company and your one review carries more weight than ten of our blog posts.

Direct link: https://www.g2.com/products/costsage/reviews/start

That's it. No follow-up if you can't get to it. Just one ask, once.

— [Founder name]
[role]
CostSage

---

## Variant 2 — Capterra (different framing for the same person 4 weeks later)

**Subject:** Different review site — ⏳ same 3 minutes

Hey [first-name],

Last month I asked about a G2 review — thank you if you wrote one. (If not, no stress.)

Capterra is a different audience — Gartner-affiliated; a lot of mid-market FinOps lead buyers check it before evaluations. Different reviewers see different sites, so a Capterra review hits a different segment than the G2 one.

Same 3 minutes: https://www.capterra.com/p/costsage/reviews/

Flagging it again because honestly, getting on Capterra's radar is the next hill we need to climb.

— [Founder name]

---

## Variant 3 — TrustRadius (the depth-detail one)

**Subject:** TrustRadius review — bigger questions, only if you have 10 min

Hi [first-name],

Last review ask, I promise. TrustRadius is the long-form one — 8-10 detailed questions including pros/cons/competitors-considered/who-this-is-for-vs-not.

This is the review that enterprise FinOps leads actually read end-to-end before evaluation. Worth more than a star rating.

If you have 10 min and want to: https://www.trustradius.com/products/costsage/reviews/new

If not — totally fine. We won't ask again.

Thanks for being one of the first.

— [Founder name]
CostSage

---

## Sequencing rules

| Touch | Channel | Day | Audience |
|---|---|---|---|
| 1 | G2 ask | day 0 | customers who've been live ≥30d AND saved ≥$1K AND haven't churned |
| 2 | Capterra ask | day 28 | only customers who responded to (or wrote) a G2 review |
| 3 | TrustRadius ask | day 56 | only customers who wrote G2 + Capterra |
| Stop | — | — | non-responders after touch 1 — never re-ask |

## Personalization required (operator)

Every send must replace these tokens:
- `[first-name]` → CRM-pulled
- `[Founder name]` — confirm
- `[founder email]` — confirm
- `[role]` — "Founder" / "CEO" / "Head of Customer"

## What "happy customer" means (gate before sending)

Send only if **all** are true:
- NPS ≥ 8 (or equivalent CSAT signal)
- ≥30 days as a paying customer
- ≥$1K in confirmed savings (or, for non-savings-tracked customers, has logged in ≥10× in the last 30d)
- No open priority-1 support ticket
- Not in trial / not renewing in <14 days

## UTM convention (for any links we tag)

```
?utm_source=email&utm_medium=ask&utm_campaign=review-request&utm_content=g2-v1
?utm_source=email&utm_medium=ask&utm_campaign=review-request&utm_content=capterra-v2
?utm_source=email&utm_medium=ask&utm_campaign=review-request&utm_content=trustradius-v3
```

## Operator action to ship

This is fully drafted. To ship today: paste each variant into your personal mail client (Superhuman / Gmail / etc.), send manually to 5 customers/day. No ESP needed.

Once an ESP is provisioned (Customer.io / HubSpot / Mailchimp): port these into the ESP, set the gate-conditions above, schedule.

## Expected impact (90 days)

If we send to 30 customers, expect:
- G2: ≥10 reviews (33% conversion is industry average for warm asks)
- Capterra: ≥5 (lower because it's the second ask)
- TrustRadius: ≥3 (lowest because the form is longer)

That moves Track 4 GEO score from 17.5/50 today → ~26/50 once these reviews are live, which is the single biggest lever on AI/LLM citation trustworthiness.
