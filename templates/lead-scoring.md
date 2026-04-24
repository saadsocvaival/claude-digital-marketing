# Lead Scoring Model — {{client}}

> Rubric: `/rubrics/lead-scoring.yaml`.

## 1. Dimensions
Final routing uses **Fit × Intent × Engagement** — not a single blended score.

### Fit (0–100)
| Attribute | Weight | Source | Rule |
|---|---|---|---|
| Industry match ICP | 25 | enrichment | +25 if in ICP list, -50 if in disqualify list |
| Company size | 20 | enrichment | … |
| Role | 25 | form / enrichment | champion +20, end-user +10, junior 0 |
| Geography | 10 | IP / form | … |
| Tech stack | 20 | BuiltWith | … |

### Intent (0–100, decaying)
| Signal | Points | Decay |
|---|---|---|
| Demo request | 60 | none |
| Pricing page visit | 20 | -50% / 14d |
| 2nd pricing visit within 7d | +30 | … |
| Comparison keyword entry | 25 | … |
| Webinar attended | 15 | … |

### Engagement (0–100, decaying)
Email opens/clicks, content consumption, product actions (if PLG).

## 2. Thresholds & Routing
| Band | Fit | Intent | Action | SLA |
|---|---|---|---|---|
| MQL | ≥60 | ≥30 | nurture + SDR on prioritized queue | 1 biz day |
| SAL | ≥60 | ≥60 | SDR call attempt | 15 min for demo-request, 4h otherwise |
| SQL | ≥70 | ≥70 | AE handoff | same day |
| Disqualified | <40 fit OR on block list | — | suppress | — |

## 3. Negative Scoring
Student email, free-mail with no company signal, competitor domain, unsubscribe — block or deduct.

## 4. Validation
Retrain quarterly against CRM won/lost. Report precision, recall, CVR by band. Drift alarm if CVR by band drops >20% WoW.

## 5. Transparency
Top 3 contributing signals visible to reps in CRM.
