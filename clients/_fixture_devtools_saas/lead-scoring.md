# Lead Scoring Model — Loopgate

> Rubric: `/rubrics/lead-scoring.yaml`. Owner: Head of Automation. Validated against 2025-H2 closed-won/lost cohort (n=312).

## 1. Dimensions — Fit × Intent × Engagement

### Fit (0–100)
| Attribute | Weight | Source | Rule |
|---|---|---|---|
| Engineering HC 50–500 | 30 | Clearbit + form | +30 if in-range, +10 if 15–49, -30 if <15 |
| Cloud-native stack (K8s, GitHub/GitLab) | 20 | BuiltWith | +20 if matches, 0 otherwise |
| Role match ICP (platform, staff eng, VP eng, PM) | 25 | form + enrichment | Priya +25, Marco +20, Rina +15, VP +20, other -10 |
| Industry allow-list (SaaS, fintech, marketplace, health, dev tooling) | 15 | Clearbit | +15 if match, 0 otherwise |
| Geography (US/EU) | 10 | IP + form | +10 if US/EU/CA/UK, 0 APAC, -20 sanctioned |
| Disqualifiers | — | form + email | -100 if competitor email (launchdarkly.com, statsig.com, split.io); -100 if edu/student; -50 if free-mail with no company |

### Intent (0–100, decaying)
| Signal | Points | Decay |
|---|---|---|
| Demo request | 70 | none for 30d, then -50% / 14d |
| Pricing page visit | 15 | -50% / 14d |
| 2nd pricing visit within 7d | +25 | — |
| TCO calculator used | 40 | -25% / 14d |
| Comparison page visit (vs-LD, vs-Statsig, vs-Split) | 25 | -50% / 14d |
| High-intent search keyword entry ("launchdarkly alternative", "feature flag self host") | 20 | -50% / 14d |
| Webinar registered | 10 | — |
| Webinar attended | 20 | -25% / 30d |
| Docs visit ≥3 pages in session | 10 | -50% / 14d |
| OSS repo star | 5 | none |
| ABM list member + any visit | +15 | — |

### Engagement (0–100, decaying)
| Signal | Points | Decay |
|---|---|---|
| Email open (last 30d) | 2 each, cap 10 | full decay after 30d |
| Email click | 6 each, cap 24 | -50% / 30d |
| Newsletter subscribe | 8 | none |
| Community sign-up (Slack/Discord) | 12 | -25% / 60d |
| Product: signup | 30 | — |
| Product: first flag created | 20 | — |
| Product: flag live in prod <14d (activation) | 25 | — |
| Product: invited a teammate | 15 | — |

## 2. Thresholds & Routing
| Band | Fit | Intent | Engagement | Action | SLA |
|---|---|---|---|---|---|
| Disqualified | <40 OR disqualifier flag | — | — | Suppress + mark in CRM | — |
| Marketing-nurture | 40–59 | <30 | any | Automated nurture sequence | n/a |
| MQL | ≥60 | ≥30 | any | SDR queue, prioritized | 1 biz day |
| SAL | ≥60 | ≥60 | any | SDR call attempt | 15 min (demo request) / 4h otherwise |
| SQL | ≥70 | ≥70 | any | AE handoff, book discovery | same day |
| Product-qualified lead (PQL) | ≥50 | any | Activation=true + ≥10 engagement | AE notified; expansion conversation | 2 biz days |

## 3. Negative Scoring
- Competitor domain: -100.
- Unsubscribe: cap engagement score at 0 for 90d.
- Bounce/complaint: suppress.
- Bot patterns (headless UA, >10 pageviews <1min): disqualify.

## 4. Validation (against 2025-H2 cohort, n=312)
| Band | Sample | Won | CVR |
|---|---|---|---|
| SQL | 54 | 17 | 31.5% |
| SAL | 78 | 12 | 15.4% |
| MQL | 96 | 9 | 9.4% |
| Nurture | 84 | 4 | 4.8% |

Precision at SQL band: 0.315 (vs target ≥0.25) ✓.
Recall at SQL+SAL: 69% of eventual wins captured ✓.
Model refreshed quarterly; drift monitor triggers re-train if any band CVR drops >20% WoW for 2 consecutive weeks.

## 5. Transparency
In HubSpot contact view, top 3 contributing signals display alongside total score. Reps see WHY, not just WHAT.
