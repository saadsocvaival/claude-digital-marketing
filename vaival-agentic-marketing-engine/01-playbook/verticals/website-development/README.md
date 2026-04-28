---
name: Website Development Vertical
owner_tier: department-head
status: active
phase: 2
playbook_source: §15.1–§15.7
---

# Website Development Vertical

## Charter
Owns the company's most important digital asset — the marketing website. For a SaaS company the website is simultaneously the primary sales tool, brand front door, SEO platform, and lead-capture engine (§15.1). At mid-size, treat the website **like a product** — backlog, sprints, defined owners, continuous testing — never in a state of "done." Highest-leverage activities: improving LP CVR, improving Core Web Vitals, faster campaign-LP delivery (§15.1 mid-size principle box).

## Team Roles + Tier (§15.2)
| Role | Tier | Headcount |
|---|---|---|
| Web Development Lead / Senior FE | Tier 2 (Vertical Lead) | 1 |
| Front-End Developer | Tier 3 | 1–2 |
| UX / UI Designer | Tier 3 | 1 |
| CRO Specialist (shared with Analytics) | Tier 3 | 1 |

Department Head: `head-of-web-experience`.

## KPIs (§15.6)
| KPI | Target | Cadence |
|---|---|---|
| Marketing site CVR (visit → lead) | ≥3% | weekly |
| Paid LP CVR | ≥4% | weekly |
| Core Web Vitals — LCP / CLS / INP | <2.5s / <0.1 / <200ms | weekly |
| Bounce rate (key LPs) | <55% | monthly |
| A/B tests completed / quarter | ≥2 | quarterly |
| Avg page load (mobile) | <3s | weekly |
| Website uptime | 99.9% | continuous |

## Quality Standards (§15.5)
LCP <2.5s · CLS <0.1 · INP <200ms · Mobile-friendly 100% · Page load <3s on 4G · SSL/HTTPS enforced sitewide · 99.9% uptime · zero broken internal links · all forms tested and tracking firing · WCAG 2.1 AA compliance (quarterly audit).

## Weekly Cadence
- Core Web Vitals review (GSC field data + PageSpeed).
- Form-functionality + tracking-firing checks (lead-capture).
- LP backlog grooming with Paid Media + Content.
- A/B test status review with CRO.
- Uptime + error budget review (UptimeRobot).

## Monthly Cadence
- Full site crawl with broken-link sweep.
- Schema validation pass on eligible templates (with SEO).
- Heatmap / session-recording review (Clarity / Hotjar).
- A/B test prioritization (PIE score, §15.4 Workflow B).
- Sprint retro + next-sprint planning.

## Quarterly Cadence
- WCAG 2.1 AA accessibility audit (§15.5).
- Design-system review with UX.
- ≥2 A/B tests completed and documented.
- Performance budget + tech-debt review.

## Key Workflows (linked)
- New Page / Landing Page Request (§15.4 Workflow A — 8-stage, 15-day SLA).
- CRO Testing Cycle (§15.4 Workflow B — hypothesis → PIE → ≥95% sig or 2 weeks → readout).
- `04-workflows/campaign-launch.workflow.md` (LPs supply paid campaigns).
- `04-workflows/secrets-vault-setup.workflow.md` (WP App Password migration).

## Tools / Connectors (linked, §15.3)
- `06-connectors/web-dev/wordpress.connector.md` + `wordpress-application-password.connector.md` (primary CMS for CostSage).
- `06-connectors/web-dev/webflow.connector.md` (alt CMS).
- `06-connectors/analytics/google-tag-manager.connector.md`.
- `06-connectors/analytics/microsoft-clarity.connector.md`, `hotjar.connector.md`.
- `06-connectors/web-dev/vwo.connector.md` / `ab-tasty.connector.md` (testing).
- `06-connectors/web-dev/pagespeed-insights.connector.md`, `gtmetrix.connector.md`.
- `06-connectors/web-dev/uptimerobot.connector.md`.
- `06-connectors/web-dev/github.connector.md` (deploy pipeline).

## Policies + Thresholds
- **Mobile-first**: every new page designed for mobile first (§15.7).
- **Paid LPs**: nav removed, single goal, single CTA — never send paid traffic to homepage (§15.7).
- **Speed is a commercial metric**: page-speed regressions block deploy.
- **Design-system discipline**: ad-hoc design without system components → refuse / refactor.
- **Analytics on every page**: no page goes live without GA4 events, GTM tags firing, conversion goals configured.
- **A/B test discipline**: do not end early; ≥95% statistical significance OR ≥2 weeks (§15.4 Workflow B step 6).
- **WCAG 2.1 AA** — quarterly audit; non-compliance is a business + legal risk.
- **HITL for**: production deploys touching pricing / checkout, redirects on top-50 traffic URLs, robots.txt / sitemap structural changes, schema removals, third-party script additions.

## Refusal / Escalation Triggers
- Deploy without staging QA + tracking-firing confirmation → refuse.
- Direct edits to live pages bypassing CMS / version control → refuse.
- New third-party script (analytics / chat / consent) without privacy review → HITL.
- Mass redirect / domain migration → HITL with rollback plan.
- Accessibility regression to a previously WCAG-compliant page → block deploy.

## Output Artifacts Produced
- Wireframes + Figma designs (UX).
- Built/deployed pages + LPs.
- A/B test briefs + readouts + CRO knowledge-base entries (Notion).
- Core Web Vitals weekly report.
- Quarterly accessibility audit report.

## Rubrics Applied
- `rubrics/landing-page.yaml` — every LP brief + build.
- `rubrics/utm.yaml` — every outbound link template.
- `rubrics/weekly-kpi-snapshot.yaml`, `rubrics/monthly-exec.yaml`.
- `rubrics/agent.yaml` for CRO test design and HITL packaging.
