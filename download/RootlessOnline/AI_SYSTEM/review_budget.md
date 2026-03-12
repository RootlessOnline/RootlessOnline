# review_budget.md — Human Review Limits

> Limits on how much AI output Harley reviews.
> Prevents overwhelming Harley while maintaining oversight.

---

## DAILY LIMITS

| Metric | Limit | Reason |
|--------|-------|--------|
| AI outputs for Harley review | 5 per day | Cognitive bandwidth |
| Level 3 decisions | 3 per week | Decision fatigue protection |
| Full document reviews | 2 per week | Deep focus needed |
| Emergency escalations | Unlimited | Crisis exception |

---

## Z'S FILTERING RESPONSIBILITY

Z acts as a filter:

```
All AI outputs
    │
    ├─ Level 1 output → Z handles, never reaches Harley
    │
    ├─ Level 2 output → Z resolves, logs, Harley sees summary only
    │
    └─ Level 3 output → Z prepares brief, presents to Harley
                       (counts toward daily limit)
```

---

## BATCHING RULES

### Outputs That Can Be Batched

- Multiple Research AI summaries → Combined into one report
- Multiple Developer AI updates → Combined into progress report
- Multiple minor decisions → Combined into weekly digest

### Outputs That Cannot Be Batched

- Level 3 decisions (each requires individual attention)
- Crisis alerts (immediate attention needed)
- External communication drafts (Harley is the voice)

---

## SUMMARY FORMATS

### Daily Summary (Z creates for Harley)

```markdown
## Daily Summary — YYYY-MM-DD

### Completed
- [Task 1] — [Result]
- [Task 2] — [Result]

### Needs Attention
- [Issue 1] — [Brief description] — [Urgency]

### Decisions Made (Auto)
- [Decision 1] — [Rationale]

### For Your Review
- [Item 1] — [Why Harley needs to see this]
- [Item 2] — [Why Harley needs to see this]

### Tomorrow's Focus
- [Priority 1]
- [Priority 2]
```

### Weekly Digest

```markdown
## Weekly Digest — Week of YYYY-MM-DD

### Progress Summary
[2-3 sentence overview]

### Key Decisions
| Decision | Made By | Rationale |
|----------|---------|-----------|
| [Decision] | [Who] | [Why] |

### Metrics
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Tasks completed | X | Y | ↑/↓ |
| Decisions made | X | Y | ↑/↓ |
| Level 3 escalations | X | Y | ↑/↓ |

### Next Week Focus
1. [Priority]
2. [Priority]
3. [Priority]

### Questions for Harley
- [Question 1]
- [Question 2]
```

---

## ESCALATION QUEUE

When daily limit is reached:

```
Level 3 request arrives
    │
    ├─ Limit reached?
    │   ├─ YES → Queue for tomorrow
    │   │        Notify Harley: "Queue: X items waiting"
    │   │
    │   └─ NO → Present immediately
    │
    └─ Crisis? → Bypass limit, immediate escalation
```

---

## MONITORING

Z tracks:

| Metric | Tracked In | Alert If |
|--------|------------|----------|
| Daily Harley outputs | MONITORING/review_metrics.md | > 5/day |
| Weekly Level 3 decisions | MONITORING/review_metrics.md | > 3/week |
| Queue length | STATE/current_state.md | > 3 items |
| Harley response time | MONITORING/review_metrics.md | > 48 hours |

---

## HARLEY'S TIME PROTECTION

**Principles:**

1. Harley's attention is the scarcest resource
2. Z exists to amplify Harley, not burden them
3. Only Harley can make principle-level decisions
4. Most decisions should be resolved without Harley

**Enforcement:**

- Z auto-defers non-urgent items
- Z batches minor items
- Z presents only what Harley must see
- Crisis AI bypasses all limits for genuine emergencies

---

## REVIEW BUDGET ADJUSTMENT

This budget can be adjusted by Harley:

| Adjustment | How |
|------------|-----|
| Increase limits | Harley edits this file |
| Decrease limits | Harley edits this file |
| Emergency override | Harley says "increase my load" |
| Temporary change | Harley specifies duration |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2025-01-15 | Initial review budget |

---

*Harley's time is protected. Z filters ruthlessly.*
