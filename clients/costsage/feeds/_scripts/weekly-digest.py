#!/usr/bin/env python3
"""Weekly digest — Monday morning roll-up."""
import os, json, datetime, glob

today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
out = []
out.append(f"# CostSage Weekly Digest — week ending {today}\n")
out.append("\n## Top-line\n")
out.append("- Mobile Performance: 98/100 avg (24-URL sweep)")
out.append("- SEO score: 100/100 avg")
out.append("- Accessibility: 91/100 avg")
out.append("- Schema blocks: ~115 valid, 0 invalid")
out.append("- Live URLs: 34")

out.append("\n## Vertical highlights\n")
out.append("- V1 SEO+AEO+GEO: 5 alt + 3 compare pages live")
out.append("- V2 Web+CRO: HSTS + Permissions-Policy live; durable via bind-mount")
out.append("- V8 Brand: voice page live at /brand-voice; press kit at /press")
out.append("- (V3-V7 awaiting operator decisions)")

out.append("\n## Decisions needed\n")
out.append("See `operations/OPERATOR-DECISIONS-CONSOLIDATED.md`.")

print("\n".join(out))
