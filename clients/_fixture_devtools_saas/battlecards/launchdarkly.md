# Battlecard — Loopgate vs LaunchDarkly

> Rubric: `/rubrics/battlecard.yaml`. Last reviewed: 2026-04-23. Cadence: quarterly.

## Cheat Card
- **They are:** the enterprise incumbent. Broad features, high price (~$180k/yr at 100 seats). Experimentation is a bolt-on.
- **When we win:** mid-market budget constraints, teams wanting flags+experiments unified, teams migrating from homegrown and wanting "LD features at 1/3 price".
- **When they win:** F500 procurement, global rollout with on-prem multi-region, accounts where incumbent relationship is entrenched.
- **3 discovery Qs:**
  1. "What does your current flag system cost you across tool+engineering-time?"
  2. "Where do flags and experiments talk to each other today?"
  3. "What did your last SOC2 auditor ask about feature flags?"
- **Top objection + rebuttal:** "LD is the safe enterprise pick" → "Agreed for F500. For mid-market, the TCO gap is 3×, our audit trail is at parity, and our migrator runs in a weekend. Here's the comparison." → send calculator.

## Full Card

### Who they are
Founded 2014. Enterprise feature-management incumbent. IPO'd/private stage (per public filings as of 2025). Broad product depth: flags, experiments, remote config, migration assistants, observability hooks. Primary ICP: F500 + large enterprise. Pricing opaque beyond "Starter"; typical Pro tier at 100 seats lands ~$180k/yr per public procurement records.

### Why they win (honest)
1. **Breadth.** They have every feature we (and everyone) could want. No feature gap blocks them.
2. **Brand safety.** "Nobody got fired for buying LaunchDarkly" at F500 scale.
3. **Global + on-prem maturity.** Multi-region + on-prem options battle-tested at scale.

### Why we win
1. **Unified flags + experiments** on one audit trail — LD experimentation is a newer bolt-on; permissions + audit split between the two surfaces at customer sites.
2. **Price-to-value at mid-market.** Public pricing, ~1/3 TCO at 100 seats. Short sales cycle, CFO-friendly.
3. **Turnkey LD migrator.** Drop-in API compat for the SDK, a migrator for flag definitions, parallel-run mode. We've done 2 migrations in <1 week.

### Trap-setting discovery questions
1. "How long did your last LD procurement take, end-to-end?" (surfaces cycle-time pain)
2. "When Product wants an experiment, who owns the flag and who owns the stats?" (surfaces 2-tool split)
3. "What does LD charge you per seat today, after the volume discount?" (surfaces TCO)
4. "How much custom tooling have you built around LD audit logs?" (surfaces gap)
5. "If you had to swap LD in 2 quarters, what would be the hardest part?" (surfaces lock-in concern we can address)

### Objection library
| They say | Root concern | Rebuttal | Proof |
|---|---|---|---|
| "LD is proven at scale" | Vendor risk | We're Series B with named lead; OSS core means no lock-in; public benchmarks | Architecture page, GitHub, benchmarks |
| "Switching cost is too high" | Migration pain | Turnkey migrator, API compat, parallel-run | Migration guide + 2 case studies |
| "Our LD contract is annual" | Timing | Run parallel in non-critical service for 1 quarter, switch at renewal | Deployment pattern doc |
| "LD has more features" | FOMO | Map the features you actually use; coverage ≥95% at 1/3 the price | Comparison calc |
| "Your audit log is just a log" | Compliance depth | SOX-grade change log, SOC2 Type II (audit 2026-05), exportable to SIEM | Trust center |

### Switch playbook (migrating from LD)
1. Inventory flags via LD export.
2. Map targeting rules to Loopgate via migrator (idempotent).
3. Enable parallel-run mode: both systems evaluate; diff-log in Loopgate. Run 2 weeks.
4. Cut over at renewal. Keep LD read-only for 30d as insurance.
Known landmines: custom webhooks, bespoke attribute resolvers — migrator covers 90%; bespoke needs 0.5d of eng time.

### Landmines (walk-away)
- F500 with global on-prem multi-region as hard requirement AND active LD relationship: long, losing cycle. Walk.
- Account where LD CSM is embedded in weekly eng ops — too entrenched.
- 18-month procurement org: we're not tuned for it.

### Intel sources
- LD pricing: public + procurement-data leaks (Vendr reports, 2025)
- Feature coverage: public docs review 2026-04
- Gong call clips where prospects described LD pricing pain
- G2 review mining (LD + Loopgate) for comparative sentiment
