import os, re, sys

ROOT = r"C:\Users\shiraz.iqbal\Documents\VMD\vaival-agentic-marketing-engine\02-agents"

MAP = {
    # tier-4
    "tier-4-specialists/analytics-ops/marketing-data-analyst.agent.md": ["analytics-tracking","google-analytics","performance-reporter","campaign-analytics","search-console"],
    "tier-4-specialists/content/content-editor.agent.md": ["copy-editing","content-quality-auditor","content-humanizer"],
    "tier-4-specialists/content/graphic-designer.agent.md": ["ai-image-gen","stock-images","seo-image-gen","seo-images"],
    "tier-4-specialists/content/senior-content-writer.agent.md": ["copywriting","write-blog","write-landing","seo-content-writer","content-humanizer","seo-content-brief","marketing-psychology"],
    "tier-4-specialists/content/video-multimedia-producer.agent.md": ["video-content-strategist","video-ad-analysis","thread-writer"],
    "tier-4-specialists/email-crm/email-marketing-specialist.agent.md": ["email-sequence","email-subject-lines","cold-email","newsletter","lead-magnet","lead-magnets"],
    "tier-4-specialists/email-crm/marketing-automation-specialist.agent.md": ["hubspot","apollo-outreach","churn-prevention","icp-builder","customer-research"],
    "tier-4-specialists/paid/cro-landing-page-specialist.agent.md": ["page-cro","form-cro","ab-test-setup","write-landing","popup-cro","copywriting"],
    "tier-4-specialists/paid/paid-media-specialist.agent.md": ["paid-ads","google-ads","facebook-ads","linkedin-ads","ad-creative","campaign-analytics","video-ad-analysis","google-ads-report"],
    "tier-4-specialists/seo/aeo-specialist.agent.md": ["ai-seo","schema-markup","geo-query-finder","geo-content-optimizer","seo-sxo","schema-markup-generator"],
    "tier-4-specialists/seo/link-building-digital-pr-specialist.agent.md": ["backlink-audit","ahrefs-research","seo-backlinks","brand-monitor","brand-research","domain-authority-auditor","directory-submissions"],
    "tier-4-specialists/seo/seo-specialist.agent.md": ["seo-audit","keyword-research","on-page-seo-auditor","internal-linking-optimizer","rank-tracker","seo-content-brief","semrush-research","search-console"],
    "tier-4-specialists/seo/technical-seo-aeo-specialist.agent.md": ["technical-seo-checker","seo-technical","schema-markup","seo-sitemap","seo-hreflang","seo-firecrawl","seo-dataforseo","schema-markup-generator"],
    "tier-4-specialists/social/short-form-video-creator.agent.md": ["video-content-strategist","thread-writer","x-twitter-growth","social-content"],
    "tier-4-specialists/social/social-media-specialist.agent.md": ["social-content","social-media-analyzer","linkedin-content","reddit-marketing","bluesky","x-twitter-growth"],
    "tier-4-specialists/web/cro-specialist.agent.md": ["page-cro","form-cro","popup-cro","paywall-upgrade-cro","ab-test-setup","signup-flow-cro"],
    "tier-4-specialists/web/front-end-developer.agent.md": ["site-architecture","schema-markup-generator","meta-tags-optimizer"],
    "tier-4-specialists/web/ux-ui-designer.agent.md": ["signup-flow-cro","onboarding-cro","page-cro","form-cro"],
    # tier-5
    "tier-5-executives/analytics-ops/attribution-analyst.agent.md": ["campaign-analytics","analytics-tracking","performance-reporter"],
    "tier-5-executives/analytics-ops/dashboard-coordinator.agent.md": ["performance-reporter","google-analytics","google-ads-report"],
    "tier-5-executives/analytics-ops/utm-tag-qa-coordinator.agent.md": ["analytics-tracking"],
    "tier-5-executives/content/content-production-coordinator.agent.md": ["content-calendar","content-repurposing","content-production"],
    "tier-5-executives/content/content-writer-junior.agent.md": ["copywriting","copy-editing","write-blog"],
    "tier-5-executives/email-crm/deliverability-analyst.agent.md": ["email-subject-lines","hubspot"],
    "tier-5-executives/email-crm/email-production-coordinator.agent.md": ["email-sequence","newsletter","email-subject-lines"],
    "tier-5-executives/email-crm/lifecycle-journey-coordinator.agent.md": ["onboarding-cro","churn-prevention","email-sequence","lead-magnet"],
    "tier-5-executives/paid/paid-search-coordinator.agent.md": ["google-ads","google-ads-report","ad-creative"],
    "tier-5-executives/paid/paid-social-coordinator.agent.md": ["facebook-ads","linkedin-ads","ad-creative","video-ad-analysis"],
    "tier-5-executives/seo/geo-monitoring-coordinator.agent.md": ["geo-query-finder","geo-content-optimizer","brand-monitor","ai-seo"],
    "tier-5-executives/seo/keyword-research-coordinator.agent.md": ["keyword-research","content-gap-analysis","serp-analyzer","semrush-research"],
    "tier-5-executives/social/community-manager.agent.md": ["community-marketing","reddit-marketing","bluesky","social-content"],
    "tier-5-executives/social/social-scheduling-coordinator.agent.md": ["social-content","content-calendar"],
    "tier-5-executives/web/cms-page-builder.agent.md": ["site-architecture","schema-markup-generator","meta-tags-optimizer"],
    "tier-5-executives/web/experimentation-coordinator.agent.md": ["ab-test-setup","page-cro","form-cro"],
    "tier-5-executives/web/qa-accessibility-reviewer.agent.md": ["content-quality-auditor"],
}

patched = 0
for rel, skills in MAP.items():
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "\nskills:" in text:
        print(f"SKIP (already has skills): {rel}")
        continue
    block = "skills:\n" + "".join(f"  - {s}\n" for s in skills)
    new_text = re.sub(r"(\ntools: \[[^\]]*\]\n)", r"\1" + block, text, count=1)
    if new_text == text:
        # no tools line, insert before status:
        new_text = re.sub(r"(\nstatus:)", "\n" + block.rstrip() + r"\1", text, count=1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    patched += 1
    print(f"OK: {rel}")

print(f"\nPatched {patched}/{len(MAP)}")
