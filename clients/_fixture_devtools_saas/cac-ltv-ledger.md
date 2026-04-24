# Loopgate — CAC / LTV Ledger (2026-Q2 synthetic)

**Synthetic fixture data.** Real-client deploy replaces with finance-sourced numbers.

## Period header
- Period: 2026-04
- Gross margin: 78% (SaaS fully-loaded including hosting + CS)
- FX: USD
- Fully-loaded CAC: **yes** (includes S&M headcount + tools + agencies)

## CAC by segment × channel (USD)
| Segment ↓ / Channel → | Paid social | Paid search | Organic | Outbound | Partner | Events | **Segment blended** |
|---|---|---|---|---|---|---|---|
| SMB | 380 | 420 | 140 | — | — | — | **310** |
| Mid-Market | 2,200 | 1,900 | 900 | 3,400 | 2,100 | 3,800 | **2,050** |
| Enterprise | — | — | 4,800 | 28,000 | 12,000 | 22,000 | **18,500** |
| PLG self-serve | 140 | 180 | 60 | — | — | — | **110** |
| **Channel blended** | **280** | **340** | **190** | **15,700** | **6,400** | **11,400** | **620** (heavily skewed by PLG volume) |

## LTV by segment
| Segment | ACV | GM | Net monthly churn | Net monthly expansion | LTV |
|---|---|---|---|---|---|
| SMB | $1,200 | 78% | 3.8% | 1.1% | $11,600 |
| Mid-Market | $18,000 | 78% | 1.1% | 2.4% | capped at 5× ACV = $90,000 (expansion>churn; NRR~115%) |
| Enterprise | $140,000 | 78% | 0.4% | 3.2% | capped at 5× ACV = $700,000 (NRR~134%) |
| PLG self-serve | $240 | 78% | 5.9% | 0.6% | $3,500 |

## Guardrails
| Segment | LTV:CAC | Payback (mo, gross-profit basis) | Status |
|---|---|---|---|
| SMB | 37.4 | 4.2 | 🟢 |
| Mid-Market | 43.9 | 17.4 | 🟢 (payback near ceiling) |
| Enterprise | 37.8 | 20.3 | 🟡 — payback above 18mo target; investigate sales-cycle |
| PLG self-serve | 31.8 | 7.1 | 🟢 |

## Portfolio
- **Burn multiple:** 1.4 (target ≤2.0; elite ≤1.0) 🟢
- **Magic number:** 0.82 🟢
- **Runway:** 22 months

## MoM deltas (vs 2026-03)
| Metric | Prior | Current | Δ | Explanation |
|---|---|---|---|---|
| Blended CAC | 590 | 620 | +5% | PLG mix up, outbound steady |
| LTV:CAC (Mid-Market) | 41.0 | 43.9 | +7% | expansion strengthened |
| Burn multiple | 1.5 | 1.4 | −0.1 | ARR growth outpaced spend |

## Decision queue (fed to CMO)
- **Reallocate:** SMB organic and Mid-Market partner have LTV:CAC >40 and under-invested — shift $80k/qtr from paid social into these.
- **Diagnose:** Enterprise payback at 20.3 mo — is sales cycle elongating or discounts deepening? Head of RevOps owns within 2 weeks.
- **Pause:** none this month.

## Change log
- 2026-04-12: added agency fees to outbound fully-loaded CAC (prior months excluded; flagged in trend).

---
**Self-score:** 82/100 — segmented, fully-loaded, decision-oriented. Loses points on: LTV caps are heuristic; NRR>100% segments need cohort-curve proof rather than formula cap.
**Critic-score:** TBD.
