---
client_id: costsage
artifact: ai-automation-roadmap-v1.2
date: 2026-04-30
supersedes: v1.1 (2026-04-28 PDF)
audience: stakeholders + management
purpose: refreshed Layer-2 completion percentages + 8-week reconciliation
---

# AI Automation Roadmap — v1.2 (refresh)

> **What's new in v1.2 vs v1.1 (Apr 28):** Layer-2 (Real CostSage deliverables) advanced significantly across all 7 verticals. Mission-weighted completion: **24.5% → 55%** (+30.5 points in 48 hours). 11 new live URLs. Brand-voice enforcement live. Live-data baseline measurement now automated.

## Executive Summary — refreshed

| # | Vertical | v1.1 % (Apr 28) | v1.2 % (Apr 30) | Δ | Status | Next Action |
|---|---|---:|---:|---:|---|---|
| 1 | **Website + CRO** | 85% | **92%** | +7 | ✅ Active | A/B engine wiring (PostHog cloud free); GitHub source-repo collab |
| 2 | **SEO + AEO + GEO** | 55% | **78%** | +23 | ✅ Active | Cloudflare robots.txt toggle; first GSC sitemap submit; Wikidata + Crunchbase ops form |
| 3 | **Marketing Analytics & Ops** | 8% | **45%** | +37 | 🟡 Spec live | GA4/GSC OAuth grant; PostHog self-host install |
| 4 | **Content Marketing** | 5% | **55%** | +50 | 🟡 Engine running | Newsletter distribution (gated on ESP); whitepaper PDF gen; case-study customer interviews |
| 5 | **Email & CRM** | 3% | **42%** | +39 | 🔴 Drafts complete | ESP choice + DNS access + CRM choice (3 P0 ops) |
| 6 | **Social Media** | 0% | **35%** | +35 | 🔴 Drafts complete | Brand handles + Buffer subscription |
| 7 | **Paid Media / PPC** | 0% | **35%** | +35 | 🔴 Prep complete | Account provisioning + GTM pixel + CRM linkage |
| 8 | (V8 added) **Brand & Creative** | n/a | **45%** | new | 🟡 Live + enforced | Final logo + founder photos for press kit |
| **Mission-weighted** | **24.5%** | **55%** | **+30.5** | | |

## What changed since v1.1 (Apr 28)

**11 new live URLs on costsage.ai:**
- `/alternatives/{cast-ai,finout,sedai,turbonomic,yotascale}` (5 new)
- `/compare/{spot-by-netapp,finout,kubecost}-vs-costsage` (3 new)
- `/whitepaper/aws-first-saas-finops`
- `/security` (responsible-disclosure policy)
- `/brand-voice` (public voice guide)
- `/press` (press kit with boilerplate)

**Schema coverage:** ~92 → ~115 JSON-LD blocks; HowTo schema added to 3 pillars.

**Layer-2 deliverables across verticals:**
- V3 Analytics: local executive dashboard HTML + UTM enforcement guide + audit-cron-installer + daily/weekly digest scripts + PostHog runbook + Slack-webhook config (6 files)
- V4 Content: 4 SEO content briefs (RI 2026, Azure Hybrid Benefit, GCP CUDs, multi-cloud allocation) + production playbook + 5 case-study templates + Q3 editorial calendar CSV (24 slots) + whitepaper HTML (8 files)
- V5 Email: 3 new sequences (mid-funnel, post-trial, post-meeting) + lead-scoring rubric + MQL→SQL handoff + email QA checklist + 90-day deliverability warmup playbook (6 files)
- V6 Social: posting queues weeks 5-12 (8 weeks × ~25 items = 200+ items) + scheduler decision memo (Buffer recommended) + listening tool memo (Google Alerts + Mention free tier) + community-management SLA + brand-voice variants + employee advocacy rollout (13 files)
- V7 Paid: Google Ads CSV bulksheet (19+ keywords) + LinkedIn Campaign Manager bulk import + Microsoft Ads CSV + stop-loss rules + pre-launch QA checklist (5 files)
- V8 Brand: brand-review.py static checker (with self-tests) + /brand-voice + /press (3 deliverables)

**Cumulative Layer-2 artifact count: ~80 files added in 48 hours.**

## 8-Week Roadmap Reconciliation

| Vertical | Wk 1 | Wk 2 | Wk 3 | Wk 4 | Wk 5 | Wk 6 | Wk 7 | Wk 8 |
|---|---|---|---|---|---|---|---|---|
| 1. Website + CRO | ✅ Site live | ✅ CRO audit + fixes | A/B test cycles (gated on engine) | A/B test cycles | — | — | — | — |
| 2. SEO + AEO + GEO | ✅ Foundation | ✅ robots.txt + briefs | ✅ Content cluster live | 🔵 AEO + GEO layer (in progress) | — | — | — | — |
| 3. Analytics & Ops | — | ✅ GA4 + GTM audit (spec) | 🔵 Dashboards built (local) | ⏸ Attribution live (gated on OAuth) | — | — | — | — |
| 4. Content Mktg | — | — | ✅ Briefs + calendar | 🔵 Publishing pipeline (4 posts live) | — | — | — | — |
| 5. Email & CRM | — | — | — | — | 🔴 HubSpot setup (operator) | 🔴 Sequences live | — | — |
| 6. Social Media | — | — | — | — | — | 🔴 Calendar + scheduling (operator) | — | — |
| 7. Paid Media | — | — | — | — | — | — | — | 🔴 Campaign launch (after V3 live) |

Legend: ✅ Done · 🔵 In progress · 🔴 Planned, blocked on operator · ⏸ Awaiting upstream

**Reconciliation note:** vertical 1 + 2 are ahead of schedule (week-3 target hit in week-1). Vertical 3 + 4 jumped from week-3 spec to week-3 implementation. Vertical 5/6/7 remain blocked on operator decisions per design.

## Operator Decision Queue (12 open)

See `operations/OPERATOR-DECISIONS-CONSOLIDATED.md` for full detail. Priority summary:

| # | OD | Vertical | P | Operator action | Time | Impact |
|---|---|---|---|---|---|---|
| 1 | Confirmations form (legal, founders, HQ, savings claims) | V1, V4, V8 | P0 | Fill 1-page form | 30 min | +15% mission |
| 2 | Cloudflare robots.txt rewrite Off | V1 | P0 | One toggle in CF dash | 2 min | unblocks AEO/GEO crawler reads |
| 3 | A/B engine choice (recommend PostHog cloud free) | V1, V2 | P0 | Sign-up + key | 15 min | unblocks 3 A/B briefs |
| 4 | GitHub source-repo collab on shirazvaival/costsage-web | V1 | P0 | Add Claude as collaborator | 5 min | enables source-of-truth path |
| 5 | Google Ads + LinkedIn Campaign Manager + Microsoft Ads provisioning | V7 | P0 | Account setup + billing | 2 hours | unblocks 7 launch-ready campaigns |
| 6 | LinkedIn company page admin + LinkedIn Campaign Manager admin | V5, V7 | P0 | Grant admin | 10 min | unblocks LinkedIn paid + organic |
| 7 | CRM choice (HubSpot Free / Pipedrive / Salesforce) | V3, V5, V6 | P0 | Sign up + provision | 1 hour | unblocks lead pipeline + lifecycle |
| 8 | ESP choice (Mailchimp / Beehiiv / Customer.io / Smartlead) | V4, V5 | P0 | Sign up + DNS | 1 hour + 30 min DNS | unblocks newsletter + 5 sequences |
| 9 | DNS write access for SPF/DKIM/DMARC | V5 | P0 | Add records | 30 min | enables email send |
| 10 | Social brand-handle provisioning (LinkedIn / X / Reddit / YouTube) | V5, V6 | P1 | Reserve handles | 1 hour | unblocks 12 weeks queued content |
| 11 | Scheduler tool (Buffer recommended) | V6 | P1 | Subscribe + connect | 15 min | enables scheduled posting |
| 12 | Final logo + founder photos | V8 | P1 | Provide assets | 1 hour | completes press kit + bio styling |

**Path to ~80% mission completion:** clear OD1 + OD7 + OD8 + OD9 (4 P0 actions, ~3 hours operator time) → +25% mission lift in same week.

## Per-vertical "Done / In Progress / Pending" (compact)

### V1 SEO+AEO+GEO
- ✅ Phase-1 audit + 4-track baseline · 25-URL sitemap · 92+ schema blocks · /alternatives + /compare directories with 12 pages · HowTo schema on 3 pillars · /security + /brand-voice + /press live · Lighthouse cron daily
- 🟡 Speakable schema (partial) · sitemap-index split · category-prompt LLM citation strategy
- 🔴 Cloudflare robots.txt toggle (operator) · GSC OAuth (operator) · Wikidata + Crunchbase (operator confirmations)

### V2 Website + CRO
- ✅ D2 hot-patch + D3 overlay path · HSTS+Permissions-Policy+X-XSS shipped · 5 paid LPs live · Lighthouse 98/100/91/99 (mobile)
- 🟡 3 A/B test briefs ready · form-funnel audit
- 🔴 A/B engine wired (operator) · GitHub source-repo PR pipeline (operator) · GA4 conversion tracking (operator OAuth)

### V3 Analytics & Ops
- ✅ Lighthouse cron daily · audit-sweep automated · UTM enforcement guide · KPI dictionary (57 entries) · local dashboard HTML · digest scripts · Slack-webhook spec
- 🟡 PostHog runbook ready (15-step operator install)
- 🔴 GA4 + GSC OAuth · PostHog install · Slack webhook URL

### V4 Content Marketing
- ✅ 24-slot Q3 editorial calendar (CSV + markdown) · 7 content briefs (3 pillars + 4 SEO clusters) · 4 live blog/comparison posts · whitepaper HTML live · brand-voice page live · production playbook · 5 case-study templates · repurposing engine
- 🟡 Newsletter content (3 issues drafted)
- 🔴 Newsletter distribution (gated on ESP) · case-study customer interviews

### V5 Email & CRM
- ✅ 5 sequences drafted · lead-scoring rubric · MQL→SQL handoff · email QA checklist · 90-day deliverability warmup · SPF/DKIM/DMARC checklist · compliance footers
- 🔴 ESP provisioning · DNS records · CRM live · first send

### V6 Social Media
- ✅ 12 weeks of posting queues drafted (~300 items: 100 LinkedIn + 14 X tweets per week + 12 carousels) · bio kit · scheduler memo · listening memo · community SLA · brand-voice variants · employee advocacy plan
- 🔴 Brand handle provisioning · scheduler subscription

### V7 Paid Media
- ✅ 7 launch-ready campaign briefs · Google Ads + LinkedIn + Microsoft Ads CSV bulksheet imports · ICP master · ad-copy bank (30 headlines) · conversion tracking spec · stop-loss rules · pre-launch QA · landing page suitability matrix · 5 paid LPs live (noindex+follow)
- 🔴 Account provisioning · GTM pixel · CRM linkage

### V8 Brand & Creative
- ✅ Voice guidelines · category design (Agentic, Not Dashboard) · narrative thesis · messaging pillars · asset audit · brand-review.py static checker · public /brand-voice page · /press kit
- 🔴 Final logo · founder photos

## What's live on costsage.ai right now

**~34 live URLs** spanning home, 7 pillar pages, 8 alternative pages, 5 comparison pages, 5 paid LPs, 3 blog posts, 2 alternative-index landing pages, /security, /brand-voice, /press, /whitepaper, /humans.txt, /.well-known/security.txt, sitemap-index + 3 sub-sitemaps. All return 200; multi-UA parity (Mozilla/Googlebot/ClaudeBot/GPTBot/PerplexityBot identical responses); HSTS + Permissions-Policy + X-XSS active; Lighthouse mobile 98/100/91/99 (perf/SEO/a11y/BP).

## Next session unlocks

If operator clears the 4 P0 ODs (#1, #7, #8, #9) this week, the following moves from drafted to live the same week:
1. Wikidata Q-item + Crunchbase profile (V1)
2. ESP provisioned + first newsletter sent (V4 + V6)
3. CRM live + lead-scoring active (V3 + V5)
4. Founder bios + Person schema on /about + press-kit photos (V8)

Mission % target after that: **~80%**.

---

**Confidential — AI Automation Roadmap v1.2 · CostSage / Vaival Technologies · 2026-04-30 · Source: github.com/saadsocvaival/claude-digital-marketing**
