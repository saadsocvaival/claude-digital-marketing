# Weekly KPI Snapshot — Loopgate — Week of 2026-04-20 (Week 1 baseline)

> Rubric: `/rubrics/weekly-kpi-snapshot.yaml`. Synthetic baseline week; numbers derived from fixture ledger + public SaaS DevTools benchmarks (OpenView 2025, SaaS Benchmarks 2025). Will be regenerated each Monday by Head of Analytics.

## 1. North Star Metrics
| NSM | Target | Current (wk) | WoW Δ | MTD vs target | Status |
|---|---|---|---|---|---|
| Net new ARR / mo | $180k | $108k (trailing 4w) | +2.1% | 60% | 🟠 |
| Free→Activated in 14d | 48% | 36.9% | +0.4pp | 77% | 🟠 |
| SQL-sourced pipeline $/mo | $720k | $420k | +3.8% | 58% | 🟠 |
| Organic non-brand sessions/mo | 55k | 28k | +1.2% | 51% | 🔴 |

## 2. Funnel (this week)
| Stage | This wk | Last wk | Δ | 4w avg | Target |
|---|---|---|---|---|---|
| Sessions | 19,420 | 19,080 | +1.8% | 20,500 | 55,000/4w avg to hit plan |
| Signups | 328 | 310 | +5.8% | 352 | 420 |
| Activated (flag in prod <14d) | 121 (36.9%) | 113 (36.5%) | +0.4pp | 130 | 48% |
| Team-plan starts | 21 | 19 | +10.5% | 21 | 35 |
| Enterprise demos | 8 | 7 | +14% | 7 | 11 |
| Enterprise SQL | 3 | 2 | +50% | 2.8 | 6 |
| Closed-won enterprise | 0 | 1 | -1 | 0.5 | 1.3 |
| MRR added | $5.1k | $4.6k | +10.9% | $4.9k | $9.0k |

## 3. Channel Table
| Channel | Sessions | Leads | CPL | MQL | SQL→Won CVR | CAC | ROAS |
|---|---|---|---|---|---|---|---|
| Google Ads | 3,800 | 42 | $131 | 18 | 15% | $720 | 1.4 |
| LinkedIn Ads | 1,200 | 22 | $205 | 12 | 22% | $890 | 1.1 |
| Organic | 6,820 | 58 | $0 (self) | 18 | 18% | $0 | — |
| Newsletter | 480 | 14 | $0 | 8 | 28% | $0 | — |
| Direct | 4,100 | 31 | — | 14 | — | — | — |
| Referral | 960 | 16 | — | 9 | 25% | — | — |
| Retargeting | 2,060 | 9 | $42 | 4 | 20% | $210 | 3.1 |

## 4. Top Movers
- **Organic gainers:** "launchdarkly alternative" +3 positions (page 2→top of page 2); "feature flag self host" +5 positions.
- **Organic losers:** "feature flag platform" -2 positions (SERP churn).
- **Paid gainers:** Google "TCO-Shock" ad group: CPL $118 (below target $180), scale 20%.
- **Paid losers:** LinkedIn "SDK-Perf" creative: CPL $320 (above $200 threshold); refresh triggered.
- **Top content by sessions:** pillar-TCO post (planned for W1 publish), positioning page, docs quickstart.
- **Top content by conversions:** positioning page, comparison page (vs LD), docs quickstart.

## 5. Experiments Concluded
| Experiment | Hypothesis | Result | Decision |
|---|---|---|---|
| Homepage hero "47ms" vs "Audit trail" | perf-angle outperforms audit | inconclusive (n=2,100, 92% conf) | iterate: add segment-split |

## 6. Anomalies (>2σ or >15% WoW)
| Metric | Δ | Hypothesis | Owner |
|---|---|---|---|
| LinkedIn SDK-Perf CPL $320 | +56% | creative fatigue (frequency 4.2) | Sam — refresh this week |
| Enterprise demo→SQL jump (50%) | +50% | n=2 → noise; watch for 2 more weeks | Sam |

## 7. Data Quality Notes
- BigQuery access: not yet provisioned → multi-touch attribution model deferred. Affected: channel ROAS for Enterprise.
- Meta tracking: iOS 14+ loss ~20%; small channel impact.
- Newsletter clicks: UTMs not enforced on 2 editions; backfilled self-report.

## 8. Recommended Actions per Head
- **Growth (Jess):** Run activation experiment #1 (guided first-flag tour); pre-register hypothesis + MDE.
- **Performance (Sam):** Refresh LinkedIn SDK-Perf creative; scale Google TCO-Shock +20%; pause if CPL stays >$180 on ramp.
- **SEO (Leo):** Publish pillar TCO this week; internal-link from homepage; submit to GSC.
- **Content (Amal):** Ship pillar + 2 spokes; begin 1→10 repurposing of pillar.
- **CRO (Dana):** Ship LP `/lp/flag-tco-calc` with CRO sign-off.
- **Analytics (Priya):** Escalate BigQuery access to CTO; ship fallback W-shaped on HubSpot-only by Friday.
- **Automation (Rae):** Launch onboarding sequence E1–E7; set up 10% control holdout.
- **Brand (Jess + PMM):** Ship LD battlecard final + begin Statsig battlecard.

## 9. Sourcing Footnote
- Sessions / Signups: GA4 property 427193, view "Marketing Site", event `page_view` + `sign_up`
- Activated: Amplitude cohort `free_activation_v2`
- Team starts: Stripe subscriptions table, filter `plan=team`
- Enterprise demos: HubSpot deal stage `Discovery`
- SQL: HubSpot deal stage `Qualified`
- CAC: cost from Ads APIs (Google Ads API, LinkedIn Campaign Manager API) / Stripe revenue
- Rankings: Ahrefs + GSC
- Experiment: Amplitude Experiment
