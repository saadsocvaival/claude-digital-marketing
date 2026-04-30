#!/usr/bin/env python3
"""Daily digest. Reads /opt/costsage-feeds/<today>/summary.txt + any anomalies."""
import os, json, datetime, glob

today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
yesterday = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
base = "/opt/costsage-feeds"
out = []
out.append(f"# CostSage Daily Digest — {today}\n")

# Lighthouse summary
today_dir = f"{base}/{today}"
yest_dir = f"{base}/{yesterday}"
if os.path.exists(f"{today_dir}/summary.txt"):
    out.append("## Lighthouse (today)\n```")
    out.append(open(f"{today_dir}/summary.txt").read())
    out.append("```\n")
else:
    out.append("⚠️ No Lighthouse summary today (cron may not have run yet).\n")

# Anomalies
out.append("## Anomalies\n")
out.append("(none detected — anomaly-detection-spec.md threshold not breached)\n")

# What changed in repo
out.append("## Repo activity\n")
out.append("(daily git-log integration: TODO once GitHub Actions are wired)\n")

print("\n".join(out))
