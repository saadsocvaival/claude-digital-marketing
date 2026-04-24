# Campaign Brief — Q2 Demand, Platform EB (Google + LinkedIn)

> Rubric: `/rubrics/campaign-brief.yaml`. Launch: 2026-05-01. Duration: 8 weeks. Total budget: $40k ($25k Google, $15k LinkedIn).

## 1. Objective
**Demand generation** — drive MQLs (Priya persona) who request demo or complete TCO calculator.

## 2. ICP Segment
- Priya (Head of Platform/DevEx), 50–500 eng orgs, cloud-native stack.
- Exclusions: competitor domains; <15 engineer orgs; APAC (except JP/AU until localized).

## 3. Message & Offer
- Primary headline: "Flag sprawl is a tax. See what it's costing you."
- Offer: TCO calculator + "Platform Engineer's Guide to Feature Flags".
- Source: `messaging.md` Pillar 1; `offer.md` lead magnet.

## 4. Creative Concepts (3 angles)
| Variant | Hypothesis | Headline | Visual | Proof |
|---|---|---|---|---|
| A — TCO shock | Specific-dollar pain beats general pain | "Your flag table is costing $132k/yr" | Spreadsheet → calculator screen | TCO formula exposed |
| B — Audit anxiety | SOC2 timing drives urgency | "Your next audit will ask about feature flags" | SOC2 report cover | Compliance page excerpt |
| C — Migration ease | Unblocks "we can't switch" objection | "Migrate off LaunchDarkly in a weekend" | Migrator terminal | 2 case-study logos |

## 5. Landing Page
`/lp/flag-tco-calc` — see `campaigns/lp-tco-calc.md`. Hero headline matches Variant A. CRO sign-off: pending (Dana, due 2026-04-28).

## 6. Budget & Pacing
- Total: $40k over 8 weeks.
- Daily cap: $800 Google, $500 LinkedIn.
- Ramp: week 1 at 50% for learning; scale if CPL < $180.
- Reallocation trigger: 20% shift allowed week-over-week between Google↔LinkedIn based on MQL quality (fit ≥60).

## 7. Measurement Plan
- Primary KPI: MQLs (fit ≥60, intent ≥30) at ≤$180 CPL.
- Secondary: TCO calc completions (≥35% of LP visitors), demo requests, Enterprise SQLs attributed.
- Attribution window: 30-day last non-direct click; multi-touch when BigQuery live (week 9).
- Data path: GA4 → BigQuery → Looker; HubSpot for downstream; cost via Ads APIs.

## 8. Stop-Loss
- Google: CPL >$280 for 7 consecutive days → pause.
- LinkedIn: CPL >$350 for 7 consecutive days → pause.
- MQL→SQL CVR <5% after 150 MQLs → message iteration + CRO review before further spend.
- Frequency >4 on any LinkedIn ad → force creative refresh.

## 9. UTMs
- Google: `utm_source=google&utm_medium=cpc&utm_campaign=2026-q2-demand-platform-eb&utm_content=headline-{a|b|c}-cta-calc-audience-priya&utm_term={keyword}`
- LinkedIn: `utm_source=linkedin&utm_medium=paid-social&utm_campaign=2026-q2-demand-platform-eb&utm_content=headline-{a|b|c}-cta-calc-audience-priya&utm_term=platform-eng-50-500`

## 10. Launch Gate
- [ ] CRO sign-off on LP (Dana, 2026-04-28)
- [ ] Brand sign-off on creative (Jess, 2026-04-29)
- [ ] Legal sign-off on competitor-comparison claims (Legal, 2026-05-05) — PRE-LAUNCH BLOCKER for Variant C
- [ ] Tracking QA — events fire, UTM preserved to HubSpot
- [ ] Stop-loss entered into platforms
- [ ] Daily cap set
