#!/bin/bash
# Install daily audit + Lighthouse cron jobs on the marketing-claude-soc server.
# Idempotent — won't duplicate if entries already present.
set -u
crontab -l > /tmp/crontab.bak.$(date +%s) 2>/dev/null || true
TMP=$(mktemp)
crontab -l 2>/dev/null > "$TMP" || true

ensure() {
  local entry="$1"
  if ! grep -Fxq "$entry" "$TMP"; then
    echo "$entry" >> "$TMP"
    echo "  + added: $entry"
  fi
}

ensure "5 6 * * * /opt/costsage-sprint1/lh-daily.sh > /var/log/costsage-lh-daily.log 2>&1"
ensure "5 7 * * * cd /tmp && python3 /opt/costsage-sprint1/audit-sweep.py > /var/log/costsage-audit-sweep.log 2>&1"
ensure "0 8 * * 1 python3 /opt/costsage-sprint1/weekly-digest.py > /var/log/costsage-weekly-digest.log 2>&1"

crontab "$TMP"
rm "$TMP"
echo "DONE. Active crontab:"
crontab -l
