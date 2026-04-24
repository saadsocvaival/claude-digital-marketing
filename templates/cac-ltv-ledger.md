# CAC / LTV Ledger — {Client}

**Refresh cadence:** monthly, close-of-books + 5 business days. Owner: Head of Analytics. Consumer: CMO digest standing section.

## 1. Period header
- Period: {YYYY-MM}
- Gross margin used: {x}% (sourced from finance, not modeled)
- FX rate used: 1 USD = {...}
- Fully-loaded CAC? **Yes** (S&M headcount + tools + agencies included)

## 2. CAC by segment × channel
| Segment ↓ / Channel → | Paid social | Paid search | Organic | Outbound | Partner | Events | **Segment blended** |
|---|---|---|---|---|---|---|---|
| SMB | $... | $... | $... | $... | $... | $... | **$...** |
| Mid-Market | $... | $... | $... | $... | $... | $... | **$...** |
| Enterprise | $... | $... | $... | $... | $... | $... | **$...** |
| PLG self-serve | $... | $... | $... | — | — | — | **$...** |
| **Channel blended** | **$...** | **$...** | **$...** | **$...** | **$...** | **$...** | **$...** |

## 3. LTV by segment
| Segment | ACV | Gross margin | Net monthly churn | Net monthly expansion | LTV = (ACV × GM) / (churn − expansion) | Notes |
|---|---|---|---|---|---|---|
| SMB | $... | ...% | ...% | ...% | $... | churn > expansion → finite |
| Mid-Market | $... | ...% | ...% | ...% | $... | ... |
| Enterprise | $... | ...% | ...% | ...% | $... | expansion > churn → cap at 5× ACV for prudence |
| PLG self-serve | $... | ...% | ...% | ...% | $... | ... |

If churn < expansion in any segment, LTV formula diverges — cap display LTV at 5× annual GP and flag NRR>100%.

## 4. Guardrail table
| Segment | LTV : CAC (≥3.0) | CAC payback months (≤18) | Action |
|---|---|---|---|
| SMB | ... | ... | ok / review / fix |
| Mid-Market | ... | ... | ... |
| Enterprise | ... | ... | ... |
| PLG | ... | ... | ... |

## 5. Portfolio metrics
- **Burn multiple** = net burn ÷ net new ARR = ... (target ≤2.0, elite ≤1.0)
- **Magic number** = (quarterly ΔARR × 4) ÷ prior-quarter S&M = ... (target ≥0.7)
- **Months of runway** at current burn = ...

## 6. MoM deltas (flag ±15%)
| Metric | Prior | Current | Δ | Explanation |
|---|---|---|---|---|
| Blended CAC | ... | ... | ... | ... |
| LTV:CAC (Mid-Market) | ... | ... | ... | ... |
| Burn multiple | ... | ... | ... | ... |

## 7. Decision queue (fed to CMO)
- Reallocate: {channel/segment combos with LTV:CAC >4.0 getting under-invested}
- Pause: {LTV:CAC <1.5 sustained 2 months}
- Diagnose: {payback trending wrong >2 months}

## 8. Change log
- YYYY-MM-DD: methodology change note (e.g., "added fully-loaded agency fees to outbound CAC").
