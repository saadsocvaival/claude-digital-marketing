# Microsoft Advertising (Bing) — AWS Cost — Q3

> Mirror of `google-search-aws-cost-tools-q3.md`, retuned for Microsoft Advertising's enterprise-IT lean (older, higher-income, more Windows/Azure-aware audience but disproportionately decision-makers).

## 1. Meta
- **Campaign name:** MS_AWS_CostTools_Q3
- **Platform:** Microsoft Advertising — Search (Bing, Yahoo, AOL, MSN syndicates).
- **Owner:** Paid Media DRI.
- **Status:** draft. `[TBD-OPERATOR: Microsoft Advertising account; UET tag verified]`.

## 2. Objective
Same as GS_AWS_CostTools_Q3.

## 3. ICP / Audience
- Same ICP. Microsoft skew:
  - **LinkedIn Profile Targeting (MSA exclusive):** Industry = Software/IT; Company size = 51–1,000; Job function = Information Technology / Engineering. Bid +25%.
  - **In-market:** Cloud computing platforms, Enterprise software.
  - **Customer Match:** seed lists same as Google (hashed).
  - **Excluded:** suppress lists.
- **Geos:** US, CA, UK, IE, AU, NZ. **+15% bid on US** (where Bing share is highest).
- **Devices:** desktop +15%, mobile −20%, tablet 0%.
- **Day-parting:** Mon–Fri 06:00–19:00 destination time.

## 4. Hypothesis
> Bing audience skews older + enterprise-IT decision-makers; AWS-cost queries on Bing convert at 1.3–1.6× Google CVR but with 30–50% lower volume, yielding equal-or-better blended CPA.

## 5. Budget
- **Monthly seed:** $750 ($25/day) — half of Google AWS to start; scale if CPA equals or beats Google.
- **Bid:** Enhanced CPC 14 days, then Maximize Conversions.

## 6. Ad-Group Structure (mirror of Google AG-1, AG-2, AG-4, AG-5; skip AG-3 broad until performance verified)
- Reuse keyword lists from `google-search-aws-cost-tools-q3.md` — Microsoft auto-imports work, but localize negatives.

## 7. Negatives — Microsoft-specific additions
On top of `Brand-Safety_Universal`:
```
-azure migration
-azure cost
-microsoft cost
-power bi cost
-windows server cost
-microsoft 365 cost
-office 365 cost
-dynamics 365 cost
-windows licensing
-vmware
```

(Bing audience inflates Azure/Microsoft-product crossover; aggressive negatives required.)

## 8. RSAs (3 per ad group)
Reuse Google RSAs but add 3 new headlines emphasizing enterprise-IT cues:
- "AWS Cost Governance For Enterprise IT"
- "AWS Cost Tooling, IT-Department Friendly"
- "Multi-Account AWS Cost — One Dashboard"

## 9. Sitelinks / Callouts / Snippets
Same as Google.

## 10. Conversion Tracking
- **UET tag** sitewide via GTM.
- Conversion goals:
  - `MS_demo_request` → `demo_request` event.
  - `MS_trial_start`.
  - `MS_cta_book_demo`.
- Offline conversion import via CRM. `[TBD-OPERATOR]`.
- UTM: `utm_source=bing&utm_medium=cpc&utm_campaign=ms_aws_cost_tools_q3&utm_content={AdId}&utm_term={keyword}`.

## 11. KPIs
| Metric | M1 | M2 | M3 |
|--------|----|----|----|
| Spend | $750 | $750 | $750–$1,500 |
| Clicks | 350 | 450 | 600 |
| CTR | 2.8% | 3.5% | 4.3% |
| LP CVR | 4% | 5% | 5.5% |
| Demo requests | 14 | 22 | 33 |
| CPA | $54 | $34 | $23 |

## 12. Kill-switch
- CPA > $400 with ≥ $500 spent (7-day).
- CTR < 1.0% with ≥ 5K impressions.
- 0 conversions in 21 days.

## 13. Operator deps
- `[TBD-OPERATOR]` Microsoft Advertising account.
- `[TBD-OPERATOR]` UET tag installed and verified.
- `[TBD-OPERATOR]` Conversion goals created.
