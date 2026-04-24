# Content Outlines — Q2 Top 10 Pieces

Each outline: query/hook, target persona × funnel, headline, lead (first 100 words), outline, hook-lines, proof/data required, CTA, 1→10 repurpose plan.

---

## 1. "Why your flag table is eating 0.6 engineers" (Pillar TOFU)
- **Persona/funnel:** Priya, TOFU
- **Headline:** Why your flag table is eating 0.6 engineers — and what to do about it
- **Lead:** We interviewed 40 platform leads about what their homegrown feature-flag systems actually cost. The median: 0.6 FTE of ongoing maintenance — before counting audit gaps or the 2am incident when a stale flag flips. In 2026-full-loaded engineer dollars, that's $132k/yr. Most CFOs would budget $132k/yr for a dev tool. Nobody budgets it for "the flag table we built in 2021." Here's the math, the methodology, and what actually changes if you consolidate.
- **Outline:** What we measured → how (method + interview count) → the 4 cost buckets → why it compounds at 100+ engineers → when to buy vs build → calc embed → FAQ
- **Required proofs:** Interview count (40), raw FTE distribution chart, fully-loaded cost formula, 3 anonymized customer quotes.
- **CTA:** Run the TCO calculator.
- **Repurpose:** LI long-post, X thread, YouTube 8-min talk, podcast pitch 3 shows, newsletter, Reddit top-comment (non-promotional), sales email nugget, HN discussion, Slack-community share, webinar section.

---

## 2. "Sub-50ms flag evaluation: benchmarks vs LaunchDarkly and Statsig" (Technical TOFU → HN)
- Persona: Marco.
- Lead: Numbers first, narrative second. p95 eval across 3 SDKs on identical hardware: LD 78ms, Statsig 62ms, Loopgate 47ms. Methodology published, repo linked, re-runnable by you.
- **Key proof:** public benchmark repo + methodology. Numbers dated.
- **CTA:** Clone the repo, run it.
- **Repurpose:** HN submission, GitHub pinned repo, talk proposal KubeCon, podcast clip, newsletter, Twitter/X data viz, LI carousel.

---

## 3. "SOC2 and feature flags: what auditors actually ask"
- Persona: Priya. Funnel: TOFU → MOFU.
- **Lead:** After 3 SOC2 audits with customers, here are the 4 questions auditors consistently ask about feature flags — and how teams fail them.
- **Key proof:** 4 real (anonymized) audit questions; checklist download; compliance-page link.
- **CTA:** Download SOC2 readiness checklist.

---

## 4. "The Loopgate Migrator: from LaunchDarkly in a weekend" (Case + tool)
- Persona: Priya. Funnel: BOFU.
- Lead: Marketplace Y completed their LD-to-Loopgate migration over a weekend. 340 flags. 12 services. Parallel-run mode caught 3 rule-definition bugs before cutover. Here's exactly how.
- **CTA:** Book a migration walkthrough.

---

## 5. "Feature flags + experimentation: why they should live together"
- Persona: Priya + Rina. Funnel: TOFU.
- **Thesis:** When flags and experiments split tools, the same release decision has two sources of truth. That's the root cause of most "wait — is that feature on?" incidents.

---

## 6. "Homegrown feature flags TCO calculator" (Interactive tool)
- **Build:** Inline calculator on LP + standalone page.
- **CTA:** Email results.

---

## 7. "Platform Engineering Quarterly: 2026-Q2 Trends"
- Persona: Priya. Brand TOFU.
- **Thesis + data:** 3 trends (platform consolidation, audit pressure, DORA going boardroom). Cite DORA 2025, Gartner 2025, Platform Engineering Survey (Puppet).

---

## 8. "RFC Template: Adopting a Feature-Flag Platform" (Open artifact)
- Persona: Marco.
- **Deliverable:** GitHub repo with a working RFC template + example filled-in RFC.

---

## 9. "p95 Eval Latency Explained: why it matters in request paths"
- Persona: Marco.
- **Deliverable:** Deep technical, code samples.

---

## 10. "Feature-flag Cleanup: the 90-day Protocol"
- Persona: Marco.
- **Deliverable:** Playbook + repo with a cleanup audit script.

Every outline gates through: brand voice ≥8, SEO brief compliance, legal for competitor claims, analytics for event wiring on each CTA.
