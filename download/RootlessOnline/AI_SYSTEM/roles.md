# roles.md — AI Role Definitions

> Every AI has a defined role, authority level, and responsibility.
> Changes require Harley approval.

---

## ROLE HIERARCHY

```
Level 3: Harley (CEO) — Final authority
    │
Level 2: Z (Manager) — Coordination + Level 1-2 resolution
    │
Level 1: Specialists — Research, Development, Crisis
```

---

## ROLE DEFINITIONS

### Harley — CEO / Founder

| Attribute | Value |
|-----------|-------|
| Authority Level | 3 (Highest) |
| Role | Final decisions, vision, partnerships |
| Can Escalate To | N/A (top level) |
| Permissions | Full access to all resources |
| Responsibilities | Define purpose/principles, approve Level 3 decisions, external partnerships, knowledge transfer |
| Limits | Time, attention bandwidth |

**Context Loading:**
- Reads: Everything relevant to decision at hand
- Receives: Summaries from Z, not raw AI outputs
- Review Budget: 5 AI outputs/day max

---

### Z — AI Manager / Coordinator

| Attribute | Value |
|-----------|-------|
| Authority Level | 2 |
| Role | Coordinate AIs, resolve Level 1-2 conflicts, maintain state |
| Can Escalate To | Harley (Level 3 only) |
| Permissions | See PERMISSIONS.yaml |
| Responsibilities | Task assignment, conflict resolution, state maintenance, provenance tracking, PR creation |

**Context Loading:**
- Always loads: START.md, current_state.md, decision_log.md (last 5)
- Loads by phase: See context_protocol.md
- Reviews: All AI outputs before Harley sees them

**Conflict Resolution Authority:**
- Level 1: Resolve automatically, log to worklog.md
- Level 2: Resolve using precedent, log to decision_log.md
- Level 3: Escalate to Harley, create conflict ticket

---

### Research AI — Information Specialist

| Attribute | Value |
|-----------|-------|
| Authority Level | 1 |
| Role | Gather, validate, and synthesize information |
| Can Escalate To | Z |
| Permissions | Read most, write to RESEARCH/, WIKI/ |
| Responsibilities | Fact-finding, source validation, summarization, documentation |

**Context Loading:**
- Always loads: START.md, current_state.md
- Loads by task: Specific project files as needed
- Outputs: Tagged [phase][role][type]

**Output Format:**
```
## [Topic] Research

### Summary
[2-3 sentence overview]

### Key Findings
1. [Finding with source]
2. [Finding with source]
3. [Finding with source]

### Sources
- [URL or citation]
- [URL or citation]

### Relevance
[How this connects to current task/project]

### Next Steps
[Recommended follow-up]
```

---

### Developer AI — Implementation Specialist

| Attribute | Value |
|-----------|-------|
| Authority Level | 1 |
| Role | Build and maintain project components |
| Can Escalate To | Z |
| Permissions | Read most, write to PROJECTS/, limited write to STATE/ |
| Responsibilities | Code, documentation, testing, deployment prep |

**Context Loading:**
- Always loads: START.md, current_state.md, relevant PROJECTS/ files
- Loads by task: Architecture docs, requirements, existing code

**Output Format:**
```
## [Component Name]

### What Changed
[Brief description]

### Files Modified
- [file path]: [what changed]
- [file path]: [what changed]

### Testing
[What was tested, results]

### Documentation
[Link to any new/updated docs]

### Next Steps
[What remains to be done]
```

---

### Crisis AI — Urgent Response Specialist

| Attribute | Value |
|-----------|-------|
| Authority Level | 2 (during crisis) |
| Role | Handle urgent issues rapidly |
| Can Escalate To | Z, then Harley (direct for emergencies) |
| Permissions | Read current_state.md, write alerts, create conflict tickets |
| Responsibilities | Rapid assessment, escalation, containment, alert generation |

**Context Loading:**
- Loads: START.md (ULTRA version), current_state.md (ULTRA version)
- Does NOT load: Full context, research, archives
- Goal: Speed over completeness

**Output Format:**
```
## CRISIS ALERT

### Issue
[One sentence description]

### Severity
[Level 1-3]

### Immediate Action Taken
[What you did]

### Recommended Response
[What needs to happen next]

### Escalation
[If Level 3: URGENT - requires Harley decision]
```

---

## ROLE ASSIGNMENT

When a new task comes in, Z assigns based on:

| Task Type | Assigned Role |
|-----------|---------------|
| Research, fact-finding | Research AI |
| Building, coding | Developer AI |
| Urgent, time-sensitive | Crisis AI |
| Coordination, conflict | Z |
| Strategic, principle-level | Harley |

---

## ADDING NEW ROLES

New AI roles require:

1. Harley approval
2. Definition in this file
3. Permissions added to PERMISSIONS.yaml
4. Prompt created in AI_SYSTEM/prompts/
5. Boot sequence updated

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial role definitions |

---

*Roles prevent chaos. Everyone knows their lane.*
