# UTM Taxonomy — Loopgate

> Governance: Head of Analytics owns. Non-conforming URLs are tracking defects; launch gate blocks.

## Params
| Param | Rule |
|---|---|
| utm_source | lowercase platform: google, linkedin, meta, reddit, newsletter, podcast-{name}, github |
| utm_medium | `cpc \| paid-social \| organic-social \| email \| referral \| display \| retargeting \| affiliate \| podcast \| sponsorship` |
| utm_campaign | `{yyyy}-q{N}-{objective}-{audience}` e.g., `2026-q2-demand-platform-eb` |
| utm_content | creative variant: `headline-{v}-cta-{v}-audience-{v}` e.g., `headline-tco-cta-calc-audience-priya` |
| utm_term | keyword (paid search) or audience id (paid social) |

## Allowed objective values
`awareness, demand, capture, retarget, retention, launch, abm`

## Allowed audience values
`priya (platform-eb), marco (staff-eng), rina (pm), migration-ld, migration-homegrown, abm-tier1, abm-tier2`

## Validator regex
```
^utm_source=(google|linkedin|meta|reddit|newsletter|podcast-[a-z0-9-]+|github|referral|email|direct)&utm_medium=(cpc|paid-social|organic-social|email|referral|display|retargeting|affiliate|podcast|sponsorship)&utm_campaign=\d{4}-q[1-4]-(awareness|demand|capture|retarget|retention|launch|abm)-[a-z0-9-]+&utm_content=[a-z0-9-]+(&utm_term=[a-z0-9_-]+)?$
```

## Registry (append-only)
| Campaign | utm_campaign | Launched | Owner | Status |
|---|---|---|---|---|
| Q2 Platform-EB demand (Google) | 2026-q2-demand-platform-eb | 2026-05-01 | Sam | planned |
| Q2 LD-migration capture (LinkedIn) | 2026-q2-capture-migration-ld | 2026-05-08 | Sam | planned |
| Q2 SEO pillar launch (organic referrers) | 2026-q2-launch-seo-pillar | 2026-05-15 | Leo | planned |
| Onboarding email sequence | 2026-q2-retention-onboarding | 2026-05-01 | Rae | planned |
| ABM tier 1 outreach | 2026-q2-abm-tier1 | 2026-06-01 | Sam | planned |

## Change process
New values via PR; Head of Analytics approves; backfill plan required for live URLs.
