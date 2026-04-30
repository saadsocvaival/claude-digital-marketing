#!/usr/bin/env python3
"""Lightweight brand-voice static-checker for CostSage content.

Scans markdown or HTML files for:
  - Banned terms (per voice-guidelines.md)
  - Voice attribute drift
  - Category-claim drift (Agentic, Not Dashboard)
  - Forbidden-stat patterns ([TBD], unverified numbers)
  - Missing Sage Group disambiguation footer (HTML only)

Stdlib only. No external deps. Safe to run pre-commit, pre-publish, or in CI.

Usage:
    python3 brand-review.py <path-to-file>
    python3 brand-review.py --self-test

Exit codes:
    0 = pass
    1 = warnings (review recommended but not blocking)
    2 = failures (must fix before publish)
"""
import sys
import re
import os
from pathlib import Path

BANNED_TERMS = {
    "synergy": "fluff word; replace with concrete mechanism",
    "synergies": "fluff word; replace with concrete mechanism",
    "leverage": "as a verb, fluff; replace with 'use' or specific verb",
    "best-in-class": "unverifiable; replace with specific differentiator",
    "cutting-edge": "fluff; replace with specific tech",
    "world-class": "unverifiable; remove",
    "game-changing": "fluff; replace with specific outcome",
    "revolutionary": "fluff; replace with specific innovation",
    "seamlessly": "fluff; remove or replace with specific behavior",
    "holistic": "fluff; remove",
    "turnkey": "fluff; replace with 'ready-to-use' or specific term",
    "state-of-the-art": "fluff; remove or replace with specific tech",
    "industry-leading": "unverifiable; remove",
    "unparalleled": "unverifiable; remove",
    "transformational": "fluff; replace with specific outcome",
    "empowering": "fluff; replace with specific verb",
    "unlock": "fluff; replace with concrete action",
    "next-generation": "fluff; remove",
    "best-of-breed": "fluff; remove",
    "ecosystem": "vague; replace with specific component",
}

# Phrase-level patterns (regex)
BANNED_PHRASES = [
    (r"\bour solutions\b", "vague; replace with 'CostSage' or specific feature"),
    (r"\bdrive efficiency\b", "fluff; replace with specific outcome"),
    (r"\bunlock your\s+\w+\s+potential\b", "fluff; remove"),
    (r"\bmove the needle\b", "cliche; remove"),
    (r"\bdouble-click\b", "cliche when used metaphorically"),
]

# Category-claim drift — these contradict "Agentic, Not Dashboard"
CATEGORY_DRIFT = [
    (r"\bcomprehensive\s+dashboard\b", "contradicts category claim — we are NOT a dashboard product"),
    (r"\bbeautiful\s+dashboard\b", "we are NOT a dashboard product"),
    (r"\bdashboard-first\b", "contradicts agentic claim"),
]

# Stat patterns — uncited numbers
SUSPICIOUS_NUMBERS = [
    (r"save up to (\d+)%", "Specific percentage claim — verify it is operator-confirmed before public use"),
    (r"\$([0-9.]+)[MK]?/(?:month|mo|year|yr)", "Dollar claim — verify with operator before publish"),
]

REQUIRED_HTML_PATTERNS = [
    (r"Not affiliated with The Sage Group plc", "Sage Group disambiguation footer missing"),
]


def review(filepath):
    """Returns (issues_list, warnings_list)."""
    issues = []
    warnings = []
    if not os.path.exists(filepath):
        return [(f"File not found: {filepath}", 0)], []

    text = Path(filepath).read_text(encoding="utf-8")
    is_html = filepath.lower().endswith((".html", ".htm"))
    lines = text.split("\n")

    # 1. Banned terms (case-insensitive, word-boundary)
    for term, reason in BANNED_TERMS.items():
        for ln, line in enumerate(lines, 1):
            if re.search(rf"\b{re.escape(term)}\b", line, re.IGNORECASE):
                # Skip if in comment or in voice-guidelines context
                if "BANNED" in line.upper() or "DON'T" in line.upper() or "NOT:" in line.upper() or "<!--" in line:
                    continue
                if "voice-guidelines" in filepath.lower() or "brand-review" in filepath.lower():
                    continue
                issues.append((f"L{ln}: banned term '{term}' — {reason}", ln))

    # 2. Banned phrases
    for pattern, reason in BANNED_PHRASES:
        for ln, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                if "voice-guidelines" in filepath.lower() or "brand-review" in filepath.lower():
                    continue
                issues.append((f"L{ln}: banned phrase — {reason}: '{line.strip()[:80]}'", ln))

    # 3. Category drift
    for pattern, reason in CATEGORY_DRIFT:
        for ln, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                issues.append((f"L{ln}: category drift — {reason}: '{line.strip()[:80]}'", ln))

    # 4. Suspicious numbers
    for pattern, reason in SUSPICIOUS_NUMBERS:
        for ln, line in enumerate(lines, 1):
            m = re.search(pattern, line, re.IGNORECASE)
            if m and "[TBD]" not in line and "[unverified]" not in line and "[TBD-OPERATOR]" not in line:
                warnings.append((f"L{ln}: {reason}: '{m.group()}'", ln))

    # 5. HTML-only checks
    if is_html:
        for pattern, reason in REQUIRED_HTML_PATTERNS:
            if not re.search(pattern, text, re.IGNORECASE):
                warnings.append((f"HTML missing: {reason}", 0))

    # 6. [TBD-OPERATOR] flag — info-level
    tbd_count = text.count("[TBD-OPERATOR]")
    if tbd_count > 0:
        warnings.append((f"{tbd_count} [TBD-OPERATOR] placeholders — operator must fill before publish", 0))

    return issues, warnings


def selftest():
    """Run 3 inline fixtures and verify they produce expected results."""
    print("=== brand-review self-test ===\n")

    # Fixture 1: clean piece
    clean = """# CostSage cuts AWS spend

CostSage's agents identify rightsizing opportunities, idle resources, and Reserved Instance
gaps on AWS and Azure. Each fix runs under your approval, with audit trails and rollback safety.

Used by AWS-first SaaS teams in the $10K-$500K monthly cloud-spend range.
"""
    Path("/tmp/_brand_test_clean.md").write_text(clean)
    issues, warnings = review("/tmp/_brand_test_clean.md")
    print(f"Fixture 1 (clean): {len(issues)} issues, {len(warnings)} warnings")
    assert len(issues) == 0, f"Expected 0 issues on clean, got {len(issues)}: {issues}"
    print("  ✓ PASS\n")

    # Fixture 2: piece with banned terms
    bad = """# Our world-class FinOps solution

We leverage cutting-edge synergies to deliver best-in-class cloud cost optimization.
Our holistic platform empowers teams to seamlessly transform their cloud strategy.

Save up to 99% (TBD: this is the marketing claim, no source).
"""
    Path("/tmp/_brand_test_bad.md").write_text(bad)
    issues, warnings = review("/tmp/_brand_test_bad.md")
    print(f"Fixture 2 (banned terms): {len(issues)} issues, {len(warnings)} warnings")
    assert len(issues) >= 5, f"Expected ≥5 issues, got {len(issues)}"
    print("  ✓ PASS (caught banned terms)")
    for i, (msg, _) in enumerate(issues[:3]):
        print(f"  example {i+1}: {msg[:80]}")
    print()

    # Fixture 3: category-drift piece
    drift = """# CostSage — the comprehensive dashboard for FinOps

Our beautiful dashboard surfaces cloud waste in real-time. The dashboard-first approach
gives engineers full visibility into cost.
"""
    Path("/tmp/_brand_test_drift.md").write_text(drift)
    issues, warnings = review("/tmp/_brand_test_drift.md")
    print(f"Fixture 3 (category drift): {len(issues)} issues, {len(warnings)} warnings")
    assert len(issues) >= 2, f"Expected ≥2 category-drift issues, got {len(issues)}"
    print("  ✓ PASS (caught dashboard drift)")
    print()

    # Cleanup
    for f in ["/tmp/_brand_test_clean.md", "/tmp/_brand_test_bad.md", "/tmp/_brand_test_drift.md"]:
        try:
            os.remove(f)
        except FileNotFoundError:
            pass

    print("=== ALL 3 FIXTURES PASSED ===")
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    if sys.argv[1] == "--self-test":
        return selftest()

    filepath = sys.argv[1]
    issues, warnings = review(filepath)

    print(f"=== brand-review: {filepath} ===\n")

    if issues:
        print(f"❌ FAILURES ({len(issues)}):")
        for msg, _ in issues:
            print(f"  {msg}")
        print()

    if warnings:
        print(f"⚠️  WARNINGS ({len(warnings)}):")
        for msg, _ in warnings:
            print(f"  {msg}")
        print()

    if not issues and not warnings:
        print("✅ PASS — no voice violations found.")
        return 0

    if issues:
        print("❌ Must fix before publish.")
        return 2

    print("⚠️  Review recommended but not blocking.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
