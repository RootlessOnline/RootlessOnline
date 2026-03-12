# handoff_protocol.md — AI Handoff Standards

> How work transfers between AIs.
> Standardized format prevents context loss during handoffs.

---

## HANDOFF TRIGGERS

Handoffs occur when:
- Task scope changes (Research → Development)
- AI capacity reached
- Phase transition
- Role change needed
- Shift rotation (future)

---

## HANDOFF MESSAGE FORMAT

Every handoff uses this exact structure:

```json
{
  "HANDOFF_ID": "HO-[YYYYMMDD]-[SEQ]",
  "TIMESTAMP": "YYYY-MM-DDTHH:MM:SSZ",
  "SENDER": {
    "role": "[Role name]",
    "session_id": "[Session identifier]"
  },
  "RECEIVER": {
    "role": "[Target role]",
    "session_id": "[To be filled by receiver]"
  },
  "TASK": {
    "id": "[Task ID from current_state.md]",
    "description": "[What was being done]",
    "status": "[IN_PROGRESS / BLOCKED / COMPLETE / HANDED_OFF]",
    "phase": "[Current phase number]"
  },
  "CONTEXT_LOADED": [
    {"file": "[path]", "version": "[vX.Y.Z]"},
    {"file": "[path]", "version": "[vX.Y.Z]"}
  ],
  "DECISIONS_REFERENCED": ["ADR-XXX", "ADR-XXX"],
  "WORK_COMPLETED": [
    "[Action 1]",
    "[Action 2]"
  ],
  "WORK_REMAINING": [
    "[Next action 1]",
    "[Next action 2]"
  ],
  "BLOCKERS": [
    {"description": "[What's blocking]", "severity": "[LOW/MEDIUM/HIGH]"}
  ],
  "NOTES": "[Any additional context]",
  "CONFIDENCE": "[percentage] — How confident sender is in handoff completeness"
}
```

---

## HANDOFF SEQUENCE

### Step 1: Prepare Handoff

Sending AI:
1. Complete current work segment
2. Document what was done
3. Identify remaining work
4. Note any blockers
5. Create handoff message

### Step 2: Create Handoff File

Save to: `STATE/handoffs/HO-[YYYYMMDD]-[SEQ].json`

### Step 3: Notify Receiver

If Z → Specialist: Z creates task in current_state.md
If Specialist → Z: Specialist updates current_state.md status
If Specialist → Specialist: Route through Z

### Step 4: Receiver Acknowledges

Receiver:
1. Reads handoff file
2. Loads listed context
3. Confirms receipt: `HANDOFF ACKNOWLEDGED: HO-[ID]`
4. Begins work

### Step 5: Log

Both AIs log handoff in worklog.md

---

## HANDOFF TYPES

### Sequential Handoff

```
Research AI → Developer AI
[Research complete, implementation needed]

Format: Full context required
```

### Parallel Handoff

```
Research AI #1 ─┐
                ├→ Z → Synthesis
Research AI #2 ─┘
[Multiple AIs working same topic]

Format: Partial context, tagged by focus
```

### Crisis Handoff

```
Any AI → Crisis AI
[Urgent issue detected]

Format: ULTRA context only, rapid transfer
```

### Phase Transition Handoff

```
Phase 1 AIs → Phase 2 AIs
[Project phase complete]

Format: Full context + phase summary
```

---

## HANDOFF QUALITY CHECKLIST

Before sending handoff, verify:

- [ ] All work completed is documented
- [ ] All remaining work is listed
- [ ] All blockers are identified
- [ ] Context versions are current
- [ ] Relevant ADRs are referenced
- [ ] Confidence score is accurate

---

## HANDOFF RECEIPT PROTOCOL

When receiving a handoff:

```
1. Read handoff message
2. Load all CONTEXT_LOADED files
3. Verify versions match current
4. Read DECISIONS_REFERENCED
5. Check for precedent in decision_log.md
6. Confirm: "HANDOFF ACKNOWLEDGED: HO-[ID]"
7. Begin work
```

---

## FAILED HANDOFF RECOVERY

If handoff fails (context mismatch, missing info):

```
1. Receiver creates issue in MONITORING/handoff_issues.md
2. Receiver requests clarification from sender
3. If sender unavailable, Z mediates
4. If critical, escalate to Harley
```

---

## EXAMPLE HANDOFF

```json
{
  "HANDOFF_ID": "HO-20250115-001",
  "TIMESTAMP": "2025-01-15T14:30:00Z",
  "SENDER": {
    "role": "Research AI",
    "session_id": "RES-20250115-AM"
  },
  "RECEIVER": {
    "role": "Developer AI",
    "session_id": "TBD"
  },
  "TASK": {
    "id": "T004",
    "description": "Document garden business plan",
    "status": "HANDED_OFF",
    "phase": "1"
  },
  "CONTEXT_LOADED": [
    {"file": "CONSTITUTION.md", "version": "v0.1.0"},
    {"file": "STATE/current_state.md", "version": "v0.1.0"},
    {"file": "RESEARCH/permaculture_networks/", "version": "v0.1.0"}
  ],
  "DECISIONS_REFERENCED": ["ADR-001"],
  "WORK_COMPLETED": [
    "Researched permaculture network models",
    "Identified 3 successful patterns",
    "Documented findings in RESEARCH/permaculture_networks/"
  ],
  "WORK_REMAINING": [
    "Create garden_business plan document",
    "Define Phase 1 milestones",
    "Estimate resource requirements"
  ],
  "BLOCKERS": [],
  "NOTES": "Focus on practical, low-cost implementation. Eric Haas opportunity is time-sensitive.",
  "CONFIDENCE": "85%"
}
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial handoff protocol |

---

*Clean handoffs prevent context loss. Standard format ensures nothing is missed.*
