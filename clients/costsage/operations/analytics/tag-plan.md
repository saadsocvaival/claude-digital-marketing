# GTM Tag & Event Plan — CostSage.ai

> Implementation-ready spec. Anyone with GTM access should be able to build every tag/trigger/variable below without follow-up. Site GTM container ID: `[TBD-OPERATOR]`.

## 0. Conventions
- Event names: `snake_case`, present tense, max 32 chars.
- Param names: `snake_case`.
- All events push to `dataLayer` first, then GTM dispatches to GA4 + per-pixel tags.
- All PII (email, phone) is **hashed sha256 client-side** before leaving the browser, except where the platform requires plaintext (LinkedIn Customer Match accepts plaintext via API, not via pixel — never pass plaintext via pixel).

## 1. dataLayer push template
```js
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  event: '<event_name>',
  page_path: location.pathname,
  page_url: location.href,
  utm_source: <from URL or cookie>,
  utm_medium: ...,
  utm_campaign: ...,
  utm_content: ...,
  utm_term: ...,
  // event-specific params follow:
  ...
});
```

## 2. Variables (GTM)

| GTM variable | Type | Source |
|--------------|------|--------|
| `dlv_event` | Data Layer Variable | `event` |
| `dlv_cta_id` | DLV | `cta_id` |
| `dlv_cta_label` | DLV | `cta_label` |
| `dlv_form_id` | DLV | `form_id` |
| `dlv_form_type` | DLV | `form_type` |
| `dlv_email_hash` | DLV | `email_hash` |
| `dlv_company_size` | DLV | `company_size` |
| `dlv_monthly_spend_band` | DLV | `monthly_spend_band` |
| `dlv_plan` | DLV | `plan` |
| `dlv_value` | DLV | `value` |
| `dlv_currency` | DLV | `currency` |
| `cookie_utm_source` | 1st-party cookie | `cs_utm_source` (90d) |
| `cookie_utm_campaign` | 1st-party cookie | `cs_utm_campaign` (90d) |
| `js_user_agent` | JS | `navigator.userAgent` |
| `lookup_page_type` | Lookup table | based on URL path |

## 3. Triggers

| Trigger name | Type | Conditions |
|--------------|------|------------|
| `trg_pageview_all` | Page View — Window Loaded | All pages |
| `trg_scroll_75` | Scroll Depth | Vertical, 75% |
| `trg_cta_click` | Custom Event | `dlv_event` equals `cta_click` |
| `trg_form_start` | Custom Event | `dlv_event` equals `form_start` |
| `trg_form_submit` | Custom Event | `dlv_event` equals `form_submit` |
| `trg_demo_request` | Custom Event | `dlv_event` equals `demo_request` |
| `trg_trial_start` | Custom Event | `dlv_event` equals `trial_start` |
| `trg_trial_complete` | Custom Event | `dlv_event` equals `trial_complete` |
| `trg_purchase` | Custom Event | `dlv_event` equals `purchase` |
| `trg_login` | Custom Event | `dlv_event` equals `login` |
| `trg_logout` | Custom Event | `dlv_event` equals `logout` |
| `trg_search` | Custom Event | `dlv_event` equals `search` |
| `trg_video_play` | Custom Event | `dlv_event` equals `video_play` |

## 4. Events (full spec)

### 4.1 `page_view`
- **Trigger:** `trg_pageview_all`.
- **Params:** `page_path`, `page_url`, `page_title`, `referrer`, `utm_*`, `page_type` (`home|aws|azure|pricing|compare|blog|app`).
- **Destinations:**
  - GA4: built-in `page_view`.
  - LinkedIn Insight Tag: built-in.
  - Microsoft UET: built-in.
  - Reddit Pixel: `ViewContent` (only on `/blog/*`, `/compare/*`).
  - Meta Pixel: `PageView`.
  - PostHog: `$pageview`.
- **Site code:** auto via GTM page-load tag.

### 4.2 `scroll_75`
- **Trigger:** `trg_scroll_75`.
- **Params:** `page_path`, `page_type`.
- **Destinations:** GA4, PostHog.
- **Site code:** GTM Scroll Depth trigger only.

### 4.3 `cta_click`
- **Trigger:** `trg_cta_click`.
- **Params (required):** `cta_id` (e.g., `cta_book_demo`), `cta_label` (visible text), `page_path`.
- **Destinations:** GA4, PostHog. LinkedIn LI_cta_book_demo conversion if `cta_id ∈ {cta_book_demo, cta_aws_audit}`.
- **Site code:** Every CTA element gets `data-cta-id="<id>"`. Click handler:
```js
document.querySelectorAll('[data-cta-id]').forEach(el => {
  el.addEventListener('click', () => {
    dataLayer.push({
      event: 'cta_click',
      cta_id: el.dataset.ctaId,
      cta_label: el.innerText.trim().slice(0, 80),
      page_path: location.pathname
    });
  });
});
```

### 4.4 `form_start`
- **Trigger:** `trg_form_start` (first focus on tracked form).
- **Params:** `form_id` (`demo`, `newsletter`, `trial`, `contact`), `page_path`.
- **Destinations:** GA4, PostHog, LinkedIn LI_form_start.
- **Site code:**
```js
document.querySelectorAll('form[data-form-id]').forEach(form => {
  let started = false;
  form.querySelector('input,textarea,select').addEventListener('focus', () => {
    if (started) return;
    started = true;
    dataLayer.push({ event: 'form_start', form_id: form.dataset.formId, page_path: location.pathname });
  }, { once: true });
});
```

### 4.5 `form_submit`
- **Trigger:** `trg_form_submit` on successful POST 2xx.
- **Params:** `form_id`, `form_type` (`demo|newsletter|trial|contact`), `email_hash`, `company_size`, `monthly_spend_band`, `page_path`.
- **Destinations:** GA4, PostHog. Conditional: also pushes `demo_request`, `trial_start` events depending on `form_id`.

### 4.6 `demo_request`
- **Trigger:** `trg_demo_request` (pushed by form-submit handler when `form_id=demo`).
- **Params:** `email_hash`, `company`, `company_domain`, `role`, `monthly_spend_band`, `page_path`, `utm_*`.
- **Destinations:** GA4 conversion, Google Ads conversion `Demo Request — Web`, LinkedIn LI_demo_request, Microsoft UET MS_demo_request, Reddit `Lead`, Meta `Lead`, PostHog, CRM webhook.

### 4.7 `trial_start`
- **Trigger:** `trg_trial_start`.
- **Params:** `email_hash`, `plan`, `page_path`.
- **Destinations:** GA4, Google Ads `Trial Start`, LinkedIn LI_trial_start, Microsoft `MS_trial_start`, Reddit `SignUp`, Meta `StartTrial`, PostHog, CRM.

### 4.8 `trial_complete`
- **Trigger:** `trg_trial_complete`.
- **Params:** `user_id_hash`, `plan`, `activation_score` (0–100), `days_to_activation`.
- **Destinations:** GA4, PostHog, CRM.

### 4.9 `purchase`
- **Trigger:** Offline import from CRM (no client-side fire).
- **Params:** `email_hash`, `value`, `currency`, `arr`, `plan`, `gclid`, `fbclid`, `li_fat_id`, `msclkid`, `rdt_cid`.
- **Destinations:** Google Ads offline conv, LinkedIn offline API, Microsoft Conversion Import, Reddit CAPI, Meta CAPI, GA4 (Measurement Protocol), PostHog.

### 4.10 `login`
- **Trigger:** `trg_login`.
- **Params:** `user_id_hash`.
- **Destinations:** GA4, PostHog.

### 4.11 `logout`
- **Trigger:** `trg_logout`.
- **Params:** `user_id_hash`.
- **Destinations:** GA4, PostHog.

### 4.12 `search`
- **Trigger:** `trg_search`.
- **Params:** `query`, `result_count`, `page_path`.
- **Destinations:** GA4, PostHog.

### 4.13 `video_play`
- **Trigger:** `trg_video_play` (YouTube/Wistia API hooked).
- **Params:** `video_id`, `video_title`, `video_provider`, `page_path`.
- **Destinations:** GA4, PostHog.

## 5. Tags

| Tag name | Type | Trigger(s) | Notes |
|----------|------|-----------|-------|
| `t_ga4_config` | GA4 Configuration | `trg_pageview_all` | Sends user_id (hashed) when logged-in. |
| `t_ga4_event_*` | GA4 Event | per-event triggers | One per event in §4. |
| `t_ga_ads_linker` | Conversion Linker | `trg_pageview_all` | First-party cookies. |
| `t_ga_ads_demo` | Google Ads Conversion | `trg_demo_request` | Enhanced Conv ON. |
| `t_ga_ads_trial` | Google Ads Conversion | `trg_trial_start` | |
| `t_li_insight` | LinkedIn Insight Tag | `trg_pageview_all` | |
| `t_li_demo` | LinkedIn Conv | `trg_demo_request` | |
| `t_li_trial` | LinkedIn Conv | `trg_trial_start` | |
| `t_ms_uet` | Microsoft UET | `trg_pageview_all` | |
| `t_ms_demo` | UET Goal | `trg_demo_request` | |
| `t_rdt_pixel` | Reddit Pixel | `trg_pageview_all` | |
| `t_rdt_lead` | Reddit Pixel — Lead | `trg_demo_request` | |
| `t_meta_pixel` | Meta Pixel | `trg_pageview_all` | |
| `t_meta_lead` | Meta Pixel — Lead | `trg_demo_request` | |
| `t_posthog` | PostHog Init | `trg_pageview_all` | If PostHog enabled. |

## 6. Consent
- Cookie banner via Cookiebot or HouseofCookies — `[TBD-OPERATOR]`.
- Until consent, only essential tags fire (consent mode v2 in Google).
- All marketing pixels gated on `analytics_storage = granted`.

## 7. QA checklist before publish
- Preview Mode walk: every URL fires the right events with correct params.
- Tag Assistant Companion shows green for GA + Google Ads.
- LI / MS / Reddit / Meta browser pixel-helper extensions verify.
- Synthetic `?test=1` data segregated from prod via GA4 secondary stream.
- Consent banner respected (block test).

**Total tracked events: 13.**
