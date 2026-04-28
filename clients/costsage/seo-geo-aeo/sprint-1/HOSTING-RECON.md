---
client_id: costsage
phase: 1
sprint: 1
artifact: hosting-topology-recon
date: 2026-04-27
access_method: ssh marketing-claude-soc (Cloudflare Access tunnel, root user)
---

# costsage.ai — hosting topology

## Server
- **Host:** `marketing-claude-soc.rundev.us` (Cloudflare Access SSH only; no public HTTP)
- **OS:** Ubuntu 22.04.5 LTS, kernel 6.8.0-110, Lenovo ThinkPad T480s (uptime 6h, load ~0.3)
- **Disk:** 234G total, 26G used (12%), 196G free
- **SSH user:** `root` (key `/Users/saad.ahmad.sec/costsage-market-team`)
- **Tunnels:** `cloudflared.service` + `cloudflared-second.service` (both running)

## What's running

| Container | Image | Port | Status | Role |
|---|---|---|---|---|
| `costsage-web` | `ghcr.io/shirazvaival/costsage-web:dev` | 8090→80 | healthy 6h | **Live costsage.ai static site** |
| `costsage-wp` | `wordpress:6.7-apache` | 8080→80 | up 6h | WordPress (likely staging/CMS) |
| `costsage-db` | `mariadb:11` | 3306 internal | healthy | DB for WP |
| `costsage-watchtower` | `containrrr/watchtower:latest` | — | **🔴 restart-loop** | auto-pull GHCR image |
| `costsage-wpcli` | `wordpress:cli` | — | exited 6 days | one-shot tool |

Compose: `/opt/wordpress/docker-compose.yml`.

## Cloudflare path

```
costsage.ai (DNS)
  → Cloudflare edge (TLS, WAF, AI-Bot rule injecting robots.txt rewrite ⚠️)
  → Cloudflare Tunnel
  → marketing-claude-soc.rundev.us:8090
  → docker container costsage-web
  → nginx serving /usr/share/nginx/html/*.html
```

## Source of truth for the live site

- **Source repo:** `https://github.com/shirazvaival/costsage-web` (per OCI label
  `org.opencontainers.image.source`).
- **Build:** GitHub Actions (presumably) → pushes `ghcr.io/shirazvaival/costsage-web:dev`.
- **Last build:** SHA `00e2ed3`, 2026-04-22T11:55:05Z.
- **Auto-deploy:** `costsage-watchtower` polls GHCR every 120s and recreates the container on a new digest. **Currently broken** — Docker API mismatch (`client version 1.25 too old, minimum 1.40`); auto-deploy is not happening. Pulls must be done manually until fixed.

## Files baked into the live container (`/usr/share/nginx/html/`)

```
about.html              35,021 B
azure.html              25,700 B
blog.html               24,752 B
cloudzero-alternative.html  36,464 B
contact.html            24,077 B
cro-audit-2026.html     80,705 B   ← in container, NOT in sitemap
data-access.html        26,009 B
features.html           28,268 B
finops-agent-vs-dashboard.html  43,378 B
index-v2.html           81,263 B   ← in container, NOT in sitemap (probably old)
index.html              76,963 B
nops-alternative.html   31,708 B
pricing.html            52,026 B
privacy.html            24,873 B
robots.txt                  65 B   ← permissive at origin; blocks injected at edge
sitemap.xml              2,230 B
terms.html              23,910 B
50x.html                   497 B
_build                      46 B   ← env=dev, sha=00e2ed3, time=2026-04-22T11:55:05Z
assets/                          (images, css, js)
```

## Critical findings (deploy-relevant, in addition to audit)

### F-H1 🔴 The "robots.txt blocks LLM bots" issue is a Cloudflare dashboard toggle, NOT a file change
The origin's `robots.txt` is already 3 lines, fully permissive. Cloudflare's
**AI Bots / AI Scrapers** managed feature is rewriting it at the edge.
**Fix path:** Cloudflare dashboard → `costsage.ai` zone → Security → Bots →
"AI Scrapers and Crawlers" → Off (Option A) or scoped (Option B). Also check
WAF managed rules and Scrape Shield → AI Labyrinth.
The file `sprint-1/patches/robots.txt.proposed` is still useful as the source-of-truth
default for the container, but the **observable** fix is the dashboard toggle.

### F-H2 🟠 Watchtower auto-deploy is broken (Docker API version mismatch)
```
client version 1.25 is too old. Minimum supported API version is 1.40
```
Restart loop. Until fixed, every image update needs `docker compose pull && docker compose up -d`.
**Fix:** update Watchtower image (`containrrr/watchtower:latest` is being pulled but the running tag is stale) or pin to a Watchtower release compatible with the host's Docker daemon.

### F-H3 🟡 Two stray HTML files baked into the image, not in sitemap
`index-v2.html` and `cro-audit-2026.html` are reachable directly (e.g. `costsage.ai/cro-audit-2026.html`) but absent from `sitemap.xml`. These need a decision:
- Remove from container if obsolete (preferred), OR
- Add to sitemap with `noindex` if intentional, OR
- Keep but add `<meta name="robots" content="noindex">` so Google doesn't surprise-index them.

### F-H4 🟡 No source-repo clone on the host; no `gh` CLI; no Watchtower-disable knob inside compose
Means **all changes must flow through `github.com/shirazvaival/costsage-web`** to be permanent.
Direct `docker exec` edits to the container are possible (write access verified) but get
clobbered the next time Watchtower wakes up (or a manual `docker compose pull`).

## Deploy paths — decision required (R5)

To ship Sprint-1 to costsage.ai, three options:

### Option D1 — Source-of-truth via PR to `shirazvaival/costsage-web` (recommended)
1. Add me as collaborator to `github.com/shirazvaival/costsage-web` (read+PR).
2. I open PRs there with the Sprint-1 file diffs (HTML edits, schema injects, new `/aws.html`, new `/blog/` posts, updated `sitemap.xml`).
3. Existing CI builds + pushes `:dev` to GHCR.
4. On the server, run `cd /opt/wordpress && docker compose pull costsage-web && docker compose up -d costsage-web` (or fix Watchtower first).
**Pros:** durable, git-tracked, reviewable, reversible. Standard workflow.
**Cons:** needs me added to the repo.

### Option D2 — Hot-patch container directly (fastest, ephemeral)
I `docker exec` into `costsage-web` and apply Sprint-1 patches directly to `/usr/share/nginx/html/*`. Live in seconds. Survives until next image pull.
**Pros:** instant validation; perfect for showing you results before committing.
**Cons:** clobbered on next Watchtower/compose-pull. Drift between live and source repo. Risky as a long-term path.

### Option D3 — Bind-mount overlay
Add a `volumes:` entry in `docker-compose.yml` mounting a host directory over `/usr/share/nginx/html/`. Maintain Sprint-1 patches in `/opt/wordpress/web-overlay/`. Survives image pulls.
**Pros:** durable without touching source repo.
**Cons:** creates a permanent fork between host overlay and source repo — operational drift hazard.

**Recommendation:** D1 as the durable path; D2 as a parallel "preview" pass so you can see/approve each change live before D1 lands. Operator picks.
