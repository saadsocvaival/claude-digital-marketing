# UTM Taxonomy — {{client}}

> Governance: any UTM deviation blocks campaign launch. Any live URL without all 5 params is a tracking defect owned by Head of Analytics.

## Params
| Param | Rule | Examples |
|---|---|---|
| utm_source | lowercase, platform | google, linkedin, meta, newsletter |
| utm_medium | channel type | cpc, paid-social, email, organic-social, referral, display, retargeting |
| utm_campaign | `{yyyy}-{qN}-{objective}-{audience}` | 2026-q2-demand-devleads |
| utm_content | creative variant | hero-v3-testimonial |
| utm_term | keyword / audience segment | {keyword} on paid search; audience id elsewhere |

## Rules
1. All lowercase, hyphen-separated, no spaces, no special chars.
2. No PII, no raw campaign IDs, no tracking-platform-generated auto values (unless mapped).
3. Source of truth: this file + `/clients/{id}/feeds/utm-registry.md`.
4. Landing pages MUST preserve UTMs to the CRM event; check monthly.

## Validator
Regex to enforce:
```
^utm_source=[a-z0-9-]+&utm_medium=(cpc|paid-social|email|organic-social|referral|display|retargeting|affiliate|direct)&utm_campaign=\d{4}-q[1-4]-(awareness|demand|capture|retarget|retention|launch)-[a-z0-9-]+.*$
```

## Change process
New values proposed via PR; Head of Analytics approves; backfill plan required for already-live URLs.
