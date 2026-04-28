# Reddit Engagement Playbook

Reddit is a karma economy. Lead with value. Disclose affiliation. CostSage links are the *exception*, not the rule. Goal in first 90 days: become a recognized helpful presence, not a brand account.

---

## Target subreddits

| Sub | Subscribers (approx) | Why | Cadence |
|---|---|---|---|
| r/aws | ~500K | Highest-density AWS practitioners | Daily skim, 2–3 quality comments/wk |
| r/devops | ~400K | Cost-as-engineering-concern crowd | 2–3 comments/wk |
| r/sre | ~80K | Reliability ↔ cost trade-off | 1–2 comments/wk |
| r/AWS_cloud | ~smaller | Beginner-leaning, easy karma + helpful | 2 comments/wk |
| r/FinOps | ~small but high signal | Direct ICP | 3+ comments/wk, no shilling |
| r/kubernetes | ~150K | K8s cost questions weekly | 1–2 comments/wk |
| r/sysadmin | ~900K | Occasional cost threads | 1 comment/wk, opportunistic |

---

## Voice rules

1. **Disclose affiliation** the first time CostSage is mentioned in any thread. Format: `(disclosure: I work on CostSage, a FinOps tool)`.
2. **Never lead with the product.** Lead with the answer. Mention CostSage only if it directly fits.
3. **No copy-paste.** Every comment is hand-written. Treat the account like a person.
4. **No DMs to OP** to pitch.
5. **Don't downvote competitors.** Don't comment on competitor mentions to redirect — that's transparent and gets banned.
6. **No link in title.** Self-posts only when sharing.
7. **9:1 ratio at minimum.** 9 value-add comments for every 1 that mentions CostSage.

---

## Value-add answer template

```
[Direct answer to question — 1–2 sentences, top]

[Reasoning / context — 2–4 sentences, why this answer is right]

[Concrete example or numbers if you have them]

[Optional: relevant resource — open-source tool, AWS doc, blog post.
   CostSage link only if directly on point AND with disclosure.]
```

Example (good):
> Commit to your trough, not your peak. SP utilization below ~90% means your effective discount is closer to 12% than 28%, so over-committing actively destroys value.
>
> Quick check: pull SP utilization for the last 90d in Cost Explorer; if you're above 92% sustained, you have headroom to commit more.
>
> (disclosure: I work on CostSage which automates this, but the math above is general — you can do it from CE alone.)

---

## When to mention CostSage (rare)

Only when ALL three are true:
1. The question is *exactly* what CostSage does (e.g., "tool to auto-recommend AWS savings actions").
2. You've already provided a non-CostSage answer they could use without us.
3. You disclose affiliation in the same comment.

Never mention in: career questions, AWS basics threads, cert questions, troubleshooting (non-cost) questions.

---

## First 30-day karma-build plan

**Week 1 — Lurk + 5 comments.** Subs: r/aws, r/devops, r/FinOps. Comments are pure helpful, zero CostSage mentions, zero links to costsage.ai. Goal: learn each sub's voice, get 100+ karma.

**Week 2 — 10 comments.** Same subs + r/sre. Still no CostSage links. Maybe one self-disclosure comment if perfectly relevant.

**Week 3 — 12 comments + 1 self-post.** Self-post is a *resource*, not a product post. Example: "I made a calculator/diagram for SP-vs-RI break-even, sharing free." Hosted on costsage.ai/blog/ri-vs-savings-plans (allowed if it's genuine resource and you disclose).

**Week 4 — 15 comments + maybe 1 more share.** First time CostSage gets mentioned in a comment, only if perfectly on-topic and you disclose.

Target karma by day 30: 500+. If under 200, slow down and re-evaluate voice.

---

## Banned moves

- Sock-puppeting / multiple accounts
- Editing comments to add links after they got upvoted
- "Just curious, anyone tried CostSage?" planted questions
- Affiliate-style "use code X" posts
- Replying to every CostSage mention (it's obvious)
- Linking the same blog post 3+ times in a week

---

## Operator workflow

- Daily: skim 6 target subs for 10 min in morning. Bookmark 1–3 threads worth answering.
- Comment in evening (off-peak posting often gets better dwell).
- Log every CostSage-linking comment in a tracker [TBD-OPERATOR sheet].
- Monthly: review which subs returned engagement → invest more / less.

[TBD-OPERATOR]: confirm Reddit account handle, decide whether founder also posts under personal handle (recommended yes, with separate cadence).
