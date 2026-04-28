# Newsletter Issue 02 — RIs vs Savings Plans, 2026 Update

**Subject A:** RIs vs Savings Plans — what changed in 2026
**Subject B:** Stop committing to peak.
**Preview text:** The decision tree we walk customers through, refreshed for 2026.
**UTM campaign slug:** `nl-issue-02-ri-sp-2026`

---

## Block 1 — Hook

"Should we buy RIs or Savings Plans?" is the wrong question.

The right question — the one that determines whether you save 30% or burn 12% — is: how predictable is your compute mix over the next 12 months?

We're refreshing our RI vs SP decision tree for 2026, factoring in [TBD-OPERATOR — confirm 2026 AWS pricing changes if any]. Below: the tree, the three traps, and what to do this week.

---

## Block 2 — Deep dive

**The decision tree.**

1. *Workload locked to a single instance family for 12+ months?* → Standard RI. Best discount (up to ~72% with 3yr all-upfront), least flexible.
2. *Mix shifts across families/regions?* → Compute Savings Plan. ~28–66% discount range, much more flexible.
3. *Fargate or Lambda dominant?* → Compute SP, full stop. RIs don't apply.
4. *Spiky workload?* → Commit to your *floor*, not your peak. On-demand handles the spikes.

**The three traps that don't go away.**

*Trap 1 — committing to peak.* The single most expensive default in FinOps. Teams look at last month's max and commit to it; every hour below that is guaranteed waste. The math: if peak is 1.8x trough and you commit to peak, you're carrying ~40% over-coverage as long as the workload is steady-state below peak.

*Trap 2 — region drift.* You bought a 1-yr SP in us-east-1; six months in, the team migrated the workload to us-west-2 for latency. The SP doesn't follow. Either modify the workload migration plan to preserve coverage or accept that the remaining commit is sunk cost — but *count* it as such, don't hide it.

*Trap 3 — family drift on non-convertible commits.* Standard RIs lock you to a family. The minute AWS launches m6i (better $/perf than m5), you're stuck either eating the loss or paying for two layers of capacity. Convertible RIs cost ~5–10% in discount but preserve flex; on a 3-yr term, that's almost always the right trade.

**The 90% rule.** Whatever you commit to, re-check utilization weekly. Below 90% sustained, your effective discount has dropped enough that you should consider modifying or letting it expire vs renewing. Below 76%, you're net-negative vs on-demand on that hour.

Full decision-tree write-up: costsage.ai/blog/ri-vs-savings-plans?utm_source=email&utm_medium=newsletter&utm_campaign=nl-issue-02-ri-sp-2026&utm_content=block2

---

## Block 3 — Tactical tip

**Tip: pull SP utilization for the last 90 days *today*.**

In Cost Explorer → Savings Plans → Utilization Report → 90-day window. If sustained <90%, you have one of three problems (under-utilization, region drift, or family drift) and need to fix the underlying issue, not buy more.

The 30-min version of this audit is the highest-ROI half hour most FinOps practitioners can spend this quarter.

---

## Block 4 — Community

The FinOps Foundation publishes a State of FinOps report annually — the 2026 edition is worth the read for benchmarking your team's maturity. ([TBD-OPERATOR — link.])

Reader (paraphrased): *"Should we ladder our SP commits or buy one big one?"* — Ladder. Same total commit, three different start dates (e.g., quarterly), so you never have one giant renewal cliff and you get to recalibrate quarterly with current data.

---

## Block 5 — CTA

We built CostSage to flag SP utilization drift the *week* it happens, not at renewal. If you want the 90-day decomposition done on your account, run the audit:

→ costsage.ai/aws?utm_source=email&utm_medium=newsletter&utm_campaign=nl-issue-02-ri-sp-2026&utm_content=cta

— {{sender_first}}
Founder, CostSage

---

[Footer per compliance-footers.md]
