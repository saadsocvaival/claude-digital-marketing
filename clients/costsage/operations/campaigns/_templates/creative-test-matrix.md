# Creative Test Matrix Template — CostSage.ai

> Use to plan structured creative experimentation. Each cell = one ad variant. Aim for 6–9 cells live per campaign at any time, refreshed every 2–3 weeks based on win/loss.

## How to use
1. Pick 3 hooks × 3 angles × 2 formats = 18 candidate cells. Cull to top 6–9 for launch.
2. Each variant gets a unique `cta_id` so the `cta_click` event in `analytics/tag-plan.md` can attribute back to the cell.
3. Declare statistical-significance thresholds before reading results: ≥ 1,000 impressions and ≥ 50 clicks per variant before a win-call.
4. Winners feed `_creative/ad-copy-bank.md`. Losers logged with reason.

## Hooks (the "stop-the-scroll" line)
| ID | Hook | Tone |
|----|------|------|
| H1 | "Your AWS bill is 30% waste. We find it in 24 hours." | Direct / quantified |
| H2 | "FinOps without the spreadsheet army." | Pain-relief |
| H3 | "Agentic AI that cuts cloud cost while you sleep." | Future-forward |
| H4 | "RIs vs. Savings Plans, decided automatically." | Specificity |
| H5 | "From cost surprise to cost confidence." | Emotional |

## Angles (the underlying argument)
| ID | Angle | Best persona |
|----|-------|--------------|
| A1 | ROI / payback math | CFO-adjacent, FinOps lead |
| A2 | Engineering time saved | VP Eng, Head of Platform |
| A3 | Risk avoidance (overage, runaway spend) | CTO |
| A4 | Competitive switch (vs CloudZero / nOps) | FinOps lead evaluating |
| A5 | Best-practice alignment (AWS Well-Architected) | Platform / SRE |

## Formats
| ID | Format | Where |
|----|--------|-------|
| F1 | Single-image static | LinkedIn, Reddit, Meta |
| F2 | Carousel (3–5 cards) | LinkedIn |
| F3 | Short video (≤ 60s) | LinkedIn, YouTube pre-roll |
| F4 | Responsive Search Ad (RSA) | Google, Bing |
| F5 | Conversation ad / Message | LinkedIn |
| F6 | Native text post | Reddit |

## Matrix (example — populate per campaign)
| Cell | Hook | Angle | Format | Persona | LP | cta_id | Status |
|------|------|-------|--------|---------|----|--------|--------|
| C01 | H1 | A1 | F4 | FinOps lead | /aws | `gs_aws_h1a1` | live |
| C02 | H1 | A2 | F1 | VP Eng | /aws | `li_aws_h1a2` | live |
| C03 | H2 | A2 | F2 | Head of Platform | /aws | `li_aws_h2a2` | live |
| C04 | H3 | A3 | F3 | CTO | / | `li_root_h3a3` | live |
| C05 | H4 | A1 | F4 | FinOps lead | /blog/ri-vs-savings-plans | `gs_ri_h4a1` | live |
| C06 | H5 | A4 | F1 | FinOps lead | /compare/cloudzero-vs-costsage | `li_cmp_h5a4` | live |

## Win/loss log
| Cell | Decision date | Verdict | Why | Next iteration |
|------|---------------|---------|-----|----------------|
