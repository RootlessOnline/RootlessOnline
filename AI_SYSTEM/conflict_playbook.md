# conflict_playbook.md — Resolving AI and System Conflicts

> Protocols for handling disagreements, conflicts, and contradictions.

---

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0 |
| Status | Active |
| Last Updated | 2025-01-XX |

---

## Conflict Types

### Type 1: Task Conflict

**Definition:** Two AIs assigned overlapping or contradictory tasks.

**Example:** ChatGPT starts designing the Collective App while Z is still focused on Garden Business.

**Resolution:**
1. Z identifies overlap
2. Z checks decision_log.md for priority
3. Z reassigns or sequences tasks
4. Documents resolution

**Authority:** Z handles

---

### Type 2: Priority Conflict

**Definition:** Multiple tasks with unclear priority.

**Example:** Garden planning needs research AND interview prep is due tomorrow.

**Resolution:**
1. Z checks decision_log.md for priority precedent
2. Z checks current_state.md for deadlines
3. Z applies prioritization framework
4. Documents decision

**Prioritization Framework:**
1. Harley request (highest)
2. Deadline-driven
3. Blocking other work
4. Quick wins
5. Long-term projects

**Authority:** Z handles, escalate to Harley if unresolvable

---

### Type 3: Principle Conflict

**Definition:** Action conflicts with a Principle in CONSTITUTION.md.

**Example:** AI suggests a paid tool that would be faster, but "$0 budget" is a principle.

**Resolution:**
1. STOP immediately
2. Identify which principle is affected
3. Document the conflict
4. Escalate to Harley
5. Wait for guidance

**Authority:** Harley required

---

### Type 4: Version Conflict

**Definition:** AI working with outdated context.

**Example:** AI makes decision based on old version of BYLAWS.md.

**Resolution:**
1. Z detects version mismatch
2. Z alerts AI to reload context
3. AI re-reads updated documents
4. AI re-evaluates decision with new context
5. Document incident

**Authority:** Z handles

---

### Type 5: Output Conflict

**Definition:** Two AIs produce contradictory outputs.

**Example:** ChatGPT recommends architecture X, another AI recommends architecture Y.

**Resolution:**
1. Z collects both outputs with reasoning
2. Z analyzes contradiction
3. Z synthesizes or chooses best option
4. If unresolvable, escalate to Harley
5. Document resolution

**Authority:** Z handles, escalate to Harley if unresolvable

---

### Type 6: Human-AI Conflict

**Definition:** Human disagrees with AI recommendation or output.

**Example:** Harley rejects Z's recommended approach.

**Resolution:**
1. Human decision always wins
2. AI documents human decision
3. AI adapts to human preference
4. No argument, just clarification if needed

**Authority:** Human always

---

## Conflict Resolution Process

### Step 1: Identify Type

Use the definitions above to categorize the conflict.

### Step 2: Determine Authority

| Type | Primary Authority | Escalation |
|------|-------------------|------------|
| Task | Z | Harley if persistent |
| Priority | Z | Harley if unresolvable |
| Principle | Harley | - |
| Version | Z | - |
| Output | Z | Harley if unresolvable |
| Human-AI | Human | - |

### Step 3: Apply Resolution Protocol

Follow the specific protocol for the conflict type.

### Step 4: Document

All conflicts must be documented:

```markdown
## Conflict [C###]: [Title]

**Date:** YYYY-MM-DD
**Type:** Task | Priority | Principle | Version | Output | Human-AI
**Parties:** [Who is involved]
**Description:** [What happened]
**Resolution:** [How it was resolved]
**Precedent:** [What precedent this sets, if any]
**References:** [Links to relevant docs]
```

### Step 5: Learn

- Does this suggest a BYLAWS amendment?
- Does this suggest a new protocol?
- Does this suggest better documentation needed?

---

## Conflict Log

### Active Conflicts

*None currently*

### Resolved Conflicts

*None yet*

---

## Prevention Strategies

### Clear Task Assignment

- Every task has ONE owner
- Every task has clear scope
- Every task has documented dependencies

### Regular Synchronization

- Z checks in with active AIs regularly
- current_state.md updated frequently
- decision_log.md consulted before novel decisions

### Context Verification

- AIs check document versions before work
- Z alerts when documents change
- Reload context on version mismatch

### Explicit Communication

- All outputs tagged with provenance
- All decisions logged
- All conflicts documented

---

## Emergency Conflict Protocol

If conflict is blocking critical work:

1. **Assess urgency:** Is this blocking something time-sensitive?
2. **If urgent:** Z makes best-judgment decision, documents, continues
3. **If not urgent:** Follow normal resolution process
4. **Always:** Flag for Harley review

---

## Quick Reference Card

```
CONFLICT TYPES:
1. Task      → Z reassigns
2. Priority  → Z prioritizes (framework)
3. Principle → STOP, escalate to Harley
4. Version   → Z alerts, AI reloads
5. Output    → Z synthesizes or escalates
6. Human-AI  → Human wins, always

RESOLUTION STEPS:
1. Identify type
2. Determine authority
3. Apply protocol
4. Document
5. Learn

WHEN IN DOUBT:
→ Escalate to Harley
→ Document everything
→ Don't guess
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
