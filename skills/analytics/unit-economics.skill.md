---
name: unit-economics
description: Computes and maintains the CAC / LTV / payback / burn-multiple ledger at client level. Standing input to the CMO weekly digest. Forces segmented (not blended) views and explicit guardrails.
invoked_by: head-of-analytics, cmo-orchestrator
frameworks:
  - David Skok SaaS metrics
  - Bessemer Cloud Index (burn multiple, NRR, magic number)
  - Fully-loaded CAC (Scale Venture Partners convention)
---

## Why a dedicated skill

Blended CAC hides the truth: one segment might be profitable at 2-month payback while another is underwater at 36 months. Without a segmented unit-economics ledger, the CMO cannot defensibly reallocate budget. This skill makes the ledger a first-class artifact.

## Inputs

```json
{
  "period": "YYYY-MM",
  "segments": ["SMB", "Mid-Market", "Enterprise", "PLG-self-serve"],
  "channels": ["paid_social", "paid_search", "organic", "outbound", "partner", "events"],
  "spend_by_channel": { "channel": "int (fully-loaded including headcount)" },
  "new_customers_by_segment_and_channel": "int matrix",
  "acv_by_segment": "float",
  "gross_margin_pct": "float",
  "monthly_churn_by_segment": "float",
  "expansion_rate_by_segment": "float"
}
```

## Outputs

```json
{
  "cac_by_segment_and_channel": "matrix",
  "blended_cac": "float (reported but not used for decisions)",
  "ltv_by_segment": "float — (ACV × gross_margin) / (churn − expansion), floored at zero",
  "ltv_cac_ratio_by_segment": "float (target ≥3.0)",
  "cac_payback_months_by_segment": "float (target ≤18)",
  "burn_multiple": "float — net burn / net new ARR (target ≤2.0, best-in-class ≤1.0)",
  "magic_number": "float — (quarterly ΔARR × 4) / S&M spend (target ≥0.7)",
  "guardrail_breaches": ["list of segments where LTV:CAC <3 or payback >18"],
  "recommended_actions": ["reallocate | cut | double-down per segment"]
}
```

## Protocol

1. **Use fully-loaded CAC.** Include S&M headcount, tools, agency fees — not just ad spend. Industry benchmarks assume fully-loaded.
2. **Segment before blending.** Report per-segment first. Blended number is for the board deck only, never for decisions.
3. **LTV guardrails.** If churn ≥ expansion, NRR <100% — LTV formula diverges. Report as "not computable; fix retention first."
4. **Payback = CAC / (ACV × gross_margin / 12).** Flag anything >24 months as unsustainable absent NRR >120%.
5. **Burn multiple is the executive truth metric.** Below 1.0 = efficient. 1–2 = OK. >2 = concerning. >3 = existential in 2026 funding environment.
6. **Monthly update.** Skill re-runs on close-of-month financials. Deltas flagged if CAC moves ±15% MoM or LTV:CAC crosses the 3.0 line.
7. **Wire into CMO digest.** Standing section. Variance from last month + 3-month rolling trend.

## Anti-patterns

- **Blended-only reporting.** Hides the segment that's subsidizing the rest.
- **LTV based on retention assumption, not data.** Use actual cohort retention curves ≥12 months old; otherwise caveat heavily.
- **CAC excluding S&M headcount.** Understates by 2–3× in most B2B orgs.
- **Burn multiple with pre-revenue ARR.** If ARR is <$1M, burn-multiple is noise; use months-of-runway instead.

## Failure modes

- **Expansion counted as new CAC efficiency.** Don't. Expansion belongs in NRR, not CAC.
- **Payback computed on revenue not gross profit.** Overstates efficiency by (1 / gross-margin). A 70%-margin business with 12-mo revenue-payback has 17-mo gross-profit-payback.
- **One-time spend smeared evenly.** A conference sponsorship benefits multiple quarters; allocate proportionally, don't blame one month.

## Rubric gate

`rubrics/unit-economics.yaml` — segmentation rigor (0–10), fully-loaded-CAC discipline (0–10), guardrail clarity (0–10). Pass bar 8.

## Output file

`clients/{id}/analytics/unit-economics-{yyyy-mm}.md` + `clients/{id}/analytics/cac-ltv-ledger.md` (rolling)
