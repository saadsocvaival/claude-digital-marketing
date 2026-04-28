# Whitepaper Outline — "The AWS-First SaaS FinOps Playbook"

> Gated lead-magnet • Length target: 2,500–3,000 words • Format: PDF, designed.
> Owner: Content Lead + PMM • Voice: `operations/brand/voice-guidelines.md`
> v1.0 • 2026-04-28

---

## Premise

The whitepaper is the playbook the CostSage agent runs on every new account, written in the operator's voice. It is gated because the contact captured (work email + company size) is the highest-quality MQL CostSage produces. The piece must read as if it would be useful even if the reader never trials the product — and feel inevitable that they should.

## Target audience reaction (what we want them to feel)

- "This is the most concrete FinOps document I've read this year."
- "These people have run the bill. They know where the bodies are."
- "I'm going to forward this to my VP Eng before I finish reading it."
- "I should probably try this product."

## Lead-gen offer mechanics

- **Form fields:** work email + company size + AWS monthly spend bracket.
- **Promise:** "The 10-step playbook. The one we run on every new customer in their first 90 days."
- **Post-download nurture:** Issue 1 of the newsletter delivered immediately; sales rep alerted on accounts >$100K/mo bracket.
- **Asset bundle inside the PDF:** the playbook + a 1-page printable checklist + a Slack-shareable infographic of the 90-day curve.

---

## Chapter Map

### Front matter (≤200 words)
- Title page: "The AWS-First SaaS FinOps Playbook — The exact 10-step program the CostSage agent runs in your first 90 days."
- Author byline: [TBD-OPERATOR] — likely founder + head of FinOps engineering.
- Two-sentence summary, expected reading time (12 min), version, date.

### Chapter 1 — The 2026 AWS-First SaaS Bill (~300w)
**What it proves:** That the canonical reader's problem is shared by hundreds of similar companies, and the shape of the bill is predictable.
**Reader reaction:** "This is exactly my bill."
**Content:** Composition of a typical $50K–$500K/mo AWS-first SaaS bill (compute 55–65%, data 12–18%, storage 6–10%, networking 4–8%, ML/AI 5–25% and rising). Cite cohort averages with [TBD-OPERATOR] confirmation marks.

### Chapter 2 — Why FinOps-1.0 Stalls (~300w)
**What it proves:** That visibility-only tools cannot move the bill on the timeline that matters.
**Reader reaction:** "Yes — that's why my CloudZero/Vantage didn't work alone."
**Content:** The dashboard era thesis (without naming competitors). The execution gap. The engineer-tax math: a 30-engineer team has ≤2 hours/week available for cost work; the backlog adds 6–10 hours/week.

### Chapter 3 — The 10-Step Playbook (the core, ~1,200w)
**What it proves:** That there is a sequenced, finite, auditable program that takes a typical bill from creep to flat-or-down inside 90 days.
**Reader reaction:** "I can run this on Monday."
**Steps:**
  1. Audit & tag (Days 1–7).
  2. Idle resource cleanup (Days 8–21) — typical recovery 6–10% of total bill.
  3. Compute rightsizing — EC2/RDS (Days 14–35) — recovery 15–22% of EC2.
  4. Storage tiering — S3 lifecycle, EBS gp2→gp3 (Days 21–30) — recovery 30–55% of S3 spend.
  5. Networking diet — NAT, inter-AZ, data egress (Days 28–45) — variable but often $5–20K/mo on a $200K bill.
  6. Commitment coverage — RI / SP, conservative ladder (Days 45–60) — recovery 18–34% of covered compute.
  7. AI workload guardrails (see related pillar) (Days 45–75).
  8. Tag drift remediation as a continuous process (Days 60+).
  9. Unit economics dashboard live to engineering teams (Days 60–90).
  10. Close the loop — agent action enabled with approval flow (Days 75–90).

For each step: what / why / mechanism / typical recovery / common failure mode / agent action.

### Chapter 4 — The 90-Day Curve (~250w)
**What it proves:** That the savings curve is non-linear — fast wins early, structural wins later.
**Reader reaction:** "I can show this to my CFO."
**Content:** Visual of the cumulative savings curve. Week 1 (12–18%), day 30 (22–28%), day 90 (28–35%) on cohort averages. [TBD-OPERATOR] confirm.

### Chapter 5 — The Human-in-the-Loop Architecture (~250w)
**What it proves:** That action does not mean autonomous; trust is non-negotiable.
**Reader reaction:** "Okay, this isn't a 'let an AI loose on prod' pitch."
**Content:** Approval flow, rollback path, confidence scoring, audit trail, ISO certification posture [TBD-OPERATOR confirm exact certs].

### Chapter 6 — Where Most Programs Fail (~250w)
**What it proves:** That CostSage knows the failure modes — pre-empts the reader's skepticism.
**Reader reaction:** "They've thought about this."
**Common failures:** the cost-police anti-pattern, the once-a-quarter review trap, the over-aggressive RI ladder, the orphaned tag schema, the "FinOps as a project not a system" mistake.

### Chapter 7 — Running the Playbook With or Without CostSage (~250w)
**What it proves:** That the playbook is independently valuable; CostSage just runs it faster and continuously.
**Reader reaction:** "These people are honest."
**Content:** Side-by-side estimate — running the playbook with engineering time vs. running it with the agent. Engineer-time cost: 240–400 person-hours over 90 days. Agent-time cost: trial + ~$X/mo (within the ≤10% of recovered savings frame). [TBD-OPERATOR confirm pricing reference.]

### Chapter 8 — What Comes Next (~150w)
**What it proves:** That the program is continuous, not a project.
**Reader reaction:** "We need this as a system, not a sprint."
**Content:** Quarterly cadence after Day 90; how unit economics graduate to a board-level metric; the role of the platform team.

### Conclusion + CTA (~200w)
**Reader reaction:** "I'm starting the trial."
**CTA:** "Connect AWS in under 60 seconds. The agent will surface step-1 audit findings before this PDF closes."

---

## Visual / design notes
- Cover: minimal, brand-locked, one chart (the 90-day savings curve teaser).
- 2 charts (bill composition pie + savings curve).
- 1 architecture diagram (the agent action loop).
- 1 printable checklist (single page, pull-out).
- Chapter pages: full-bleed quote pull-outs from the playbook.

## Voice & length checks
- ≤2,800 words body (excluding front matter).
- All [TBD-OPERATOR] markers resolved before publication.
- Voice-guideline self-check applied chapter-by-chapter.
- Banned vocabulary scan complete.
- Every chapter contains at least one number with unit + timeframe.

## Distribution map (V5 + V6)
- **V5:** Gated landing page; LinkedIn organic announcement (5 posts in launch week); X thread; HackerNews Show; FinOps Foundation Slack #playbook channel; AWS partner newsletter mention [TBD-OPERATOR if available].
- **V6:** Newsletter Issue 1 lead links to the gate; subsequent issues drop chapter excerpts in link block.

## Success metrics (90-day)
- 5,000 downloads.
- 200 trial signups attributed.
- ≥30 SQLs from accounts in $100K+/mo bracket.
- ≥3 inbound podcast invites referencing the playbook.
