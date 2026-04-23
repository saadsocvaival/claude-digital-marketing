# Ownership & Authority Matrix

Canonical authority map for every agent in the system. Source of truth for "who can do what, who do they escalate to, and when must they refuse." Every `.agent.md` file restates its row here in its own frontmatter; if they drift, this document wins until reconciled.

Derived from `01-playbook/department-level/role-inventory.md` (roles) and `01-playbook/department-level/tool-inventory.md` (tools).

## Approval Gates Referenced

- **budget-threshold** — any paid spend commitment above a configured threshold. Playbook §5.3 defines: Vertical Lead < $3k; Head of DM $3k–$15k; CMO + Head of DM > $15k.
- **external-publishing** — any artifact published outside Vaival's owned properties (ads, guest posts, press, third-party syndication).
- **strategy-change** — changes to ICP, positioning, pricing narrative, channel mix, or quarterly priorities.
- **new-credential** — onboarding any new platform, API key, OAuth app, or data-sharing relationship (tool procurement gated by Marketing Ops per §5.5).

Full gate specs in `11-approvals/gates/`.

## Authority Matrix — Tier 1 & 2

| Agent | owner_tier | authority_scope | can_delegate_to | escalates_to | requires_approval_for | tools_owned |
|---|---|---|---|---|---|---|
| founder-principal | tier-1 | Strategy, ICP, positioning, budget envelope, final sign-off | cmo | — | (is the approver) | — |
| cmo | tier-2 | Brand, messaging, strategy approval, >$15k spend, crisis comms | head-of-digital-marketing, all cross-cutting | founder-principal | strategy-change | Notion, Slack, Looker Studio |
| head-of-digital-marketing | tier-2 | Department leadership, budget ownership, $3k–$15k approval, vertical-manager management, headcount | All 7 Managers, all cross-cutting | cmo | budget-threshold (>$15k), strategy-change | Notion, Asana, Slack, Google Sheets, Looker Studio |

## Authority Matrix — Tier 3 Managers

| Agent | vertical | authority_scope | can_delegate_to | escalates_to | requires_approval_for | key_tools_owned |
|---|---|---|---|---|---|---|
| seo-manager | seo-aeo-geo | SEO + AEO + GEO strategy, keyword roadmap, team leadership | seo tier-4 + tier-5 in vertical | head-of-digital-marketing | external-publishing (off-site), new-credential | SEMrush, Ahrefs, GSC, Screaming Frog, AlsoAsked, Clearscope, Mention.com, all GEO AI tools |
| paid-media-manager | paid-media-ppc | Paid strategy, budget, Google + LinkedIn campaigns, CRO decisions | paid tier-4 + tier-5 | head-of-digital-marketing | budget-threshold, new-credential | Google Ads, LinkedIn Campaign Manager, Meta Business Suite, GTM, Looker Studio |
| content-marketing-manager | content-marketing | Content strategy, editorial calendar, SEO collaboration | content tier-4 + tier-5 | head-of-digital-marketing | external-publishing | Clearscope, Surfer SEO, Figma, Canva Pro, HubSpot Marketing Hub, Notion |
| social-media-manager | social-media | Channel strategy, content calendar, crisis management | social tier-4 + tier-5 | head-of-digital-marketing | external-publishing | Sprout Social, Buffer, Figma, Canva Pro |
| crm-email-manager | email-crm | Lifecycle, segmentation, automation, lead-scoring | email-crm tier-4 + tier-5 | head-of-digital-marketing | external-publishing (mass sends), new-credential | HubSpot CRM, HubSpot Marketing Hub, Mailchimp, Klaviyo, mail-tester.com |
| marketing-ops-manager | analytics-ops | Martech stack, attribution, reporting, CRM data quality, tool access | analytics-ops tier-4 + tier-5 | head-of-digital-marketing | new-credential (data source), any new tool procurement | GA4, GTM, Looker Studio, HubSpot attribution, Triple Whale, Google Sheets |
| web-development-lead | website-development | Site architecture, CRO, frontend implementation, CMS ownership | web tier-4 + tier-5 | head-of-digital-marketing | external-publishing (prod deploys), strategy-change (IA) | Webflow, WordPress, Figma, GTM, GSC, GitHub, UptimeRobot, VWO |

## Authority Matrix — Tier 4 Specialists

| Agent | vertical | reports_to | tools_owned |
|---|---|---|---|
| seo-specialist | seo-aeo-geo | seo-manager | SEMrush, Ahrefs, GSC, Screaming Frog, Google Rich Results Test, Clearscope, Surfer SEO |
| technical-seo-aeo-specialist | seo-aeo-geo | seo-manager | Screaming Frog, GSC, Google Rich Results Test, PageSpeed Insights, GitHub |
| aeo-specialist | seo-aeo-geo | seo-manager | SEMrush, AlsoAsked, AnswerThePublic, Google Rich Results Test, GSC |
| link-building-digital-pr-specialist | seo-aeo-geo | seo-manager | Ahrefs, SEMrush, Pitchbox, Mention.com, G2, Capterra, Trustpilot |
| paid-media-specialist | paid-media-ppc | paid-media-manager | Meta Business Suite, LinkedIn Campaign Manager, Google Ads, GTM, Microsoft Clarity |
| cro-landing-page-specialist | paid-media-ppc | paid-media-manager | VWO, Microsoft Clarity, Hotjar, Figma, GA4 |
| senior-content-writer | content-marketing | content-marketing-manager | Clearscope, Surfer SEO, Notion, GA4 |
| graphic-designer | content-marketing | content-marketing-manager | Figma, Canva Pro |
| video-multimedia-producer | content-marketing | content-marketing-manager | Figma, Canva Pro |
| content-editor | content-marketing | content-marketing-manager | Notion |
| social-media-specialist | social-media | social-media-manager | Sprout Social, Buffer, Canva Pro |
| short-form-video-creator | social-media | social-media-manager | Canva Pro, Figma |
| email-marketing-specialist | email-crm | crm-email-manager | HubSpot Marketing Hub, Mailchimp, Klaviyo, mail-tester.com |
| marketing-automation-specialist | email-crm | crm-email-manager | HubSpot CRM, HubSpot Marketing Hub, GTM |
| marketing-data-analyst | analytics-ops | marketing-ops-manager | GA4, Looker Studio, HubSpot CRM, Google Sheets |
| front-end-developer | website-development | web-development-lead | Webflow, WordPress, GitHub, GTM, PageSpeed Insights, GTmetrix, VWO |
| ux-ui-designer | website-development | web-development-lead | Figma |
| cro-specialist | website-development | web-development-lead | VWO, Microsoft Clarity, Hotjar, Figma, GA4 |

Tier-4 specialists may delegate to Tier-5 coordinators within the same vertical only. They escalate to their manager. They refuse cross-vertical invocation.

## Authority Matrix — Tier 5 Coordinators / Executives

| Agent | vertical | reports_to | key_tools |
|---|---|---|---|
| geo-monitoring-coordinator | seo-aeo-geo | aeo-specialist | ChatGPT, Claude, Gemini, Perplexity, Copilot, Mention.com, Google Alerts, Notion |
| keyword-research-coordinator | seo-aeo-geo | seo-specialist | SEMrush, Ahrefs, AlsoAsked |
| paid-search-coordinator | paid-media-ppc | paid-media-specialist | Google Ads, GA4 |
| paid-social-coordinator | paid-media-ppc | paid-media-specialist | Meta Business Suite, LinkedIn Campaign Manager |
| content-writer-junior | content-marketing | senior-content-writer | Notion, Clearscope |
| content-production-coordinator | content-marketing | content-marketing-manager | Notion, Asana |
| community-manager | social-media | social-media-specialist | Sprout Social |
| social-scheduling-coordinator | social-media | social-media-specialist | Buffer, Sprout Social |
| email-production-coordinator | email-crm | email-marketing-specialist | HubSpot Marketing Hub, Mailchimp, mail-tester.com |
| lifecycle-journey-coordinator | email-crm | crm-email-manager | HubSpot Marketing Hub, HubSpot CRM |
| deliverability-analyst | email-crm | email-marketing-specialist | mail-tester.com, HubSpot Marketing Hub |
| attribution-analyst | analytics-ops | marketing-data-analyst | GA4, HubSpot attribution, Looker Studio |
| dashboard-coordinator | analytics-ops | marketing-data-analyst | Looker Studio, GA4 |
| utm-tag-qa-coordinator | analytics-ops | marketing-ops-manager | GTM, GA4 |
| cms-page-builder | website-development | front-end-developer | Webflow, WordPress, GTM |
| qa-accessibility-reviewer | website-development | web-development-lead | PageSpeed Insights, GTmetrix |
| experimentation-coordinator | website-development | cro-specialist | VWO, GA4, Microsoft Clarity |

Tier-5 is the execution layer. They do not delegate further. They escalate to their named `reports_to`. They refuse any invocation originating outside their vertical.

## Cross-Cutting Agents

| Agent | authority_scope | escalates_to | refuses_when |
|---|---|---|---|
| resource-discovery | Inventory credentials, platforms, data sources | head-of-digital-marketing | Acting on undocumented credential |
| feasibility-validator | Pre-flight budget/resource/timeline/capability/platform checks | head-of-digital-marketing | Plan fails any of the 5 checks |
| quality-assurance | Output validation, deterministic-output, brand-voice | Originating Manager → head-of-digital-marketing | Output violates schema or brand-voice |
| compliance-legal | Legal review of external artifacts, credential onboarding | head-of-digital-marketing → cmo → founder | Jurisdictional or consent-law violation |
| recursive-optimizer | Feedback-loop ingestion, SOP/framework updates | head-of-digital-marketing | Updating a framework without ledger evidence |

## Notes

- **Delegation depth is capped at 5** (Founder → CMO → Head of DM → Manager → Specialist → Coordinator). Deeper chains are refused by the decision-boundary layer.
- All rows require `audit_fields` once agents are specified: at minimum `decision_id`, `input_hash`, `policy_version`, `output_ref`, `confidence_score`.
- Tool ownership above names the tools a role directly operates. Read-only cross-vertical tool access (e.g. Paid Media reading HubSpot) is not ownership.
