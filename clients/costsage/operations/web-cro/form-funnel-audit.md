# Form & Funnel Audit — costsage.ai

**Status:** Initial pass
**Date:** 2026-04-28
**Scope:** All conversion forms and the funnel from awareness → trial / sales-conversation.

---

## 1. Inventory

| Touchpoint | URL | Form? | Destination |
|---|---|---|---|
| Homepage hero CTA | / | No (link) | /contact or /pricing — `[TBD-OPERATOR]` confirm |
| Pricing tier CTA | /pricing | No (link → /contact) | /contact |
| AWS landing CTA | /aws | No (link) | /contact |
| Azure landing CTA | /azure | No (link) | /contact |
| Comparison page CTAs | /compare/* | No (link) | /pricing + /contact |
| Contact form | /contact | Yes | inbox `[TBD-OPERATOR]` |
| Newsletter / footer | global | `[TBD-OPERATOR]` confirm if exists | — |
| AWS Marketplace | external | n/a | AWS subscription flow |

## 2. Friction points (current state)

1. **Single funnel terminus** — every CTA lands on /contact. No self-serve trial path. High-intent buyers who want to try before booking a call have no option except AWS Marketplace.
2. **Contact form fields** — `[TBD-OPERATOR]` audit current fields. Standard friction-cutting rule: ≤5 fields (name, email, company, monthly cloud spend, message). Confirm current form length.
3. **No qualification** — without a "monthly cloud spend" field, sales call quality suffers; without a "primary cloud (AWS/Azure)" field, routing is manual.
4. **No newsletter or low-commit option** — buyers in the research phase (8-12 months out) have no way to stay in touch without becoming a sales lead.
5. **No exit-intent capture** — high-traffic pages (/, /pricing, /aws) have no exit-intent modal.
6. **No social proof on form pages** — /contact doesn't show logos / testimonials. Standard CRO uplift: 10-20%.

## 3. Funnel-stage gaps

| Stage | Current asset | Gap |
|---|---|---|
| Awareness | Blog, /compare/*, /alternatives/* | OK (improving with this sprint) |
| Consideration | /pricing, /features, /aws, /azure | OK |
| Evaluation | /contact only | **Missing self-serve trial / sandbox / demo video** |
| Decision | /contact + AWS Marketplace | OK |
| Onboarding | `[TBD-OPERATOR]` | Out of CRO scope |

## 4. Recommendations (prioritised)

1. **P0 — Add a self-serve trial path (or AWS Marketplace deep-link with one-click)** on /pricing and /aws. Either `[TBD-OPERATOR]` /signup or `[TBD-OPERATOR]` AWS Marketplace SKU URL.
2. **P0 — Standardise contact form to 5 fields max** with conditional logic (cloud spend → routes to relevant SDR).
3. **P1 — Add testimonial / logo bar on /contact** above the form.
4. **P1 — Newsletter capture in footer + at end of long pages** (/finops-for-ai-workloads, /multi-cloud, blog posts) — low-friction email capture for research-phase buyers.
5. **P2 — Exit-intent modal on /pricing** offering "see a 60-second product demo" → embedded video.
6. **P2 — Add a "Compare CostSage" widget** to /pricing showing a 3-product comparison snippet pulling from /compare/* and /alternatives/*.

## 5. Operator-confirmation TBDs

- Current /contact form fields and routing destinations
- Newsletter capability + ESP (Mailchimp / ConvertKit / etc)
- Self-serve trial readiness
- AWS Marketplace SKU URL for one-click subscribe
- Existing analytics/event-tracking maturity (GA4? Plausible? Self-hosted?)

## 6. Measurement plan

Once the gaps above are closed, weekly funnel report:
- Sessions → CTA clicks → form starts → form submits → SQLs → opportunities → closed-won
- Conversion rate at each step
- Cohort by source (organic, AWS Marketplace, comparison-page traffic, paid)

Single tool requirement: GA4 + a session-recording tool (`[TBD-OPERATOR]` Hotjar / Microsoft Clarity — Clarity is free).
