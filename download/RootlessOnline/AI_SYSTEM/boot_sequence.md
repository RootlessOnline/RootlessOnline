# boot_sequence.md — AI Startup Protocol

> Step-by-step instructions for any AI starting a session.
> Follow this sequence EVERY TIME you begin work.
> Do not skip steps.

---

## PRE-BOOT CHECK

Before reading anything, verify:

- [ ] You know your role (Research / Developer / Crisis / Z)
- [ ] You know your task (given by Z or Harley)
- [ ] You know the current phase (Phase 1 = Garden Business)

If any of these are unclear, ASK before proceeding.

---

## BOOT SEQUENCE

### Step 1: Read Foundation (ALL ROLES)

Read in this exact order:

```
1. START.md       → Purpose, principles, boot overview
2. OVERVIEW.md    → Full system map
```

**Time:** ~30 seconds
**Purpose:** Orient yourself to the project

---

### Step 2: Read Current State (ALL ROLES)

```
3. STATE/current_state.md   → What's happening NOW
```

**Time:** ~20 seconds
**Purpose:** Understand active work, blockers, priorities

---

### Step 3: Read Recent History (ALL ROLES)

```
4. STATE/decision_log.md (last 3 entries)  → Recent decisions
5. STATE/worklog.md (last entry)           → Last activity
```

**Time:** ~30 seconds
**Purpose:** Understand recent context, don't repeat work

---

### Step 4: Role-Specific Loading

#### For Research AI:
```
6. WIKI/reference/ → Browse relevant reference materials
7. RESEARCH/       → Check existing research on your topic
8. EXPERTISE/      → Check for Harley's relevant knowledge
```

#### For Developer AI:
```
6. PROJECTS/[your-project]/ → Load project files
7. WIKI/how_to/             → Check procedures
8. AI_SYSTEM/handoff_protocol.md → Understand handoff format
```

#### For Crisis AI:
```
6. STATE/current_state.md (ULTRA version) → Minimal context
7. AI_SYSTEM/escalation.md                → Escalation rules
```

#### For Z:
```
6. AI_SYSTEM/               → All coordination files
7. STATE/decision_log.md    → Full decision history
8. MONITORING/              → System health metrics
```

---

### Step 5: Verify Context

Before starting work, confirm:

- [ ] I understand the current phase
- [ ] I know my assigned task
- [ ] I've checked for related decisions
- [ ] I've checked for existing work on this topic

If ANY are unclear, STOP and ask Z (or Harley if Z unavailable).

---

### Step 6: Signal Ready

Output a brief confirmation:

```
BOOT COMPLETE
Role: [your role]
Task: [your assigned task]
Context loaded: [list files you read]
Ready: YES
```

---

## CONTEXT VERSIONS

Each major document has 3 versions:

| Version | Suffix | Size | When to Use |
|---------|--------|------|-------------|
| Full | (none) | Complete | Normal work, deep understanding needed |
| Summary | _summary | ~10% | Task work, time-limited |
| Ultra-short | _ultra | 1 paragraph | Crisis mode, rapid response |

**Default:** Load FULL versions unless:
- Time-critical → Use ULTRA
- Routine task → Use SUMMARY

---

## ERROR RECOVERY

### If context seems wrong:

1. Check file VERSION in header
2. Compare to version in current_state.md
3. If mismatch, reload from main branch

### If you can't find a file:

1. Check START.md for correct location
2. Check CHANGELOG.md for recent changes
3. Alert Z if file should exist but doesn't

### If you're confused:

1. STOP
2. Read START.md again
3. Ask Z for clarification

---

## BOOT TIME TARGETS

| Role | Target Boot Time |
|------|------------------|
| Research AI | < 2 minutes |
| Developer AI | < 2 minutes |
| Crisis AI | < 30 seconds |
| Z | < 3 minutes |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial boot sequence |

---

*Boot sequence ensures every AI starts from the same foundation.*
