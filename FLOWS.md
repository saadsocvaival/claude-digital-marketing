# Execution Flows

Mermaid diagrams (GitHub renders natively). Covers: system map, onboarding, weekly loop, per-artifact production, decision authority, stop-loss, and escalation.

---

## 1. System Map — who talks to what

```mermaid
flowchart TB
    Operator([👤 Operator / VP Marketing])
    CMO[🎯 CMO Orchestrator<br/>.claude/agents/cmo-orchestrator.md]

    subgraph Heads[8 Department Heads]
      direction LR
      HG[Head of Growth]
      HP[Head of Performance]
      HS[Head of SEO/GEO/AEO]
      HC[Head of Content]
      HCR[Head of CRO]
      HA[Head of Analytics]
      HAU[Head of Automation]
      HB[Head of Brand]
    end

    Skills[(146 canonical skills<br/>+ 4 orchestration skills)]
    Rubrics[(19 rubrics<br/>pass bar 8)]
    Templates[(15 templates)]

    subgraph Client[clients/{id}/]
      Ledger[ledger.md]
      Plan[plan.md + okrs/]
      Feeds[feeds/weekly-kpi-snapshot.md]
      Artifacts[campaigns/ · emails/ · ads/<br/>seo-cluster/ · battlecards/ · content/]
      Events[(ledger-events/*.jsonl<br/>append-only)]
    end

    Vault[🔐 Secret vault<br/>1Password/Doppler]

    Operator -- goal / HITL answers --> CMO
    CMO -- delegate --> Heads
    Heads -- invoke --> Skills
    Skills -- use --> Templates
    Skills -- emit --> Artifacts
    Artifacts -- gated by --> Rubrics
    Heads -- read --> Ledger
    Heads -- read --> Plan
    HA -- publishes --> Feeds
    Heads -- read --> Feeds
    CMO -- reads all --> Client
    CMO -- writes --> Events
    Heads -- pointer-only --> Vault
    CMO -- weekly digest --> Operator
    CMO -. HITL when needed .-> Operator
```

---

## 2. Onboarding → Activation (one-time per client)

```mermaid
sequenceDiagram
    participant Op as 👤 Operator
    participant CMO as 🎯 CMO Orchestrator
    participant Onb as onboarding.skill
    participant GD as goal-decomposer.skill
    participant Heads as 8 Heads
    participant QA as quality-assurance
    participant FS as clients/{id}/

    Op->>CMO: "Onboard client {id} with goal X"
    CMO->>Onb: start(clientId)
    loop 12 leverage questions
        Onb->>Op: ask question N
        Op-->>Onb: answer
    end
    Onb->>FS: write ledger.md
    Onb->>QA: grade ledger.md vs rubrics/client-ledger.yaml
    QA-->>Onb: score (must be ≥8)
    alt score < 8
        Onb->>Op: request clarifications
    else score ≥ 8
        Onb-->>CMO: ledger ready
    end

    CMO->>GD: decompose(goal, ledger)
    GD->>GD: pick NSM + 3 supporting<br/>(rejected alts documented)
    GD->>GD: funnel math with 1.3× buffer
    GD->>GD: 8 Heads × (1 Obj + 3 KRs)
    GD->>FS: write plan.md + okrs/
    GD->>QA: grade vs rubrics/90-day-plan.yaml
    QA-->>GD: score (≥8)

    par parallel priming
        CMO->>Heads: load context (ledger, plan, OKRs)
    end
    Heads-->>CMO: ready + first-week action lists
    CMO-->>Op: activation digest + HITL (credentials, open Qs)
```

---

## 3. Weekly Execution Loop (recurring, Monday cadence)

```mermaid
flowchart TD
    Start([🗓️ Monday 09:00 trigger])
    Snap[Head of Analytics:<br/>publish weekly-kpi-snapshot.md]

    Start --> Snap
    Snap --> Read[CMO reads: ledger + plan + OKRs + snapshot + last week's events]
    Read --> Fan{Fan-out to 8 Heads}

    Fan --> G1[Growth: experiment portfolio review]
    Fan --> G2[Performance: paid health + stop-loss check]
    Fan --> G3[SEO: ranking + GEO/AEO citation check]
    Fan --> G4[Content: editorial calendar status + repurpose]
    Fan --> G5[CRO: LP experiment readouts]
    Fan --> G6[Analytics: anomaly flag + data quality]
    Fan --> G7[Automation: lifecycle program health]
    Fan --> G8[Brand: audience + press + voice drift]

    G1 & G2 & G3 & G4 & G5 & G6 & G7 & G8 --> Collect[CMO collects:<br/>3 actions per Head + HITL candidates]

    Collect --> Decide{Each action:<br/>authority level?}

    Decide -->|Full authority| Exec[Head executes<br/>→ write artifact<br/>→ rubric gate ≥8<br/>→ ledger-event]
    Decide -->|HITL required| Hitl[Emit hitl-request<br/>with options + recommendation]
    Decide -->|Escalate| Esc[CEO/CFO/Legal gate]

    Exec --> Digest
    Hitl --> Digest
    Esc --> Digest

    Digest[CMO assembles weekly digest<br/>rubrics/weekly-digest.yaml]
    Digest --> QA{Digest rubric ≥8?}
    QA -->|No| Iterate[Iterate / compress]
    Iterate --> QA
    QA -->|Yes| Deliver[Deliver to operator<br/>Slack + email]
    Deliver --> Ledger[Append ledger-events/*.jsonl]
    Ledger --> End([🏁 Next Monday])
```

---

## 4. Per-Artifact Production + Rubric Gate

```mermaid
stateDiagram-v2
    [*] --> Brief: Head receives brief
    Brief --> Draft: invoke skill<br/>(uses template + context)
    Draft --> BrandGate: brand-voice.yaml check
    BrandGate --> Rework1: score <8
    Rework1 --> Draft
    BrandGate --> SpecificGate: score ≥8

    SpecificGate: Artifact-specific rubric<br/>(e.g., ad-copy / seo-brief / campaign-brief)
    SpecificGate --> Rework2: score <8
    Rework2 --> Draft
    SpecificGate --> LegalGate: score ≥8

    LegalGate: Legal review?<br/>(only for regulated claims /<br/>competitor naming)
    LegalGate --> Hold: needs review
    Hold --> Legal[Legal sign-off]
    Legal --> LegalGate
    LegalGate --> CROGate: clean or N/A

    CROGate: CRO sign-off?<br/>(only for LPs / forms)
    CROGate --> DanaReview[Head of CRO approval]
    DanaReview --> CROGate
    CROGate --> Ship: clean or N/A

    Ship --> Event[append ledger-events/*.jsonl]
    Event --> Measure: wired to measurement plan
    Measure --> Review: review date (14/30/90d)
    Review --> Scale: ≥threshold
    Review --> Kill: <threshold
    Review --> Iterate2: inconclusive
    Scale --> [*]
    Kill --> [*]
    Iterate2 --> Draft
```

---

## 5. Decision Authority Matrix (who decides what)

```mermaid
flowchart LR
    Action([Proposed action])

    Action --> Check1{Inside<br/>policy +<br/>budget?}
    Check1 -->|Yes| Check2{Routine<br/>pattern?}
    Check1 -->|No| Hitl2[🟡 HITL request]

    Check2 -->|Yes| Full[🟢 Head executes<br/>under full authority]
    Check2 -->|No| Check3{Affects<br/>spend >10%,<br/>legal claims,<br/>pricing, brand?}

    Check3 -->|No| Full
    Check3 -->|Yes| Check4{Reversible<br/>within 48h?}

    Check4 -->|Yes| Hitl2
    Check4 -->|No| Check5{Strategic<br/>or<br/>external-facing?}

    Check5 -->|No| Hitl2
    Check5 -->|Yes| Esc2[🔴 Escalate<br/>CEO/CFO/Legal]

    Full --> Ledger1[ledger-events]
    Hitl2 --> Queue[HITL queue<br/>w/ deadline + default]
    Esc2 --> Queue
    Queue --> Ledger1
```

Defaults encoded in `.claude/agents/cmo-orchestrator.md` and per-Head agent files. Thresholds from `clients/{id}/ledger.md §7` override global defaults.

---

## 6. Stop-Loss Enforcement (paid campaigns)

```mermaid
flowchart TD
    Tick([Daily tick — Head of Performance])
    Tick --> Pull[Pull spend + CAC + ROAS + frequency from ad platforms]
    Pull --> Loop{For each campaign}

    Loop --> R1{ROAS <1.0<br/>for 14d?}
    R1 -->|Yes| Pause1[⛔ Auto-pause]
    R1 -->|No| R2

    R2{CAC >1.5× target<br/>for 21d?}
    R2 -->|Yes| Reallocate[🔄 Shift 50%<br/>to next-best channel]
    R2 -->|No| R3

    R3{Frequency >3.5<br/>on any creative?}
    R3 -->|Yes| Refresh[🎨 Force creative refresh<br/>within 14d]
    R3 -->|No| R4

    R4{Daily spend<br/>>$1,000<br/>per campaign?}
    R4 -->|Yes| Hitl3[🟡 HITL — CFO approval]
    R4 -->|No| Continue[✅ Continue pacing]

    Pause1 & Reallocate & Refresh & Hitl3 & Continue --> Event2[ledger-event emitted]
    Event2 --> Surface[Surfaced in weekly digest]
```

Thresholds live in each `campaigns/*.md` brief and in `.claude/agents/head-of-performance.md`. Customizable per client in `ledger.md`.

---

## 7. HITL (Human-In-The-Loop) Lifecycle

```mermaid
sequenceDiagram
    participant H as Dept Head
    participant CMO as CMO Orchestrator
    participant Q as HITL queue
    participant Op as Operator
    participant Led as ledger-events

    H->>CMO: needs decision (cites policy/threshold)
    CMO->>CMO: apply hitl-request.skill schema:<br/>why • options(2-4) • recommendation<br/>• deadline • default-if-no-response<br/>• blast radius
    CMO->>Q: enqueue
    Q->>Op: deliver via digest or urgent ping
    alt Op responds before deadline
        Op-->>Q: decision
        Q-->>CMO: resolve
    else deadline hits
        Q-->>CMO: apply default
    end
    CMO->>H: unblock + execute
    CMO->>Led: append resolution event
```

Constraints: ≤5 HITL items per weekly digest (more → compress with count). All HITL schema-compliant per `skills/orchestration/hitl-request.skill.md`.

---

## 8. When / What / How — at a glance

| When | Who triggers | What happens | Where it lands |
|---|---|---|---|
| New client | Operator invokes CMO | Onboarding skill (12 Qs) → ledger | `clients/{id}/ledger.md` |
| After ledger | CMO | Goal-decomposer → NSM, plan, OKRs | `plan.md`, `okrs/` |
| Every Monday 09:00 | Cron (Stage 4) or Operator | Weekly tick → snapshot → 8 Heads → digest | `feeds/`, digest, `ledger-events/` |
| Continuously | Head of Performance | Stop-loss checks on paid | auto-pause / reallocate / refresh |
| Any artifact shipped | Head via skill | Rubric gate (voice + specific + legal + CRO where applicable) | artifact file ends with `## Rubric Evaluation` |
| Decision outside authority | Head → CMO | HITL request schema → operator queue | digest + ledger-events |
| Experiment concludes | Head of Growth + owner | Readout + decision (ship/kill/iterate) | `experiments/{id}.md` |
| Quarter end | CMO | Monthly report aggregation + OKR grade | `feeds/monthly-*.md` |

---

## Notes
- Every arrow in these diagrams is a real file or a real skill invocation, not aspirational. Paths cited map to this repo.
- Stage 3 (MCP tool-calling) makes the "read from GA4 / write to Ads API" edges live — today those edges are specified, not wired. See `ROADMAP.md`.
- Stage 4 (autonomous scheduler) replaces "Operator triggers Monday" with a real cron.
