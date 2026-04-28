---
client_id: costsage
artifact: digital-marketing-dept-operational-plan
date: 2026-04-27
version: 1.0
audience: stakeholders + operators + agents
purpose: end-to-end execution plan for every Digital Marketing vertical, with workflows, dependencies, executable-now tasks, blockers, and tracking
---

# CostSage — Digital Marketing Department Operational Plan

> Single document covering **all 8 verticals**, with the same shape per vertical: outcomes → workflows → tools/accounts/permissions → tasks executable today → tasks blocked on dependencies → KPIs → tracking artifact. Companion file `STATUS-TRACKER.md` is the live status board. No vertical is "isolated" — dependencies are mapped explicitly so a blocked vertical doesn't stall the others.

## Table of contents
1. [Vertical map + dependency graph](#1-vertical-map)
2. [Cross-vertical operating model](#2-cross-vertical-operating-model)
3. [V1 — SEO + AEO + GEO](#v1-seo-aeo-geo) (status: Sprint-2 in progress)
4. [V2 — Website Development + CRO](#v2-website-development--cro) (status: Sprint-1 shipped)
5. [V3 — Paid Media & Advertising](#v3-paid-media--advertising) (status: planning, blocked on ad-accounts)
6. [V4 — Content Marketing](#v4-content-marketing) (status: editorial engine startable today)
7. [V5 — Social Media Marketing](#v5-social-media-marketing) (status: blocked on platform credentials)
8. [V6 — Email Marketing](#v6-email-marketing) (status: blocked on ESP)
9. [V7 — Marketing Analytics & Operations](#v7-marketing-analytics--operations) (status: tag plan startable; live data blocked on OAuth)
10. [V8 — Brand & Creative Operations](#v8-brand--creative-operations) (status: brief library startable today)
11. [Master credential dependency table](#master-credential-table)
12. [Master cadence — daily / weekly / monthly / quarterly](#master-cadence)

---

## 1. Vertical map + dependency graph

```
                   ┌──────────────────────┐
                   │  V8 Brand & Creative │  (foundation — feeds every other vertical)
                   └──────────┬───────────┘
                              │
       ┌──────────────────────┼─────────────────────┐
       ▼                      ▼                     ▼
  ┌─────────┐           ┌─────────┐           ┌─────────────┐
  │ V1 SEO  │           │ V4      │           │ V8 Creative │
  │ AEO/GEO │◄──┐       │ Content │──┐        │ assets      │
  └────┬────┘   │       └────┬────┘  │        └──────┬──────┘
       │        │            │       │               │
       ▼        │            ▼       │               ▼
  ┌────────────┐│       ┌─────────┐ │         ┌─────────────┐
  │ V2 Web/CRO ├┤       │ V5      │ │         │ V3 Paid     │
  │ (overlay   │└───────┤ Social  │ └────────►│ media       │
  │  + repo)   │        └────┬────┘           │ (Google/Meta│
  └─────┬──────┘             │                │  /LinkedIn) │
        │                    ▼                └──────┬──────┘
        │             ┌──────────────┐               │
        └────────────►│ V6 Email     │◄──────────────┘
                      │ (cold/promo/ │
                      │  lifecycle)  │
                      └──────┬───────┘
                             │
                             ▼
                   ┌──────────────────────┐
                   │ V7 Analytics + Ops   │  (closes the loop on every vertical)
                   └──────────────────────┘
```

**Reading rules:**
- V8 (Brand) is upstream of everything — voice/tone/positioning rules govern V1/V4/V5/V6 output.
- V1 (SEO/AEO/GEO) and V2 (Web) feed each other; both produce assets that V4/V5/V6 distribute.
- V4 (Content) is the supply chain for V5 (Social) and V6 (Email).
- V3 (Paid) consumes assets from V2/V4/V8 and produces leads that flow into V6.
- V7 (Analytics) instruments and measures everything — without it, no vertical can prove ROI.

---

## 2. Cross-vertical operating model

### 2.1 Cadence
- **Daily** — agent stand-up (auto-generated digest of last 24h actions per vertical, exceptions only)
- **Weekly tick** — Monday 09:00 local: pipeline review across all verticals, blocker triage
- **Sprint** — 2-week cadence per vertical; staggered so no two verticals ship the same day
- **Monthly** — KPI review across full funnel; rubric calibration
- **Quarterly** — strategy revisit, budget reallocation across verticals

### 2.2 Single sources of truth
- **Status board:** `STATUS-TRACKER.md` (this directory) — every vertical's current state
- **Editorial calendar:** Trello board "CostSage Editorial" (creds in vault) — covers V4/V5/V6
- **Campaign tracker:** `operations/campaigns/` — one folder per active V3 paid-media campaign
- **Credentials manifest:** `secrets.pointer.md` — every account, with `Last rotated` dates
- **Ledger:** `clients/costsage/ledger-events/*.jsonl` — every material event (deploy, campaign launch, A/B win, KPI bump)

### 2.3 Decision authority
- **Ship/no-ship for any public-facing artifact** — operator gate (HITL); no vertical auto-publishes
- **Budget changes ≥ $500/day or ≥ 20% delta** — operator gate
- **New external account creation** — operator approval required (so secrets land in vault before use)
- **Anything below those thresholds** — agent autonomy

### 2.4 Quality gates (every vertical)
1. **Brand voice** check — must match V8 guidelines
2. **Truthfulness** check — no fabricated stats, claims, customer names
3. **Legal/compliance** check — GDPR/CAN-SPAM/CASL for V6, ad-platform policies for V3
4. **Accessibility** check (V2/V4/V8) — WCAG AA on visible UI
5. **Tracking** check (V7) — UTMs/events present before a campaign goes live

---

# V1 — SEO + AEO + GEO

**Status: Sprint-2 in flight. Phase-1 baseline 89.5/200; Sprint-1 shipped, 8/10 Sprint-2 P0 gaps closed live.**

(Full plan + execution log: `seo-geo-aeo/PHASE-1-EXECUTION-REPORT.md`. Summary kept here for cross-vertical visibility.)

### Outcomes
- Be **discoverable** in Google + AI answer engines for brand queries (achieved: 5/5) and category queries (target: 0/10 → ≥2/10 by 90 days).
- **Authority graph** entries (Wikidata, Crunchbase, G2, Capterra) live within 30 days.
- **Rich-result eligibility** on every public page within 30 days.

### Workflows (active)
1. **Weekly crawl + delta** — 16-URL crawl, schema validation, CWV PSI run; deltas vs last week tracked.
2. **Authority-graph progression** — one new external listing per week (Wikidata → Crunchbase → G2 → Capterra → AlternativeTo …).
3. **Content pillar publishing** — see V4.
4. **AEO citation probe** — weekly LLM citation tests on 15 fixed prompts.

### Tools / accounts
- ✅ **Have:** GSC/GA4/GTM (web), Semrush/Ahrefs/Surfer/ATP (web), Screaming Frog (web), server SSH, bind-mount overlay, Google Rich Results.
- 🔴 **Need:** API keys for Semrush/Ahrefs/Surfer/ATP (extraction runbook authored), GSC OAuth grant.

### Executable now
- Sprint-2 batch 3 (G9/G10/G11 — claim/enrich LinkedIn, G2, Capterra, TrustRadius, AlternativeTo, Product Hunt, SaaSworthy, Owler, Wellfound).
- Sprint-2 batch 4 (G15 — homepage hero category statement; G16/G17 — 4 new pillar pages incl. AI-workloads moat).
- 30-day re-audit dry-run (using only public PSI + WebSearch).

### Blocked
- **G2 Wikidata** + **G3 Crunchbase** submission — operator confirmations form.
- **G1 Cloudflare second toggle** — operator (deferred per request).
- **D1 source-repo PR access** — operator GitHub collab.

### KPIs (V1)
| Metric | Baseline | 30d | 90d |
|---|---|---|---|
| Indexed URLs (GSC) | TBD | ≥17 | ≥25 |
| Brand-prompt LLM citation rate | 5/5 | 5/5 | 5/5 |
| Category-prompt LLM citation rate | 0/10 | ≥1/10 | ≥2/10 |
| Schema rich-result eligibility | 9 types | 9 | 11 |
| Authority-graph entries | 5 | 9 | 13 |

### Tracking artifact
`seo-geo-aeo/PHASE-1-EXECUTION-REPORT.md` + per-track files. Status row in `STATUS-TRACKER.md`.

---

# V2 — Website Development + CRO

**Status: Sprint-1 shipped (D2 hot-patch + D3 overlay). Site durable. CRO not yet started.**

### Outcomes
- **Conversion rate** on homepage CTAs, /pricing, /aws, /azure measurably improved within 60 days.
- **Page experience** (CWV) — all 18 URLs hit ≥75 mobile perf score.
- **A/B testing capability** — at least 1 live test running by week-3 of Sprint-2.

### Workflows
1. **Hot-fix / overlay deploy** (already operational) — change → overlay → bind-mount reload → verify curl.
2. **Source-repo PR flow** (D1, blocked on collab access) — change → PR → CI → GHCR → docker pull.
3. **CRO test cycle** — hypothesis → variant → A/B engine setup → ship → 14-day run → decision.
4. **Lighthouse-CI** — every overlay deploy triggers Lighthouse run, deltas logged.
5. **Form / signup audit** — quarterly funnel walk-through.

### Tools / accounts
- ✅ **Have:** SSH to server, Docker, nginx, bind-mount overlay, WordPress admin (`https://costsage.ai/wp-admin/` — for CMS-side changes if we route those through WP).
- 🔴 **Need:** A/B engine (recommend Cloudflare Workers split, GrowthBook, or VWO — choose one). GitHub collab on `shirazvaival/costsage-web`. Lighthouse-CI host (can run on the same server).

### Executable now
- Replace homepage hero (G15) once V8 finalises the category statement.
- Ship ANY copy/schema/HTML edits via the overlay path (already proven 3 times).
- Form-funnel audit on /contact, /pricing → /signup, /aws → CTA.
- Set up Lighthouse-CI as a daily cron on the server (writes to `clients/costsage/feeds/lighthouse-daily-*.json`).
- Pricing-page split test — author hypothesis + variant copy now; wire to A/B engine when chosen.

### Blocked
- A/B engine choice (operator decision).
- GitHub collab access (operator decision; without it, all changes are overlay-only — durable but separate from source).
- Watchtower currently fixed but tied to `nickfedor/watchtower:1.16.1` — schedule a maintenance review in 90d.

### KPIs (V2)
| Metric | Baseline | 30d | 60d |
|---|---|---|---|
| Mobile perf score (avg, all pages) | ~50 | ≥70 | ≥75 |
| Pricing → signup CTR | TBD (V7 dependency) | +10% | +25% |
| /aws → CTA click rate | TBD | +10% | +25% |
| Active A/B tests | 0 | 1 | 2 |

### Tracking artifact
`operations/web-cro/` — one folder per active CRO test. Status row in `STATUS-TRACKER.md`.

---

# V3 — Paid Media & Advertising

**Status: Planning authorable now; execution blocked on ad accounts.**

### Outcomes
- **First lead** from paid channel within 30 days of operator unblocking ad accounts.
- **CAC by channel** known (vs unknown today).
- **Working ICP** validated in-market (which audience pays?).

### Sub-channels in scope
| Channel | Best-fit motion | Priority for CostSage |
|---|---|---|
| **Google Search Ads** | high-intent capture | P0 (intent-rich queries: "AWS cost tool", "FinOps platform") |
| **Google Display + Remarketing** | re-engagement | P1 |
| **Microsoft / Bing Ads** | overflow + enterprise IT buyers | P2 |
| **LinkedIn Ads (Sponsored Content + InMail)** | account-based targeting | P0 (CFO/VP Eng/FinOps lead personas) |
| **Meta (FB+IG)** | brand + lookalike | P2 (B2B FinOps audience is small there) |
| **X / Twitter Ads** | dev community | P2 |
| **Reddit Ads** | r/aws, r/devops, r/sre | P1 |
| **Capterra / G2 sponsored placements** | review-site SQLs | P0 (alongside V1 G2 listing) |

### Workflows
1. **Account setup** — billing, conversion-tracking pixel, audience seeds (CRM upload + Lookalike), GTM containers per platform.
2. **Campaign brief** — `operations/campaigns/<channel>-<date>-<theme>.md` (objective, ICP, budget, creative spec, landing page, KPIs, kill-switch criteria).
3. **Creative production** (delegates to V8 + V4) — 3 ad variants per campaign minimum.
4. **Launch + 72h watch** — daily QA; if CPC > 2× target or CTR < 0.5× target, pause.
5. **Weekly optimization** — pause bottom-quartile creatives; reallocate to top quartile.
6. **30-day reporting** — campaign report with CAC, MQL, SQL, attribution.

### Tools / accounts (the credential reality check)
- 🔴 **None of the ad accounts are in the credential bundle.** Operator action: provision ad-account access on Google Ads / LinkedIn Campaign Manager / Microsoft Advertising / Meta Business Manager / X Ads. Each requires:
  - billing method
  - admin access to the relevant brand entity (LinkedIn company page, Meta page, etc.)
  - GTM tag installation on costsage.ai (V2 dependency)
  - conversion tracking (V7 dependency)
- 🔴 **Pixel/tag plan** authorable now; pixel firing blocked until accounts exist.
- 🔴 **CRM** for lead routing — not provisioned. Recommend HubSpot Free or Pipedrive starter.

### Executable now
- **Channel-priority brief** — written below; review-and-approve.
- **Creative brief library** — 4 ad variants per priority channel, paired to landing pages we already have (/aws, /azure, /pricing, /compare/cloudzero-vs-costsage, /compare/nops-vs-costsage). Authorable today.
- **ICP target audiences** — define exact LinkedIn filters (job titles, seniority, company size, industry, skills) and Google keyword lists (broad + phrase + exact match).
- **Tracking plan** (V7 dependency) — UTM convention + conversion event spec.
- **Dummy budget model** — proposed monthly spend split with break-even math at our pricing tiers.

### Blocked
- Account provisioning (the gating step).
- Pixel/tag installation (depends on V7 GTM container).
- CRM for lead handoff.

### Channel sequencing recommendation
- **Week 1 (after unblock):** Google Search Ads + LinkedIn Sponsored Content (the two with highest signal-to-spend for B2B FinOps).
- **Week 2:** add Capterra/G2 sponsored slots.
- **Week 4:** add Reddit + X if Week 1 channels are converting; otherwise double down on the winners.
- **Week 8:** add Meta Lookalikes off the converted-customer seed list.

### KPIs (V3)
| Metric | Target (90d) |
|---|---|
| CAC by channel | known + ≤ $1500 LinkedIn, ≤ $400 Google Search |
| MQLs / month | ≥40 |
| SQLs / month | ≥10 |
| CPL by channel | tracked weekly |
| Pipeline contribution | ≥30% of total |
| Cost per channel-experiment | ≤ $2,000 to reach signal |

### Tracking artifact
`operations/campaigns/` — one folder per campaign with brief + weekly report + post-mortem. Status row per active campaign in `STATUS-TRACKER.md`.

---

# V4 — Content Marketing

**Status: Editorial engine fully startable today (no external accounts beyond what we have).**

### Outcomes
- **Publishing cadence** — 1 long-form post / week + 1 short-form / week, sustained.
- **Topical authority** in FinOps + AI cost optimization.
- **Lead-gen via gated content** by week-6.

### Content types in scope
| Type | Format | Cadence | Owner | Distribution (V5/V6) |
|---|---|---|---|---|
| Pillar long-form | 2,000-3,000w blog | 1/week | Head of Content | LinkedIn, X thread, newsletter |
| Tactical how-to | 800-1,200w blog | 1-2/week | Head of Content | Reddit + LinkedIn |
| Comparison page | landing page | as competitive set evolves | Head of Content + V1 | sales enablement + V3 |
| Customer story | 1,200w + interview | 1/month | Head of Content + Sales | newsletter, LinkedIn, sales |
| Whitepaper / report | 5,000w + design | 1/quarter | Head of Content + V8 | gated lead-gen |
| Newsletter | bi-weekly digest | every 2 weeks | Head of Content + V6 | email list |
| Podcast/YouTube | 30 min | monthly (Q3+) | Head of Content | LinkedIn + YouTube + transcript |
| Webinar | 45 min | monthly | Head of Content + Sales | gated registration → V6 nurture |

### Workflows
1. **Quarterly editorial calendar** (Trello board "CostSage Editorial") — 12 weeks of slots, themes mapped to V1 keyword targets.
2. **Brief → draft → review → schema-pack → publish** — 4-stage flow per piece. Brief authored by content-strategy agent; draft by writer agent; review by brand-voice agent (skill: `brand-voice:enforce-voice`); schema-pack by V1 agent.
3. **Distribution map per piece** — every piece ships with a distribution-per-piece column (V5 dark-social, V6 newsletter slot, sales-enablement note, repurpose plan).
4. **Repurposing engine** — 1 long-form piece → 5 LinkedIn posts + 3 X threads + 1 newsletter section + 1 sales enablement card.
5. **Content audit** — quarterly: which posts ranked? which converted? prune / refresh / decline.

### Tools / accounts
- ✅ **Have:** WordPress admin (`tayyabnaqvi` / app-password rotation pending), Trello (web; API key extraction pending), ChatGPT/Claude/Gemini/Perplexity (web; API keys pending — for research, not generation gating), Surfer SEO (web; API key pending — for content briefs), AnswerThePublic (web; API key pending — for question discovery).
- ✅ **Bind-mount overlay** path means we can publish to costsage.ai without touching WP (for long-form blog posts). WP is for staging/dynamic content if needed.
- 🟡 **Recommend:** Notion for content ops if Trello becomes too kanban-flat. Decision deferred.

### Executable now
- **Q3 editorial calendar** (12 weeks × 2 pieces/week = 24 slots) authored against V1 pillar map.
- **Content brief library** — 5 fully-fleshed briefs ready for drafting.
- **3 long-form pillar drafts** — "FinOps for AI workloads" (the moat), "AWS cost optimization tools 2026", "Building a cloud cost culture".
- **Newsletter program design** — bi-weekly format, 5-block template, kickoff issue draft.
- **Lead-magnet whitepaper outline** — "The AWS-First SaaS FinOps Playbook" (gated PDF for V6 lead-gen).
- **Repurposing engine** — automation rules + Trello workflow.

### Blocked
- **Newsletter sending** — needs ESP (V6 dependency).
- **Gated content fulfillment** — needs ESP + form/CRM (V6 + V3 dependency).
- **Customer stories** — need customer interviews (sales/CSM dependency).

### KPIs (V4)
| Metric | Baseline | 30d | 90d |
|---|---|---|---|
| Posts published | 2 (Sprint-1) | 8 | 24 |
| Avg organic traffic / post / month | TBD | tracked | ≥150 |
| Newsletter subscribers | 0 | 100 | 500 |
| Whitepaper downloads | 0 | 0 (not yet shipped) | 200 |
| Content-attributed pipeline | 0 | tracked | ≥10% |

### Tracking artifact
`operations/content/editorial-calendar.md` (mirror of Trello) + `operations/content/briefs/` (one md per brief). Status row in `STATUS-TRACKER.md`.

---

# V5 — Social Media Marketing

**Status: Strategy + content authorable today; publishing blocked on platform access.**

### Outcomes
- **Owned presence** on LinkedIn (priority), X (developer audience), YouTube (long-form), Reddit (community).
- **Engagement-led growth** — comments and threads, not announcement-only.
- **Pipeline-attributable** social — at least 1 SQL/month from LinkedIn-sourced traffic by 60 days.

### Channels in scope
| Channel | Priority | Posting cadence | Format mix |
|---|---|---|---|
| LinkedIn (company + founder personal brand) | P0 | 5x/week | text posts (40%), carousels (20%), video (15%), articles (10%), polls (5%), reposts (10%) |
| X / Twitter | P1 | 2x/day | threads, single-tweet hot-takes, quote-replies |
| YouTube | P2 | 1x/month | long-form (FinOps explainers, customer stories) |
| Reddit | P1 (lurk-first) | community-driven | answer real questions on r/aws, r/devops, r/sre — never link-drop |
| Hacker News | P2 (event-driven) | Show HN posts on launches | |
| TikTok / Threads / Bluesky | P3 (defer) | — | not the right ICP today |

### Workflows
1. **Voice + bio kit** (V8 dependency) — 1-line bio, founder bio, link-in-bio page, brand assets sized per platform.
2. **Weekly content plan** — 5 LinkedIn posts × 2 X threads × 1 long-form blog amplification (V4 → V5 repurposing engine).
3. **Engagement window** — 30 min/day comment-and-reply on relevant accounts (engineering managers, FinOps practitioners, competing-product employees acting as customers).
4. **Listening + response** — alerts for "CostSage", "FinOps tool", "AWS cost", competitor names; queue responses.
5. **Publishing pipeline** — Buffer or Hootsuite (TBD) for scheduled posts; native engagement only (no auto-replies).
6. **Analytics roll-up** (V7) — weekly LinkedIn analytics + X impressions + Reddit karma → into the unified dashboard.

### Tools / accounts
- 🔴 **No platform credentials in the bundle for X / LinkedIn / Reddit / YouTube.** Operator action: provision either personal accounts or a brand-owned Page/handle on each.
- 🔴 **Scheduler** — recommend Buffer free tier (1 channel each free) or Hootsuite professional. Operator decision.
- 🔴 **Listening tool** — Brand24 / Mention / Google Alerts (Google Alerts free, web-login provisioned today; insufficient depth but a start).
- ✅ **Have:** Google Alerts (provisioned).

### Executable now
- **Platform bio kit** — copy + image specs per channel.
- **First 4 weeks of content** — 20 LinkedIn posts, 16 X threads, 4 carousels, 1 founder thought-leadership piece — drafted and queued, ready to schedule on day-1 of credentials landing.
- **Reddit engagement playbook** — which subreddits, voice rules, what counts as "value-add", when to reference CostSage (rarely, only when asked).
- **Listening map** — keywords + brand mentions + competitor mentions.
- **LinkedIn employee-amplification kit** — pre-written posts the founder/team can post-from when CostSage publishes a milestone.

### Blocked
- Actual publishing.
- Paid amplification (V3 dependency).
- Direct engagement.

### KPIs (V5)
| Metric | Baseline | 30d (post-unblock) | 90d |
|---|---|---|---|
| LinkedIn followers (company) | TBD | +500 | +2,000 |
| LinkedIn weekly impressions | 0 | 20K | 100K |
| X followers | TBD | +200 | +1,000 |
| Reddit positive engagement events | 0 | 10 | 50 |
| Social-attributed SQLs | 0 | 1 | 5 |

### Tracking artifact
`operations/social/posting-queue.md` + `operations/social/weekly-report-*.md`. Status row per active channel in `STATUS-TRACKER.md`.

---

# V6 — Email Marketing

**Status: Strategy + sequences authorable today; ALL execution blocked on ESP.**

### Outcomes
- **Bi-weekly newsletter** to 500+ subscribers within 90 days.
- **Cold-outreach engine** producing ≥5 booked meetings / week by 60 days.
- **Lifecycle automation** for trial→paid + expansion + winback.
- **Deliverability** above 98% inbox rate.

### Sub-streams in scope
| Stream | Cadence | Audience | KPI |
|---|---|---|---|
| Cold outreach (1:1 sales) | sequence-driven | targeted ICP list | meeting-booked rate |
| Cold outreach (1:few campaigns) | weekly campaigns | LinkedIn lookalikes | reply rate |
| Newsletter | bi-weekly | opted-in subscribers | open rate / CTR |
| Promotional / launch | event-driven | full list | conversion |
| Company updates | quarterly | full list + investors | open rate |
| Onboarding nurture | drip | trial signups | trial→paid conversion |
| Retention / lifecycle | trigger-based | active customers | retention |
| Reactivation / winback | trigger-based | dormant > 90d | reactivation rate |

### Workflows
1. **List hygiene** — double opt-in, suppression list, weekly bounce sweep.
2. **Cold-outreach sequence** — 5-touch sequence (email 1 → wait 4d → email 2 → wait 5d → LinkedIn touch → wait 4d → email 3 → wait 5d → break-up email).
3. **Newsletter production** — Friday plan → Monday draft → Tuesday review → Wednesday schedule → Thursday send.
4. **Lifecycle automation** — trigger map: signup→D0 welcome→D1 setup nudge→D3 first-value→D7 case study→D14 trial-end-coming→D15 trial converted-or-extension.
5. **A/B testing** — every campaign → 2 subject lines → 10% / 10% / 80% split.
6. **Compliance** — CAN-SPAM + CASL + GDPR per-region; physical address footer; one-click unsubscribe.

### Tools / accounts
- 🔴 **No ESP in the credential bundle.** Mandatory: choose one. Recommend by use-case:
  - **Customer.io** or **Intercom** for lifecycle (best trigger model)
  - **Mailchimp** or **Beehiiv** for newsletter (simplest editor)
  - **Smartlead.ai** or **Instantly.ai** for cold outreach (warmup + rotation)
- 🔴 **Domain authentication** — SPF + DKIM + DMARC must be set on costsage.ai before any send. (Server-side DNS work, ~30 min once decided.)
- 🔴 **CRM** — lead/account/contact model. HubSpot Free is a fine starting point.
- 🔴 **Deliverability monitoring** — GlockApps / MailGenius once volume justifies.

### Executable now
- **5-touch cold-outreach sequence** for the AWS-first SaaS persona (full copy, ready to load into any sender).
- **Newsletter program** — 5-block template + 3 issues drafted (issue 1: "FinOps for AI workloads", issue 2: "RI vs Savings Plans 2026 update", issue 3: "Cost-of-bad-tagging deep dive").
- **Onboarding nurture sequence** — 7 emails for trial users.
- **Winback sequence** — 3 emails for dormant customers.
- **Domain-authentication checklist** — SPF/DKIM/DMARC records ready to paste once ESP chosen.
- **Compliance footers** — physical address, unsubscribe text, GDPR-suppression model.

### Blocked
- Sending anything.
- List import (no ESP yet).
- Lifecycle automation wiring.
- Deliverability tests.

### KPIs (V6)
| Metric | Baseline | 30d (post-ESP) | 90d |
|---|---|---|---|
| Newsletter subscribers | 0 | 100 | 500 |
| Cold-outreach reply rate | — | ≥8% | ≥15% |
| Booked-meeting rate | — | 1/week | 5/week |
| Trial→paid conversion | — | tracked | ≥18% |
| Inbox placement rate | — | ≥95% | ≥98% |

### Tracking artifact
`operations/email/sequences/`, `operations/email/newsletter-issues/`, `operations/email/lifecycle-map.md`. Status rows in `STATUS-TRACKER.md`.

---

# V7 — Marketing Analytics & Operations

**Status: Tag plan + dashboard spec authorable today. Live data pipelines blocked on OAuth grants.**

### Outcomes
- **Single source of truth** for marketing performance — every other vertical reads from the same dashboard.
- **Attribution model** — multi-touch + last-touch + position-based; channel-level CAC.
- **Anomaly detection** — alerts when KPIs swing > 2σ.

### Workflows
1. **GTM container build** — events: page_view, scroll_75, cta_click, form_submit (all CTAs), trial_start, trial_complete, demo_request, newsletter_signup, login.
2. **GA4 + GSC + GTM linking** — verify property and view, configure conversion events.
3. **UTM convention** — every paid + email + social link uses `?utm_source=…&utm_medium=…&utm_campaign=…&utm_content=…&utm_term=…`. Documented; enforced via shortener (Bitly Pro or self-hosted).
4. **Data warehouse** — once volume justifies, pipe GA4 + GSC + ad platforms + ESP + CRM into BigQuery (free tier) or PostHog (self-host).
5. **Dashboard** — weekly KPI roll-up; one tab per vertical + one all-up CMO dashboard.
6. **Anomaly + monitoring** — daily check + Slack alert on > 2σ moves.

### Tools / accounts
- ✅ **Have:** GA4, GSC, GTM (web logins).
- 🔴 **Need OAuth grant** for programmatic access (one-click flow).
- 🟡 **Recommend:** PostHog (self-host on the marketing-claude-soc server — already has 196G free disk).
- 🔴 **CRM:** required for lead-attribution closeout (V3 + V6 dependency).
- 🔴 **Slack** webhook for anomaly alerts.

### Executable now
- **Tag/event plan** (`operations/analytics/tag-plan.md`) — every event we want to capture, every property dimension, GTM trigger spec.
- **UTM convention doc** — single source of truth.
- **Dashboard wireframe** — what each tab shows, refresh cadence, who reads it.
- **KPI dictionary** — every metric with formal definition + formula + owner.
- **PostHog self-host install plan** — Docker compose addition to `/opt/wordpress/docker-compose.yml`.
- **Lighthouse-CI cron** (V2 dependency) — daily perf snapshot writing to `clients/costsage/feeds/`.

### Blocked
- Live data ingestion (OAuth grant).
- Cross-channel attribution (depends on every other vertical's tags being live).

### KPIs (V7)
This vertical *measures* the others; it has no independent KPI besides:
- **Coverage**: % of cross-vertical events flowing into the dashboard (target: 100% by 30d post-OAuth).
- **Freshness**: dashboard data lag ≤ 24h (target: ≤ 1h once warehoused).

### Tracking artifact
`operations/analytics/` — tag plan, UTM convention, dashboard spec, KPI dictionary. Status row in `STATUS-TRACKER.md`.

---

# V8 — Brand & Creative Operations

**Status: Brand-voice extraction startable today using the brand-voice skill suite.**

### Outcomes
- **Brand voice guidelines** documented and enforced across V1/V4/V5/V6.
- **Asset library** — logos, colors, type, photography rules, ad-template library.
- **Category claim** — the 5-7-word noun-anchored statement that LLMs and humans can repeat.

### Workflows
1. **Brand discovery** — `brand-voice:discover-brand` → ingest existing site/blog/sales calls → produce voice guidelines.
2. **Voice enforcement** — `brand-voice:enforce-voice` runs before any V4/V5/V6 publish.
3. **Visual asset library** — Figma file (or local SVG/PNG library if no Figma).
4. **Category-design exercise** — Play Bigger / Dunford hybrid; output the canonical CostSage category claim.
5. **Narrative-thesis** — 1-pager that every Head reads and references.

### Tools / accounts
- ✅ **Have:** brand-voice skill suite (in this repo); existing costsage.ai content as discovery source.
- 🔴 **Need:** Figma seat (or decision to use SVG/PNG only); approved logo file.

### Executable now
- **Brand-voice guidelines** generated from existing site copy (run `brand-voice:discover-brand` then `brand-voice:generate-guidelines`).
- **Category-design draft** — `templates/category-design.md` filled in for CostSage.
- **Narrative-thesis** — 1-pager.
- **Asset audit** — what we have vs need (logo variations, ad templates, OG image library).
- **Brand-review skill wired** — every V4/V5/V6 publish runs `marketing:brand-review` first.

### Blocked
- Approved final logo file (operator).
- Founder photos for /about + Person schema (operator).

### KPIs (V8)
- **Adoption**: 100% of V4/V5/V6 artifacts pass `marketing:brand-review` before publish.
- **Consistency**: < 3 brand-voice deviations per month flagged.
- **Recognition** (long-term): brand-recall lift in customer interviews.

### Tracking artifact
`operations/brand/` — guidelines, asset-library manifest, category-design, narrative-thesis. Status row in `STATUS-TRACKER.md`.

---

# Master credential table

Cross-references `secrets.pointer.md`. Status as of 2026-04-27.

| Vertical | Credential | Have? | Type | Blocker |
|---|---|---|---|---|
| V1 | Semrush / Ahrefs / Surfer / ATP | web only | api-key | extract from dashboard |
| V1 | Screaming Frog | web | license | install on server |
| V1, V7 | GA4 / GSC / GTM | web | oauth | grant flow |
| V1 | Google Rich Results / Alerts | web | public | none |
| V1, V7 | LLM platforms (ChatGPT/Claude/Gemini/Perplexity/Copilot) | web | api-key | extract from dashboard |
| V2 | Server SSH | ✅ | key | none |
| V2 | WordPress admin | ✅ | password | rotate to per-agent app-password |
| V2 | GitHub source repo | 🔴 | collab | operator add |
| V2 | A/B engine | 🔴 | TBD | choose engine |
| V3 | Google Ads | 🔴 | account | provision |
| V3 | LinkedIn Campaign Manager | 🔴 | account | provision |
| V3 | Meta Business Manager | 🔴 | account | provision |
| V3 | Microsoft Advertising | 🔴 | account | provision |
| V3 | X Ads | 🔴 | account | provision |
| V3 | Reddit Ads | 🔴 | account | provision |
| V3 | Capterra / G2 sponsored | 🔴 | account | provision (after V1 listings live) |
| V3, V6 | CRM (HubSpot etc.) | 🔴 | account | choose + provision |
| V4 | Trello | web | api-key | extract |
| V4 | WordPress | ✅ | — | (see V2) |
| V5 | LinkedIn / X / Reddit / YouTube | 🔴 | account | provision brand handles |
| V5 | Scheduler (Buffer/Hootsuite) | 🔴 | account | choose + provision |
| V5 | Listening (Brand24/Mention) | 🔴 | account | optional, defer |
| V6 | ESP (Mailchimp / Beehiiv / Customer.io / Smartlead) | 🔴 | account | choose + provision |
| V6 | DNS write access (SPF/DKIM/DMARC) | 🔴 | DNS console | operator |
| V7 | PostHog (self-host) | startable | docker | none — startable on server |
| V7 | Slack webhook | 🔴 | webhook | provision |
| V8 | Figma | 🔴 | account | optional |
| V8 | Approved logo file | 🔴 | asset | operator |

**Bottom line:** ~60% of immediately-executable work doesn't need any new credential. The other 40% lives behind 8 operator decisions (ad accounts, ESP, A/B engine, scheduler, CRM, GitHub collab, A/B engine, DNS access).

---

# Master cadence

| Cadence | Vertical | Action |
|---|---|---|
| **Daily** | V1 | crawl health (16 URLs) |
| | V3 | active-campaign QA (CPC/CTR/spend pacing) |
| | V5 | engagement-window 30 min |
| | V7 | dashboard freshness check + anomaly scan |
| **Weekly (Mon)** | All | cross-vertical tick — `STATUS-TRACKER.md` updated; blockers triaged |
| | V1 | weekly LLM citation probe + GSC delta |
| | V3 | campaign optimization (pause + reallocate) |
| | V4 | content brief → draft pipeline review |
| | V5 | weekly content plan published |
| | V6 | newsletter draft → Wed send |
| | V7 | weekly KPI digest |
| **Sprint (2-week)** | V1, V2, V4 | sprint demo + rubric grade |
| **Monthly** | All | KPI review; monthly stakeholder report |
| | V1 | full re-audit (all 4 tracks) |
| | V3 | per-channel post-mortem |
| | V4 | content audit (refresh / prune) |
| | V8 | brand-voice deviation log review |
| **Quarterly** | All | strategy revisit; budget reallocation |
| | V1 | re-baseline against rubric |
| | V4 | new editorial calendar |
| | V8 | brand asset audit |

---

# Closing — what changes operationally

Up to today the work was **vertical-deep** on SEO/AEO/GEO/Web. From this plan forward it's **vertical-broad**:

1. Every vertical has a **named operating model** above.
2. Every vertical has **explicit dependencies** with status.
3. Every executable-now task can start without waiting on operator decisions; every blocked task is named with the specific operator action that unblocks it.
4. The **single status board** (`STATUS-TRACKER.md`) gives stakeholders a one-screen view across all 8 verticals.
5. Cadences are stacked so no week passes without progress visible somewhere.

This plan is the contract. The status tracker is the proof. Anything not in either is out of scope.
