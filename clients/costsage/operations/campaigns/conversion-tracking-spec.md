# Conversion Tracking Spec — Cross-Platform — CostSage.ai

> Every event we want fired across paid channels, with platform-specific firing rules. All event names match `analytics/tag-plan.md` (no orphan events).

## 1. Canonical event list (cross-platform)

| Event | Trigger | Page(s) | Required params | Funnel stage |
|-------|---------|---------|-----------------|--------------|
| `page_view` | Any URL navigation | All | `page_path`, `utm_*` | TOFU |
| `scroll_75` | 75% scroll depth | All | `page_path` | TOFU |
| `cta_click` | Click on element with `data-cta-id` | All | `cta_id`, `page_path`, `cta_label` | TOFU/MOFU/BOFU |
| `form_start` | First focus into a tracked form's first field | LP forms | `form_id` | MOFU |
| `form_submit` | Successful form POST | LP forms | `form_id`, `form_type` | MOFU/BOFU |
| `demo_request` | `form_submit` where `form_id=demo` | `/aws`, `/`, `/compare/*` | `email_hash`, `company_size`, `monthly_spend_band` | BOFU |
| `trial_start` | Trial activation success page | `/pricing`, app | `email_hash`, `plan` | BOFU |
| `trial_complete` | Trial 14-day completion / first activation milestone | App | `email_hash`, `activation_score` | BOFU |
| `purchase` | Closed-won (offline import) | CRM → ad platforms | `value`, `currency`, `arr`, `email_hash` | Revenue |
| `login` | Successful auth | App | `user_id_hash` | Retention |
| `logout` | Logout click | App | `user_id_hash` | — |
| `search` | Site search submit | Site | `query`, `result_count` | TOFU |
| `video_play` | First play of any embedded video | LP/blog | `video_id`, `video_title` | TOFU |

## 2. Per-platform pixel firing rules

### 2.1 Google Ads
- Tag: Google Ads Conversion via GTM (Conversion Linker tag installed sitewide).
- Mapped events:

| GA event | Google Ads conversion action | Conv ID/Label | Value | Notes |
|----------|------------------------------|---------------|-------|-------|
| `demo_request` | `Demo Request — Web` | `[TBD-OPERATOR]` | `1` (placeholder) | Primary conversion |
| `trial_start` | `Trial Start` | `[TBD-OPERATOR]` | `0` | Secondary |
| `cta_click` (id=`cta_book_demo`) | `Book Demo CTA` | `[TBD-OPERATOR]` | `0` | Engagement only |
| `purchase` (offline import) | `Closed Won` | `[TBD-OPERATOR]` | `value=arr` | Offline conv import w/ GCLID |

- Enhanced Conversions: ON; pass user_data (sha256 email + name + phone) on `demo_request` and `trial_start`.
- Attribution: Data-driven (auto-Google) once 50 conversions in 30 days; manual last-click before then.

### 2.2 LinkedIn Insight Tag
- Installed sitewide via GTM, partner ID `[TBD-OPERATOR]`.
- Conversion definitions (LCM → Account Assets → Conversions):

| LCM conv name | Source event | Match | Type |
|---------------|--------------|-------|------|
| LI_demo_request | `demo_request` | URL `/thank-you/demo` OR event-trigger | Primary |
| LI_trial_start | `trial_start` | URL `/trial/started` | Primary |
| LI_form_start | `form_start` | event | Engagement |
| LI_cta_book_demo | `cta_click` w/ `cta_id` ∈ {`cta_book_demo`, `cta_aws_audit`} | event | Engagement |

- Attribution: 30-day click + 1-day view.
- Offline conversion upload via API for `purchase`.

### 2.3 Microsoft UET
- UET tag sitewide via GTM, ID `[TBD-OPERATOR]`.
- Goals:

| UET goal | Source | Type |
|----------|--------|------|
| MS_demo_request | `demo_request` event | Conversion |
| MS_trial_start | `trial_start` | Conversion |
| MS_cta_book_demo | `cta_click` filter | Engagement |

- Offline import via Microsoft Conversion Import.

### 2.4 Reddit Pixel
- Reddit Pixel sitewide via GTM, ID `[TBD-OPERATOR]`.
- Standard events mapped:

| Reddit event | Source |
|--------------|--------|
| `Lead` | `demo_request` |
| `SignUp` | `trial_start` |
| `ViewContent` | `page_view` on `/blog/*` |
| `AddToCart` (proxy for newsletter) | `form_submit` w/ `form_id=newsletter` |
| `Purchase` | `purchase` (offline) |

### 2.5 Meta Pixel (reserved for retargeting only — no prospecting in M1)
- Pixel sitewide via GTM (CAPI optional, recommended in M2). ID `[TBD-OPERATOR]`.
- Standard events mapped:

| Meta event | Source |
|------------|--------|
| `PageView` | `page_view` |
| `ViewContent` | `page_view` on `/blog/*`, `/compare/*` |
| `Lead` | `demo_request` |
| `StartTrial` | `trial_start` |
| `Purchase` | `purchase` |

### 2.6 GA4 (always-on, source of truth for first-party)
All events pushed to GA4 via GTM `gtag` config, with full param set per `analytics/tag-plan.md`.

### 2.7 Reddit + Meta Pixel deduplication
- For events where both client-side pixel and CAPI fire: pass `event_id` (GUID) to dedupe.

## 3. Event → channel attribution matrix

| Event | Google Ads | LinkedIn | Microsoft | Reddit | Meta | GA4 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| page_view | — | engagement | — | ViewContent | PageView | ✅ |
| scroll_75 | — | — | — | — | — | ✅ |
| cta_click | engagement | engagement | engagement | — | — | ✅ |
| form_start | — | engagement | — | — | — | ✅ |
| form_submit | — | — | — | — | — | ✅ |
| demo_request | **PRIMARY** | **PRIMARY** | **PRIMARY** | Lead | Lead | ✅ |
| trial_start | secondary | secondary | secondary | SignUp | StartTrial | ✅ |
| trial_complete | — | — | — | — | — | ✅ |
| purchase (offline) | offline import | offline import | offline import | offline | offline (CAPI) | ✅ |
| login | — | — | — | — | — | ✅ |
| search | — | — | — | — | — | ✅ |
| video_play | — | — | — | — | — | ✅ |

## 4. QA before launch
1. GTM Preview Mode walk-through of `/`, `/aws`, `/pricing`, `/compare/*`, `/blog/*` — every event in section 1 must fire at the right moment.
2. Tag Assistant (Google) confirms Google Ads conversion + GA4 hit for `demo_request`.
3. LinkedIn Tag Assistant confirms Insight Tag + conversion fire.
4. Microsoft UET Tag Helper confirms.
5. Reddit Pixel Helper confirms.
6. Synthetic test submission from a non-customer email with `?test=1` UTM — verify it appears in each platform within 24h.
7. CRM end-to-end: a synthetic `demo_request` reaches CRM and Closed-Won → Closed-Won is uploaded back to ad platforms within 7 days.

## 5. Operator deps
- `[TBD-OPERATOR]` All conversion IDs (Google, LI, MS, Reddit, Meta).
- `[TBD-OPERATOR]` Offline-conversion import path from CRM.
- `[TBD-OPERATOR]` GTM container ID and admin access.
