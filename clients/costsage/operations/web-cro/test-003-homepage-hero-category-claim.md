# CRO Test 003 — Homepage Hero Category Claim

**Status:** Drafted
**Page:** / (homepage)
**Hypothesis:** Asserting a clear category position in the hero ("The agentic AI FinOps platform for AWS and Azure") will increase scroll depth and CTA engagement vs the current more-generic positioning.

---

## 1. Background

The homepage is the entry point for ~`[TBD-OPERATOR]`% of organic traffic. Category claims drive memorability (per April Dunford's "Obviously Awesome" model) and improve AEO answer-engine alignment — when ChatGPT/Perplexity is asked "what is costsage," it should echo our category statement back.

## 2. Variants

- **Control (A):** Current hero copy
- **Variant B:** "The agentic AI FinOps platform for AWS and Azure." + sub "AI agents that find and fix cloud cost waste — under your approval. Published pricing. AWS Marketplace listed."
- **Variant C:** Problem-led — "Your cloud bill keeps going up. Your FinOps tool keeps showing charts." + sub "CostSage's AI agents close the loop. They find waste, plan the fix, and execute with your approval."

## 3. Primary metric

Composite engagement score: scroll-past-fold rate × time-on-page × any-CTA-click rate. Secondary: bounce rate.

## 4. Sample size

- Need ≥10,000 sessions per arm (homepage traffic, lower-intent than /pricing)
- ETA `[TBD-OPERATOR]` weeks based on current homepage volume

## 5. Implementation

Client-side via A/B engine. Critical: H1 change can affect SEO. Use server-side rendering with cookie-based variant pinning if engine supports, else accept that crawlers see Control (A) only.

## 6. Risks

- H1 variations seen by Googlebot can fragment ranking signal. Mitigation: pin Googlebot to Control via user-agent rule, or use SEO-safe SSR variant.
- Category claim ("agentic AI FinOps") must be defensible — Pivot to "AI FinOps" if "agentic" research shows poor recognition (`[TBD-OPERATOR]` qualitative test with 5 buyers first).

## 7. Decision log

| Date | Decision | Owner |
|---|---|---|
| `[TBD-OPERATOR]` | Buyer-resonance check on "agentic" terminology | Marketing |
| `[TBD-OPERATOR]` | SEO pin rule confirmed | Eng |
| `[TBD-OPERATOR]` | Test launched | CRO operator |
