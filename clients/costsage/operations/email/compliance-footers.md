# Compliance Footers — CAN-SPAM + CASL + GDPR

Every CostSage email — cold, lifecycle, newsletter, promo, announcement — must include a compliant footer. Transactional emails (password reset, billing receipts) follow narrower rules but still include physical address.

[TBD-OPERATOR]: confirm legal entity name, registered physical address, DPO contact (if EU/UK contacts > threshold).

---

## Master footer template

```
---

You're receiving this because {{consent_reason}}.

CostSage, Inc.
{{registered_street_address}}
{{city, state/region, postal code, country}}

Manage preferences: {{preferences_url}}
Unsubscribe (one-click): {{unsubscribe_url}}

Privacy policy: https://costsage.ai/privacy
Contact: privacy@costsage.ai

---
```

---

## Field-by-field requirements

### `{{consent_reason}}` — must be specific

Examples by audience:
- **Cold outreach:** "you're listed as {{role}} at {{company}} on a publicly visible profile, and we believe FinOps tooling may be relevant to your role."
- **Newsletter:** "you subscribed to the CostSage newsletter on {{date}}."
- **Trial / customer:** "you have an active or recent CostSage account."
- **Webinar attendee:** "you registered for the {{webinar_name}} webinar on {{date}}."
- **Promotional:** "you opted in to product updates from CostSage."

### Physical address (CAN-SPAM mandatory)

Real, monitored mailing address (not a PO box for non-postal mail in some jurisdictions). [TBD-OPERATOR — provide registered address.]

### Unsubscribe — one-click

- Link MUST work without login.
- MUST honor request within 10 business days (CAN-SPAM); within 24h for CASL; "without undue delay" for GDPR.
- Recommended: instant suppression on click.
- One-click headers (RFC 8058) on all marketing mail:
  ```
  List-Unsubscribe: <mailto:unsubscribe@costsage.ai>, <https://costsage.ai/u/{{token}}>
  List-Unsubscribe-Post: List-Unsubscribe=One-Click
  ```

### Manage preferences

Granular: separate toggles for newsletter / product updates / promos / company news. Unsubscribing from one ≠ unsubscribing from all (GDPR consent granularity).

### Privacy policy + contact

- Link to https://costsage.ai/privacy
- DPO / privacy contact: privacy@costsage.ai

---

## Jurisdiction-specific add-ons

### CASL (Canada)

- Express OR implied consent must be documented per contact.
- Sender identification mandatory (full legal name).
- Footer must include: legal name, mailing address, *one* additional contact method (email or phone).
- Unsubscribe must be effective within 10 business days; we target instant.

**CASL footer add-on:**
```
Sent on behalf of CostSage, Inc.
Email: contact@costsage.ai
```

### GDPR / UK GDPR (EEA + UK)

- Lawful basis for sending (typically: consent for marketing, legitimate interest for cold B2B with extra safeguards).
- Right to access / erasure / portability — must be honored.
- Data Protection Officer or representative for EU/UK if processing thresholds met. [TBD-OPERATOR.]
- Footer must enable a path to exercise rights.

**GDPR footer add-on (for EU/UK contacts):**
```
You can request access to, correction of, or deletion of your personal data at privacy@costsage.ai. Lawful basis: {{consent | legitimate-interest}}.
```

### CAN-SPAM (US) — minimum required

- No deceptive subject lines (subject must reflect content).
- Identify message as commercial (implicit OK if obvious).
- Valid physical postal address.
- Clear, conspicuous unsubscribe.
- Honor opt-outs within 10 business days; suppress permanently.

---

## Suppression model

**Suppression list is canonical.** Stored centrally; synced across ESP, CRM, and any sending tool nightly (real-time preferred).

**Sources of suppression:**
1. User-clicked unsubscribe (any link, any campaign)
2. List-Unsubscribe header used (one-click)
3. Reply containing "unsubscribe", "remove me", "stop", "do not contact" (auto-detected, low-threshold)
4. Spam complaint / abuse feedback loop
5. Hard bounce (invalid address)
6. Soft bounces ≥5 in 30 days
7. Manual operator add (privacy/erasure request)
8. Inactivity threshold [TBD-OPERATOR — recommended: 12 mo zero opens for marketing]

**Suppression is per-domain per-purpose:** a user can suppress newsletter while remaining a transactional / customer recipient. Critical for GDPR granularity.

**Suppression record fields:**
- `email`
- `domain`
- `suppressed_at`
- `reason` (enum)
- `source` (which campaign / event triggered)
- `scope` (newsletter / promo / all-marketing / all-inc-transactional)
- `requested_by` (user / operator / system)

---

## One-click unsubscribe spec

**URL pattern:** `https://costsage.ai/u/{{token}}`

**Token:** signed JWT or HMAC, includes `email_id`, `contact_id`, `scope`, `expiry` (90 days). Single-use.

**Behavior:**
1. GET `/u/{{token}}` → no login required.
2. Validate token. If invalid/expired → friendly page, no leak.
3. If valid → suppress immediately, write to suppression list, fire downstream sync to ESP/CRM.
4. Show one-click "Done — you're unsubscribed from {{scope}}." with optional preferences page link to manage other scopes.
5. POST same URL with `List-Unsubscribe-Post: List-Unsubscribe=One-Click` → identical behavior, returns 200.

**Latency target:** suppression effective in <60 seconds across all sending tools.

**Audit log:** every suppression event logged immutably.

---

[TBD-OPERATOR]: legal review, especially for cold outreach lawful basis under GDPR; confirm registered address; appoint EU rep if thresholds met.
