---
client_id: costsage
sprint: 2
artifact: operator-confirmations-needed
date: 2026-04-27
audience: operator
priority: P0
---

# Operator confirmations needed (single-form for batch sign-off)

> Multiple Sprint-2 P0 actions are blocked on the same set of facts. Confirm these once and we unblock G2 (Wikidata), G3 (Crunchbase), G7 (Org JSON-LD), Person schema (about page), and the /aws FAQ truthfulness gate in one shot.

## Field 1 — Legal + corporate
- [ ] **Legal entity name** of the company that owns CostSage (e.g., "CostSage AI Inc." or "Vaival Technologies LLC d/b/a CostSage")
- [ ] **HQ country**
- [ ] **HQ city / region**
- [ ] **Founding date** (YYYY-MM-DD, exact)
- [ ] **Parent / operating relationship**: confirm "Vaival Technologies" is the parent and how to phrase it ("a Vaival Technologies company" / "incubated by Vaival" / etc.)
- [ ] **Funding stage** (Bootstrapped / Pre-Seed / Seed / Series A / etc.)

## Field 2 — Founders / leadership
- [ ] **Founder name(s)** + role(s)
- [ ] **Founder LinkedIn URL(s)**
- [ ] OK to publish founder names on the public site? Y/N
- [ ] Founder bio (1-2 sentences each)

## Field 3 — Brand assets
- [ ] **Logo file URL** (PNG, transparent, ≥400×400 — for Wikimedia, Crunchbase, OG image)
- [ ] **Twitter / X handle** if any
- [ ] **YouTube / other video channel** if any

## Field 4 — Customer claims gate (TRUTHFULNESS REQUIRED)
The following claims appear on shipped pages. Confirm each is **truthful, citable, and approved for public use**:
- [ ] "Customers save $61K/month on average" (homepage hero — current copy)
- [ ] "Save up to 65%" (homepage hero variant)
- [ ] "25–40% savings within 60 days" (Crunchbase long-description draft)
- [ ] "$10K–$500K/month cloud spend" target range (Crunchbase + ICP copy)

If any of these is aspirational/unconfirmed, mark which and we'll replace with conservative defaults.

## Field 5 — AWS Marketplace
- [ ] Confirm CostSage is **listed live** on AWS Marketplace
- [ ] Canonical URL (current draft uses `https://aws.amazon.com/marketplace/pp/prodview-l7gymco6bhnxg` from Track-4 discovery — confirm)

## Field 6 — Cloudflare (deferred per operator)
- [ ] (Deferred) AI-Audit "Manage robots.txt" toggle — flip when ready; not a Sprint-2 blocker

## Field 7 — Source-repo access (D1 path)
- [ ] Add Claude as collaborator on `https://github.com/shirazvaival/costsage-web` so visible-UI changes can land permanently? (Without this, all Sprint-2 work survives only via the bind-mount overlay — durable but operationally distinct from source.)

## How to return

Reply with a filled-in version of this list (or paste the values inline). On receipt:
1. We patch the homepage Organization JSON-LD with real values (replacing TBD literals).
2. Submit Wikidata Q-item.
3. Submit Crunchbase profile.
4. Update Person schema on /about with real founder fields.
5. Replace any unconfirmed savings claims with conservative copy.
6. Re-deploy via overlay (no Cloudflare dependency).

Estimated turnaround: same day, once we have the values.
