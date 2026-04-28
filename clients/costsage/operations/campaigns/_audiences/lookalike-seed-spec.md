# Lookalike Seed-List Spec — CostSage.ai

> Exact spec for building seed CSVs that platforms ingest to build lookalike / matched audiences. One file per seed, versioned.

## 1. Seed lists to build

| Seed name | Source | Min size for upload | Refresh cadence | Used by |
|-----------|--------|---------------------|-----------------|---------|
| `seed_customers_paying.csv` | CRM closed-won, ARR > 0 | 100 (LI), 1,000 (Google) | Weekly | LI lookalike, Google customer-match LAL, Meta LAL, Reddit n/a |
| `seed_customers_high_ltv.csv` | Closed-won, ARR ≥ $10K | 100 LI minimum | Weekly | LI lookalike (1% then 3%) |
| `seed_trial_signups_30d.csv` | Trial-started in last 30 days, not yet paying | 300 | Daily | LI matched, Google customer-match, Meta |
| `seed_demo_requested_90d.csv` | demo_request event, last 90 days | 300 | Weekly | All platforms — retargeting + LAL |
| `seed_newsletter_engaged.csv` | ESP: opened ≥ 2 of last 5 | 1,000 | Weekly | Google customer-match, Meta |
| `seed_high_intent_pages.csv` | Visited /pricing OR /compare/* in last 30d | n/a (pixel-based, not CSV) | n/a | Retargeting only |
| `suppress_current_customers.csv` | Active paying accounts | full list | Weekly | Excluded from ALL prospecting campaigns |
| `suppress_competitors.csv` | Hand-curated competitor employee domains | full list | Quarterly | Excluded |

## 2. Required CSV schema

All CSVs share the same shape; platforms use the columns they need. Columns are lowercase, comma-separated, UTF-8, with header row.

```
email,phone_e164,first_name,last_name,company,company_domain,job_title,country,zip,linkedin_url,external_id
```

- `email` — primary identity. Lowercased. Trim whitespace. Hash with SHA-256 (lowercase hex) before upload to Google / Meta / Reddit. **LinkedIn accepts plaintext via Customer Match — confirm current API requirement at upload time.**
- `phone_e164` — `+15551234567` format. Optional but boosts match rate.
- `company_domain` — root domain only (`acme.com`, not `app.acme.com`).
- `external_id` — internal CRM ID; never PII; used for suppression sync.

## 3. Build steps (CRM → CSV)

1. Run CRM export (HubSpot / Salesforce — `[TBD-OPERATOR: confirm CRM]`) with the saved view "Seed: <name>".
2. Pipe through `clients/costsage/operations/campaigns/_audiences/scripts/build-seed.py` (TBD-build) which:
   - Lowercases + trims emails.
   - Validates E.164 phones.
   - Drops rows with missing email AND missing phone.
   - Splits into `_plain.csv` (LinkedIn) and `_hashed.csv` (Google/Meta/Reddit).
   - Writes a manifest with row count + SHA of source export.
3. Drop into `clients/costsage/operations/campaigns/_audiences/exports/<YYYY-MM-DD>/`.
4. Update this doc's "Last build" table.

## 4. Per-platform upload notes

| Platform | Path | Match rate floor | Notes |
|----------|------|------------------|-------|
| LinkedIn Campaign Manager | Account Assets → Matched Audiences → Upload list | 30% | Plaintext supported; min audience 300 to activate. Build LAL: "Audience expansion" off, then on for cold prospecting. |
| Google Ads | Tools → Audience Manager → Customer List | 30% | SHA-256 hashed. Customer Match needs ≥ 1,000 active members for Search/YouTube serving. |
| Microsoft Advertising | Audiences → Customer Match | 30% | Mirror of Google. |
| Meta Ads | Audiences → Custom Audience → Customer List | 50%+ | SHA-256 hashed. LAL 1% (US) is most efficient. |
| Reddit Ads | Custom Audience → Customer List | 20% | SHA-256 hashed. Smaller match rates expected. |
| X / Twitter Ads | Audience Manager → Tailored Audiences | 30% | Optional channel. |

## 5. Suppression discipline (DO NOT SKIP)

Every prospecting campaign across every platform MUST attach `suppress_current_customers.csv` AND `suppress_competitors.csv` as **excluded** audiences. This is enforced in the campaign-brief checklist (section 3 of `campaign-brief-template.md`).

## 6. Privacy & compliance
- Lawful basis: legitimate interest (B2B contact data) + consent for marketing emails (GDPR / UK GDPR / CAN-SPAM / CASL).
- Honor unsubscribes: ESP unsub list is appended to `suppress_*.csv` on next build.
- Data retention: seed CSVs older than 90 days are deleted from `exports/`.
- DPA: each ad platform's standard DPA + Customer Match terms accepted by operator — `[TBD-OPERATOR]`.

## 7. Last-build log
| Date | Seed | Rows | Match rate | Operator |
|------|------|------|------------|----------|
