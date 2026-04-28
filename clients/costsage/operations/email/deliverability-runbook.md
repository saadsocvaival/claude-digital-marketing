# Deliverability Runbook

Cold sequences and high-volume marketing fail when deliverability fails. This runbook covers warmup, ongoing monitoring, blacklist checks, and the "we got blocklisted" panic procedure.

[TBD-OPERATOR]: confirm ESP, sending domain strategy (recommended: subdomain split — see below).

---

## Sending domain strategy

**Strongly recommend subdomain split:**

| Subdomain | Purpose | ESP |
|---|---|---|
| `costsage.ai` apex | Transactional only (password reset, billing) | [TBD-OPERATOR — Postmark / Resend] |
| `mail.costsage.ai` | Marketing (newsletter, promos, announcements) | [TBD-OPERATOR — Customer.io / SendGrid / Loops] |
| `out.costsage.ai` | Cold outreach / outbound | [TBD-OPERATOR — Smartlead / Instantly / lemlist] |

Why split: a single bounce/complaint storm on cold outreach won't poison transactional or marketing reputation. Apex domain reputation stays pristine.

Each subdomain gets its own SPF, DKIM, DMARC records. See `spf-dkim-dmarc-checklist.md`.

---

## Week 1 — Warmup plan

**Pre-warmup checklist:**
- [ ] DNS (SPF, DKIM, DMARC) verified on all sending subdomains
- [ ] mail-tester.com score: 10/10
- [ ] Suppression list active and synced
- [ ] Footer compliance verified
- [ ] Reply monitoring: a real human reads `founder@costsage.ai`

**Daily volume ramp (cold outreach `out.costsage.ai`):**

| Day | Daily sends | Notes |
|---|---|---|
| 1–2 | 20 | Manual sends to engaged contacts (not cold). Check inbox placement seed list. |
| 3–4 | 40 | Add cold contacts gradually. |
| 5–7 | 60 | Maintain ≤10% bounce, ≤0.1% complaint. |
| 8–10 | 100 | Steady ramp. |
| 11–14 | 150 | If reply rate >3% and bounce <5%, continue ramping next week. |
| 15–21 | 250 | |
| 22–28 | 400 | |
| 29+ | 500+ (steady state) | Cap at [TBD-OPERATOR — typically 800–1500/day per inbox] |

**Per-inbox cap:** 1 sending mailbox = max ~1500/day. To send more, add inboxes (e.g., `founder@out.costsage.ai`, `team@out.costsage.ai`), each warmed independently.

**Use a warmup service** ([TBD-OPERATOR — Mailwarm / Warmup Inbox / built into Smartlead/Instantly]) to simulate inbox conversation and lift sender reputation during week 1–2.

**Marketing (`mail.costsage.ai`) warmup:**
- Day 1: send to 50 most-engaged subscribers only.
- Day 3: 200 most-engaged.
- Day 5: 500.
- Day 7: full segment, but exclude any contact with 0 opens in last 90 days (cold-list cleanup first).

---

## Ongoing monitoring (daily / weekly)

### Daily (5 min)
- ESP dashboard: bounce rate, complaint rate, delivered rate.
- Cold inbox: any out-of-office, manual replies, "remove" requests → suppress immediately.

### Weekly (15 min)
- **Google Postmaster Tools** ([postmaster.google.com](https://postmaster.google.com)): domain reputation = Medium or High; spam rate <0.1%; auth = pass.
- **Microsoft SNDS** ([sendersupport.olc.protection.outlook.com](https://sendersupport.olc.protection.outlook.com)): IP reputation = Green.
- **DMARC reports** (via [TBD-OPERATOR — Postmark DMARC / dmarcian / Valimail]): aligned-pass rate ≥95%.
- **Blacklist scan** (`mxtoolbox.com/blacklists.aspx`): all sending IPs + sending domains. Clean.
- **Inbox placement test** ([TBD-OPERATOR — GlockApps / MailGenius / seed list]): ≥90% inbox.
- **Reply rate, open rate, click rate trends:** any 30%+ drop is a deliverability red flag.

### Monthly
- Re-run mail-tester from a fresh template
- Suppression list audit — total suppressed, growth rate, reason distribution
- List hygiene: validate addresses with [TBD-OPERATOR — NeverBounce / ZeroBounce] before any large send

---

## Health metrics — green / yellow / red

| Metric | Green | Yellow (act) | Red (stop sending) |
|---|---|---|---|
| Bounce rate | <2% | 2–5% | >5% |
| Complaint rate | <0.05% | 0.05–0.1% | >0.1% |
| Open rate (cold) | >25% | 15–25% | <15% |
| Open rate (newsletter) | >35% | 25–35% | <25% |
| Reply rate (cold) | >3% | 1–3% | <1% |
| Google Postmaster reputation | High | Medium | Low / Bad |
| Aligned DMARC pass | ≥95% | 90–95% | <90% |
| Blacklist hits | 0 | 1–2 minor RBLs | Spamhaus / SpamCop / SORBS |

---

## Runbook: "we're blocklisted"

### Step 1 — Identify (10 min)
1. Run `mxtoolbox.com/blacklists.aspx` against sending IP and domain.
2. Note exactly which RBL(s) listed us.
3. Pull Postmaster + SNDS to check whether reputation tanked.

### Step 2 — Stop the bleeding (immediate)
1. **Pause all sending** on the affected subdomain/IP.
2. Notify ops in #email-deliverability [TBD-OPERATOR Slack channel].
3. Pull last-7-day send logs for affected segment.

### Step 3 — Diagnose root cause (1 hour)
Most common causes, ranked:
1. **Bad list / scraped data** — high bounce rate triggered RBL.
2. **Spam-trap hit** — list contained zombie/honeypot addresses.
3. **Compromised credentials** — third party sent mail from our domain.
4. **Sudden volume spike** — too fast a ramp, RBLs flagged.
5. **Content trigger** — spammy phrases, suspicious links, attachments.
6. **Auth misconfiguration** — DKIM key rotated incorrectly, SPF over-limit.

### Step 4 — Fix and request delisting
1. Address root cause (clean list, rotate creds, slow ramp, fix DNS).
2. Submit delisting request per RBL's process:
   - **Spamhaus:** [spamhaus.org/lookup/](https://www.spamhaus.org/lookup/)
   - **SpamCop:** [spamcop.net/bl.shtml](https://www.spamcop.net/bl.shtml)
   - **Barracuda:** [barracudacentral.org/rbl/removal-request](https://www.barracudacentral.org/rbl/removal-request)
   - **UCEPROTECT:** rarely worth fast removal — let it expire.
3. Provide root cause, fix, and prevention plan in delisting form.

### Step 5 — Resume
1. Wait 24–72h after delisting.
2. Resume sending at 25% of pre-incident volume.
3. Ramp back up over 7 days.
4. Postmortem doc to [TBD-OPERATOR — internal channel].

---

## List hygiene rules

- Never send to scraped lists. Buying lists is not allowed.
- Validate emails ([TBD-OPERATOR — NeverBounce / ZeroBounce] or ESP-native) before any list >500.
- Re-engagement campaign before suppressing >12mo inactive: one final "do you still want to hear from us?" email; if no open in 30d, auto-suppress.
- Hard bounces: suppress immediately, never retry.
- Soft bounces: retry 3x; on 5th cumulative soft bounce in 30d, suppress.

---

## Operator weekly checklist

- [ ] Postmaster + SNDS reputation green
- [ ] DMARC aligned-pass ≥95%
- [ ] Blacklist scan clean
- [ ] Bounce + complaint rates inside green band
- [ ] No anomalous send-volume spike vs plan
- [ ] Suppression list synced across all tools
- [ ] Inbox-placement seed test ≥90%

[TBD-OPERATOR]: confirm ESP, warmup tool selection, who pages whom on a deliverability incident.
