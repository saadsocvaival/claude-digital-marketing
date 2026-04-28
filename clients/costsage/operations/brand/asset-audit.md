# Brand Asset Audit — CostSage

> Owner: Brand • v1.0 • 2026-04-28
> Method: Inspection of https://costsage.ai/ + standard channel checklist. Anything not directly verifiable from the live site is marked `[TBD-OPERATOR]`.

---

## 1. What We Have (verified or inferred from live site)

| Asset | Status | Source / location | Notes |
|---|---|---|---|
| Wordmark / logo (web) | ✅ Have | costsage.ai header | [TBD-OPERATOR] confirm vector source file (SVG/AI) and color variants exist |
| Favicon | ✅ Have | costsage.ai/favicon.ico | [TBD-OPERATOR] confirm 16/32/180/512 set |
| Color palette | ⚠️ Partial | Inferred from site | [TBD-OPERATOR] confirm hex codes, accessibility-checked variants |
| Typography stack | ⚠️ Partial | Inferred from site | [TBD-OPERATOR] confirm web font licensing + heading/body pairings |
| Hero illustration / product UI screenshots | ⚠️ Partial | Homepage | Confirm export-quality versions exist |
| Founder headshots | ❓ Unknown | About page | [TBD-OPERATOR] |
| Tagline / hero copy | ✅ Have | "Your cloud bill is hiding thousands. We find them." | Locked in voice guidelines |
| Trust seals (ISO, SOC2, etc.) | ⚠️ Partial | About page references ISO-cert | [TBD-OPERATOR] confirm SOC2 Type II status + badge files |

## 2. What We Need (by channel + spec)

### Social profiles

| Channel | Asset | Spec | Priority | Status |
|---|---|---|---|---|
| LinkedIn | Company banner | 1584 × 396 px, <8 MB, PNG/JPG | P0 | Need |
| LinkedIn | Company logo | 300 × 300 px, square, PNG | P0 | Need (vector source) |
| LinkedIn | Featured-section card images | 1200 × 627 px ×3 | P1 | Need |
| X / Twitter | Header | 1500 × 500 px | P0 | Need |
| X / Twitter | Profile | 400 × 400 px | P0 | Need |
| X / Twitter | Pinned post graphic | 1200 × 675 px | P1 | Need |
| YouTube | Channel art | 2560 × 1440 px (safe area 1546 × 423) | P2 | Need |
| YouTube | Thumbnails template | 1280 × 720 px | P2 | Need |
| GitHub | Org avatar | 500 × 500 px | P2 | Need (only if we open-source SDK) |

### Open Graph / sharing

| Asset | Spec | Priority | Status |
|---|---|---|---|
| OG image — homepage | 1200 × 630 px | P0 | Need |
| OG image — blog post template | 1200 × 630 px, parameterized title overlay | P0 | Need |
| OG image — comparison page template | 1200 × 630 px | P1 | Need |
| Twitter Card image | 1200 × 600 px (or reuse OG) | P0 | Need |

### Web / product

| Asset | Spec | Priority | Status |
|---|---|---|---|
| Favicon set | 16, 32, 48, 180 (Apple), 192, 512 px | P0 | Verify completeness |
| Apple touch icon | 180 × 180 px | P0 | Verify |
| Web app manifest icons | 192, 512 (maskable) | P1 | Verify |
| Email header (transactional) | 600 × 200 px | P0 | Need |
| Email signature graphic (sales) | 200 × 60 px | P1 | Need |

### Sales / fundraising / events

| Asset | Spec | Priority | Status |
|---|---|---|---|
| Pitch deck template (16:9) | 1920 × 1080 px slides, brand-locked | P0 | [TBD-OPERATOR] |
| Investor one-pager (PDF) | US Letter, single page | P0 | Need |
| Sales one-pager | US Letter, single page | P0 | Need |
| Customer case study template | 2-page PDF | P1 | Need (gated on customer logo approval) |
| Conference booth backdrop | 8 × 8 ft, 300dpi | P2 | Defer to Q4 |
| Sticker / swag sheet | Vector, single-color | P2 | Defer |

### Product marketing

| Asset | Spec | Priority | Status |
|---|---|---|---|
| Product UI hero screenshot (light + dark) | 2880 × 1800 px, retina | P0 | Need |
| Demo GIF library (5 core flows) | 1280 × 720 px, <5MB each | P0 | Need |
| 90-second product video | 1920 × 1080, MP4 | P1 | Need |
| Architecture diagram (agent loop) | SVG | P1 | Need |
| Whitepaper cover template | US Letter | P0 | Need (blocks deliverable #11) |

### Newsletter & content

| Asset | Spec | Priority | Status |
|---|---|---|---|
| Newsletter masthead | 600 × 150 px | P0 | Need |
| Issue header template (parameterized) | 1200 × 600 px | P0 | Need |
| Author byline avatars | 256 × 256 px | P1 | [TBD-OPERATOR] for headshots |

---

## 3. Gap Summary

- **P0 gaps blocking launch (count: 11):** LinkedIn banner, LinkedIn logo (vector), X header, X profile, OG homepage, OG blog template, Twitter Card, email header, sales one-pager, pitch deck template, product UI hero screenshot, demo GIFs, whitepaper cover.
- **P1 gaps (count: 9):** Featured cards, X pinned, blog OG variants, email signature, case study template, 90-sec video, architecture diagram, newsletter masthead, byline avatars.
- **P2 gaps (count: 5):** YouTube channel art + thumbnails, GitHub avatar, booth backdrop, swag.

## 4. Recommended Action

1. **Brand sprint week 1 (next 5 working days):** Lock color/type system with [TBD-OPERATOR]. Produce the 11 P0 assets in Figma against the locked system. Export at all required sizes.
2. **Brand sprint week 2:** P1 templates as parameterized Figma files so content team can ship without a designer.
3. **Vendor question for operator:** Do we have an in-house designer, a contractor, or do we run this through a sprint shop? [TBD-OPERATOR]

## 5. File Locations (proposed)

```
clients/costsage/operations/brand/assets/
  ├── logo/             (svg, png variants, light/dark)
  ├── color/            (palette.json, accessibility-report.md)
  ├── type/             (font-license.txt, type-scale.md)
  ├── social/           (li-banner.png, x-header.png, og-templates/)
  ├── product/          (ui-hero.png, demo-gifs/, architecture.svg)
  └── deck/             (investor.key/.pptx, sales-onepager.pdf)
```
