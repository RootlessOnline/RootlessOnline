# decision_log.md — Decision Record

> All major decisions logged here with full reasoning.
> This becomes precedent for future AI decisions.
> Format: Architecture Decision Record (ADR)

---

## HOW TO USE

**Reading:**
- Check here before making any significant decision
- Look for precedent: "Has this been decided before?"
- If yes, follow the precedent unless you have strong reason to revisit

**Writing:**
- Create new ADR for each Level 2-3 decision
- Include: Context, Decision, Reasoning, Alternatives, Consequences
- Number sequentially: ADR-001, ADR-002, etc.

---

## DECISION INDEX

| ADR | Title | Date | Status |
|-----|-------|------|--------|
| ADR-001 | Garden Business First | Pending | Draft |

---

## ARCHITECTURE DECISION RECORDS

---

### ADR-001: Garden Business First

**Status:** DRAFT (Awaiting Harley approval)

**Date:** 2025-01-15

**Context:**
Harley has limited resources ($0 budget, solo founder) and needs to choose where to start. Options include garden business, Collective app, community tools, or political party.

**Decision:**
Garden business will be Phase 1 of The Collective.

**Reasoning:**
1. Gardens provide immediate tangible value
2. Low capital requirement (land access through partnerships)
3. Proof of concept for regenerative model
4. Harley has existing expertise and passion
5. Creates credibility for later phases
6. Eric Haas retreat opportunity provides immediate land access

**Alternatives Considered:**

| Alternative | Rejected Because |
|-------------|------------------|
| Collective App first | No users yet; need proof of concept first |
| Community tools first | Need community first; tools without users = waste |
| Political party first | Need credibility and base; 4-year deadline allows time |

**Consequences:**
- Positive: Fast path to proof of concept, income potential, credibility
- Positive: Aligns with Eric Haas opportunity
- Risk: May be slower to scale than digital-first approach
- Mitigation: Document everything for replication

**Referenced By:**
- START.md (phase definition)
- PROJECTS/garden_business/

**Precedent For:**
- Future project prioritization decisions

---

## DECISION LOG TEMPLATE

```
### ADR-XXX: [Title]

**Status:** PROPOSED / APPROVED / SUPERSEDED

**Date:** YYYY-MM-DD

**Context:**
[What is the issue that is motivating this decision?]

**Decision:**
[What is the change that we're proposing and/or doing?]

**Reasoning:**
[Why are we doing this? What's the logic?]

**Alternatives Considered:**
| Alternative | Rejected Because |
|-------------|------------------|
| [Option A] | [Reason] |
| [Option B] | [Reason] |

**Consequences:**
- Positive: [What good comes from this?]
- Risk: [What could go wrong?]
- Mitigation: [How do we handle the risk?]

**Referenced By:**
- [Files that reference this decision]

**Precedent For:**
- [Future situations where this applies]
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial decision log, ADR-001 draft |

---

*Decisions are the skeleton of the project. Document them all.*
