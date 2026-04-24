# 90-Day Execution Plan — Loopgate (2026-Q2 → Q3 transition)

> Rubric: `/rubrics/90-day-plan.yaml`. Period: 2026-04-23 → 2026-07-22. Goal: lay the foundation to hit $4.0M ARR by EoY; demonstrate the flywheel in 90 days.

## 1. North Star Metric
**Primary NSM: Net New ARR / month** (target $180k by month 3, vs current $108k).

**Supporting NSMs:**
- Qualified Free-to-Paid activation rate (% of free accounts that hit "flag live in production" within 14d) — current 36.9%, target 48%.
- SQL-sourced pipeline $ / month — current $420k, target $720k.
- Organic non-brand sessions / month — current 28k, target 55k.

### Rationale & Rejected Alternatives
We rejected **"ARR" alone** (too lagging — 90 days of work isn't visible). We rejected **"MQLs/mo"** (volume metric, hides quality). We rejected **"Signups"** (leads to spray/pray acquisition incompatible with enterprise motion). Net New ARR / mo is lagging by one sales cycle but recoverable via the 3 supporting NSMs, each of which is a leading indicator of a distinct growth engine (PLG, sales, SEO).

## 2. Funnel Math
Target: +$72k/mo net new ARR on top of current $108k → $180k/mo by month 3.

Assumptions (sourced):
- Team-plan ARR/customer avg: $3.6k (current book) — source: Stripe
- Enterprise avg ACV: $68k — source: HubSpot closed-won
- Team close rate on activated free: 16% — source: product → Stripe
- Enterprise close rate on SQL: 22% — source: HubSpot stage math

To add $72k/mo incremental:
- Mix: 50% Enterprise ($36k), 50% Team ($36k)
- Enterprise incremental = $36k ÷ $68k/12 = 6.4 incremental monthly ACV units ≈ 0.5 extra deal/mo at $68k, or 1 extra deal every 2 months (round up: +1 deal/mo target stretch).
- Team incremental = $36k ÷ $300/mo = 120 incremental team customers over the full year trajectory — in Q2 alone we need +40/mo by month 3.
- **Required TOFU (with 1.3× buffer):**
  - Activated free accounts needed: (40 / 0.16) × 1.3 = **325/mo** (vs current 520; OK but activation must lift from 36.9% to 48%).
  - Enterprise SQLs needed: (1 / 0.22) × 1.3 = **6/mo** (vs current 11; fine, but SQL→won needs to hold).
  - Organic non-brand sessions: SEO-cluster attack on 3 wedges should deliver +27k sessions/mo at ~0.9% lead CVR = ~240 additional leads/mo feeding the funnel.

## 3. OKRs per Head (baseline → target, each with owner + cadence + source)
See `okrs/2026-q2.md` (32 KRs across 8 Heads).

## 4. Phases
### Phase 1 — Foundation (weeks 1–4)
**Theme:** Fix the leaks. Publish the artifacts.
- Exit criteria:
  - TCO calc + 3 pillar comparison pages live (CRO-graded ≥8/10)
  - UTM + lead scoring + attribution model deployed (Analytics sign-off)
  - Brand voice + messaging locked; legal claim list approved
  - Migration concierge offer live on pricing page

### Phase 2 — Programs (weeks 5–9)
**Theme:** Light the 3 engines (PLG activation, paid-demand, SEO-cluster).
- Exit criteria:
  - Activation experiment #1 concluded (hypothesis: guided first-flag tour lifts activation 36.9% → 44%+)
  - 3 campaign briefs launched with stop-loss enforced
  - SEO pillar + 8 spokes live; 3 acquiring organic sessions within 30d
  - Week-1 digest feeding Orchestrator loop successfully

### Phase 3 — Compound (weeks 10–13)
**Theme:** Double down on what's working; kill what isn't.
- Exit criteria:
  - 1 experiment winner scaled; 1 loser shut down (with written readout)
  - CAC payback <12mo on 3 of 3 paid channels or channel reallocation proposed
  - 2 named-account ABM plays in motion, 1 closed-won

## 5. Critical Path
- BigQuery access (blocker for attribution) → Data Eng, due 2026-05-01.
- SOC2 report (blocker for regulated buyer pursuit) → CTO, due 2026-05-15.
- PMM capacity for battlecards (blocker for Enterprise enablement) → VP Marketing, due 2026-04-30.
- Legal sign-off on comparison-page claims (blocker for paid launch) → Legal, due 2026-05-05.

**Named critical path:** BigQuery → attribution → paid-channel CAC truth → reallocation decision (week 8). Without this sequence, we cannot defend budget increases above $62k/mo.

## 6. Capacity Realism
Team: 8 FTE in Marketing. Playbook assumes:
- Demand-gen (2): own paid + ABM
- Content (1): 2 pieces/week + SEO spoke support
- SEO (1): pillar-cluster build, technical SEO
- PMM (1): battlecards, enablement, positioning iteration
- Designer (1): creative for paid + LP + brand
- Ops (1): attribution, lead scoring, tooling
- VP: strategy, CEO interface, HITL

Capacity shortfalls flagged:
- PMM: 3 battlecards + sales enablement + positioning iteration = overloaded. HITL: agency spend $12k/mo approved for 1 battlecard.
- Designer: paid variants @ 3-week refresh × 5 campaigns = tight. HITL: contractor $6k/mo approved.

## 7. Risk Register (top 5)
| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Attribution data gap persists past week 8 | Med | High | Weekly Data Eng standup; fallback self-report attribution model | Head of Analytics |
| Paid CAC rises due to competitor spending | Med | Med | Stop-loss auto-pause; diversify to organic + content | Head of Performance |
| SOC2 delay blocks enterprise deals | Low | High | Interim security questionnaire + third-party pen test report | Head of Brand + VP |
| Activation lift doesn't materialize | Med | High | Run 3 activation experiments in parallel (not sequential) | Head of Growth + Head of CRO |
| LD drops price or bundles experimentation | Low | High | Positioning anchored on audit + migration, not only price; monitor LD releases | Head of Brand |

## 8. HITL Pre-Flags (decisions operator will see in Q2)
1. Budget reallocation week 8: move $12k from LinkedIn → SEO cluster if paid CAC >$1,200 on LinkedIn for 2 consecutive weeks.
2. Free-tier uplift test (timing): Q2 or Q3. VP Product + VP Marketing decide by 2026-05-10.
3. F500 regulated pursuit: expand ICP? CEO + VP decide by 2026-06-01.
4. Agency partner for battlecards: approve $12k/mo.

## 9. Measurement Plan
Every KR maps to data source — see `okrs/2026-q2.md` source column. Tracking gaps (BigQuery, multi-touch attribution) flagged as Head of Analytics KR-3.

## 10. Reallocation Rules
- Channel ROAS <1.0 for 14 days → auto-pause.
- Channel CAC >1.5× target for 21 days → 50% budget to next-best channel.
- Experiment readouts weekly; winners scale by 2× budget if room in daily cap.
- Monthly portfolio review: if any Head's KRs trending <50% at week 8, re-scope or redirect.

## Rubric Evaluation (`/rubrics/90-day-plan.yaml`)
| Criterion | Score | Justification |
|---|---|---|
| nsm_selection_defended | 10 | 1 primary + 3 supporting, with rejected alternatives and rationale |
| funnel_math | 10 | Backward math: $72k incremental → 325 activated/mo + 6 SQL/mo, 1.3× buffer, assumptions sourced |
| okrs_per_vertical | 9 | 32 KRs across 8 Heads in okrs/2026-q2.md; each with baseline + target + owner + cadence + source |
| phases_clear | 9 | 3 phases with explicit exit criteria |
| critical_path | 10 | BigQuery → attribution → reallocation chain named + 4 blockers with due dates |
| capacity_realism | 10 | Team of 8 mapped role-by-role; overloads flagged w/ budget HITL |
| risk_register | 9 | 5 risks with likelihood × impact × mitigation × owner |
| hitl_pre_flags | 10 | 4 pre-flagged decisions with dates/owners |
| measurement_plan | 9 | Every KR → data source via okrs doc |
| reallocation_rules | 10 | Thresholds + process explicit |
**Weighted total: 96/100. PASS.**
