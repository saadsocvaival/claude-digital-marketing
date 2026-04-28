# Promotional Email Templates (4)

Each template: subject A/B, preview, body, single CTA, UTM. Compliance footer per `compliance-footers.md`.

UTM convention: `?utm_source=email&utm_medium=promo&utm_campaign=<campaign>&utm_content=<variant>`

---

## Template 1 — Product Launch

**When to use:** Major new product / module / cloud-parity launch (e.g., GCP support, SOC2 milestone, new agentic capability).

**Subject A:** It's live: {{launch_name}}
**Subject B:** {{first_name}} — meet {{launch_name}}
**Preview text:** Built because {{customer_pain_one_line}}.

**Body:**

{{first_name}},

We just shipped **{{launch_name}}**.

**What it does:**
{{one_paragraph_what}}

**Why we built it:**
{{one_paragraph_why}} ([TBD-OPERATOR — anchor on a real customer-shape if possible]).

**Who should care:**
- {{audience_segment_1}}
- {{audience_segment_2}}

We kept the launch small intentionally — wanted to ship the version we'd want to use, not the version with the longest feature list.

**One CTA →** {{primary_cta_label}}: {{primary_cta_url}}?utm_source=email&utm_medium=promo&utm_campaign=launch-{{slug}}&utm_content=A

— {{sender_first}}

---

## Template 2 — Feature Update

**When to use:** Smaller release that's nonetheless worth telling existing customers about (new integration, expanded coverage, UX improvement).

**Subject A:** Small but useful: {{feature_name}}
**Subject B:** {{first_name}} — {{feature_name}} is live
**Preview text:** Two-minute read.

**Body:**

{{first_name}},

Quick update — we shipped {{feature_name}} this week.

**What changed:**
- {{change_1}}
- {{change_2}}
- {{change_3}}

**For you, this means:**
{{benefit_one_paragraph}}

No action needed from your side — it's already on for {{company}}'s account. If you want to see it in action, the dashboard view is here:

**One CTA →** Open dashboard: [TBD-OPERATOR app URL]?utm_source=email&utm_medium=promo&utm_campaign=feature-{{slug}}&utm_content=A

— {{sender_first}}

---

## Template 3 — Webinar Invite

**When to use:** Live event — webinar, AMA, deep-dive workshop. Single primary CTA = register.

**Subject A:** {{first_name}} — webinar on {{topic}} ({{date}})
**Subject B:** {{date}}: {{topic_short}} (live, 30 min)
**Preview text:** {{date}}, 30 minutes, replay if you can't make it.

**Body:**

{{first_name}},

Hosting a live session on **{{topic}}** on **{{date}} at {{time}} {{tz}}**.

**Format:** 20 minutes content, 10 minutes Q&A. Replay sent to registrants if you can't make it live.

**What we'll cover:**
- {{point_1}}
- {{point_2}}
- {{point_3}}

**Who it's for:**
{{audience_one_line}}

**Hosts:**
- {{host_1}}, {{title}}
- {{host_2}}, {{title}}

**One CTA →** Register: {{registration_url}}?utm_source=email&utm_medium=promo&utm_campaign=webinar-{{slug}}&utm_content=A

— {{sender_first}}

---

## Template 4 — Customer Story

**When to use:** Anonymized or named customer case study published. Subscriber-friendly, low-pressure.

**Subject A:** How {{customer_or_descriptor}} cut AWS by {{savings_pct}}%
**Subject B:** {{first_name}} — one customer story
**Preview text:** {{one_line_outcome}}.

**Body:**

{{first_name}},

Wanted to share how {{customer_or_descriptor}} ({{ICP_descriptor}}, ~{{spend}} on AWS) used CostSage in their first {{timeframe}}.

**The shape:**
- **Top finding:** {{top_finding}}
- **Action shipped:** {{action}}
- **Outcome:** {{outcome}}

**What surprised me:**
{{one_paragraph_human_observation}}

If your AWS profile looks similar, the patterns probably rhyme.

**One CTA →** Read the full case: {{case_url}}?utm_source=email&utm_medium=promo&utm_campaign=case-{{slug}}&utm_content=A

— {{sender_first}}

---

## Operational notes

- Promotional sends must respect frequency cap: max 1 promo email/contact/week, max 2 promos/contact/month (excluding lifecycle / transactional).
- Always honor newsletter-only consent: contacts who opted in to newsletter ONLY do not receive promos unless explicitly re-permissioned.
- Suppression list applies to all four.
- Compliance footer auto-appended.
