# escalation.md — Escalation Protocol

> When and how issues escalate.
> Clear rules prevent confusion and ensure Harley's time is protected.

---

## SEVERITY LEVELS

| Level | Type | Example | Resolver |
|-------|------|---------|----------|
| 1 | Task/Format | "Which formatting style?", "Who does this task?" | Z auto-resolves |
| 2 | Process/Priority | "Which comes first?", "How should we do this?" | Z + precedent |
| 3 | Principle/Strategic | "Does this align with our values?", "Major direction change" | Harley must approve |

---

## ESCALATION TRIGGERS

### Level 1 → Level 2 Escalation

Escalate when:
- No precedent exists in decision_log.md
- Two reasonable options exist, both valid
- Task affects multiple projects
- Z confidence < 80%

### Level 2 → Level 3 Escalation

Escalate when:
- Decision would violate a principle
- Decision affects CONSTITUTION.md or BYLAWS.md
- Financial commitment > $100 (when budget exists)
- External partnership decisions
- Z confidence < 60% OR principle conflict detected

---

## ESCALATION PROCESS

### Level 1 Resolution (Z handles)

```
Conflict detected
    │
    ├─ Classify as Level 1
    ├─ Z checks current_state.md for task assignments
    ├─ Z assigns or resolves
    ├─ Log to worklog.md
    └─ Done (no human needed)
```

**Time target:** < 5 minutes

---

### Level 2 Resolution (Z + precedent)

```
Conflict detected
    │
    ├─ Classify as Level 2
    ├─ Z checks decision_log.md for precedent
    │
    ├─ Precedent exists?
    │   ├─ YES → Apply precedent → Log to decision_log.md → Done
    │   │
    │   └─ NO → Z proposes resolution
    │            │
    │            ├─ Create proposed ADR
    │            ├─ Harley approves?
    │            │   ├─ YES → Log as ADR → Done
    │            │   └─ NO → Revise or escalate to Level 3
    │            │
    │            └─ If no response in 48 hours → Z implements with fallback
    │
    └─ Log to decision_log.md
```

**Time target:** < 24 hours (or 48 hours if Harley input needed)

---

### Level 3 Resolution (Harley decides)

```
Conflict detected
    │
    ├─ Classify as Level 3
    ├─ Z creates conflict_ticket.md
    │   ├── Context: What's the situation?
    │   ├── Options: What are the choices?
    │   ├── Implications: What happens with each?
    │   └── Recommendation: What does Z suggest?
    │
    ├─ Present to Harley
    │
    ├─ Harley decides
    │
    ├─ Log as ADR in decision_log.md
    │
    └─ All AIs notified via current_state.md update
```

**Time target:** Depends on Harley availability

---

## CRISIS ESCALATION (BYPASS NORMAL)

When Crisis AI detects URGENT:

```
URGENT detected
    │
    ├─ Crisis AI loads ULTRA context only
    ├─ Crisis AI takes containment action
    ├─ Crisis AI creates alert
    │
    ├─ Life/safety issue? → Direct to Harley immediately
    │                      → CC Z for awareness
    │
    └─ Project issue? → Alert Z
                      → Z escalates to Harley if needed
```

**Time target:** < 5 minutes to alert

---

## REVIEW BUDGET ENFORCEMENT

Z monitors Harley's decision load:

| Metric | Limit | Enforcement |
|--------|-------|-------------|
| AI outputs for review per day | 5 | Z batches smaller items |
| Level 3 decisions per week | 3 | Z defers non-urgent |
| Escalation response time | 48 hours | Auto-implement fallback |

---

## ESCALATION LOG FORMAT

Every escalation creates a record:

```markdown
## ESCALATION-[ID]

**Date:** YYYY-MM-DD HH:MM
**From:** [AI or person]
**Level:** 1 / 2 / 3
**Type:** [Task/Process/Principle]

### Issue
[One paragraph description]

### Options
1. [Option A] — [Pros/Cons]
2. [Option B] — [Pros/Cons]

### Resolution
[What was decided]

### Reasoning
[Why this option was chosen]

### Precedent Created?
[Yes/No — if Yes, note ADR number]
```

---

## FALLBACK DEFAULTS

If Harley unavailable for Level 3:

| Scenario | Fallback |
|----------|----------|
| New project proposal | Defer until Harley returns |
| Partnership decision | Z keeps conversation alive, no commitments |
| Financial > $100 | Do not spend without Harley |
| Principle conflict | Pause action, document conflict |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial escalation protocol |

---

*Clear escalation protects Harley's time while ensuring nothing falls through.*
