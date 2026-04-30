---
artifact: community-management-sla
date: 2026-04-30
purpose: response-time commitments + escalation paths for social engagement
---

# Community Management SLA

## SLA by message type

| Type | Response time (business hours) | Out-of-hours | Owner | Escalation path |
|---|---|---|---|---|
| Positive (thank-you, like, share) | 24 hours | n/a | Marketing | n/a |
| Question / inquiry | 2 hours | next business day | Marketing → Sales if SQL | If hot SQL: SDR → AE within 4 hr |
| Complaint / negative | 30 min | DM founder direct | Marketing + Founder | Critical issues to founder same day |
| Spam / abuse | 4 hours (just filter) | n/a | Marketing | Block + report only |
| Customer support inquiry on social | 1 hour | next business day | Marketing → Customer Success | Hot issue: page CS rotation |
| Press inquiry | 4 hours | n/a | Founder | Always reply same day |
| Investor / partnership | 24 hours | n/a | Founder | Same day if specifically named investor |

## Tone guide (per `operations/brand/voice-guidelines.md`)

- Confident, not boastful
- Specific, not aspirational
- Plain, not jargony
- Honest, not hedge-everything
- Engineering-first, not sales-first

When responding:
- Use first-person plural for company replies ("we") or first-person singular for founder amplifications ("I")
- Acknowledge specifically what was said before responding
- If you can answer the actual question, answer it; don't redirect to a sales rep
- Mention links/resources where they actually help; don't drop generic /pricing in every reply

## Out-of-hours coverage

For now (small team):
- Marketing operator on-call Mon-Fri 9am-7pm local
- Founder on-call for "critical" tier 24/7
- Weekends + holidays: tier-3 only (i.e., complaints, press, customer-support emergencies)

## Escalation triggers

Auto-escalate to founder if:
- Customer publicly threatens churn
- Negative review/post mentions specific dollar loss
- Press outlet asks for comment with deadline
- Influencer (>10k followers in our niche) raises an issue
- Compliance/security/legal flag

## Templates (copy-paste, then personalise)

### Positive thank-you
"Thanks for the kind words, [name]. Means a lot. If you ever want to share specifics on what worked, we'd love to feature it — no pressure, no sales pitch."

### Question / general inquiry
"[Direct answer to their question — 1-3 sentences]. If you want the deeper version: [link to pillar/blog]. Happy to dig into any specific part."

### Complaint
"[Acknowledgment]. We're sorry that happened. [What we'll do specifically.] If you'd like to talk through it directly, my email is [founder@costsage.ai] — I'll respond same day."

### Press inquiry
"Thanks for reaching out. Yes, we can comment by [their deadline]. Quick context: [1-paragraph factual]. Founder available for follow-up at [link]. Feel free to reach back if you need anything else."

## Reporting

Weekly review (Friday) covers:
- Avg response time per tier
- Total interactions volume
- Top 3 themes / questions
- Any escalations + outcomes
- Net sentiment trend (rough thumb-count)

Reported in V7 weekly digest (`feeds/_scripts/weekly-digest.py`).

## Operator confirmations

- [ ] Marketing operator hours / coverage
- [ ] Founder pager rotation
- [ ] Customer Success escalation contact
- [ ] After-hours coverage policy formalized in HR docs
