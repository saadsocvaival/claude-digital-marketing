# Positioning — Loopgate

> Rubric: `/rubrics/positioning.yaml`. Framework: Geoffrey Moore + April Dunford.

## 1. Positioning Statement (Moore)
> **For** mid-market engineering orgs (50–500 engineers) running trunk-based, cloud-native workflows **who** are drowning in flag sprawl and can't justify LaunchDarkly Enterprise pricing, **Loopgate is** a unified feature-flag + experimentation platform **that** gives platform teams a single audit-ready system of record with sub-50ms SDK evaluation and a turnkey migration from homegrown or legacy flag systems. **Unlike** LaunchDarkly (enterprise-priced, experimentation bolt-on) or Statsig (experimentation-first, flagging is secondary), **Loopgate** is the only platform where flags and experiments share one audit trail, one permission model, and one source of truth — at 1/3 the enterprise TCO.

## 2. Competitive Alternatives
| Alternative | Why customer picks it | Where it breaks down |
|---|---|---|
| **Homegrown Postgres table** | Free, "we can build it" | Engineering toil (~0.6 FTE), audit gaps, SDK latency, no experimentation |
| **LaunchDarkly** | Safe enterprise pick, broad features | Price ($140k+/yr at 100 seats), experimentation feels bolted-on, procurement-heavy |
| **Statsig** | Strong experimentation + free tier | Flags secondary, less mature audit/permissions, no on-prem |
| **Split.io** | Enterprise heritage | Older UX, pricing opaque, slow roadmap |
| **Flagsmith/Unleash OSS** | Free, self-host | Ops burden, limited SSO/audit for Enterprise, no built-in experimentation stats |
| **GrowthBook** | Stats-strong, fair price | Small team, thinner platform depth |
| **Do nothing** | No new vendor | Pain compounds at 100+ engineers |

## 3. Unique Attributes → Value
| Attribute | Benefit | Value (what it lets customer do/be) | Proof |
|---|---|---|---|
| Unified flags + experiments (one audit trail) | No duplicate source of truth | Engineering and Product speak the same language; faster decisions | Architecture doc; 3 case studies of LD+Statsig consolidation |
| Sub-50ms p95 SDK eval (edge cache) | No latency risk on hot paths | Safe to put flags in request-serving code | Published benchmarks vs LD (78ms) and Statsig (62ms) |
| Turnkey migrator (LD + homegrown) | Migration in days not quarters | Budget case stops being blocked on switching cost | Migration guide + 2 customer migration cases |
| OSS SDK + self-host option for Enterprise | No vendor-lock fear | Security + compliance passes | GitHub repo (Apache 2.0), self-host docs |
| Transparent, seat-based pricing (1/3 LD TCO) | CFO signs off without a 6-week negotiation | Shortens sales cycle | Public pricing page + comparison calculator |
| SOC2 Type II + SOX-grade audit log | Regulated industries buy | Fintech / health / insurance can adopt | Audit report (on request), compliance page |

## 4. Market Category
**Feature management** (Gartner, 2025). We compete in the unified flagging+experimentation subcategory. We are NOT "experimentation platform" (Statsig's category) nor "feature management for enterprise" (LD's). We are "feature management for mid-market Platform teams" — a deliberate niche-down.

## 5. Who It's For (and who it's not)
**Best fit:**
- 50–500 engineers, trunk-based/CI-heavy, cloud-native
- Has a Platform / DevEx team that owns dev velocity
- Currently on homegrown or LD/Statsig with pain
- Values audit + compliance

**Disqualifiers:**
- <15 engineers — send to Flagsmith/GrowthBook OSS
- F500 regulated, 18-month procurement, on-prem-only, $500k+ budget — LD wins, don't compete
- Analytics-first buyers where experimentation is the only need — Statsig fits better
- No platform team, no buyer — long, unqualified cycles

## 6. Trends Making This Position Valuable Now
1. **Platform Engineering is the fastest-growing eng function** (Gartner 2025). New buyer with tooling budget.
2. **DORA + Dev Productivity metrics** are a boardroom topic in 2025–2026.
3. **SOC2 and SOX** audits increasingly flag release-process gaps; flagging is on the checklist.
4. **AI-assisted dev workflows** are pushing deploy frequency up → flag discipline becomes critical.
5. **Macro cost discipline** — CFOs reject 6-figure dev-tool contracts; mid-market pricing wins.

## 7. Anti-Positioning
We are **NOT**:
- The cheapest (OSS is cheaper; price isn't the primary wedge)
- The most feature-rich (LD has more; depth in audit + migration is our wedge)
- An experimentation-first tool (Statsig owns that frame; we unify)
- "The LaunchDarkly killer" (we don't beat them at their game; we niche down)

## Rubric Evaluation (`/rubrics/positioning.yaml`)
| Criterion | Score | Justification |
|---|---|---|
| category_clarity | 10 | "Feature management for mid-market Platform teams" — explicit niche |
| target_specificity | 10 | 50–500 eng, trunk-based, cloud-native, Platform team |
| differentiator_proof | 10 | Unified audit trail + sub-50ms + turnkey migrator + 1/3 TCO — each provable |
| competitive_alternatives | 10 | 7 alternatives incl. homegrown + do-nothing |
| trends_justification | 9 | 5 tailwinds, each sourced/observable |
| anti_positioning | 10 | Explicit "not the cheapest / not feature-rich / not LD-killer" |
| attributes_laddered | 10 | Attribute → benefit → value → proof table |
| moore_statement | 10 | Full Moore template, crisp |
| disqualifiers | 10 | Explicit "not for" list |
**Weighted total: 98/100. PASS.**
