# SPF / DKIM / DMARC Checklist — costsage.ai

Goal: every email sent from `@costsage.ai` passes SPF, DKIM, and DMARC. Failures put us in spam regardless of content quality.

[TBD-OPERATOR]: confirm ESP. Placeholder values below assume **{{ESP}}**. Most-likely candidates: Postmark, SendGrid, Customer.io, Mailgun, Resend, Loops. Each has slightly different specifics — substitute their published values.

---

## Step 1 — SPF (Sender Policy Framework)

**What:** TXT record listing IPs/services authorized to send mail for `costsage.ai`.

**DNS record:**

| Type | Host | Value | TTL |
|---|---|---|---|
| TXT | `costsage.ai` (apex / `@`) | `v=spf1 include:{{esp_spf_include}} ~all` | 3600 |

Examples by ESP:
- Postmark: `include:spf.mtasv.net`
- SendGrid: `include:sendgrid.net`
- Mailgun: `include:mailgun.org`
- Customer.io: `include:mailgun.org` (they use Mailgun)
- Resend: `include:_spf.resend.com`

**If sending from multiple ESPs (transactional + marketing):**

Combine into one TXT record (max 1 SPF per domain):
```
v=spf1 include:spf.mtasv.net include:sendgrid.net ~all
```
Use `~all` (soft fail) until DMARC is `quarantine`/`reject`-confirmed; then upgrade to `-all` (hard fail).

---

## Step 2 — DKIM (DomainKeys Identified Mail)

**What:** Public key in DNS that the ESP uses to sign outgoing messages. Receivers verify the signature.

**DNS record (per ESP — usually 2–3 CNAMEs):**

ESP-provided. Pattern looks like:

| Type | Host | Value | TTL |
|---|---|---|---|
| CNAME | `{{selector}}._domainkey.costsage.ai` | `{{selector}}.dkim.{{esp_domain}}` | 3600 |

Example (SendGrid): `s1._domainkey.costsage.ai` → `s1.domainkey.u{{user_id}}.wl{{n}}.sendgrid.net`

Each ESP gives 2–3 selectors (e.g., `s1`, `s2`, `mte1`). Add all of them.

**Do not** use a single shared selector across multiple ESPs. Each ESP owns its own selector.

---

## Step 3 — DMARC (Domain-based Message Authentication, Reporting, and Conformance)

**What:** Policy telling receivers what to do if SPF or DKIM fail, plus where to send aggregate reports.

**Phased rollout — do not start at `reject`.**

### Phase 1 — Monitor (week 1–2)

| Type | Host | Value | TTL |
|---|---|---|---|
| TXT | `_dmarc.costsage.ai` | `v=DMARC1; p=none; rua=mailto:dmarc-reports@costsage.ai; ruf=mailto:dmarc-failures@costsage.ai; fo=1; adkim=r; aspf=r; pct=100` | 3600 |

Watch aggregate reports for 7–14 days. Use a tool like [TBD-OPERATOR — DMARC Digests, Postmark DMARC, Valimail, dmarcian] to parse XML.

### Phase 2 — Quarantine (week 3–4)

Once 95%+ of legit mail is passing aligned SPF or DKIM:

`v=DMARC1; p=quarantine; pct=25; rua=...; ruf=...`

Increase `pct` from 25 → 50 → 100 over 2 weeks while monitoring.

### Phase 3 — Reject (week 5+)

Final state:

`v=DMARC1; p=reject; rua=...; ruf=...; adkim=s; aspf=s`

Strict alignment (`adkim=s`, `aspf=s`) — only commit to this once you're confident.

---

## Step 4 — BIMI (optional but recommended once DMARC is at reject)

**What:** Brand logo in supporting inboxes (Gmail, Apple Mail, Yahoo).

**Prereq:** DMARC at `quarantine` or `reject` with `pct=100`. Verified Mark Certificate (VMC) from [TBD-OPERATOR — DigiCert, Entrust] for Gmail.

**DNS record:**

| Type | Host | Value |
|---|---|---|
| TXT | `default._bimi.costsage.ai` | `v=BIMI1; l=https://costsage.ai/assets/bimi-logo.svg; a=https://costsage.ai/assets/vmc.pem` |

Logo: SVG Tiny PS, square, ≤32KB.

---

## Step 5 — MX (only if receiving mail at costsage.ai)

[TBD-OPERATOR]: confirm whether Google Workspace / Microsoft 365 / etc. handles `@costsage.ai` inbound. If yes, ensure MX records are correct and point to the right provider.

---

## Verification steps

1. **mxtoolbox.com** — run SPF, DKIM, DMARC checks on `costsage.ai`. All should pass.
2. **Send test mail to `check-auth@verifier.port25.com`** — receive auto-reply with auth report. SPF, DKIM, DMARC, all "pass".
3. **mail-tester.com** — send a test email; aim for 10/10 score before launching any campaign.
4. **Send to seed accounts:** Gmail, Outlook.com, Yahoo, ProtonMail, iCloud personal addresses [TBD-OPERATOR — set up seed list]. Verify inbox placement.
5. **Check Google Postmaster Tools** (after warmup volume picks up): domain reputation should reach Medium or High; spam rate <0.1%.

---

## Deliverability test plan (pre-launch)

| Test | Tool | Pass criteria |
|---|---|---|
| Auth (SPF/DKIM/DMARC) | mail-tester.com | 10/10 |
| DMARC alignment | DMARC reports | ≥95% mail passing aligned |
| Inbox placement (Gmail) | Seed test | Primary inbox, not Promotions |
| Inbox placement (Outlook) | Seed test | Inbox, not Junk |
| Blacklist | mxtoolbox blacklist check | Clean on all major RBLs |
| Reverse DNS | rDNS lookup | Sending IPs resolve to ESP-owned PTR |

---

## What to do if a record fails

- SPF fails → check for >10 DNS lookups (common limit), flatten if needed via tools like SPFlat / EasyDMARC SPF flattener.
- DKIM fails → re-copy CNAMEs from ESP exactly; selector typos are the #1 cause.
- DMARC fails → check whether mail is signed at all; check alignment (return-path domain must match `From:` domain or DKIM domain must align).

[TBD-OPERATOR]: ESP confirmation, ownership of `dmarc-reports@costsage.ai` mailbox, decision on BIMI investment.
