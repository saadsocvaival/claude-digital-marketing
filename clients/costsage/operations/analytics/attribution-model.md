# Attribution Model — CostSage.ai

> Multi-touch attribution methodology with concrete worked example. The default reporting model is **position-based (40/20/40)**; we also report first-touch and last-touch alongside for triangulation.

## 1. Models in use

| Model | When to use | Strength | Weakness |
|-------|-------------|----------|----------|
| First-touch | Top-of-funnel valuation; brand / awareness channels | Rewards channel that started the journey | Ignores closers |
| Last-touch | Cash-now attribution; bottom-funnel optimization | Rewards channel that closed | Ignores everything before |
| Linear | Equal credit; channels in long journeys | Simple; equal | Treats CTA click same as paid demo signup |
| Time-decay | When recency matters (BOFU heavy) | Recent touches weighted | Penalizes long-cycle B2B early touches |
| Position-based 40/20/40 (U-shape) | **B2B SaaS w/ multi-month cycle — DEFAULT** | Rewards first AND last; middle gets the rest | Arbitrary weights |
| Data-driven (Google) | Once 50+ conversions/30d in a channel | Algorithmic | Black box; depends on Google data |

**Default reporting:** position-based 40/20/40.
**For paid-channel optimization:** last-touch (operationally fastest signal).
**For long-cycle deals (> 60 days):** time-decay with 14-day half-life.

## 2. Touchpoint definitions
A touchpoint = any of:
- Paid click landing on costsage.ai (UTM-tagged).
- Organic click (medium=organic).
- Direct visit (no UTM).
- Email click (UTM-tagged).
- Referral click.
- Form interaction (form_start, form_submit).
- App login.

Window: 90 days for B2B (first-touch reach-back) → demo_request → 90 days to closed-won.

## 3. Worked example — synthetic deal

A FinOps lead at "Acme SaaS" closes for $5,988 ARR. Touchpoint sequence:

| # | Day | Channel | utm_source/medium | Touch type |
|---|-----|---------|-------------------|------------|
| 1 | -62 | Reddit ad → blog | reddit/paid_social | First touch |
| 2 | -55 | Organic search → blog | organic | Repeat visit |
| 3 | -41 | Newsletter click | newsletter/email | Email |
| 4 | -28 | Direct (typed in browser) | (direct) | Direct |
| 5 | -22 | LinkedIn ad → /aws | linkedin/paid_social | Paid social |
| 6 | -14 | Google branded search | google/cpc (branded) | Paid branded |
| 7 | -14 | demo_request (form_submit) | google/cpc (branded) | Conversion event |
| 8 | -3 | App login (trial) | n/a | Activation |
| 9 | 0 | Closed-Won | — | Revenue |

**Credit allocation by model** (revenue $5,988):

### First-touch
- Reddit: $5,988 (100%)
- All others: $0.

### Last-touch (last non-direct before conversion)
- Google branded search: $5,988 (100%) — though branded clicks usually warrant discounting; see §5.

### Linear (6 touches credited equally)
- Each: $5,988 / 6 = $998.

### Position-based 40/20/40 — DEFAULT
- First (Reddit): $5,988 × 40% = $2,395.
- Last (Google branded): $5,988 × 40% = $2,395.
- Middle 4 touches share 20% = $299.40 each (Organic, Newsletter, Direct, LinkedIn).

### Time-decay (14-day half-life)
Weights from conversion (day -14): Reddit (-62)=2^(-48/14)=0.087; Organic (-55)=0.137; Newsletter (-41)=0.260; Direct (-28)=0.499; LinkedIn (-22)=0.658; Google (-14)=1.0. Sum = 2.641.
- Reddit: $5,988 × 0.087/2.641 = $197.
- Organic: $311.
- Newsletter: $589.
- Direct: $1,131.
- LinkedIn: $1,492.
- Google: $2,267.

## 4. Operational rules
- **Direct discount:** Direct visits are typically dark-social or branded re-entry. Discount direct credit by 50% in any reporting except customer-journey QA.
- **Branded vs non-branded paid search:** Split into separate channels in the report; do not credit "branded paid" as a sole driver — it's defensive intent capture.
- **Form fill on first touch (no prior touches):** all models collapse to "single-touch — that channel".
- **Cross-device:** rely on logged-in user_id_hash and email-form match to stitch (best-effort).

## 5. CAC reconciliation
- For LTV:CAC headline (#33), use **position-based** model on a rolling-quarter window.
- For paid-channel-pause decisions (kill-switches), use **last-touch** to be aggressive on what's not closing.
- For brand investment (Reddit, top-funnel), use **first-touch** to defend.

## 6. Limits
- Anonymous users coalesced via cookie + email-hash on form_submit — match rate ≤ 100%.
- 3rd-party-cookie deprecation reduces cross-domain stitching; first-party 90-day cookie carries the load.
- Self-reported attribution ("How did you hear about us?" form field) supplements but doesn't replace.

## 7. Tooling
- Computed in BigQuery via `mart_attribution.sql` (TBD-build), output to a Sheet → Looker tab.
- Re-runs nightly. Snapshot stored — do not retroactively recompute closed quarters.
