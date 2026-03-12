# conflict_playbook.md — Conflict Resolution Procedures

> Specific procedures for different conflict types.
> Z references this to resolve Level 1-2 conflicts automatically.
> Level 3 conflicts escalate to Harley.

---

## CONFLICT TYPE INDEX

| Type | Level | Auto-Resolve? | Resolution Path |
|------|-------|---------------|-----------------|
| Task Assignment | 1 | YES | Section 1 |
| Task Priority | 1-2 | YES | Section 2 |
| Method Disagreement | 2 | YES (with precedent) | Section 3 |
| Resource Conflict | 2 | YES (with precedent) | Section 4 |
| Principle Violation | 3 | NO | Section 5 |
| Version Mismatch | 1 | YES | Section 6 |
| Role Overlap | 2 | YES | Section 7 |

---

## SECTION 1: TASK ASSIGNMENT CONFLICT

**Trigger:** Two AIs assigned same task, or task unassigned

**Resolution:**

```
1. Check current_state.md for active tasks
2. Check AI availability (last activity in worklog.md)
3. Assign to:
   a. AI with least active tasks
   b. AI with relevant expertise (check EXPERTISE/)
   c. AI with relevant recent work (check worklog.md)
4. Update current_state.md
5. Log to worklog.md
```

**Precedent:** First available AI with relevant expertise takes task.

---

## SECTION 2: TASK PRIORITY CONFLICT

**Trigger:** Multiple tasks competing for same resource or attention

**Resolution:**

```
1. Check decision_log.md for priority precedent
2. If precedent exists → apply
3. If no precedent → evaluate by:
   a. Phase alignment (Phase 1 tasks > future tasks)
   b. Time sensitivity (deadlines, external dependencies)
   c. Harley-stated priorities (check current_state.md)
   d. Dependencies (unblocking others)
4. If still unclear → escalate to Level 2
```

**Precedent Matrix:**

| Higher Priority | Lower Priority |
|-----------------|----------------|
| Active Phase 1 task | Phase 2+ planning |
| External deadline | Internal deadline |
| Harley-stated priority | AI-suggested priority |
| Unblocking other work | Independent work |

---

## SECTION 3: METHOD DISAGREEMENT

**Trigger:** Two AIs propose different approaches to same task

**Resolution:**

```
1. Check decision_log.md for similar past decision
2. If precedent → apply
3. If no precedent → evaluate:
   a. Alignment with principles (check CONSTITUTION.md)
   b. Resource requirements (lower resource = preferred)
   c. Risk level (lower risk = preferred for now)
   d. Reversibility (reversible = preferred)
4. Document reasoning
5. Log as decision if significant
```

**Evaluation Checklist:**

- [ ] Aligns with principles?
- [ ] Uses fewer resources?
- [ ] Has lower risk?
- [ ] Is more reversible?
- [ ] Has precedent?

Most checks = preferred method.

---

## SECTION 4: RESOURCE CONFLICT

**Trigger:** Multiple tasks need same file, context, or attention

**Resolution:**

```
1. Identify resource type:
   - File access → Create branch/lock
   - Context attention → Batch requests
   - Harley attention → Defer non-urgent
   
2. Apply resolution:
   - Files: Git branching (see handoff_protocol.md)
   - Context: Z batches requests (max 5/day for Harley)
   - Attention: Priority queue (see Section 2)
```

---

## SECTION 5: PRINCIPLE VIOLATION

**Trigger:** Proposed action would violate a core principle

**Resolution:** ALWAYS ESCALATE TO HARLEY

```
1. STOP immediately
2. Identify which principle is violated
3. Create conflict_ticket.md:
   - Context: What's being proposed?
   - Principle: Which principle is at stake?
   - Options: What alternatives exist?
   - Recommendation: Z's analysis
4. Present to Harley
5. Log Harley's decision as ADR
6. All AIs notified
```

**Never auto-resolve principle conflicts.**

---

## SECTION 6: VERSION MISMATCH

**Trigger:** AI references outdated version of a file

**Resolution:**

```
1. Z detects version mismatch in PROVENANCE
2. Alert AI: "Context stale. Reload [file] v[current]"
3. AI reloads and re-evaluates
4. If AI output already produced:
   a. Tag as "STALE_CONTEXT" in audit_trail/
   b. Mark for review
   c. Re-run with correct context
```

**Detection:** Z compares PROVENANCE context versions to current file versions.

---

## SECTION 7: ROLE OVERLAP

**Trigger:** Unclear which AI should handle a task

**Resolution:**

```
1. Check AI_SYSTEM/roles.md for role definitions
2. Match task type to role:
   - Research → Research AI
   - Building → Developer AI
   - Urgent → Crisis AI
   - Coordination → Z
   - Strategic → Harley
3. If overlap persists:
   a. Assign to role with least active tasks
   b. Or assign to role with most expertise
```

---

## CONFLICT TICKET TEMPLATE

For Level 3 conflicts:

```markdown
# CONFLICT TICKET — [ID]

**Created:** YYYY-MM-DD HH:MM
**Severity:** Level 3
**Status:** PENDING / RESOLVED

## The Conflict

[What's the disagreement?]

## Principles at Stake

[Which principles from CONSTITUTION.md are relevant?]

## Options

### Option A: [Name]
- Pros:
- Cons:
- Implications:

### Option B: [Name]
- Pros:
- Cons:
- Implications:

## Z Recommendation

[What Z recommends and why]

## Harley Decision

[To be filled by Harley]

**Decision:** [Choice]
**Reasoning:** [Why]
**Date:** [When]

## Follow-up

- [ ] ADR created in decision_log.md
- [ ] All AIs notified
- [ ] current_state.md updated
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial conflict playbook |

---

*Conflicts are opportunities to clarify. Document every resolution.*
