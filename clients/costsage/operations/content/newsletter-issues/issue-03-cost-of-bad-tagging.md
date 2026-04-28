# Bill of Materials — Issue 03

> "The Cost of Bad Tagging"
> Send: Tuesday Q3 W8 • 9:00 ET • From: [TBD-OPERATOR — founder] • Length: ~830 words.
> Subject line: **25–40% of your AWS spend is unallocated. Here's what that costs.**
> Preview text: Why tagging is the most boring high-leverage problem in your bill.

---

## Block 1 — Editor's Note

Tagging is the most boring problem in FinOps and the most expensive one to ignore. I have never met a team that *wanted* to talk about tagging. I have also never seen a meaningful FinOps program survive a year without solving it. So this issue is the short, honest argument for spending a week on tags before you spend a quarter on commitments.

## Block 2 — The Teardown

Here is the math nobody runs.

Take a $200K/mo AWS bill. Assume the cohort-average 25–40% of resources are untagged, partially-tagged, or tagged with a schema that nobody uses. Call it 32% — the midpoint. That is **$64K/mo of spend you cannot allocate to a service, a team, or a product line.**

What does that actually cost you?

**1. You can't rightsize what you can't see.** Rightsizing recommendations require a workload context: who owns it, what SLA it's serving, what traffic shape. Untagged resources don't have that context. You either skip them (leaving the recovery on the table) or you guess (and break something). On 32% of the bill, the missed recovery is typically 6–10% of total spend. On a $200K bill: $12K–$20K/mo, gone.

**2. You can't talk to engineering teams about cost.** Cost-aware culture (Issue 6, coming up) requires that an engineer can see *their* cost. If 32% of the bill is untagged, every engineering conversation about cost has the same caveat: "and a third of it is in some other bucket I can't show you." That caveat kills the conversation every time.

**3. You can't trust your forecast.** If a third of the bill is unallocated, the forecast model is built on a foundation of "and the rest." When the bill spikes, you can't tell the CFO whether it was a known team's roadmap landing or a silent runaway. That's a credibility tax that compounds.

**4. You can't claim Savings Plans intelligently.** Commitment coverage decisions need a reliable baseline by service. Untagged spend pollutes the baseline. Most teams over-correct (under-commit, leaving discount on the table) rather than under-correct (over-commit, taking stranded risk). Either way, the cost is real.

**The fix is not glamorous, but it's tractable in two weeks.**

- **Day 1:** Lock the schema. Five required keys: `Service`, `Owner`, `Environment`, `CostCenter`, `Sunset`. Anything else is optional.
- **Days 2–4:** Backfill the top 50% of resources by spend. This usually covers 85% of the dollars. Use a script; don't try to do this by hand.
- **Days 5–8:** Block creation of new untagged resources. AWS Organizations SCPs, or a Terraform policy gate, or both.
- **Days 9–14:** Run the drift detector. Anything older than 30 days that drifts off-schema gets flagged and (with approval) auto-remediated.

Once the schema is enforced, the value compounds: every other FinOps move (rightsizing, commitments, allocation, retros) gets cheaper to run.

The agent role here is straightforward: detect drift, propose tag values from cost and usage patterns, route approvals to the right service owner. Boring work. Done well, it pays for everything else.

→ [Long version: The True Cost of Untagged Resources](https://costsage.ai/blog/cost-of-bad-tagging)

## Block 3 — One Number

**32%** — the midpoint of untagged or wrongly-tagged spend across our customer cohort in 2026. On a $200K/mo bill, that's $64K/mo you cannot allocate, rightsize confidently, or commit against. [TBD-OPERATOR — confirm cohort number before sending.]

## Block 4 — Three Links

- **AWS Tag Editor** — under-used; combine with bulk operations.
- **AWS Cost Allocation Tags activation guide** — required step most teams skip.
- **FinOps Foundation, "Allocation" capability** — the canonical capability framing.

Internally: tagging is step 1 of our 10-step playbook for a reason — [the playbook](https://costsage.ai/playbook).

## Block 5 — The Ask

Connect AWS to CostSage in under 60 seconds. Within the first minute, the agent reports your tag coverage by spend (not by resource count, which lies). If it's under 75%, that's the place to start — before commitments, before rightsizing, before AI workload audits.

→ [Start your trial](https://costsage.ai/trial)

Or: reply with your current tag schema (just the required-keys list). We'll send back the most common drift modes we see for that shape.

— [TBD-OPERATOR]

---

**Word count: ~830** ✅
**Voice checks:** number-with-unit in B1 ✅ • no banned vocabulary ✅ • CTAs present ✅ • no copilot ✅ • competitor-neutral ✅
