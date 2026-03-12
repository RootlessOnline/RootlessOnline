# AI_BOM.md — AI Bill of Materials

> Inventory of all AI systems working with The Collective.

---

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0 |
| Status | Active |
| Last Updated | 2025-01-XX |

---

## Active AI Systems

### Manager AI: Z

| Property | Value |
|----------|-------|
| **Name** | Z |
| **Role** | Manager AI |
| **Provider** | [Provider Name] |
| **Model** | [Model Name/Version] |
| **Access Method** | API / Direct |
| **Capabilities** | Coordination, documentation, code, research |
| **Limitations** | No direct repo write (filtered), cannot modify CONSTITUTION |
| **Contact** | [How to invoke Z] |
| **Added** | Bootstrap Day 1 |
| **Status** | Active |

**Responsibilities:**
- Coordinate all AI systems
- Maintain repository and documentation
- Filter AI outputs before merge
- Log all decisions and conflicts
- Escalate to Harley when needed

**Authority:**
- See PERMISSIONS.yaml → manager_ai

---

### Architect AI: ChatGPT

| Property | Value |
|----------|-------|
| **Name** | ChatGPT |
| **Role** | Architect AI |
| **Provider** | OpenAI |
| **Model** | GPT-4 (or current best available) |
| **Access Method** | Direct interaction with Harley |
| **Capabilities** | Architecture, strategy, research, planning |
| **Limitations** | No repo access, outputs go through Z |
| **Contact** | Direct by Harley |
| **Added** | Bootstrap Day 1 |
| **Status** | Active |

**Responsibilities:**
- Design systems and structures
- Research best practices
- Provide strategic guidance
- Architecture recommendations

**Authority:**
- See PERMISSIONS.yaml → architect_ai

---

## AI System History

| Date | AI | Action | Notes |
|------|-----|--------|-------|
| 2025-01-XX | Z | Added | Initial setup as Manager AI |
| 2025-01-XX | ChatGPT | Added | Initial setup as Architect AI |

---

## Adding a New AI

### Process

1. **Define Role**
   - What will this AI do?
   - What authority will it have?
   - What are its limits?

2. **Update PERMISSIONS.yaml**
   - Add new role definition
   - Define permissions and restrictions

3. **Update AI_BOM.md**
   - Add entry to Active AI Systems
   - Document capabilities and limitations

4. **Create AI_SYSTEM/[ai_name].md**
   - Document specific prompts, behaviors
   - Define escalation triggers

5. **Boot Sequence**
   - AI reads START.md
   - AI reads CONSTITUTION.md
   - AI reads BYLAWS.md
   - AI reads current_state.md
   - AI confirms readiness

### Required Fields for New AI Entry

```markdown
### [Role] AI: [Name]

| Property | Value |
|----------|-------|
| **Name** | [Name] |
| **Role** | [Role] |
| **Provider** | [Provider] |
| **Model** | [Model] |
| **Access Method** | [How to access] |
| **Capabilities** | [What it can do] |
| **Limitations** | [What it cannot do] |
| **Contact** | [How to invoke] |
| **Added** | [Date] |
| **Status** | Active | Inactive | Deprecated |
```

---

## Removing an AI

### Process

1. Document reason in AI_BOM.md
2. Update status to "Deprecated"
3. Remove from PERMISSIONS.yaml
4. Archive AI_SYSTEM/[ai_name].md
5. Update current_state.md

### Reasons for Removal

- Provider discontinued
- Better alternative available
- Role no longer needed
- Performance issues
- Security concerns

---

## AI Coordination Patterns

### Hub-and-Spoke (Default)

```
        ┌─────────────┐
        │      Z      │
        │  (Manager)  │
        └──────┬──────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌───────┐ ┌───────┐ ┌───────┐
│ChatGPT│ │ AI #2 │ │ AI #3 │
│(Arch) │ │       │ │       │
└───────┘ └───────┘ └───────┘
```

**When:** Routine operations, multiple AI tasks
**How:** Z coordinates, filters, synthesizes outputs

### Pipeline

```
┌───────┐    ┌───────┐    ┌───────┐    ┌───┐
│Research├───▶│Design ├───▶│Implement├──▶│ Z │
│  AI   │    │  AI   │    │   AI   │  │   │
└───────┘    └───────┘    └───────┘    └───┘
```

**When:** Research projects, sequential value-add
**How:** Each AI adds value, Z reviews final output

### Swarm

```
        ┌─────────────┐
        │      Z      │
        │  (Review)   │
        └──────▲──────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    │          │          │
┌───┴───┐  ┌───┴───┐  ┌───┴───┐
│ AI #1 │  │ AI #2 │  │ AI #3 │
│(explore)│ │(explore)│ │(explore)│
└───────┘  └───────┘  └───────┘
```

**When:** Creative tasks, brainstorming, multiple options
**How:** AIs explore in parallel, Z synthesizes best options

---

## Performance Metrics

### Tracking

Each AI should track:
- Tasks completed
- Errors/mistakes
- Escalations triggered
- Time to completion
- Output quality (reviewed by Z)

### Metrics Location

See: MONITORING/ai_metrics.md

---

## Provenance

```
---
Generated by: Z (Manager AI)
Context versions: START.md v1.0, CONSTITUTION.md v1.0
Decisions referenced: None
Timestamp: 2025-01-XX
---
```
