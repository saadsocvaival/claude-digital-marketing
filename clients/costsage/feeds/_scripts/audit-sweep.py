#!/usr/bin/env python3
"""Comprehensive real-data audit sweep across all 23 costsage.ai URLs.
Captures: HTTP headers, security headers, schema/JSON-LD validity, on-page SEO,
broken-link surface, image alt coverage, canonical correctness, multi-UA parity.
No external API. Pure curl + json.loads. Output as JSON for the feeds/ directory.
"""
import json, os, re, subprocess, time, hashlib, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse, urljoin

URLS = [
    "https://costsage.ai/",
    "https://costsage.ai/about",
    "https://costsage.ai/features",
    "https://costsage.ai/pricing",
    "https://costsage.ai/contact",
    "https://costsage.ai/azure",
    "https://costsage.ai/aws",
    "https://costsage.ai/data-access",
    "https://costsage.ai/finops-agent-vs-dashboard",
    "https://costsage.ai/nops-alternative",
    "https://costsage.ai/cloudzero-alternative",
    "https://costsage.ai/blog",
    "https://costsage.ai/blog/aws-cost-optimisation-best-practices",
    "https://costsage.ai/blog/ri-vs-savings-plans",
    "https://costsage.ai/finops-for-ai-workloads",
    "https://costsage.ai/azure-cost-optimization",
    "https://costsage.ai/multi-cloud",
    "https://costsage.ai/alternatives/vantage",
    "https://costsage.ai/alternatives/prosperops",
    "https://costsage.ai/compare/cloudzero-vs-costsage",
    "https://costsage.ai/compare/nops-vs-costsage",
    "https://costsage.ai/privacy",
    "https://costsage.ai/terms",
]

UAS = {
    "Mozilla":   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Googlebot": "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "ClaudeBot": "ClaudeBot/1.0",
    "GPTBot":    "GPTBot/1.0",
    "PerplexityBot": "PerplexityBot/1.0",
}

SECURITY_HEADERS = [
    "strict-transport-security",
    "content-security-policy",
    "x-frame-options",
    "x-content-type-options",
    "referrer-policy",
    "permissions-policy",
    "x-xss-protection",
]

def curl(url, ua, head=False, follow=False):
    cmd = ["curl", "-s", "-A", ua, "-o", "/dev/null", "-w",
           "%{http_code}\t%{time_starttransfer}\t%{size_download}\t%{url_effective}"]
    if head: cmd.append("-I")
    if follow: cmd.append("-L")
    cmd.append(url)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    parts = r.stdout.strip().split("\t")
    if len(parts) < 4: return None
    return {"status": parts[0], "ttfb": parts[1], "size": parts[2], "final": parts[3]}

def fetch_headers(url, ua):
    r = subprocess.run(["curl", "-sI", "-A", ua, url], capture_output=True, text=True, timeout=30)
    headers = {}
    for line in r.stdout.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            headers[k.strip().lower()] = v.strip()
    return headers

def fetch_html(url, ua):
    r = subprocess.run(["curl", "-s", "-A", ua, url], capture_output=True, text=True, timeout=60)
    return r.stdout

def analyse_html(html, url):
    out = {"url": url}
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.DOTALL | re.IGNORECASE)
    out["title"] = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    out["title_len"] = len(out["title"])
    m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', html, re.IGNORECASE)
    out["desc"] = m.group(1) if m else ""
    out["desc_len"] = len(out["desc"])
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', html, re.IGNORECASE)
    out["canonical"] = m.group(1) if m else ""
    out["canonical_matches_url"] = (out["canonical"].rstrip("/") == url.rstrip("/")) if out["canonical"] else False
    m = re.search(r'<html[^>]*\blang=["\']([^"\']+)', html, re.IGNORECASE)
    out["lang"] = m.group(1) if m else ""
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL | re.IGNORECASE)
    out["h1_count"] = len(h1s)
    out["h1_first"] = re.sub(r"<[^>]+>", "", h1s[0]).strip()[:140] if h1s else ""
    out["h2_count"] = len(re.findall(r"<h2[^>]*>", html, re.IGNORECASE))
    out["h3_count"] = len(re.findall(r"<h3[^>]*>", html, re.IGNORECASE))
    # Question-shaped H2s (AEO signal)
    h2_texts = re.findall(r"<h2[^>]*>(.*?)</h2>", html, re.DOTALL | re.IGNORECASE)
    out["h2_question_form"] = sum(1 for h in h2_texts if "?" in h)
    # links
    links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', html, re.IGNORECASE)
    out["links_total"] = len(links)
    out["links_internal"] = sum(1 for l in links if l.startswith("/") or "costsage.ai" in l)
    out["links_external"] = sum(1 for l in links if l.startswith("http") and "costsage.ai" not in l)
    out["links_anchor_only"] = sum(1 for l in links if l.startswith("#"))
    # imgs
    imgs = re.findall(r"<img[^>]*>", html, re.IGNORECASE)
    out["img_count"] = len(imgs)
    out["img_no_alt"] = sum(1 for i in imgs if not re.search(r'\balt=', i, re.IGNORECASE))
    out["img_lazy"] = sum(1 for i in imgs if re.search(r'loading=["\']lazy', i, re.IGNORECASE))
    # words (visible)
    txt = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    txt = re.sub(r"<style[^>]*>.*?</style>", "", txt, flags=re.DOTALL | re.IGNORECASE)
    txt = re.sub(r"<[^>]+>", " ", txt)
    out["word_count"] = len(re.findall(r"\b\w+\b", txt))
    # OG / TwCard
    out["og_title"] = bool(re.search(r'property=["\']og:title["\']', html, re.IGNORECASE))
    out["og_desc"]  = bool(re.search(r'property=["\']og:description["\']', html, re.IGNORECASE))
    out["og_image"] = bool(re.search(r'property=["\']og:image["\']', html, re.IGNORECASE))
    out["tw_card"]  = bool(re.search(r'name=["\']twitter:card["\']', html, re.IGNORECASE))
    # JSON-LD
    blocks = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    out["jsonld_blocks"] = len(blocks)
    valid, invalid, types = 0, 0, []
    for b in blocks:
        try:
            j = json.loads(b.strip())
            valid += 1
            def walk(o):
                if isinstance(o, dict):
                    if "@type" in o:
                        v = o["@type"]
                        if isinstance(v, list): types.extend(v)
                        else: types.append(v)
                    for k, v in o.items():
                        if isinstance(v, (dict, list)): walk(v)
                elif isinstance(o, list):
                    for x in o: walk(x)
            walk(j)
        except Exception:
            invalid += 1
    out["jsonld_valid"] = valid
    out["jsonld_invalid"] = invalid
    out["jsonld_types"] = sorted(set(types))
    # broken-anchor probe
    out["external_links_sample"] = list(set(l for l in links if l.startswith("http") and "costsage.ai" not in l))[:10]
    return out

def per_url(url):
    print(f"  fetching {url}", flush=True)
    result = {"url": url, "ts": int(time.time())}
    # Multi-UA HEAD
    result["status_by_ua"] = {}
    for label, ua in UAS.items():
        h = fetch_headers(url, ua)
        result["status_by_ua"][label] = {
            "status": h.get("status_line", ""),
            "x-robots-tag": h.get("x-robots-tag", ""),
        }
    # security headers
    h = fetch_headers(url, UAS["Mozilla"])
    result["security_headers"] = {k: h.get(k, "") for k in SECURITY_HEADERS}
    result["headers"] = {k: h.get(k, "") for k in ["server", "cache-control", "content-type", "cf-cache-status", "content-encoding"]}
    # body fetch + analyse
    html = fetch_html(url, UAS["Mozilla"])
    result["analysis"] = analyse_html(html, url)
    result["body_size"] = len(html)
    return result

def main():
    print(f"=== sweep starting ({len(URLS)} URLs) ===", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(per_url, u): u for u in URLS}
        for fut in as_completed(futures):
            try: results.append(fut.result())
            except Exception as e: results.append({"url": futures[fut], "error": str(e)})
    results.sort(key=lambda r: URLS.index(r["url"]) if r["url"] in URLS else 999)
    return results

results = main()
out = {
    "swept_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "url_count": len(results),
    "tool": "audit-sweep.py v1.0 (curl + python regex + json.loads)",
    "summary": {},
    "results": results,
}
# aggregates
ok = sum(1 for r in results if r.get("status_by_ua",{}).get("Mozilla",{}).get("status","").endswith("200") or r.get("body_size",0)>0)
out["summary"] = {
    "urls_returning_200_to_mozilla": sum(1 for r in results if r.get("status_by_ua",{}).get("Mozilla",{}).get("status","")),
    "urls_with_body": sum(1 for r in results if r.get("body_size",0) > 1000),
    "total_jsonld_blocks": sum(r.get("analysis",{}).get("jsonld_blocks",0) for r in results),
    "total_jsonld_valid": sum(r.get("analysis",{}).get("jsonld_valid",0) for r in results),
    "total_jsonld_invalid": sum(r.get("analysis",{}).get("jsonld_invalid",0) for r in results),
    "schema_types_present": sorted({t for r in results for t in r.get("analysis",{}).get("jsonld_types",[])}),
    "avg_word_count": round(sum(r.get("analysis",{}).get("word_count",0) for r in results) / max(1,len(results))),
    "total_words": sum(r.get("analysis",{}).get("word_count",0) for r in results),
    "total_internal_links": sum(r.get("analysis",{}).get("links_internal",0) for r in results),
    "total_external_links": sum(r.get("analysis",{}).get("links_external",0) for r in results),
    "total_imgs_no_alt": sum(r.get("analysis",{}).get("img_no_alt",0) for r in results),
    "total_imgs_lazy": sum(r.get("analysis",{}).get("img_lazy",0) for r in results),
    "h2_question_form_total": sum(r.get("analysis",{}).get("h2_question_form",0) for r in results),
    "missing_canonical": [r["url"] for r in results if not r.get("analysis",{}).get("canonical")],
    "canonical_mismatches": [r["url"] for r in results if r.get("analysis",{}).get("canonical") and not r.get("analysis",{}).get("canonical_matches_url")],
    "missing_og_image": [r["url"] for r in results if not r.get("analysis",{}).get("og_image")],
    "missing_security_hsts": [r["url"] for r in results if not r.get("security_headers",{}).get("strict-transport-security")],
    "missing_security_csp": [r["url"] for r in results if not r.get("security_headers",{}).get("content-security-policy")],
    "missing_security_xfo": [r["url"] for r in results if not r.get("security_headers",{}).get("x-frame-options")],
}
print(json.dumps(out, indent=2, default=str))
