---
artifact: operator-decisions-consolidated
date: 2026-04-30
purpose: single document listing all 12 operator-gated decisions blocking forward execution
audience: operator + Sheraz Iqbal + management
---

# Operator Decisions — Consolidated

> Every gate below blocks one or more verticals. Numbers in column `Vertical(s)` map to verticals 1-8. Priority `P0` = unblocks ≥2 verticals; `P1` = unblocks 1 vertical or low business impact.

## Quick-glance

| # | OD | Vertical(s) | P | Time | Impact |
|---|---|---:|---|---:|---|
| 1 | Operator confirmations form | 1, 4, 8 | P0 | 30 min | +15% mission |
| 2 | Cloudflare robots.txt toggle | 1 | P0 | 2 min | crawler unblock |
| 3 | A/B engine choice | 1, 2 | P0 | 15 min | CRO loop |
| 4 | GitHub source-repo collab | 2 | P0 | 5 min | source-of-truth |
| 5 | Ad account provisioning | 7 | P0 | 2 hr | paid launch |
| 6 | LinkedIn admin grant | 5, 7 | P0 | 10 min | LinkedIn channel |
| 7 | CRM choice | 3, 5, 6 | P0 | 1 hr | lead pipeline |
| 8 | ESP choice | 4, 5 | P0 | 1 hr | email send |
| 9 | DNS write access | 5 | P0 | 30 min | email delivery |
| 10 | Social handle provisioning | 5, 6 | P1 | 1 hr | social channel |
| 11 | Scheduler subscription | 6 | P1 | 15 min | scheduled posting |
| 12 | Logo + founder photos | 8 | P1 | 1 hr | press kit |

---

## OD1 — Operator confirmations form

**Vertical(s):** V1 (SEO/AEO/GEO), V4 (Content), V8 (Brand)
**Priority:** P0 (highest leverage)
**Operator time:** 30 min

**Why this matters:** Wikidata Q-item, Crunchbase profile, Person schema on /about, customer-savings claims across 11+ pages, press kit, founder bios — all block on these 6 facts.

**Run-book:**
1. Open `clients/costsage/seo-geo-aeo/sprint-2/G2-G3-G7-OPERATOR-CONFIRMATIONS.md`
2. Fill the 7 fields:
   - [ ] Legal entity name
   - [ ] HQ city + country
   - [ ] Founded date (YYYY-MM-DD)
   - [ ] Founder names + LinkedIn URLs
   - [ ] Customer-savings claims (which numbers we can publish without [TBD])
   - [ ] AWS Marketplace canonical URL
   - [ ] Y/N approve adding Claude as collaborator on `shirazvaival/costsage-web` (also unblocks OD4)
3. Reply via PR comment or email
4. Agent applies edits in same sprint

---

## OD2 — Cloudflare robots.txt rewrite toggle

**Vertical(s):** V1
**Priority:** P0 (single highest single-toggle impact)
**Operator time:** 2 min (deferred earlier per your call)

**Why:** Cloudflare's "AI Audit / Manage robots.txt" feature is rewriting robots.txt at the edge with `Disallow: /` for ClaudeBot, GPTBot, Google-Extended, Applebot-Extended. Even though pages are reachable (we verified), well-behaved AI crawlers self-block on robots.txt before fetch.

**Run-book:**
1. Cloudflare dashboard → Zero Trust → Bots → AI Audit → "Manage robots.txt" toggle → **Off**
2. Verify: `curl -A "ClaudeBot/1.0" https://costsage.ai/robots.txt` returns origin file (no `# Cloudflare Managed Content` block)

---

## OD3 — A/B engine choice

**Vertical(s):** V1 (Web/CRO), V2 (Analytics)
**Priority:** P0
**Operator time:** 15 min
**Recommendation:** PostHog cloud free tier

**Run-book:**
1. Sign up at posthog.com (free tier; no card)
2. Create project "CostSage"
3. Copy project API key (`phc_...`)
4. Vault as `vault://costsage/posthog/project-api-key`
5. (Once vaulted, agent integrates PostHog snippet sitewide + wires the 3 drafted A/B test briefs)

---

## OD4 — GitHub source-repo collaboration

**Vertical(s):** V2 (Website + CRO)
**Priority:** P0
**Operator time:** 5 min
**Why:** All current changes live durably in the bind-mount overlay only. Operator-side source repo at `shirazvaival/costsage-web` is the canonical truth; without collab access, the agent can't sync changes back.

**Run-book:**
1. github.com/shirazvaival/costsage-web → Settings → Collaborators
2. Add `saadsocvaival` (already has the parent repo)
3. Permission: Write
4. (Agent sets up PR pipeline + overlay-to-source sync skill)

---

## OD5 — Ad account provisioning

**Vertical(s):** V7 (Paid Media)
**Priority:** P0
**Operator time:** 2 hours total

**Run-book per platform:**
- **Google Ads:** ads.google.com → New Account → "[Company name TBD]" → set up billing (CC required) → grant Claude (manager) access
- **LinkedIn Campaign Manager:** business.linkedin.com → New Account → connect to LinkedIn company page (OD6 dependency) → set up billing
- **Microsoft Advertising:** ads.microsoft.com → Sign in with operator's Microsoft account → New Account → billing
- **Meta Business Manager:** business.facebook.com → Create → connect Meta page → billing
- **X / Twitter Ads:** ads.twitter.com → operator-personal or company-handle → billing
- (Reddit Ads + Capterra/G2 sponsored: defer to V7 launch)

**After provisioning:** vault each account ID + API key.

---

## OD6 — LinkedIn admin grant

**Vertical(s):** V5, V7
**Priority:** P0
**Operator time:** 10 min

**Run-book:**
1. LinkedIn company page (must exist already; if not, create at linkedin.com/company)
2. Settings → Admin → add `saadsocvaival` (or operator-equivalent) as Sponsored Content Poster + Page Admin
3. Verify access at admin level

---

## OD7 — CRM choice

**Vertical(s):** V3, V5, V6 (analytics + email + social attribution)
**Priority:** P0
**Operator time:** 1 hour
**Recommendation:** HubSpot Free (limits: 1M contacts, 1k emails/mo) — free start; upgrade later

**Run-book:**
1. hubspot.com → Sign Up Free
2. Verify domain (DNS record)
3. Settings → API Keys → generate Private App access token
4. Vault as `vault://costsage/hubspot/access-token`
5. (Agent wires lead-pipeline + email sequences)

Alternative: **Pipedrive** if HubSpot's free tier feels too constrained. **Salesforce** if enterprise expectation later.

---

## OD8 — ESP choice

**Vertical(s):** V4, V5
**Priority:** P0
**Operator time:** 1 hour + DNS work
**Recommendation:** Customer.io for lifecycle automation; Beehiiv for newsletter-only.

**Run-book per ESP:**
- **Customer.io** (recommended): customer.io → sign up → connect domain → SPF/DKIM records (OD9) → API key → vault
- **Mailchimp**: mailchimp.com → Free tier (1k contacts) → DNS auth → API key
- **Beehiiv**: beehiiv.com → newsletter-focused; cleanest for issue 01-05 distribution
- **Smartlead.ai**: smartlead.ai → cold-outreach focused; good for V5 cold sequences

After provisioning: import drafted sequences from `operations/email/sequences/` (already HubSpot-import-formatted).

---

## OD9 — DNS write access (SPF/DKIM/DMARC)

**Vertical(s):** V5
**Priority:** P0
**Operator time:** 30 min
**Pre-req:** ESP chosen (OD8)

**Run-book:** see `operations/email/spf-dkim-dmarc-checklist.md`. Records to add (replace placeholder ESP IDs):
- `costsage.ai TXT v=spf1 include:[ESP-include] include:_spf.google.com ~all`
- `selector1._domainkey.costsage.ai CNAME [ESP-dkim-target]`
- `_dmarc.costsage.ai TXT v=DMARC1; p=none; rua=mailto:dmarc@costsage.ai; ruf=mailto:dmarc@costsage.ai; fo=1; aspf=r; adkim=r`

(Start with `p=none` for monitoring; advance to `p=quarantine` after 2 weeks of clean reports.)

---

## OD10 — Social brand-handle provisioning

**Vertical(s):** V5, V6
**Priority:** P1
**Operator time:** 1 hour

**Run-book per platform:**
- **LinkedIn:** company page exists (OD6); confirm posting access for the operator-marketing-account
- **X / Twitter:** twitter.com → claim handle `@costsageai` (or alt) → bio → link → 1.5MB profile pic
- **Reddit:** reddit.com → claim brand username → join r/aws + r/devops + r/sre + r/finops (lurk-first per playbook)
- **YouTube:** youtube.com/create → channel name "CostSage" → handle → first banner

After: vault each account password (rotate to ESP per-agent app-passwords later).

---

## OD11 — Scheduler subscription

**Vertical(s):** V6
**Priority:** P1
**Operator time:** 15 min
**Recommendation:** Buffer Essentials ($15/mo per channel)

**Run-book:**
1. buffer.com → sign up
2. Connect LinkedIn company page (OD6) + X account (OD10)
3. Settings → Apps & Integrations → API Access → generate token
4. Vault as `vault://costsage/buffer/api-token`
5. Agent imports posting queues weeks 1-12

---

## OD12 — Final logo + founder photos

**Vertical(s):** V8 (Brand)
**Priority:** P1
**Operator time:** 1 hour (or designer hour)

**Run-book:**
1. Logo: PNG transparent + SVG, 1x + 2x, dark + light variants. Save to `pages/assets/logos/` then place at canonical URLs
2. Founder photos: 1 headshot per founder, 1024×1024 minimum, on white + on brand-color backgrounds (2 versions each)
3. Once received: agent updates `/press/index.html` + `/about` Person schema + LinkedIn bio kit + cold-outreach signature blocks

---

## What clears with each OD

| OD | Mission % lift | Verticals fully unblocked |
|---|---:|---|
| OD1 | +5-8% | V1 (Wikidata + Crunchbase + Org schema), V4 (case studies), V8 (press kit) |
| OD2 | +3-5% | V1 (LLM crawler reach) |
| OD3 | +4-6% | V1 + V2 (CRO loop) |
| OD4 | +1-2% | V2 (source-of-truth path) |
| OD5+OD6 | +6-9% | V7 (paid launch) |
| OD7 | +5-7% | V3 + V5 + V6 (lead pipeline) |
| OD8+OD9 | +6-9% | V4 + V5 (newsletter + email send) |
| OD10+OD11 | +4-6% | V5 + V6 (social channel) |
| OD12 | +1-2% | V8 (asset library) |

**If all 12 ODs clear in next 7 days: mission % lifts ~30-50 points → ~85-90% completion.**

## Recommended order

If the operator only has 30 min today:
1. OD2 (Cloudflare toggle) — 2 min, immediate AEO/GEO unlock
2. OD1 (confirmations form) — 30 min, unlocks 5 P0 actions

If the operator has 4 hours:
3. OD3 (PostHog signup) + OD4 (GitHub collab) — 20 min combined
4. OD7 (HubSpot Free) — 1 hour
5. OD8 (Customer.io / Beehiiv signup) + OD9 (DNS) — 1.5 hours

Everything else (OD5/OD6/OD10/OD11/OD12) can roll into next week.
