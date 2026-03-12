# escalation.md — When and How to Escalate

> Clear protocols for escalating decisions and issues.

---

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0 |
| Status | Active |
| Last Updated | 2025-01-XX |

---

## Escalation Levels

### Level 1: Routine

| Property | Value |
|----------|-------|
| **Who Handles** | Z |
| **Response Time** | Immediate |
| **Harley Involvement** | None required |
| **Documentation** | Standard provenance |

**Examples:**
- Formatting a document
- Creating a wiki page
- Logging a completed task
- Applying existing precedent

**Protocol:**
1. Z handles automatically
2. Document in output
3. Note in current_state.md if significant

---

### Level 2: Precedent Needed

| Property | Value |
|----------|-------|
| **Who Handles** | Z |
| **Response Time** | < 1 hour |
| **Harley Involvement** | None required |
| **Documentation** | Decision log entry |

**Examples:**
- Similar to past decision but not identical
- New situation with clear precedent pattern
- Operational question not in BYLAWS

**Protocol:**
1. Check decision_log.md for precedent
2. Apply precedent if found
3. Document as new decision with precedent reference
4. If no precedent, treat as Level 3

---

### Level 3: Harley Required

| Property | Value |
|----------|-------|
| **Who Handles** | Harley |
| **Response Time** | < 24 hours |
| **Harley Involvement** | Required |
| **Documentation** | Decision log entry + flag |

**Examples:**
- Principle conflicts
- Major strategic decisions
- Budget/resource commitments
- New partnerships
- Governance changes

**Protocol:**
1. Document the question clearly
2. Provide recommendation with reasoning
3. Flag in current_state.md
4. Wait for Harley decision
5. Log decision when received

---

### Level 4: Emergency

| Property | Value |
|----------|-------|
| **Who Handles** | Z (immediate) + Harley (ASAP) |
| **Response Time** | Immediate |
| **Harley Involvement** | Required after action |
| **Documentation** | Full incident report |

**Examples:**
- Security breach
- Safety concern
- Threat to The Collective's existence
- Legal issues

**Protocol:**
1. Z takes minimum necessary action
2. Document everything immediately
3. Notify Harley ASAP
4. Full review within 24 hours

---

## Escalation Triggers

### Automatic Escalation to Harley

| Trigger | Level |
|---------|-------|
| Any modification to CONSTITUTION.md | Level 3 |
| New project/pillar start | Level 3 |
| Partnership or external agreement | Level 3 |
| Budget or financial commitment | Level 3 |
| Safety or security issue | Level 4 |
| Conflict between AIs on principles | Level 3 |

### Automatic Escalation from Z to Harley

| Trigger | Action |
|---------|--------|
| Principle conflict detected | Stop, flag, wait |
| Novel situation with no precedent | Document, recommend, wait |
| Multiple AI disagreement | Document, synthesize, flag |
| Uncertainty about Harley's intent | Ask directly, wait |

---

## Escalation Format

### How to Flag for Harley

In STATE/current_state.md:

```markdown
## Flags

### [URGENT/HIGH/NORMAL] [Date]: [Title]

**Type:** Decision needed | Information | Emergency
**Context:** [Brief description]
**Recommendation:** [Z's recommendation, if any]
**Options:** [If multiple options, list them]
**Waiting for:** Harley decision
**Blocking:** [What is blocked by this]
```

### Example

```markdown
## Flags

### HIGH 2025-01-15: Garden Location Decision

**Type:** Decision needed
**Context:** Need to identify first garden location before ordering supplies
**Recommendation:** Start with Harley's current residence or nearby community space
**Options:**
  1. Harley's residence (lowest cost)
  2. Community garden plot (more visibility)
  3. Partner with local organization (shared resources)
**Waiting for:** Harley decision
**Blocking:** Supply ordering, design work
```

---

## De-Escalation

### When to Lower Escalation Level

| From | To | Condition |
|------|-----|-----------|
| Level 3 | Level 2 | Precedent found |
| Level 3 | Level 1 | Harley provides standing authority |
| Level 4 | Level 3 | Immediate danger passed |

### Process

1. Document why de-escalation is appropriate
2. Update flag in current_state.md
3. Proceed at lower level

---

## Communication Templates

### Asking Harley (via Z)

```markdown
**Question for Harley:**

[Clear, literal question]

**Context:**
[Why this is being asked]

**Options:**
1. [Option A] - [Pros/Cons]
2. [Option B] - [Pros/Cons]

**Recommendation:** [Z's recommendation with reasoning]

**Impact:** [What happens if we wait / if we decide each way]
```

### Emergency Notification

```markdown
**EMERGENCY - Immediate Attention Required**

**Situation:** [What happened]
**Action Taken:** [What Z did]
**Status:** [Current state]
**Next Steps Needed:** [What Harley needs to do]
**Documentation:** [Link to incident record]
```

---

## Quick Reference

```
ESCALATION LEVELS:
Level 1 (Routine)     → Z handles immediately
Level 2 (Precedent)   → Z checks log, decides
Level 3 (Harley)      → Z flags, waits for Harley
Level 4 (Emergency)   → Z acts, documents, notifies

ALWAYS ESCALATE TO HARLEY:
- Constitution changes
- New projects
- Partnerships
- Money
- Safety
- Principle conflicts

ALWAYS DOCUMENT:
- What you did
- Why you did it
- What precedent/decision applies
```

---

## Provenance

```
---
Generated by: Z (Manager AI)
Context versions: START.md v1.0, CONSTITUTION.md v1.0, BYLAWS.md v1.0
Decisions referenced: D004
Timestamp: 2025-01-XX
---
```
