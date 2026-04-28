# Month-1 Budget Pacing Model — CostSage.ai Paid Media

> Total ≤ $5,000 across all paid channels. Includes break-even math vs. CostSage SMB-tier ARR.

## 1. Channel allocation (Month 1)

| # | Campaign | Monthly $ | Daily $ | % of total | Rationale |
|---|----------|-----------|---------|------------|-----------|
| 1 | Google Search — AWS cost tools | 1,500 | 50 | 30% | Highest-intent demand capture |
| 2 | Google Search — FinOps platform | 1,000 | 33 | 20% | Adjacent demand |
| 3 | LinkedIn — CTO | 2,000 (split see below) | 70 | — | Combined LI = 40% |
| 4 | LinkedIn — FinOps lead | (see note) | | | |
| 5 | Microsoft Bing — AWS cost | 750 | 25 | 15% | Cheaper inventory, enterprise IT |
| 6 | Reddit — AWS/DevOps | 500 | 16 | 10% | Awareness + content top-of-funnel |
| 7 | G2/Capterra | 1,000 | n/a | — | **BLOCKED** by V1 listings — defer to M2 |

**Resolution:** Month-1 active spend ≤ $5,000 split as:

| Channel | Month 1 $ |
|---------|-----------|
| Google AWS | 1,500 |
| Google FinOps | 1,000 |
| LinkedIn CTO | 1,000 |
| LinkedIn FinOps | 1,000 |
| Microsoft Bing | 250 (delayed soft-launch) |
| Reddit | 250 (delayed soft-launch) |
| **Total** | **$5,000** |

LinkedIn split 50/50 between CTO and FinOps audiences during M1 (each $1,000 vs. eventual $2,000) so we can read signal on both audiences without going over total budget.

## 2. Pacing rules
- **Daily caps:** as listed.
- **Weekly review:** Monday 10:00 GMT — reallocate ≤ 20% across channels based on prior-week CPA.
- **Auto-pause:** any campaign at 130% of weekly target spend with 0 conversions → pause and escalate.
- **Spend ramp (M1 → M3):**
  - M1: $5,000 (proof phase).
  - M2: $7,500 (M2 unblocks G2/Capterra; LI scales toward $4K combined).
  - M3: $10,000 (scale winners; introduce Meta retargeting; full LI $4K).

## 3. Break-even math (LTV:CAC ≥ 3:1)

**Inputs (assumed; replace with operator-confirmed numbers):**
- SMB tier price: **$499/mo** = **$5,988 ARR/customer/year**. `[TBD-OPERATOR]`
- Gross margin: **80%** (typical SaaS). `[TBD-OPERATOR]`
- Gross-margin-adjusted ARR (year 1): $5,988 × 80% = **$4,790**.
- Average customer lifetime: **3 years** (SMB SaaS median; `[TBD-OPERATOR]`).
- Annual net revenue retention: **110%** (target).
- **LTV (margin-adjusted, 3-year, with NRR):** $4,790 × (1 + 1.10 + 1.21) ≈ $4,790 × 3.31 = **$15,855**.

**Maximum allowable CAC for 3:1 LTV:CAC:**
- Max blended CAC = LTV / 3 = $15,855 / 3 = **$5,285**.

**That sounds generous, but it's gross — must subtract:**
- Sales-rep cost per closed deal (SDR + AE attribution): assume **$2,500/closed deal** (`[TBD-OPERATOR]`).
- Onboarding cost: $300.
- → **Maximum paid-media CAC** = $5,285 − $2,800 = **$2,485 per closed customer**.

**Funnel conversion assumptions (to be measured, not assumed long-term):**

| Stage | Rate | Implied # |
|-------|------|-----------|
| Demo request → SQL | 30% | |
| SQL → Opportunity | 60% | |
| Opportunity → Closed-Won | 25% | |
| **Demo request → Closed-Won (compound)** | **4.5%** | |

**→ Maximum paid CPA per `demo_request` = $2,485 × 4.5% = $112.**

| Channel | Target CPA per demo_request | Target CPA per closed customer | At target | Notes |
|---------|------------------------------|----------------------------------|-----------|-------|
| Google AWS | $100 | $2,222 | ✅ within bound | Highest intent — should be cheapest |
| Google FinOps | $150 | $3,333 | ⚠️ over $2,485 — accept M1 only | Tighten by M2 or kill |
| LinkedIn CTO | $250 | $5,555 | ❌ over — but pipe is bigger ACV | Track ACV mix; CTO leads → enterprise tier `[TBD]` |
| LinkedIn FinOps | $200 | $4,444 | ❌ similar caveat | |
| Bing | $80 | $1,777 | ✅ | |
| Reddit | $50 (assist-credited) | n/a | ✅ as influence | |
| G2/Capterra | $150 | $3,333 | ✅ as BOFU | |

**Reading:** AWS Google + Bing must carry direct payback. LinkedIn must justify itself via larger ACV (mid-market+) — track separately. If CTO LinkedIn leads close at $25K+ ACV, max CPA scales.

## 4. Sensitivity
- If SMB tier is actually $299 (lower): max paid CPA per demo drops to ~$50; only Google AWS & Bing survive.
- If SMB tier is actually $999 + better NRR: max paid CPA per demo rises to $200+; LinkedIn becomes payback-positive directly.
- **→ This model must be re-run within 7 days of operator-confirmed pricing.**

## 5. Reporting cadence
- **Daily:** spend, clicks, conversions per channel — automated dashboard (`analytics/dashboard-wireframe.md`).
- **Weekly:** CPA + LTV:CAC roll-up.
- **Monthly:** budget reallocation decision + post-mortem snapshot per campaign.

## 6. Operator-confirmation TBDs
- `[TBD-OPERATOR]` SMB tier price (assumed $499/mo).
- `[TBD-OPERATOR]` Gross margin (assumed 80%).
- `[TBD-OPERATOR]` Sales-rep cost per closed deal.
- `[TBD-OPERATOR]` Average customer lifetime.
- `[TBD-OPERATOR]` Whether enterprise tier exists and at what ACV (changes LinkedIn math).
