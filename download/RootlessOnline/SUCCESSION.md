# SUCCESSION.md — Continuity Protocol

> This document defines what happens if Harley is unavailable.
> Changes require Harley approval.
> This is critical infrastructure.

---

## AVAILABILITY LEVELS

| Level | Definition | Duration | Authority |
|-------|------------|----------|-----------|
| GREEN | Harley available | Normal | Full authority |
| YELLOW | Harley delayed | < 72 hours | Z handles Level 1-2, queues Level 3 |
| ORANGE | Harley extended absence | 3-14 days | Proxy council activated |
| RED | Harley indefinite absence | > 14 days | Succession protocol triggered |

---

## DELEGATION CHAIN

If Harley is unavailable, authority passes in this order:

### Primary Proxy
**Name:** [Harley: Designate a trusted person]
**Authority:** Level 1-3 decisions during YELLOW/ORANGE
**Contact:** [Method to reach them]

### Secondary Proxy
**Name:** [Harley: Designate a backup]
**Authority:** Level 1-2 decisions, can escalate to council
**Contact:** [Method to reach them]

### Council (Phase 2+)
**Members:** [To be designated when community exists]
**Authority:** Collective decisions by vote
**Quorum:** 3 members minimum

---

## Z AUTHORITY DURING ABSENCE

| Duration | Z Can Do | Z Cannot Do |
|----------|----------|-------------|
| < 24 hours | All Level 1-2 decisions | Level 3, modify CONSTITUTION |
| 24-72 hours | All Level 1-2, queue Level 3 | Level 3 without proxy approval |
| 3-14 days | Coordinate with proxy, maintain operations | Make irreversible decisions |
| > 14 days | Maintain stability, alert council | Any major changes |

---

## TRIGGER CONDITIONS

### YELLOW (Delay)
- Harley doesn't respond to Level 3 request within 24 hours
- Harley indicates temporary unavailability
- External factors prevent immediate response

### ORANGE (Extended)
- YELLOW persists for 72+ hours
- Harley explicitly delegates to proxy
- No contact for 72 hours (automatic)

### RED (Indefinite)
- ORANGE persists for 14+ days
- Harley explicitly transfers control
- Council vote to activate (unanimous)

---

## RECOVERY PROTOCOL

When Harley returns:

1. Z provides summary of all decisions made during absence
2. Harley reviews decision_log.md entries
3. Harley confirms or revises any proxy decisions
4. State returns to GREEN
5. CHANGELOG.md notes absence period

---

## KNOWLEDGE PRESERVATION

To ensure continuity, Harley should:

- [ ] Complete EXPERTISE/harley_intuition/ documentation
- [ ] Record 3+ Critical Decision Method interviews
- [ ] Define at least one proxy
- [ ] Review this document quarterly

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial succession plan — awaiting Harley's designations |

---

## STATUS

- [ ] Primary proxy designated
- [ ] Secondary proxy designated
- [ ] Emergency contact methods defined
- [ ] Knowledge transfer initiated

---

*The project continues even if the founder cannot.*
