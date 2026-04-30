---
artifact: utm-taxonomy-enforcement-guide
date: 2026-04-30
purpose: single source of truth for every UTM string used across CostSage marketing
audience: every agent + operator producing trackable links
---

# UTM Taxonomy Enforcement Guide

> **Rule of thumb:** if a link goes anywhere a human will click, it has a UTM. No exceptions.

## Canonical structure

```
?utm_source=<channel>&utm_medium=<format>&utm_campaign=<initiative>&utm_content=<variant>&utm_term=<keyword-or-audience>
```

## Per-channel conventions

### Email (V6)
- `utm_source=email`
- `utm_medium=` one of: `cold` (cold-outreach sequences), `nurture` (lifecycle drips), `newsletter`, `promo`, `transactional`
- `utm_campaign=<sequence-or-issue-name>` e.g. `cold-aws-saas-2026q3` or `newsletter-issue-01`
- `utm_content=<variant>` e.g. `email-1-of-5` or `subject-a` for A/B
- `utm_term=` rarely used; for persona segmentation use `utm_term=cto` / `utm_term=finops-lead`

### Paid Search (V7)
- `utm_source=` `google` / `microsoft-bing`
- `utm_medium=cpc`
- `utm_campaign=` campaign name from V3 brief, e.g. `google-search-aws-cost-tools-q3`
- `utm_content=` ad-group + ad-variant, e.g. `awsoptimization-rsa-1`
- `utm_term=` actual keyword (Google's `{keyword}` substitution token)

### Paid Social (V7)
- `utm_source=` `linkedin` / `meta` / `reddit` / `x`
- `utm_medium=` `paid-social` (or `paid-display` for Meta display)
- `utm_campaign=<brief-slug>`
- `utm_content=<creative-variant>` e.g. `cto-single-image-v1` / `cto-carousel-v2`
- `utm_term=<audience>` e.g. `cto-saas-50-500`

### Organic Social (V5)
- `utm_source=` `linkedin-organic` / `x-organic` / `reddit-organic` / `youtube`
- `utm_medium=social`
- `utm_campaign=` content theme, e.g. `editorial-q3-week-05`
- `utm_content=` post-id from posting queue, e.g. `linkedin-w05-post-3`

### Review sites (V1 GEO + V7)
- `utm_source=` `g2` / `capterra` / `trustradius` / `alternativeto`
- `utm_medium=review-site`
- `utm_campaign=organic-listing` (for free listings) or `sponsored-q3` for paid placements
- `utm_content=<placement-id>`

### AWS Marketplace (V1 + V3)
- `utm_source=aws-marketplace`
- `utm_medium=listing`
- `utm_campaign=organic-listing`
- `utm_content=` page section, e.g. `homepage-cta` / `pricing-cta`

## URL builder snippet (Python)

```python
def utm(base, source, medium, campaign, content="", term=""):
    from urllib.parse import urlencode
    params = {"utm_source": source, "utm_medium": medium, "utm_campaign": campaign}
    if content: params["utm_content"] = content
    if term: params["utm_term"] = term
    return f"{base}?{urlencode(params)}"
```

## URL builder snippet (Bash)

```bash
utm() {
  local base="$1" source="$2" medium="$3" campaign="$4" content="$5" term="$6"
  local q="utm_source=$source&utm_medium=$medium&utm_campaign=$campaign"
  [ -n "$content" ] && q="$q&utm_content=$content"
  [ -n "$term" ] && q="$q&utm_term=$term"
  echo "$base?$q"
}
```

## Audit examples (UTM strings already used in the engagement)

Pulled from `/lp/*` LPs and email sequences:

- `?utm_source=paid&utm_medium=lp&utm_campaign=google-search-aws` (from /lp/google-aws-cost-tools)
- `?utm_source=paid&utm_medium=lp&utm_campaign=linkedin-cto-q3` (from /lp/linkedin-cto-aws-saas)
- `?utm_source=paid&utm_medium=lp&utm_campaign=linkedin-finops-q3` (from /lp/linkedin-finops-lead)
- `?utm_source=paid&utm_medium=lp&utm_campaign=bing-aws-q3` (from /lp/bing-aws-cost)
- `?utm_source=paid&utm_medium=lp&utm_campaign=reddit-aws-devops-q3` (from /lp/reddit-devops)
- `?utm_source=email&utm_medium=ask&utm_campaign=review-request&utm_content=g2-v1` (from review-request emails)

## Enforcement

- Pre-publish hook: scan all new links in HTML/Markdown; flag any external link to `costsage.ai/*` lacking UTM.
- Daily audit: `clients/costsage/feeds/_scripts/audit-utm.py` (TODO) — crawls all pages, extracts links, reports UTM coverage %.
- Reporting: V3 weekly digest includes `utm_coverage_pct`. Target: 100%.

## What to do when

| Scenario | Action |
|---|---|
| New ad campaign | Use V7 paid-search/social convention above |
| New blog post link in newsletter | Use email convention with `utm_campaign=newsletter-issue-NN` |
| Founder LinkedIn post linking to a pillar | Use organic-social convention |
| Press mention link-back | `?utm_source=press&utm_medium=editorial&utm_campaign=<outlet>` |
| Internal docs / Slack | No UTM needed (not external traffic) |

## Red flags

- ❌ A link without `utm_source` going to costsage.ai from outside.
- ❌ Two different campaigns sharing the same `utm_campaign` value (collision).
- ❌ Mixed-case (`utm_campaign=Newsletter-Issue-01` vs `utm_campaign=newsletter-issue-01`) — always lowercase + dash-separated.
- ❌ Spaces or special chars in any UTM value — use hyphens.
