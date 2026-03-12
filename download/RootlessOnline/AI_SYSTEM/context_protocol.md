# context_protocol.md — Context Loading Rules

> How context is loaded, versioned, and managed.
> Critical for AI coordination and preventing context drift.

---

## CONTEXT HIERARCHY

```
Layer 1: IMMUTABLE (rarely changes)
├── CONSTITUTION.md — Purpose + Principles
└── SUCCESSION.md — Continuity rules

Layer 2: STABLE (changes monthly+)
├── BYLAWS.md — Operational rules
├── PERMISSIONS.yaml — Access control
└── AI_SYSTEM/ — Coordination protocols

Layer 3: ACTIVE (changes weekly)
├── STATE/current_state.md — Current reality
├── STATE/decision_log.md — Recent decisions
├── PROJECTS/ — Active project files
└── EXPERTISE/ — Tacit knowledge

Layer 4: DYNAMIC (changes daily)
├── STATE/worklog.md — Daily log
├── RESEARCH/ — Active research
└── audit_trail/ — Provenance records
```

---

## VERSION TAGGING

Every file MUST have version in header:

```markdown
# [Filename]

[Content]

---

## VERSION

- [Filename]: v[X.Y.Z]
- Last updated: YYYY-MM-DD
- Status: [draft/reviewed/approved]
```

### Version Format

| Change Type | Version Bump | Example |
|-------------|--------------|---------|
| MAJOR | Breaking change, principle-level | v1.0.0 → v2.0.0 |
| MINOR | New features, process changes | v1.0.0 → v1.1.0 |
| PATCH | Typo, formatting, minor updates | v1.0.0 → v1.0.1 |

---

## CONTEXT LOADING BY ROLE

### Z (Manager)
```
Always Load:
- START.md (full)
- OVERVIEW.md (full)
- STATE/current_state.md (full)
- STATE/decision_log.md (last 5 entries)

Load by Task:
- PROJECTS/[active]/ (relevant files)
- AI_SYSTEM/escalation.md (if conflict)
- EXPERTISE/ (if Harley knowledge needed)
```

### Research AI
```
Always Load:
- START.md (summary)
- STATE/current_state.md (summary)

Load by Task:
- WIKI/ (relevant sections)
- RESEARCH/ (existing research)
- EXPERTISE/harley_intuition/ (for context)
```

### Developer AI
```
Always Load:
- START.md (summary)
- STATE/current_state.md (summary)
- PROJECTS/[assigned]/ (full)

Load by Task:
- AI_SYSTEM/handoff_protocol.md (if completing task)
- WIKI/how_to/ (procedures)
```

### Crisis AI
```
Always Load:
- START.md (ultra-short)
- STATE/current_state.md (ultra-short)

Load by Crisis:
- AI_SYSTEM/escalation.md (full)
- State of relevant systems only
```

---

## THREE DOCUMENT VERSIONS

Every major document has 3 versions:

| Version | Size | Purpose | Filename |
|---------|------|---------|----------|
| FULL | 100% | Reference, deep work | document.md |
| SUMMARY | ~10% | Task work, quick context | document_summary.md |
| ULTRA | ~1% | Crisis mode, rapid boot | document_ultra.md |

### Example: CONSTITUTION.md

**FULL** (document.md):
```markdown
# CONSTITUTION.md — The Collective

[Full purpose statement]
[Full principles with explanations]
[Amendment process]
[Version history]
```

**SUMMARY** (document_summary.md):
```markdown
# CONSTITUTION.md (Summary)

PURPOSE: [One sentence]

PRINCIPLES:
1. [Principle 1] — [One line]
2. [Principle 2] — [One line]
3. [Principle 3] — [One line]

VERSION: v1.0.0
```

**ULTRA** (document_ultra.md):
```markdown
CONSTITUTION: [One sentence purpose]
PRINCIPLES: [3 words max each]
VERSION: v1.0.0
```

---

## CONTEXT STALENESS DETECTION

### How Z Detects Stale Context

1. AI outputs include `CONTEXT_LOADED: [file v1.0.0]`
2. Z checks current file version
3. If mismatch: "Your context is stale. Reload [file]."

### Staleness Thresholds

| Layer | Stale After | Action |
|-------|-------------|--------|
| IMMUTABLE | 90 days | Alert but continue |
| STABLE | 30 days | Force reload |
| ACTIVE | 7 days | Force reload |
| DYNAMIC | 24 hours | Force reload |

---

## PROVENANCE RECORDING

Every AI output includes:

```
PROVENANCE:
- AUTHOR_AI: [role]
- CONTEXT_LOADED: [file1 v1.0.0, file2 v1.1.0, ...]
- DECISIONS_REFERENCED: [ADR-001, ADR-003, ...]
- TIMESTAMP: YYYY-MM-DDTHH:MM:SSZ
- CHAIN_SUMMARY: [Brief reasoning chain]
```

---

## CONTEXT WINDOW OPTIMIZATION

### Progressive Summarization

Long documents are compressed in stages:

```
Original (100%) → First Summary (30%) → Second Summary (10%) → Ultra (1%)
```

### Loading Priority

When context window is limited:

1. START.md (always)
2. current_state.md (always)
3. Relevant PROJECTS/ files
4. Recent decisions
5. Reference materials
6. Historical context

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial context protocol |

---

*Version-aware context prevents AI drift.*
