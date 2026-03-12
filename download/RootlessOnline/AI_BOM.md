# AI_BOM.md — AI Bill of Materials

> Tracks who contributed what to each version.
> Like SBOM (Software Bill of Materials) but for AI outputs.

---

## REPO VERSION: v0.1.0 (Bootstrap)

### AI Contributors

| AI Role | Version | Contributions | Dependencies |
|---------|---------|---------------|--------------|
| Z | v0.1.0 | Repo structure, AI_SYSTEM design, STATE setup | CONSTITUTION.md (Harley), Research findings |
| ChatGPT | v0.1.0 | System architecture, prompts, protocols | Z coordination, Harley direction |

### Human Contributors

| Person | Role | Contributions |
|--------|------|---------------|
| Harley | CEO | Vision, direction, purpose/principles (pending) |
| Eric Haas | Potential Partner | Interview opportunity |

### File Lineage

| File | Created By | Based On | Approved By |
|------|------------|----------|-------------|
| START.md | Z | Harley's direction | Harley (pending) |
| OVERVIEW.md | ChatGPT, Z | System research | Harley (pending) |
| CONSTITUTION.md | Z (template) | — | Harley must complete |
| BYLAWS.md | Z | Organizational research | Harley (pending) |
| SUCCESSION.md | Z | Succession planning research | Harley must designate proxies |
| PERMISSIONS.yaml | Z | RBAC research | Harley (pending) |
| AI_SYSTEM/ | Z, ChatGPT | Multi-agent research | Harley (pending) |

### Knowledge Sources

| Source | Type | Used In |
|--------|------|---------|
| Multi-agent failure research | Academic | AI_SYSTEM/conflict_playbook.md |
| Organizational memory research | Academic | STATE/, EXPERTISE/ |
| RBAC patterns | Industry | PERMISSIONS.yaml |
| GraphRAG documentation | Microsoft | AI_SYSTEM/context_protocol.md |
| Chaordic organization | Dee Hock/VISA | OVERVIEW.md, CONSTITUTION.md |
| Time banking | Research | Future: volunteer currency |

### Decision Chain

```
Harley: "Over-engineer to perfection"
    │
    ├─→ Z: Research + coordinate
    │       │
    │       ├─→ ChatGPT: Architecture + protocols
    │       │
    │       └─→ Research findings: Multi-agent, governance, memory
    │
    └─→ This repo
```

---

## UPDATE LOG

| Date | Update Type | Description |
|------|-------------|-------------|
| 2025-01-15 | CREATE | Initial repo structure created by Z |

---

## HOW TO UPDATE

When a new AI contributes:

1. Add to AI Contributors table
2. Add any new files to File Lineage
3. Add any new knowledge sources to Knowledge Sources
4. Update Decision Chain if significant

---

## VERSION

- AI_BOM.md: v0.1.0
- Last updated: 2025-01-15
