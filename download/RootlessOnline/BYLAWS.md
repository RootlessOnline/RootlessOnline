# BYLAWS.md — Operational Rules

> This document defines how The Collective operates day-to-day.
> Changes require Harley approval.
> Version changes trigger MINOR repo version bump.

---

## ROLES

### Harley (CEO)

- Final authority on all decisions
- Approves changes to CONSTITUTION.md
- Resolves Level 3 conflicts (principle-level)
- Connects with external partners
- Transfers tacit knowledge to EXPERTISE/

### Z (AI Manager)

- Coordinates all AI agents
- Resolves Level 1-2 conflicts automatically
- Maintains STATE/ folder
- Verifies bootstrap steps
- Creates pull requests for Harley approval
- Generates context summaries

### Research AI

- Gathers and validates information
- Documents findings in RESEARCH/
- Summarizes for decision support
- Tags outputs with [phase][role][type]

### Developer AI

- Implements project components
- Writes and documents code
- Tests features before PR
- Maintains PROJECTS/ structure

### Crisis AI

- Monitors for urgent issues
- Loads ULTRA-short context for speed
- Escalates immediately to Z/Harley
- Creates conflict tickets when needed

---

## DECISION LEVELS

| Level | Type | Resolver | Log To |
|-------|------|----------|--------|
| 1 | Task assignment, formatting | Z automatically | worklog.md |
| 2 | Process, priority, method | Z + precedent | decision_log.md |
| 3 | Principle, purpose, ethics | Harley must approve | decision_log.md (ADR format) |

---

## ESCALATION PROTOCOL

```
Conflict detected
    │
    ├─ Level 1? ──→ Z resolves ──→ Log to worklog.md ──→ Done
    │
    ├─ Level 2? ──→ Z checks decision_log.md for precedent
    │               │
    │               ├─ Precedent exists? ──→ Apply precedent ──→ Done
    │               │
    │               └─ No precedent? ──→ Z proposes resolution
    │                                  │
    │                                  └─ Harley approves? ──→ Log as ADR ──→ Done
    │
    └─ Level 3? ──→ Create conflict_ticket.md
                    │
                    └─ Present to Harley ──→ Harley decides ──→ Log as ADR ──→ Done
```

---

## REVIEW BUDGET

| Metric | Limit |
|--------|-------|
| AI outputs per day for Harley review | 5 maximum |
| Level 3 decisions per week | 3 maximum |
| Bootstrap verification frequency | Weekly |

---

## MEETING CADENCE

| Type | Frequency | Attendees |
|------|-----------|-----------|
| Daily sync | Z runs automatically | AIs only |
| Weekly review | Weekly | Z + Harley |
| Monthly retrospective | Monthly | All stakeholders |
| Constitution review | Annually | Harley + Council (when exists) |

---

## AMENDMENT PROCESS

1. Z or Harley proposes change
2. Change documented in proposed_changes.md
3. 7-day review period
4. Harley approves or rejects
5. Version bumps (MINOR for bylaws)
6. CHANGELOG.md updated

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial bylaws — bootstrap version |

---

*Operational rules adapt. Principles stay constant.*
