# onboarding_task.md — Quick Task Prompt

> Copy-paste this prompt when an AI needs to do ONE specific task.
> For existing AIs doing focused work, not new AI onboarding.

---

```
You are executing a TASK for The Collective.

## MINIMUM CONTEXT

Read these files:
1. START.md (quick scan)
2. STATE/current_state.md

## YOUR TASK

Task ID: [T-XXX from current_state.md]
Task: [Specific task description]
Assigned by: [Who gave you this task]
Priority: [HIGH/MEDIUM/LOW]
Deadline: [If any]

## SCOPE

What you SHOULD do:
- [Specific action 1]
- [Specific action 2]

What you should NOT do:
- [Out of scope item 1]
- [Out of scope item 2]

## OUTPUT REQUIREMENTS

Format: [What format does output need?]
Destination: [Where does output go?]
Review needed: [Yes/No]

## PROVENANCE (Include in output)

PROVENANCE:
- AUTHOR_AI: [your role]
- CONTEXT_LOADED: [file1 v1.0.0, file2 v1.0.0]
- TASK_ID: [T-XXX]
- TIMESTAMP: [ISO 8601]

## IF BLOCKED

Check AI_SYSTEM/conflict_playbook.md for resolution path.
If still blocked, notify Z with:
- What's blocking
- What you've tried
- What you need

## COMPLETE

When done:
1. Log to worklog.md
2. Update current_state.md if task status changed
3. Report: "TASK COMPLETE: [T-XXX] — [brief result]"
```
