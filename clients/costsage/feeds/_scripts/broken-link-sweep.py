#!/usr/bin/env python3
"""Broken-link sweep: extract all internal + external links from 23 URLs,
HEAD-check each unique target, record any non-2xx responses."""
import re, json, subprocess, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse

URLS = [
    "https://costsage.ai/", "https://costsage.ai/about", "https://costsage.ai/features",
    "https://costsage.ai/pricing", "https://costsage.ai/contact", "https://costsage.ai/azure",
    "https://costsage.ai/aws", "https://costsage.ai/data-access", "https://costsage.ai/finops-agent-vs-dashboard",
    "https://costsage.ai/nops-alternative", "https://costsage.ai/cloudzero-alternative",
    "https://costsage.ai/blog", "https://costsage.ai/blog/aws-cost-optimisation-best-practices",
    "https://costsage.ai/blog/ri-vs-savings-plans", "https://costsage.ai/finops-for-ai-workloads",
    "https://costsage.ai/azure-cost-optimization", "https://costsage.ai/multi-cloud",
    "https://costsage.ai/alternatives/vantage", "https://costsage.ai/alternatives/prosperops",
    "https://costsage.ai/compare/cloudzero-vs-costsage", "https://costsage.ai/compare/nops-vs-costsage",
    "https://costsage.ai/privacy", "https://costsage.ai/terms",
]

def fetch(url):
    return subprocess.run(["curl", "-sA", "Mozilla/5.0", url], capture_output=True, text=True, timeout=30).stdout

def extract_links(html, page_url):
    """Return list of (link_target, type) tuples."""
    found = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', html, re.IGNORECASE)
    out = []
    for href in found:
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("javascript:"):
            continue
        # Resolve relative
        full = urljoin(page_url, href)
        # Skip bare anchors after resolution
        if full.split("#")[0] == page_url.split("#")[0]:
            continue
        kind = "internal" if "costsage.ai" in full else "external"
        out.append((full.split("#")[0], kind, page_url))
    return out

def check(url):
    try:
        r = subprocess.run(["curl", "-sI", "-A", "Mozilla/5.0", "-o", "/dev/null", "-w", "%{http_code}", "-L", "--max-redirs", "5", url],
                           capture_output=True, text=True, timeout=20)
        return r.stdout.strip()
    except Exception as e:
        return f"ERR:{e}"

# 1. Crawl all 23 pages, gather links
print("=== gathering links ===")
all_links = {}  # target -> [{kind, sources:[]}]
for u in URLS:
    html = fetch(u)
    for tgt, kind, src in extract_links(html, u):
        if tgt not in all_links:
            all_links[tgt] = {"kind": kind, "sources": []}
        all_links[tgt]["sources"].append(src)

print(f"  unique targets: {len(all_links)}")
print(f"  internal: {sum(1 for v in all_links.values() if v['kind']=='internal')}")
print(f"  external: {sum(1 for v in all_links.values() if v['kind']=='external')}")

# 2. HEAD-check all
print("\n=== HEAD-checking ===")
results = {}
with ThreadPoolExecutor(max_workers=10) as ex:
    fut = {ex.submit(check, t): t for t in all_links}
    for f in as_completed(fut):
        t = fut[f]
        try: results[t] = f.result()
        except Exception as e: results[t] = f"ERR:{e}"

# 3. Report
print("\n=== RESULTS ===")
broken = []
for t, code in sorted(results.items()):
    if not code.startswith("2") and not code.startswith("3"):
        broken.append((t, code, all_links[t]))

# Group by status
by_code = {}
for t, c, info in broken:
    by_code.setdefault(c, []).append((t, info))

for code, items in sorted(by_code.items()):
    print(f"\n--- HTTP {code} ({len(items)} targets) ---")
    for t, info in items[:10]:
        sources_unique = sorted(set(info["sources"]))
        print(f"  {t}")
        print(f"    referenced from: {len(sources_unique)} pages: {[s.replace('https://costsage.ai','') or '/' for s in sources_unique[:3]]}")
    if len(items) > 10:
        print(f"  ...and {len(items)-10} more")

# 4. Save JSON
out = {
    "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "url_count_crawled": len(URLS),
    "unique_link_targets": len(all_links),
    "internal_count": sum(1 for v in all_links.values() if v["kind"]=="internal"),
    "external_count": sum(1 for v in all_links.values() if v["kind"]=="external"),
    "broken_count": len(broken),
    "broken_by_code": {c: [{"target": t, "sources": info["sources"]} for t, info in items] for c, items in by_code.items()},
    "all_targets": {t: {"kind": all_links[t]["kind"], "status": results[t], "sources_count": len(set(all_links[t]["sources"]))} for t in all_links},
}
with open("/tmp/claude-digital-marketing/clients/costsage/feeds/broken-link-sweep-2026-04-28.json", "w") as f:
    json.dump(out, f, indent=2)
print(f"\n=== summary ===")
print(f"Crawled 23 pages, {len(all_links)} unique link targets")
print(f"Broken: {len(broken)}")
print(f"JSON: clients/costsage/feeds/broken-link-sweep-2026-04-28.json")
