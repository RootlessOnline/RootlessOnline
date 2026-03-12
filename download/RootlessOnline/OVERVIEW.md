# OVERVIEW.md — The Collective

## One-Sentence Description

The Collective is a regenerative civic network that builds local communities through gardens, shared resources, and participatory governance — guided by principles, coordinated by AI, and led by Harley.

---

## Roles & Responsibilities

| Actor | Role / Responsibility |
|-------|----------------------|
| Harley | CEO / Decision-maker: Approves foundational changes, resolves principle-level conflicts, oversees mission execution. |
| Z | AI Manager / Coordinator: Runs the AI hub, ensures tasks align with purpose and principles, verifies bootstraps and escalations. |
| Research AI | Collects, structures, and summarizes knowledge; supports decision-making. |
| Developer AI | Implements projects, writes code, maintains project artifacts. |
| Crisis AI | Monitors for urgent issues, enforces escalation, and applies ultra-short context for rapid response. |

---

## Minimal Starting Steps (Bootstrapping)

### Day 1

- Write CONSTITUTION.md — one sentence purpose + 3–5 principles.
- Create START.md linking to purpose + principles.
- Make first decision: Garden project = Phase 1 → logged as ADR-001.

### Week 1

- Set up Z coordination protocol (AI_SYSTEM/boot_sequence.md).
- Create current_state.md with active tasks and phase.
- Document first garden iteration (projects/garden_business/plan.md).
- Log all decisions in decision_log.md.

### Month 1

- Draft BYLAWS.md defining operational rules and roles.
- Create PERMISSIONS.yaml for AI role access.
- Establish review_budget.md for governance oversight.
- Verify foundational systems work; fallback defaults applied if steps skipped.

---

## Core Principles for Daily Operation

1. **Purpose First** — All actions align with the constitution and principles.
2. **Principles Guide Decisions** — Bylaws, precedent, and escalation enforce the framework.
3. **AI Coordination** — Hub-and-Spoke for standard operations; Swarm for creativity; Pipeline for research.
4. **Provenance & Versioning** — Every decision, output, and document has traceable lineage.
5. **Knowledge + Expertise** — Explicit and tacit knowledge captured in WIKI/ and EXPERTISE/ folders.
6. **Conflict Handling** — Decision tree + playbook resolves most issues automatically; principle conflicts escalate to Harley.

---

## Key Repositories & Structure

| Category | Files/Folders |
|----------|---------------|
| FOUNDATION | CONSTITUTION.md, BYLAWS.md, SUCCESSION.md |
| KNOWLEDGE | WIKI/, EXPERTISE/, RESEARCH/ |
| STATE | current_state.md, decision_log.md, worklog.md |
| AI SYSTEM | roles.md, boot_sequence.md, context_protocol.md, escalation.md, conflict_playbook.md, handoff_protocol.md, prompts/ |
| PROVENANCE | audit_trail/, AI_BOM.md |
| VERSIONING | CHANGELOG.md, semantic version tags, 3-level context compression |
| BOOTSTRAP | BOOTSTRAP_SEQUENCE.md |
| PROJECTS | All community, garden, app, and political initiatives |
| TEMPLATES | Starter kits for new projects or communities |

---

## How to Read & Act

- **Harley** focuses on principle-level decisions, approves changes to foundational docs, and escalates only principle conflicts.
- **Z and AIs** run all operational tasks, load the appropriate context versions, and maintain provenance.
- **All decisions** are logged in decision_log.md and linked to related outputs.
- **Every document** has FULL / SUMMARY / ULTRA versions for normal, rapid, and crisis operations.
- **Updates** follow semantic versioning; MAJOR changes trigger review and approval.

---

## Version

- Repo: v0.1.0 (Bootstrap)
- OVERVIEW.md: v0.1.0
- Last updated: 2025-01-15
