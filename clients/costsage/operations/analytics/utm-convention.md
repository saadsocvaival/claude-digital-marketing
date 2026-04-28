# UTM Convention — CostSage.ai (Single Source of Truth)

> Every paid + owned link uses this convention. No exceptions. Inconsistent UTMs poison attribution; always validate via the URL builder template before publishing.

## 1. Parameter rules

- Lowercase only.
- No spaces — use underscores.
- No PII, no internal IDs that change between platforms.
- Stable: do not rename live campaigns; archive + start new.

## 2. Per-channel taxonomy

| Channel | utm_source | utm_medium | utm_campaign pattern | utm_content pattern | utm_term pattern |
|---------|-----------|------------|----------------------|---------------------|------------------|
| Google Ads — Search | `google` | `cpc` | `gs_<theme>_<quarter>` (e.g., `gs_aws_cost_tools_q3`) | `{ad_id}` (auto-token) | `{keyword}` (auto-token) |
| Google Ads — Display | `google` | `display` | `gd_<theme>_<quarter>` | `{creative_id}` | n/a |
| Google Ads — YouTube | `youtube` | `video` | `yt_<theme>_<quarter>` | `{ad_id}` | n/a |
| Microsoft Advertising | `bing` | `cpc` | `ms_<theme>_<quarter>` | `{AdId}` | `{keyword}` |
| LinkedIn — Sponsored | `linkedin` | `paid_social` | `li_<persona>_<quarter>` | `<ad_slot>_<format>` (e.g., `ad1_si_margin`) | n/a |
| LinkedIn — Conversation Ad | `linkedin` | `paid_social_conv` | `li_<persona>_<quarter>_conv` | `<button_id>` | n/a |
| Reddit | `reddit` | `paid_social` | `rdt_<theme>_<quarter>` | `<ad_slot>` | `<subreddit>` |
| Meta — retargeting | `meta` | `paid_social_rt` | `meta_rt_<theme>_<quarter>` | `<adset>_<creative>` | n/a |
| G2 / Capterra | `g2` / `capterra` | `review_site` | `rev_<quarter>` | `<placement>` (e.g., `g2_category`) | n/a |
| Email — newsletter | `newsletter` | `email` | `nl_<yyyy_mm_dd>` | `<link_position>` (e.g., `hero`, `cta_1`) | n/a |
| Email — drip | `<drip_name>` | `email` | `drip_<name>_step_<n>` | `<link_position>` | n/a |
| Organic social | `linkedin_org` / `x_org` / `youtube_org` | `social` | `org_<yyyy_mm>` | `<post_id>` | n/a |
| Partner / referral | `<partner_slug>` | `referral` | `partner_<name>_<quarter>` | `<placement>` | n/a |
| QR codes (events) | `qr` | `offline` | `event_<event_slug>_<yyyy>` | `<placement>` | n/a |

## 3. Reserved values

- `utm_source=direct` is **not used** (direct = no UTM).
- `utm_source=internal` is **forbidden** (internal links do not carry UTMs; use internal `data-cta-id` instead).
- `utm_medium` enum: `cpc | display | video | paid_social | paid_social_rt | paid_social_conv | email | social | referral | review_site | offline`.

## 4. URL builder template

```
https://costsage.ai/<path>?utm_source=<source>&utm_medium=<medium>&utm_campaign=<campaign>&utm_content=<content>&utm_term=<term>
```

Use this Google Sheet as the single builder: `[TBD-OPERATOR-LINK: ops/Marketing UTM Builder]`.

Validation checklist (all must pass before publishing):
- [ ] All five params present (use `_` if no value, e.g., `utm_term=_`).
- [ ] Lowercase, no spaces.
- [ ] Source ∈ enum.
- [ ] Medium ∈ enum.
- [ ] Campaign matches per-channel pattern.

## 5. Examples (every active channel)

| Channel | Example URL |
|---------|-------------|
| Google Search AWS | `https://costsage.ai/aws?utm_source=google&utm_medium=cpc&utm_campaign=gs_aws_cost_tools_q3&utm_content={creative}&utm_term={keyword}` |
| Google Search FinOps | `https://costsage.ai/aws?utm_source=google&utm_medium=cpc&utm_campaign=gs_finops_platform_q3&utm_content={creative}&utm_term={keyword}` |
| LinkedIn CTO | `https://costsage.ai/aws?utm_source=linkedin&utm_medium=paid_social&utm_campaign=li_cto_q3&utm_content=ad1_si_margin&utm_term=_` |
| LinkedIn FinOps | `https://costsage.ai/compare/cloudzero-vs-costsage?utm_source=linkedin&utm_medium=paid_social&utm_campaign=li_finops_q3&utm_content=ad1_si_compare&utm_term=_` |
| Microsoft Bing | `https://costsage.ai/aws?utm_source=bing&utm_medium=cpc&utm_campaign=ms_aws_cost_tools_q3&utm_content={AdId}&utm_term={keyword}` |
| Reddit | `https://costsage.ai/blog/aws-cost-optimisation-best-practices?utm_source=reddit&utm_medium=paid_social&utm_campaign=rdt_aws_devops_q3&utm_content=ad1_guide&utm_term=r_aws` |
| G2 | `https://costsage.ai/compare/cloudzero-vs-costsage?utm_source=g2&utm_medium=review_site&utm_campaign=rev_q3&utm_content=g2_category&utm_term=_` |
| Capterra | `https://costsage.ai/aws?utm_source=capterra&utm_medium=review_site&utm_campaign=rev_q3&utm_content=capterra_top3&utm_term=_` |
| Newsletter | `https://costsage.ai/blog/ri-vs-savings-plans?utm_source=newsletter&utm_medium=email&utm_campaign=nl_2026_05_06&utm_content=hero&utm_term=_` |
| LinkedIn Org | `https://costsage.ai/aws?utm_source=linkedin_org&utm_medium=social&utm_campaign=org_2026_05&utm_content=post_42&utm_term=_` |
| Partner | `https://costsage.ai/?utm_source=finops_foundation&utm_medium=referral&utm_campaign=partner_finops_q3&utm_content=newsletter_slot&utm_term=_` |

## 6. Storage in GA4
- UTMs persist for the session by default.
- Custom dimension: `first_touch_campaign` and `first_touch_source` set on a 1st-party 90-day cookie via GTM, surfaced as user-scoped CDs in GA4.
- Last-touch is the default attribution. Multi-touch reported via the attribution model in `attribution-model.md`.
