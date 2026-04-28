# CRO Test 002 — AWS Page CTA

**Status:** Drafted
**Page:** /aws
**Hypothesis:** Replacing the generic "Contact us" CTA with a tool-specific, action-anchored CTA ("Connect your AWS account — see waste in 10 minutes") will improve conversion to a meaningful next-step (trial start or contact form).

---

## 1. Background

The /aws page targets the highest-volume keyword cluster (AWS cost optimisation). Current CTA is generic. Highest-converting SaaS landing pages typically use action-anchored CTAs that pre-frame the next step.

## 2. Variants

- **Control (A):** "Contact us" → /contact
- **Variant B:** "Connect your AWS account — see waste in 10 minutes" → /signup or AWS Marketplace listing (`[TBD-OPERATOR]` confirm destination)
- **Variant C:** "See pricing" → /pricing (lower-friction, qualifies budget first)

## 3. Primary metric

CTA-click rate, then qualified outcome (trial start OR /contact form submit OR /pricing → /contact).

## 4. Sample size

- Baseline CTA-click: `[TBD-OPERATOR]` (estimated 2-4%)
- MDE: +40% relative lift
- Sample per arm: ~2,500 sessions
- At current /aws traffic, ETA `[TBD-OPERATOR]`

## 5. Implementation

Client-side injection via A/B engine (see decision memo). Add UTM tag `?utm_source=aws-page&utm_campaign=cro-002&utm_content={variant}` to track downstream conversion in analytics.

## 6. Risks

- Variant B implies a working /signup or AWS Marketplace flow. If self-serve onboarding is not yet ready, Variant B will create a dead-end and harm trust. `[TBD-OPERATOR]` confirm onboarding readiness before shipping.
- If CTA destination changes mid-test, test is invalidated. Lock destination URL before launch.

## 7. Decision log

| Date | Decision | Owner |
|---|---|---|
| `[TBD-OPERATOR]` | Confirm /signup readiness | Eng |
| `[TBD-OPERATOR]` | Variants approved | Marketing |
| `[TBD-OPERATOR]` | Test launched | CRO operator |
