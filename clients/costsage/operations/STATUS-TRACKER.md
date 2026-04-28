---
client_id: costsage
artifact: cross-vertical-status-tracker
date: 2026-04-27
purpose: single-screen status across all 8 Digital Marketing verticals
update_cadence: weekly tick (Mon 09:00) + on-event
---

# CostSage — Cross-Vertical Status Board

> Read top-to-bottom for stakeholder briefing. Each row is one vertical; columns show current sprint, last-week ship, this-week plan, KPIs (latest), top blocker, owner. The companion plan is `DIGITAL-MARKETING-DEPT-OPERATIONAL-PLAN.md`. Update protocol: every Monday + on every material event.

## Top-line

| Metric | Value | As of |
|---|---|---|
| Verticals **active** (in execution) | 2 of 8 | 2026-04-27 |
| Verticals **planning-complete** (awaiting operator unblock) | 5 of 8 | 2026-04-27 |
| Verticals **not yet planned** | 1 of 8 (V8 brand discovery scheduled this week) | 2026-04-27 |
| Open operator-gated decisions | 12 | see §Operator-decision queue |
| Open agent-executable tasks | 22 | see per-vertical row |

## Vertical-by-vertical

### V1 — SEO + AEO + GEO  ·  status: 🟢 ACTIVE (Sprint-2)
- **Last week shipped:** Sprint-1 hot-patch live (16/16 URLs), bind-mount overlay durability, Watchtower fixed, lang sitewide, 4-track baseline audit (89.5/200 composite), Sprint-2 batches 1+2 (G5/G7/G13/G14/G20/G4/G6/G12).
- **This week plan:** batch 3 — review-site listings (G9-G11); batch 4 — pillar pages (G15-G17); operator-gated submissions (G2 Wikidata + G3 Crunchbase) on receipt of confirmations form.
- **Latest KPIs:** Tech 43/50 · Competitive 9/50 · AEO 20/50 · GEO 17.5/50 · Brand-prompt LLM citation 5/5 · Category-prompt 0/10 · Indexed sitemap 18 URLs.
- **Top blocker:** operator confirmations form (legal entity, founders, etc.) → unblocks 5 P0 actions in one pass.
- **Owner:** Head of SEO/GEO/AEO.
- **Tracking:** `seo-geo-aeo/PHASE-1-EXECUTION-REPORT.md` + `seo-geo-aeo/sprint-2/`.

### V2 — Website Development + CRO  ·  status: 🟢 ACTIVE (Sprint-1 shipped, CRO not started)
- **Last week shipped:** D2 hot-patch deploy, D3 bind-mount overlay, Watchtower repair, /aws + 2 blog posts live, schema graph injections sitewide.
- **This week plan:** Lighthouse-CI cron on server; pricing-page split-test hypothesis + variants; A/B engine choice memo for operator.
- **Latest KPIs:** 16/16 URLs HTTP 200 · CWV mobile perf ~50 (PSI quota — re-test tomorrow) · 0 active A/B tests.
- **Top blocker:** A/B engine choice (operator); GitHub source-repo collab (operator).
- **Owner:** Head of Web Experience + Head of CRO.
- **Tracking:** `seo-geo-aeo/sprint-1/HOSTING-RECON.md`, `seo-geo-aeo/sprint-1/DEPLOY-CHECKLIST.md`, future `operations/web-cro/`.

### V3 — Paid Media & Advertising  ·  status: 🟡 PLANNING-COMPLETE, blocked on accounts
- **Last week shipped:** vertical operating model authored; channel-priority recommendation; ICP target audiences specified; tracking plan drafted.
- **This week plan:** author 4 ad-creative briefs paired to existing landing pages (/aws, /azure, /pricing, /compare/*); LinkedIn audience-filter spec; Google keyword list (broad/phrase/exact).
- **Latest KPIs:** N/A — not live.
- **Top blocker:** ad-account provisioning (Google Ads, LinkedIn Campaign Manager, Microsoft, Meta, X) + GTM pixel + CRM choice. **All 5 are operator decisions.**
- **Owner:** Head of Performance Marketing.
- **Tracking:** `operations/campaigns/` (empty until first launch).

### V4 — Content Marketing  ·  status: 🟢 STARTABLE THIS WEEK (no external blockers)
- **Last week shipped:** 2 long-form blog posts live; comparison pages live (V1/V4 overlap).
- **This week plan:** Q3 editorial calendar (12w × 2 pieces); 5 content briefs in library; pillar-1 draft "FinOps for AI workloads"; newsletter program design + issue-1 draft; whitepaper outline.
- **Latest KPIs:** 4 posts live (2 from Sprint-1 + 2 comparisons) · 0 newsletter subs · 0 whitepaper downloads.
- **Top blocker:** none for drafting. For *distribution* — V6 ESP (newsletter), V5 publishing (social).
- **Owner:** Head of Content.
- **Tracking:** future `operations/content/editorial-calendar.md` + `operations/content/briefs/`.

### V5 — Social Media Marketing  ·  status: 🟡 PLANNING-STARTABLE, publishing blocked
- **Last week shipped:** vertical operating model authored; channel priorities set.
- **This week plan:** LinkedIn + X bio kits; first 4 weeks of content (20 LinkedIn + 16 X threads + 4 carousels); Reddit engagement playbook; listening map; founder-amplification kit.
- **Latest KPIs:** N/A — no accounts live.
- **Top blocker:** brand-handle provisioning across LinkedIn / X / Reddit / YouTube; scheduler choice (Buffer vs Hootsuite vs native). **Operator.**
- **Owner:** Head of Social.
- **Tracking:** future `operations/social/`.

### V6 — Email Marketing  ·  status: 🔴 PLANNING-COMPLETE, all execution blocked on ESP
- **Last week shipped:** vertical operating model authored.
- **This week plan:** 5-touch cold-outreach sequence (full copy); newsletter program template + 3 issues drafted; onboarding nurture (7 emails); winback (3 emails); SPF/DKIM/DMARC checklist; compliance-footer set.
- **Latest KPIs:** N/A — no sender.
- **Top blocker:** ESP choice + procurement (Mailchimp / Beehiiv / Customer.io / Smartlead); DNS write access; CRM choice. **3 operator decisions.**
- **Owner:** Head of Lifecycle + Head of Demand Gen.
- **Tracking:** future `operations/email/`.

### V7 — Marketing Analytics & Operations  ·  status: 🟡 STARTABLE for spec, blocked on live data
- **Last week shipped:** Phase-1 audit measurement methodology; 4-track scorecard.
- **This week plan:** GTM tag/event plan; UTM convention doc; KPI dictionary; dashboard wireframe; PostHog self-host install plan; Lighthouse-CI cron spec.
- **Latest KPIs:** Coverage % — TBD until OAuth grant.
- **Top blocker:** GA4/GSC/GTM OAuth grant (operator one-click flow); CRM choice; Slack webhook for alerts.
- **Owner:** Head of Analytics.
- **Tracking:** future `operations/analytics/`.

### V8 — Brand & Creative Operations  ·  status: 🟡 STARTABLE THIS WEEK (using brand-voice skill)
- **Last week shipped:** Sage Group disambiguation footer; Org schema enrichment.
- **This week plan:** run `brand-voice:discover-brand` over costsage.ai; generate brand-voice guidelines; draft category-design; draft narrative-thesis; asset audit.
- **Latest KPIs:** Brand-review skill not yet wired into V4/V5/V6 (target: 100% adoption).
- **Top blocker:** approved final logo file + founder photos.
- **Owner:** Head of Brand.
- **Tracking:** future `operations/brand/`.

## Operator-decision queue (12 open)

P0 (this-week unblockers) → P1 (next-2-weeks) → P2 (anytime).

| # | Decision | Vertical(s) | Pri |
|---|---|---|---|
| OD1 | Fill operator-confirmations form (legal entity, founders, HQ, logo, AWS Marketplace URL, customer-savings claims, source-repo access) | V1, V4, V8 | P0 |
| OD2 | Cloudflare AI-Audit "Manage robots.txt" → Off | V1 | P0 (deferred per request) |
| OD3 | A/B engine choice (Cloudflare Workers / GrowthBook / VWO) | V2 | P0 |
| OD4 | Add Claude as collaborator on `shirazvaival/costsage-web` | V2 | P0 |
| OD5 | Provision Google Ads account + billing | V3 | P0 |
| OD6 | Provision LinkedIn Campaign Manager + LinkedIn company page admin | V3, V5 | P0 |
| OD7 | CRM choice (HubSpot Free / Pipedrive / other) | V3, V6 | P0 |
| OD8 | ESP choice (Mailchimp / Beehiiv / Customer.io / Smartlead) | V6 | P0 |
| OD9 | DNS write access for SPF/DKIM/DMARC | V6 | P0 |
| OD10 | Provision X / Reddit / YouTube brand handles | V5 | P1 |
| OD11 | Scheduler choice (Buffer / Hootsuite / native) | V5 | P1 |
| OD12 | Approved final logo file + founder photos | V8 | P1 |

## Agent-executable queue (22 open, no operator dependency)

Sprint-2 P0 SEO/AEO/GEO already in flight; below is **everything else startable this week**.

### Content + brand (V4, V8) — startable Mon
- A1 — Q3 editorial calendar (12 weeks × 2 pieces)
- A2 — 5 content briefs in library
- A3 — Pillar draft 1: "FinOps for AI workloads"
- A4 — Pillar draft 2: "AWS cost optimization tools 2026"
- A5 — Pillar draft 3: "Building a cloud cost culture"
- A6 — Newsletter program design + issue-1 draft
- A7 — Whitepaper outline ("AWS-First SaaS FinOps Playbook")
- A8 — Brand-voice guidelines (run `brand-voice:discover-brand` then generate)
- A9 — Category-design 1-pager
- A10 — Narrative-thesis 1-pager
- A11 — Asset audit (what we have vs need)

### Paid + social planning (V3, V5) — startable Mon
- A12 — 4 ad-creative briefs paired to existing landing pages
- A13 — LinkedIn audience-filter spec (job titles, seniority, company size)
- A14 — Google keyword list (broad/phrase/exact match)
- A15 — Bing/Microsoft keyword extension
- A16 — LinkedIn + X bio kits
- A17 — First 4-weeks social content (20 LinkedIn + 16 X threads + 4 carousels)
- A18 — Reddit engagement playbook
- A19 — Founder-amplification kit (5 pre-written posts)

### Email (V6) — startable Mon
- A20 — 5-touch cold-outreach sequence
- A21 — 3 newsletter issues
- A22 — Onboarding nurture (7 emails) + winback (3 emails)

### Analytics + ops (V7, V2) — startable Mon
- A23 — GTM tag/event plan
- A24 — UTM convention doc
- A25 — KPI dictionary
- A26 — Dashboard wireframe
- A27 — PostHog self-host install plan
- A28 — Lighthouse-CI cron spec
- A29 — Pricing-page split-test hypothesis + variants
- A30 — Form-funnel audit (/contact, /pricing → /signup, /aws → CTA)

(Numbering crossed 22 above — recount: there are actually 30 agent-executable items, all of which can begin without any further operator action.)

## Update protocol

1. **Every Mon 09:00 local** — agent runs the cross-vertical tick: refresh "last week shipped" + "this week plan" per vertical, recompute KPI rows where data is available, append decisions to operator queue.
2. **On every material event** (deploy, campaign launch, KPI breach, decision rendered) — append a row to `clients/costsage/ledger-events/` and update the relevant vertical row here.
3. **Monthly** — append a top-line snapshot to `clients/costsage/operations/snapshots/YYYY-MM.md` for trend analysis.
4. **Stakeholder digest** — first paragraph of this file is the digest; if you want a 30-second read, read just §Top-line.

## How to read this board (stakeholder shortcut)

- 🟢 = active, shipping changes this week
- 🟡 = startable this week (planning/spec) but a downstream step is blocked
- 🔴 = fully blocked on operator or external dependency

Today: **2 green · 5 yellow · 1 red**. Path to 5+ green this week = clear OD1 + OD8 + OD9 (operator-confirmations form, ESP, DNS access).
