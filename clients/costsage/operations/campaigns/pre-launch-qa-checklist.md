---
artifact: pre-launch-qa-checklist
date: 2026-04-30
purpose: every paid campaign passes through this checklist before going live
---

# Pre-Launch QA Checklist (Paid Media)

## 1. Pixel + tracking
- [ ] Conversion pixel firing correctly on landing-page form submission (test in browser DevTools Network tab)
- [ ] Conversion event matches the spec in `operations/campaigns/conversion-tracking-spec.md`
- [ ] UTM params preserved through any redirects
- [ ] No double-firing (e.g., on browser back button)
- [ ] Cross-domain tracking working if traffic crosses costsage.ai → app domain
- [ ] Mobile-Safari tested (most likely platform with tracking quirks)

## 2. Landing page CRO-ready
- [ ] LP loads in <3s on mobile (test via Lighthouse)
- [ ] Hero matches ad creative promise (no bait-and-switch)
- [ ] CTA above fold on mobile
- [ ] Form-funnel friction minimised per `operations/web-cro/form-funnel-audit.md`
- [ ] Mobile preview clean (no overlapping CTAs, broken buttons)
- [ ] Page is `noindex,follow` for paid LPs (don't cannibalise organic)

## 3. Audience size sanity check
- [ ] Total addressable audience >50K? (too narrow = wasted impressions)
- [ ] Total addressable audience <5M? (too broad = wasted spend)
- [ ] Excludes existing customers
- [ ] Excludes recent unsubscribes
- [ ] Excludes employees / interns (cheap-impression source)

## 4. Creative review
- [ ] Brand-voice review passes (`operations/brand/brand-review.py`)
- [ ] No banned terms (synergy, leverage, best-in-class)
- [ ] No fabricated stats; every number sourced
- [ ] Disclaimer/footer compliance check (esp. EU markets)
- [ ] A/B variant clearly differentiated (not just word changes)

## 5. Budget + bid sanity check
- [ ] Daily budget matches `stop-loss-rules.md` cap
- [ ] Auto-pause rules wired (where platform allows)
- [ ] Bid strategy = "Maximize conversions" with target CPL set
- [ ] No "Maximize clicks" (vanity metric) unless reason documented

## 6. Kill-switch tested
- [ ] Single human can pause campaign in <30 seconds
- [ ] After-hours kill path documented
- [ ] All on-call rotation members briefed

## 7. Post-launch 72h watch
- [ ] Hour 1: pixel firing verified live
- [ ] Hour 4: first impressions reviewed
- [ ] Hour 24: CTR / CPC vs target reviewed
- [ ] Hour 72: conversion rate vs target reviewed
- [ ] If any breach in 72h: pause + investigate (auto-pause script)

## 8. Sign-off

- Brief author: ___________
- Pixel/tracking review: ___________
- Brand-voice review: ___________
- Budget approver: ___________
- Final sign-off (founder or marketing lead): ___________
- Launch time: ___________
- 72h post-launch review scheduled: ___________
