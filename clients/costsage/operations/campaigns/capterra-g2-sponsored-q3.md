# Capterra + G2 Sponsored Placements — Q3

> Review-site sponsored placements. **Depends on V1: G2 and Capterra listings live, claimed, with a baseline of ≥ 5 verified reviews each.** Do not launch sponsored before the listings are claim-ready.

## 1. Meta
- **Campaign name:** REV_G2_Capterra_Q3.
- **Platforms:** G2 (g2.com), Capterra (capterra.com — Gartner Digital Markets network: Capterra + GetApp + Software Advice).
- **Owner:** Paid Media DRI.
- **Status:** **BLOCKED** until V1 listings live + claimed. `[TBD-OPERATOR]`.

## 2. Objective
- **Primary:** `demo_request` from review-shopping BOFU traffic.
- **Secondary:** category ranking lift; review velocity (incentivized via separate non-paid program).

## 3. Audience targeting
G2 and Capterra targeting is largely category- and intent-based (the platform serves your placement to users browsing the relevant category). Optional behavioral filters available:
- **G2 Buyer Intent (paid add-on):** firmographic filter — Industry: Software, Internet, IT Services; Employees: 51–1,000; Geo: US/CA/UK/AU. `[TBD-OPERATOR]` budget.
- **Capterra:** category sponsorship — see categories below.

**Categories to claim presence in:**
- Cloud Cost Management Software (G2 + Capterra).
- Cloud Management Platforms (Capterra).
- IT Cost Management Software (Capterra).
- Cloud Optimization Services (G2).
- AWS Cost Management Tools (G2 — sub-listing).

## 4. Placement types & spend

| Placement | Platform | Cost model | Monthly seed | Notes |
|-----------|----------|------------|--------------|-------|
| Category sponsorship — Cloud Cost Management | G2 | CPC, ~$8–$15 | $400 | Per public docs; confirm operator quote. |
| Comparison-page placement (vs CloudZero) | G2 | CPC | $300 | Pulls switch-shoppers. |
| Capterra category top-3 placement | Capterra | CPC ~$3–$8 | $200 | |
| GetApp / Software Advice cross-list | Capterra network | CPC | $100 | Bundled with Capterra. |
| **Total** | | | **$1,000** | |

`[TBD-OPERATOR]` confirm exact CPC ranges with platform AEs before activation.

## 5. Creative
G2 and Capterra placements primarily display: logo, tagline, star rating, "Get Demo" CTA. Submit:
- **Logo (SVG + PNG transparent).**
- **Tagline (≤ 90 chars):** "Agentic FinOps for AWS-first SaaS — cut waste, automate commitments, free your engineers."
- **One-line value prop:** "AWS-first cloud cost optimization for 50–500 employee SaaS."
- **Hero screenshot (1280×720):** dashboard overview.
- **Long description (≤ 1,000 chars):** see `_creative/ad-copy-bank.md` D02+D04+D11 stitched.
- **Demo CTA URL:** `/aws?utm_source=g2&utm_medium=review_site&utm_campaign=rev_q3&utm_content=g2_category`.

## 6. Landing Pages
- Primary: `/compare/cloudzero-vs-costsage` (review-shoppers are inherently comparing).
- Secondary: `/aws`, `/pricing`.

## 7. Conversion Tracking
- UTM-driven (review sites do not provide platform-native pixels for sponsored placements).
- GA4 + GTM picks up the UTM, fires `demo_request` and `trial_start`.
- Custom dimension: `review_site_source` (g2/capterra/getapp/software_advice).
- Manual reconciliation in monthly review by matching CRM "Lead source" = review-site UTM.

## 8. Review-velocity dependency (NOT paid, but required for paid to work)
- Target: ≥ 20 verified reviews on G2 within 90 days; ≥ 15 on Capterra.
- Mechanism: post-onboarding email from `success@costsage.ai` requesting review (G2/Capterra both run incentive programs — Amazon $25 gift card etc.; abide by their terms).
- DRI: Customer Success.

## 9. KPIs
| Metric | M1 | M2 | M3 |
|--------|----|----|----|
| Spend | $1,000 | $1,000 | $1,000 |
| Profile views | 1,500 | 2,500 | 4,000 |
| Compare-page views | 200 | 400 | 700 |
| Demo requests | 3 | 8 | 18 |
| CPA | $333 | $125 | $56 |
| Verified reviews (cumulative) | 8 | 20 | 35 |

## 10. Kill-switch
- 0 demo requests in 30 days post live → reduce to category sponsorship only, drop comparison placements.
- Review velocity < 5 in 60 days → pause sponsored (unsupported by review base).

## 11. Operator deps
- `[TBD-OPERATOR]` Claim G2 + Capterra listings.
- `[TBD-OPERATOR]` Sign vendor agreements with Gartner Digital Markets.
- `[TBD-OPERATOR-CLAIM]` Approve all on-platform copy.
- `[TBD-OPERATOR]` Customer Success review-request workflow live.
