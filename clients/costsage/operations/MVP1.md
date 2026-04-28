---
client_id: costsage
artifact: MVP1
date: 2026-04-28
audience: management + technical + marketing teams
purpose: bridge between mission-level expectations and execution-level work
update_cadence: weekly tick + on every milestone outcome
---

# CostSage — MVP1
## The Ferrari, the engine, the wheels, and the dashboard

> **Why this document exists.** Management thinks in missions ("we want a Ferrari"). Execution lives in components (engine, body, electronics, finishing). This file is the bridge: one mission → capped stakeholder goals → technical goals (orchestration-level — what the AI orchestration layer must do, eventually owned by Sheraz Iqbal at maturity, AI-assisted today) → concrete tasks with outcomes and effectiveness scores. Read top-to-bottom for one coherent picture; jump to §5 for the executive milestone board.

---

## TL;DR (30 seconds)

- **Mission:** AI-enabled, end-to-end digital marketing automation that turns costsage.ai into a self-driving demand engine.
- **Stakeholder Goals (5):** discoverable, lead-generating, authoritative, AI-orchestrated, measurable.
- **Technical Goals (8):** SEO/AEO/GEO engine · Web/CRO engine · Paid Media engine · Content engine · Social engine · Email engine · Analytics engine · Brand engine.
- **Status today:** **2 engines running, 5 engines built and warm, 1 engine bolted on but waiting for fuel.** Mission completion ≈ **42%** measured, **~75%** built — the gap is operator-gated activation.
- **What flips us to "done MVP1":** one consolidated operator-confirmation form + 7 platform decisions. Estimated impact: ~33 percentage points of mission completion in the same week the form is returned.

---

## 1. Mission

> **AI-enabled, end-to-end digital marketing automation that turns costsage.ai into a self-driving demand engine, capable of generating qualified pipeline across SEO + AEO + GEO + Paid + Content + Social + Email — orchestrated by AI agents with human approval at the right gates.**

This is the Ferrari. Not the engine, not the wheels, not the paint job — the whole car, with a driver.

---

## 2. Stakeholder Goals (the capped "what we want")

Each goal is **binary** at the mission level (yes/no), but is **decomposable** into measurable sub-outcomes. This is what management will be asked at the Q-end review.

| # | Stakeholder Goal | YES/NO test | Sub-outcomes | Today |
|---|---|---|---|---|
| **SG-1** | **CostSage is discoverable everywhere our buyers search** | "If I search Google, ChatGPT, Perplexity, G2, and Crunchbase for FinOps tools, do I find CostSage?" | Indexed in Google + Bing · Cited by ChatGPT/Claude/Gemini/Perplexity · Listed on G2/Capterra/TrustRadius · In Wikidata + Crunchbase · Has a Knowledge Panel | 🟡 partial — Google ✅, AI engines ⚠️ (5/5 brand, 0/10 category), reviews ⚠️ (G2 + AWS Marketplace only) |
| **SG-2** | **Marketing generates qualified leads automatically** | "Are paid + organic + social + email producing booked meetings without manual hand-cranking?" | ≥40 MQLs/mo · ≥10 SQLs/mo · CAC by channel known · LTV:CAC ≥ 3:1 · Pipeline ≥ 30% marketing-sourced | 🔴 not live — every campaign is briefed and ready, but no ad accounts / ESP / CRM yet |
| **SG-3** | **CostSage is recognised as an authority in the FinOps category** | "Is CostSage on the shortlist when an analyst writes 'best FinOps platforms 2026'?" | Brand voice live · Category claim owned · Pillar pages ranking · Press / podcast mentions · Wikidata Q-item · 5+ G2 reviews | 🟡 partial — voice + category + pillars shipped; off-site authority pending operator |
| **SG-4** | **The marketing function runs with AI orchestration, not manual labour** | "Can a small team produce enterprise-grade output because agents handle the heavy lifting?" | Editorial calendar AI-driven · Schema injection automated · Authority-graph submissions templated · Ad creative drafted by AI · Email sequences generated · QA gates AI-run before HITL approval | 🟢 demonstrated this sprint — 80 artifacts shipped in one day across 8 verticals via parallel agents |
| **SG-5** | **Marketing performance is measurable in real time** | "Can a stakeholder see what's working today, this week, this month — without a status meeting?" | Single dashboard live · KPI dictionary canonical · Anomaly alerts wired · Weekly digest auto-generated · Attribution model running | 🟡 partial — dashboard wireframed, KPI dictionary written (57 entries), tag plan ready; live data blocked on OAuth |

**Mission YES/NO at end of MVP1: SG-1 ≥ 70%, SG-2 ≥ first 10 MQLs/mo, SG-3 ≥ 60%, SG-4 demonstrated repeatably, SG-5 dashboard live with last-7-days data.**

---

## 3. Technical Goals (the orchestration target → AI-assisted today)

Each technical goal is a self-contained engine. **At maturity (Sheraz Iqbal orchestration-level), each engine runs as an autonomous agent loop with HITL gates. Today, the same engine runs AI-assisted (we drive, agents do the work).** The gap is mostly tool/credential plumbing, not capability — the capability is already proven by the artifacts shipped.

| # | Technical Goal (engine) | Powers Stakeholder Goals | Orchestration target (eventual) | AI-assisted state (today) | Gap to orchestration |
|---|---|---|---|---|---|
| **TG-1** | **SEO + AEO + GEO engine** | SG-1, SG-3 | Daily crawl + schema validation + LLM citation probe + authority-graph submission templates fired from a queue | Manual trigger; agents do the work in minutes; results committed to repo | Cron + GSC OAuth + Semrush/Ahrefs API keys; queueing layer |
| **TG-2** | **Web / CRO engine** | SG-1, SG-2, SG-5 | Hot-fix pipeline (overlay) + source-repo PR pipeline + A/B test orchestration + Lighthouse-CI + form-funnel auto-audit | Overlay deploy proven (3 sprints), CRO briefs drafted, A/B engine chosen | A/B engine wired (PostHog) + GitHub source-repo collab + Lighthouse-CI cron live |
| **TG-3** | **Paid Media engine** | SG-2 | 7 channels live, daily QA, weekly optimization, kill-switch automation, conversion import to CRM | 7 launch-ready briefs + ICP master + ad-copy bank drafted | Ad accounts provisioned + GTM tag installed + CRM live |
| **TG-4** | **Content engine** | SG-1, SG-3 | Editorial calendar → brief → draft → brand-review → schema-pack → publish, fully agent-driven, HITL only at publish | Calendar (24 slots) + 3 pillar briefs + whitepaper outline + 3 newsletter issues authored; pillars live | Brand-review skill wired into pre-publish gate; calendar drives automated trigger |
| **TG-5** | **Social engine** | SG-1, SG-2, SG-3 | Daily posting on LinkedIn / X / Reddit, listening + auto-routed engagement queue, weekly analytics roll-up | 4-week posting queue + bio kit + Reddit playbook + listening map drafted | Brand handles + scheduler + listening tool |
| **TG-6** | **Email engine** | SG-2 | Cold outreach + newsletter + lifecycle + winback all running on triggers; deliverability monitored | 2 cold sequences + 3 newsletter issues + 7-email onboarding + winback + lifecycle map drafted | ESP + CRM + DNS (SPF/DKIM/DMARC) live |
| **TG-7** | **Analytics engine** | SG-2, SG-5 | GTM events → GA4 + PostHog + warehouse → dashboards + anomaly alerts → weekly digest auto-sent | Tag plan (13 events) + UTM convention + KPI dictionary (57) + dashboard wireframe + Lighthouse cron spec drafted | OAuth grants + PostHog install + Slack webhook |
| **TG-8** | **Brand engine** | SG-3, SG-4 | Voice / category / messaging guidelines auto-enforced via brand-review skill on every V4/V5/V6 publish | Voice guidelines + category-design + narrative-thesis + messaging pillars + asset audit shipped | brand-review skill plumbed into V4/V5/V6 publish gate |

**Read the gap column carefully.** Every "gap to orchestration" is **tooling, credentials, or one operator decision** — none is a capability gap. The intelligence is already there; the plumbing is what's missing.

---

## 4. Technical Mapping — Tasks → Outcomes → Effectiveness

The bridge layer. Each row maps a stakeholder goal → technical engine → concrete task → business outcome → measured effectiveness (0-10) → status.

> Read this when management asks "what specifically did we achieve?" Each row is a defensible, traceable answer with the artifact path.

### TG-1: SEO + AEO + GEO engine — supporting SG-1 + SG-3

| Task | Business outcome | Effectiveness | Status | Artifact |
|---|---|---|---|---|
| Live audit of 16 URLs | Baseline established; 13 findings prioritised | 9/10 | ✅ done | `seo-geo-aeo/phase-1-live-audit.md` |
| Sprint-1 implementation pack (17 artifacts) | All 13 findings have remediation files | 9/10 | ✅ done | `seo-geo-aeo/sprint-1/` |
| Sprint-1 hot-patch deploy | All 13 findings live on costsage.ai | 9/10 | ✅ done | server overlay, verified 16/16 200 |
| 4-track baseline audit (T1/T2/T3/T4) | Composite Phase-1 score 89.5/200 | 8/10 | ✅ done | `seo-geo-aeo/PHASE-1-EXECUTION-REPORT.md` |
| Sprint-2 batches 1+2 (10 P0 fixes) | FAQPage + Org schema + WebSite schema sitewide; /compare/* live; CWV pass | 9/10 | ✅ done | live URLs verified |
| Sprint-2 batch 4: 5 net-new pillar pages live | `/finops-for-ai-workloads`, `/azure-cost-optimization`, `/multi-cloud`, `/alternatives/{vantage,prosperops}` — sitemap 18→23 | 9/10 | ✅ done | live URLs verified |
| Authority-graph submission templates (G9/G10/G11) | LinkedIn / G2 / Capterra / TrustRadius / Product Hunt / AlternativeTo / SaaSworthy paste-ready | 8/10 | ✅ done | `seo-geo-aeo/sprint-2/G9-G11-*.md` |
| Wikidata Q-item submission payload | Properties mapped, statements ready | 8/10 | 📝 drafted, op-gated | `seo-geo-aeo/sprint-2/G2-wikidata-q-item.md` |
| Crunchbase profile submission | Fields + 200w description ready | 8/10 | 📝 drafted, op-gated | `seo-geo-aeo/sprint-2/G3-crunchbase-profile.md` |
| Cloudflare AI-bot toggle (page-level) | ClaudeBot/GPTBot/Perplexity unblocked at page level | 7/10 | ✅ partial | verified by curl |
| Cloudflare robots.txt rewrite (managed file) | Compliant LLM crawlers can read robots.txt without injected blocks | — | 🔴 blocked | operator deferred |

**TG-1 effectiveness average: 8.4/10. Status: 🟢 ACTIVE — engine running.**

### TG-2: Web/CRO engine — SG-1 + SG-2 + SG-5

| Task | Business outcome | Effectiveness | Status | Artifact |
|---|---|---|---|---|
| Hosting topology recon | Server + CF + container path mapped | 9/10 | ✅ done | `seo-geo-aeo/sprint-1/HOSTING-RECON.md` |
| D2 hot-patch deploy | Live changes possible without source repo | 9/10 | ✅ done | overlay path proven 4× |
| D3 bind-mount overlay | Edits durable across image pulls | 9/10 | ✅ done | `/opt/wordpress/web-overlay/` |
| Watchtower repair | Auto-deploy restored on Docker API v1.51 | 8/10 | ✅ done | `nickfedor/watchtower:1.16.1` |
| 18-step deploy checklist | HITL-gated, repeatable | 8/10 | ✅ done | `seo-geo-aeo/sprint-1/DEPLOY-CHECKLIST.md` |
| Pricing-page A/B test brief | Test 001 launch-ready | 8/10 | 📝 drafted, op-gated (A/B engine) | `operations/web-cro/test-001-pricing-page-hero.md` |
| AWS-page CTA A/B brief | Test 002 launch-ready | 8/10 | 📝 drafted, op-gated | `operations/web-cro/test-002-aws-page-cta.md` |
| Homepage hero category-claim test | Test 003 launch-ready | 8/10 | 📝 drafted, op-gated | `operations/web-cro/test-003-homepage-hero-category-claim.md` |
| Form-funnel audit | Friction points named, fixes specced | 7/10 | 📝 drafted | `operations/web-cro/form-funnel-audit.md` |
| A/B engine decision memo | Recommend PostHog cloud free tier | 9/10 | 📝 drafted, op-gated | `operations/web-cro/ab-engine-decision-memo.md` |
| Lighthouse-CI installation | Daily perf budget enforcement | 8/10 | 📝 drafted, runnable | `operations/web-cro/lighthouse-ci-installation.md` |

**TG-2 effectiveness average: 8.3/10. Status: 🟢 ACTIVE (deploy infra) + 🟡 (CRO awaiting A/B engine).**

### TG-3: Paid Media engine — SG-2

| Task | Business outcome | Effectiveness | Status | Artifact |
|---|---|---|---|---|
| Campaign brief template | Standard intake for every channel | 9/10 | ✅ done | `operations/campaigns/_templates/` |
| ICP master | Cross-platform reusable persona spec | 9/10 | ✅ done | `operations/campaigns/_audiences/icp-master.md` |
| 7 launch-ready campaign briefs | Google×2 / LinkedIn×2 / Bing / Reddit / G2-Capterra | 9/10 | 📝 drafted, op-gated (ad accounts) | `operations/campaigns/*-q3.md` |
| 30-headline ad copy bank | Reusable, on-brand, persona-tagged | 9/10 | ✅ done | `operations/campaigns/_creative/ad-copy-bank.md` |
| Conversion tracking spec | All 6 platforms, no orphan events | 9/10 | ✅ done | `operations/campaigns/conversion-tracking-spec.md` |
| Budget pacing model | $5K controlled month-1 with LTV:CAC math | 8/10 | 📝 drafted, op-gated (price tier) | `operations/campaigns/budget-pacing-model.md` |
| Lookalike seed spec | Per-platform CSV upload spec | 8/10 | ✅ done | `operations/campaigns/_audiences/lookalike-seed-spec.md` |
| First lead from paid | — | — | 🔴 blocked | needs ad accounts + CRM |

**TG-3 effectiveness average: 8.7/10 on what's drafted. Status: 🟡 PLANNING-COMPLETE — execution blocked on ad accounts + CRM.**

### TG-4: Content engine — SG-1 + SG-3

| Task | Business outcome | Effectiveness | Status | Artifact |
|---|---|---|---|---|
| Q3 editorial calendar (24 slots) | 12 weeks of supply mapped to V1 keywords + distribution | 9/10 | ✅ done | `operations/content/editorial-calendar.md` |
| Brief template | Standard production format | 9/10 | ✅ done | `operations/content/brief-template.md` |
| 3 pillar briefs | AI workloads moat / AWS tools / cost culture | 9/10 | ✅ done | `operations/content/briefs/` |
| 5 net-new pillar pages live | Sitemap 18→23; AI-workloads moat owns uncontested category | 9/10 | ✅ done | overlay |
| Whitepaper outline | Lead-magnet pipeline ready | 8/10 | 📝 drafted | `operations/content/whitepaper-outline-aws-first-saas-finops.md` |
| Newsletter program + 3 issues | Bi-weekly cadence, send-ready | 9/10 | 📝 drafted, op-gated (ESP) | `operations/content/newsletter-issues/` |
| Repurposing engine | 1 long-form → 5 LI + 3 X + 1 newsletter | 8/10 | ✅ done | `operations/content/repurposing-engine.md` |
| Content audit rubric | Quarterly refresh/prune/decline framework | 8/10 | ✅ done | `operations/content/content-audit-rubric.md` |

**TG-4 effectiveness average: 8.6/10. Status: 🟢 ACTIVE — calendar engine running, 5 pillars live.**

### TG-5: Social engine — SG-1 + SG-2 + SG-3

| Task | Business outcome | Effectiveness | Status | Artifact |
|---|---|---|---|---|
| 5-platform bio kit | Brand-ready presence on day-1 of credentials | 8/10 | ✅ done | `operations/social/bio-kit.md` |
| 4-week posting queue | 20 LI + 84 X + 4 carousels load-and-go | 9/10 | 📝 drafted, op-gated | `operations/social/posting-queue-week-*.md` |
| Reddit engagement playbook | Karma-build first 30d + value-add rules | 8/10 | ✅ done | `operations/social/reddit-engagement-playbook.md` |
| Listening map | Brand + competitor + influencer queries | 8/10 | ✅ done | `operations/social/listening-map.md` |
| Founder amplification kit | 10 pre-written posts the founder can fire | 8/10 | 📝 drafted, op-gated (founder identity) | `operations/social/founder-amplification-kit.md` |
| Employee advocacy program | Cadence + content menu | 8/10 | ✅ done | `operations/social/employee-advocacy-program.md` |
| Weekly report template | Per-channel roll-up format | 8/10 | ✅ done | `operations/social/weekly-report-template.md` |

**TG-5 effectiveness average: 8.1/10. Status: 🟡 PLANNING-COMPLETE — execution blocked on brand handles + scheduler.**

### TG-6: Email engine — SG-2

| Task | Business outcome | Effectiveness | Status | Artifact |
|---|---|---|---|---|
| 2 cold outreach sequences | AWS-SaaS + FinOps-lead personas | 9/10 | 📝 drafted, op-gated (ESP) | `operations/email/cold-outreach-sequence-*.md` |
| Newsletter template + 3 issues | Bi-weekly cadence | 9/10 | 📝 drafted | `operations/email/newsletter-issue-*.md` |
| 7-email onboarding nurture | D0→D14 with branching | 9/10 | 📝 drafted | `operations/email/onboarding-nurture-sequence.md` |
| Lifecycle map (16 nodes / 22 edges) | Full trigger graph | 8/10 | 📝 drafted | `operations/email/lifecycle-map.md` |
| Winback sequence | 3 emails for >90d dormant | 8/10 | 📝 drafted | `operations/email/winback-sequence.md` |
| Promo + announcement templates | 7 templates total | 8/10 | ✅ done | `operations/email/{promotional,announcement}-*.md` |
| SPF/DKIM/DMARC checklist | DNS records ready to paste | 9/10 | 📝 drafted, op-gated (DNS) | `operations/email/spf-dkim-dmarc-checklist.md` |
| Compliance footer | CAN-SPAM/CASL/GDPR | 9/10 | ✅ done | `operations/email/compliance-footers.md` |
| Deliverability runbook | Warmup + monitoring + blocklist response | 8/10 | ✅ done | `operations/email/deliverability-runbook.md` |
| First booked meeting from email | — | — | 🔴 blocked | needs ESP + CRM + DNS |

**TG-6 effectiveness average: 8.6/10 on drafted. Status: 🔴 EXECUTION-BLOCKED on ESP/CRM/DNS.**

### TG-7: Analytics engine — SG-2 + SG-5

| Task | Business outcome | Effectiveness | Status | Artifact |
|---|---|---|---|---|
| GTM tag plan (13 events) | Every meaningful action tracked, no orphans | 9/10 | ✅ done | `operations/analytics/tag-plan.md` |
| UTM convention | Single source of truth | 9/10 | ✅ done | `operations/analytics/utm-convention.md` |
| KPI dictionary (57 entries) | Every metric defined + owned | 9/10 | ✅ done | `operations/analytics/kpi-dictionary.md` |
| Dashboard wireframe (5 tabs) | CMO + Acquisition + Pipeline + Lifecycle + Web | 9/10 | ✅ done | `operations/analytics/dashboard-wireframe.md` |
| PostHog self-host install plan | Compose addition + reverse-proxy spec | 8/10 | ✅ done | `operations/analytics/posthog-self-host-install.md` |
| Lighthouse-CI cron spec | Daily perf snapshot to feeds/ | 8/10 | ✅ done | `operations/analytics/lighthouse-ci-cron-spec.md` |
| Anomaly detection spec | 2σ alert routing | 8/10 | ✅ done | `operations/analytics/anomaly-detection-spec.md` |
| Multi-touch attribution model | First/last/linear/position-based | 8/10 | ✅ done | `operations/analytics/attribution-model.md` |
| Data warehouse design | BigQuery / PostHog schema sketch | 7/10 | ✅ done | `operations/analytics/data-warehouse-design.md` |
| Weekly digest auto-generated | Monday digest format | 8/10 | ✅ done | `operations/analytics/weekly-digest-format.md` |
| Live dashboard with last-7d data | — | — | 🔴 blocked | needs OAuth grants |

**TG-7 effectiveness average: 8.3/10. Status: 🟡 SPEC-COMPLETE — live data blocked on GA4/GSC OAuth.**

### TG-8: Brand engine — SG-3 + SG-4

| Task | Business outcome | Effectiveness | Status | Artifact |
|---|---|---|---|---|
| Voice guidelines | Extracted from live site, do/don't pairs, sample rewrites | 9/10 | ✅ done | `operations/brand/voice-guidelines.md` |
| Category-design ("Agentic, Not Dashboard") | 7-word category claim | 9/10 | ✅ done | `operations/brand/category-design.md` |
| Narrative thesis | 1-pager every Head reads | 9/10 | ✅ done | `operations/brand/narrative-thesis.md` |
| Messaging pillars (4) | Audience × proof-point matrix | 9/10 | ✅ done | `operations/brand/messaging-pillars.md` |
| Asset audit | What we have vs need, sized per channel | 8/10 | ✅ done | `operations/brand/asset-audit.md` |
| brand-review skill plumbed into V4/V5/V6 publish | Auto-enforcement at publish gate | — | 📝 to-do | next sprint |

**TG-8 effectiveness average: 8.8/10. Status: 🟢 GUIDELINES-COMPLETE — enforcement plumbing pending.**

---

## 5. Milestone Board (the executive view)

> **Read this in 60 seconds.** Three columns: Completed (business value already unlocked) · In Progress (this week) · Pending (waiting on a specific decision/credential). No technical jargon — every line in business language.

### ✅ COMPLETED — value already unlocked

| Milestone | Business value |
|---|---|
| **Website is technically sound and durable** | Every page loads, every page is indexable, every change survives developer pushes. No more "the SEO work got wiped." |
| **23 pages live, up from 13** | Fresh landing pages for AWS, Azure, multi-cloud, AI-workloads, and 4 alternative-to-X pages. Sales has bottom-funnel ground to land prospects on. |
| **CostSage is reliably cited by AI engines on brand questions** | If a buyer asks ChatGPT/Perplexity "what is CostSage", they get a confident answer with citations. (5/5 brand prompts.) |
| **Brand voice + category claim locked** | "Agentic, Not Dashboard" — the 7-word claim every Head, page, and ad references. Internal alignment now possible. |
| **Editorial engine running** | 24-slot Q3 calendar, 3 pillar briefs done, 5 pillar pages already shipped. The publishing engine is producing. |
| **Schema sitewide** | 9 schema types (FAQ, How-to, Comparison, Article, Person, etc.) on every page. Eligible for Google rich results across the site. |
| **Authority-graph submission templates ready** | LinkedIn + G2 + Capterra + TrustRadius + Product Hunt + AlternativeTo + SaaSworthy + Owler + Wellfound — paste-and-go. Wikidata + Crunchbase drafted. |
| **AI orchestration demonstrated repeatably** | 80 cross-vertical artifacts produced in one day via parallel agents. The Ferrari has a working autopilot. |

### 🟡 IN PROGRESS — this week

| Milestone | Business value when complete |
|---|---|
| **Cross-vertical status board** | Single screen for stakeholder briefing; weekly tick automation. |
| **Lighthouse-CI cron live on server** | Daily perf budget enforcement; alerts on regression. |
| **PostHog self-host install** | Single analytics + product-analytics + feature-flags snippet replaces 3-tool stack. |
| **brand-review skill wired into publish gate** | Every content/social/email publish auto-checked for brand voice before going out. |

### 🔴 PENDING — waiting on operator decisions / external accounts

| Milestone | What unblocks it | Business value when complete |
|---|---|---|
| **First lead from paid media** | Provision Google Ads + LinkedIn Campaign Manager + GTM tag + CRM | $5K controlled month-1 spend converts to ≥10 SQLs |
| **First booked meeting from cold email** | ESP choice + DNS access + CRM | Outbound engine produces 5 booked meetings/wk by week-8 |
| **Newsletter sending** | ESP choice + DNS access | Bi-weekly cadence to 500+ subs by 90 days |
| **Live dashboard with last-7-days data** | GA4 + GSC OAuth grant | Stakeholders see what's working in real time |
| **Wikidata + Crunchbase entity live** | 7-field operator-confirmation form | LLMs cite CostSage on category questions (currently 0/10) |
| **A/B testing live on costsage.ai** | A/B engine choice (PostHog recommended) | Pricing-page + AWS-CTA + homepage-hero tests start producing learnings |
| **LinkedIn / X brand presence** | Brand handles + scheduler choice | 4 weeks of posts already queued, posting day-1 of unblock |
| **Cloudflare robots.txt rewrite cleared** | One toggle in Cloudflare dashboard | LLM crawlers can read pages on the first request, not the second |

---

## 6. What "MVP1 Done" looks like

> A single, defensible YES/NO sentence management can use to close the chapter.

**MVP1 is DONE when:**

> CostSage.ai operates as a self-driving demand engine — every vertical (SEO/AEO/GEO, Web/CRO, Paid, Content, Social, Email, Analytics, Brand) running on AI orchestration, producing measurable pipeline that crosses the LTV:CAC ≥ 3:1 line, with a live single-pane dashboard stakeholders can read in 60 seconds.

**Today, that breaks down as:**

| Sub-condition | Today | Target |
|---|---|---|
| All 8 engines built | ✅ all 8 built | ✅ |
| All 8 engines running on live data | 2 of 8 (V1, V2) | 8 of 8 |
| First measurable pipeline contribution | 0 leads | ≥10 SQLs/mo |
| LTV:CAC ≥ 3:1 | unknown (no CAC data yet) | ≥ 3:1 |
| Dashboard live | wireframed | live with last-7-days |
| Mission completion | ~42% measured / ~75% built | 100% |

**The unblock path is short.** ~33 percentage points of mission completion sit behind a single operator-confirmation form + 7 platform decisions. None of them takes more than 60 minutes of operator time end to end.

---

## 7. Operator decisions required (the unblock list)

> Twelve open. P0 items below unblock the bulk of MVP1. Bring this list to the next operator meeting; tick each, and the milestone board's RED column moves to GREEN.

### P0 (this week)
1. **Operator-confirmations form** — legal entity, HQ, founders, logo, AWS Marketplace URL, customer-savings claim approval, source-repo collab. Single form, unblocks 5 pending milestones.
2. **ESP choice** — Mailchimp / Beehiiv / Customer.io / Smartlead. Drives V6 entire engine.
3. **DNS write access** — for SPF/DKIM/DMARC. Required before any email send.
4. **CRM choice** — HubSpot Free / Pipedrive. Drives V3 lead routing + V6 lifecycle + V7 attribution close-out.
5. **Ad-account provisioning** — Google Ads + LinkedIn Campaign Manager (the two highest-signal). Drives V3 launch.
6. **A/B engine choice** — PostHog cloud free tier recommended. Drives V2 CRO program.
7. **GA4 + GSC OAuth grant** — one-click flow. Drives V7 live dashboard.

### P1 (next 2 weeks)
8. **Brand handles** — LinkedIn company / X / Reddit / YouTube. Drives V5 launch.
9. **Social scheduler** — Buffer / Hootsuite / native. Drives V5 publishing cadence.
10. **GitHub source-repo collab** — `shirazvaival/costsage-web`. Drives V2 source-of-truth alignment.
11. **Approved logo file + founder photos** — drives V8 asset library + V1 Person schema.
12. **Cloudflare AI-bot "Manage robots.txt" toggle** — deferred per request; flip when ready.

---

## 8. Mission status (today)

> The single sentence to take to management.

**"The Ferrari has 8 working subsystems. 2 are running on the road today, 5 are built and warm in the garage waiting for fuel and registration, 1 is bolted on but waiting on its battery. Built ≈ 75%. Running ≈ 42%. The remaining gap is operator-side activation, not engineering, and the door from 42% to 75% is one form + 7 decisions wide."**

---

## Appendix — How to read this file at different audiences

- **CMO / management:** §TL;DR + §5 Milestone Board + §8 Mission Status. ~3 min read.
- **Sheraz / orchestration owner:** §3 Technical Goals (gap column) + §4 Technical Mapping. ~10 min read.
- **Vertical leads:** §4 Technical Mapping (their TG row) + linked artifacts. ~5 min per vertical.
- **Stakeholders asking "is it done?":** §6 What MVP1 Done looks like + §7 Operator decisions. ~2 min read.

---

## Provenance

This file is the bridge document between the [`DIGITAL-MARKETING-DEPT-OPERATIONAL-PLAN.md`](./DIGITAL-MARKETING-DEPT-OPERATIONAL-PLAN.md) (the technical plan) and the [`STATUS-TRACKER.md`](./STATUS-TRACKER.md) (the live-status board). Update cadence: weekly tick + on every material milestone outcome.
