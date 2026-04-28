# BreadcrumbList JSON-LD — F15

Add one `<script type="application/ld+json">` block to each of these 9 pages.
Drop in `<head>` adjacent to existing schema.

---

## /features
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Features", "item": "https://costsage.ai/features"}
  ]
}
```

## /pricing
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Pricing", "item": "https://costsage.ai/pricing"}
  ]
}
```

## /nops-alternative
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Compare", "item": "https://costsage.ai/#compare"},
    {"@type": "ListItem", "position": 3, "name": "nOps Alternative", "item": "https://costsage.ai/nops-alternative"}
  ]
}
```

## /cloudzero-alternative
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Compare", "item": "https://costsage.ai/#compare"},
    {"@type": "ListItem", "position": 3, "name": "CloudZero Alternative", "item": "https://costsage.ai/cloudzero-alternative"}
  ]
}
```

## /finops-agent-vs-dashboard
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://costsage.ai/blog"},
    {"@type": "ListItem", "position": 3, "name": "FinOps Agent vs Dashboard", "item": "https://costsage.ai/finops-agent-vs-dashboard"}
  ]
}
```

## /azure
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Azure Cost Optimisation", "item": "https://costsage.ai/azure"}
  ]
}
```

## /aws (new — already in pages/aws.html)
Already included in `pages/aws.html`. No additional patch needed.

## /data-access
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Data Access", "item": "https://costsage.ai/data-access"}
  ]
}
```

## /privacy
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Privacy Policy", "item": "https://costsage.ai/privacy"}
  ]
}
```

## /terms
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://costsage.ai/"},
    {"@type": "ListItem", "position": 2, "name": "Terms of Service", "item": "https://costsage.ai/terms"}
  ]
}
```
