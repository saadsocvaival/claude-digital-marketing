# `<html lang>` patch — F13

## Current state
None of the 13 audited pages declares `lang` on the `<html>` root element.
Site uses British English ("optimisation").

## Fix
Update the layout/template's root `<html>` tag site-wide:
```html
<html lang="en-GB">
```

## Verification
```bash
curl -sL https://costsage.ai/ | grep -oE '<html[^>]*>'
# expect: <html lang="en-GB">
```

## Why
- Tells search and answer engines the language and regional dialect.
- Improves voice-search and accessibility (screen readers).
- One-line change; no UX impact.

## Optional follow-up (Phase 2)
If you ever ship en-US content (rewriting "optimisation" → "optimization"):
- Use `lang="en-US"` on those specific pages, OR
- Author a parallel `costsage.ai/us/` tree with `hreflang` pairs.

For now, single-language en-GB is correct.
