# Collective App Hub — Project Overview

> An app store / hub for multiple community-focused applications.

---

## Project Information

| Property | Value |
|----------|-------|
| Phase | Concept Development |
| Priority | Phase 2 |
| Platform | TBD (Mobile-first? Web? PWA?) |

---

## The Concept

**Not one app — many apps.**

The Collective App Hub is like an app store, but specifically for tools that help communities:

1. **The Hub** — Central place to discover and access all apps
2. **Individual Apps** — Each solves a specific problem
3. **Integration** — Apps can share data when useful
4. **Community-owned** — Not corporate, not for-profit extraction

---

## App Ideas

### Category: Food & Growing

| App Name | Purpose | Key Features |
|----------|---------|--------------|
| **Garden Locator** | Find gardens near you, add your own | Map view, garden details, contact, photos |
| **Plant Doctor** | Identify plant problems, get help | Photo upload, AI diagnosis, community advice |
| **Seed Swap** | Exchange seeds with locals | Listings, messaging, meetups |
| **Harvest Tracker** | Track what you grow and harvest | Yields, season tracking, sharing |
| **Garden Planner** | Design your garden | Layout tool, planting calendar, companion planting |

### Category: Community & Connection

| App Name | Purpose | Key Features |
|----------|---------|--------------|
| **Neighbor Network** | Connect with people nearby | Location-based, interests, skills |
| **Skill Share** | Teach and learn skills | Listings, scheduling, reviews |
| **Time Bank** | Exchange services without money | Hour tracking, service listings, matching |
| **Event Finder** | Find local community events | Calendar, categories, RSVP |

### Category: Sharing Economy

| App Name | Purpose | Key Features |
|----------|---------|--------------|
| **Tool Library** | Borrow tools from neighbors | Inventory, reservations, return tracking |
| **Stuff Share** | Lend/borrow items | Listings, condition tracking, trust system |
| **Ride Share** | Community carpooling | Routes, scheduling, cost splitting |
| **Space Share** | Share community spaces | Booking, availability, rules |

### Category: Knowledge & Learning

| App Name | Purpose | Key Features |
|----------|---------|--------------|
| **How-To Hub** | Community-created guides | Step-by-step, photos/videos, ratings |
| **Local Wiki** | Community knowledge base | Articles, history, local info |
| **Mentor Match** | Connect mentors and learners | Profiles, matching, scheduling |

### Category: Health & Wellbeing

| App Name | Purpose | Key Features |
|----------|---------|--------------|
| **Green Rx** | Nature prescriptions | Local green spaces, activities, tracking |
| **Mood Garden** | Track mental health + garden time | Journal, mood log, patterns |
| **Community Care** | Request/offer help | Needs posting, volunteer matching |

### Category: Civic & Democracy

| App Name | Purpose | Key Features |
|----------|---------|--------------|
| **Local Voice** | Community voting on local issues | Proposals, voting, results |
| **Rep Tracker** | Track local representatives | Actions, voting record, contact |
| **Budget Watch** | See where public money goes | Data visualization, reporting |

---

## Hub Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    COLLECTIVE APP HUB                        │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Discover │  │  My Apps │  │  Profile │  │ Community│    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    FEATURED APPS                        ││
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐              ││
│  │  │ 🌱  │ │ 🔧  │ │ 👥  │ │ 📍  │ │ 💬  │              ││
│  │  │Grow │ │Tools│ │Net  │ │Map  │ │Chat │              ││
│  │  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘              ││
│  └─────────────────────────────────────────────────────────┘│
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    ALL APPS                             ││
│  │                                                         ││
│  │  Food & Growing │ Community │ Sharing │ Knowledge │ ... ││
│  │  [Grid of all available apps]                          ││
│  │                                                         ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

---

## Technical Considerations

### Platform Options

| Option | Pros | Cons |
|--------|------|------|
| **PWA (Web)** | Works anywhere, no app store, $0 | Limited offline, no push notifications |
| **Native Mobile** | Best UX, offline, notifications | Need iOS + Android, app store rules |
| **Hybrid (React Native)** | One codebase, native feel | Still needs app stores |
| **Telegram/WhatsApp Bots** | No install needed, familiar | Limited functionality |

**Recommendation for $0 budget:** Start with PWA, expand to native if successful

### Architecture

```
Hub (Container)
├── Authentication (shared)
├── Profile (shared)
├── Messaging (shared)
├── Location Services (shared)
└── Apps (modular)
    ├── Garden Locator
    ├── Tool Library
    ├── Skill Share
    └── ... (each as separate module)
```

---

## MVP Strategy

### Phase 1: Hub + 1 App

Start with:
- **Hub shell** (discovery, profile, community)
- **Garden Locator** (one working app)

Why Garden Locator first:
- Supports Garden Business (Phase 1 project)
- Relatively simple (map + listings)
- Immediately useful

### Phase 2: Add More Apps

Based on usage and feedback:
- Tool Library
- Skill Share
- Event Finder

### Phase 3: Integration

- Apps talk to each other
- Shared data (profile, location)
- Community features across apps

---

## Monetization (If Needed)

| Model | How | Notes |
|-------|-----|-------|
| **Free** | Grant-funded, community-supported | Aligns with $0 barrier principle |
| **Freemium** | Basic free, premium features paid | Could violate accessibility |
| **Community subscription** | Communities pay, individuals free | Organizations have budgets |
| **Transaction fees** | Small % on exchanges | Only for marketplace apps |

**Recommendation:** Grant + community funding, keep free for users

---

## Files to Create

| File | Purpose | Status |
|------|---------|--------|
| README.md | This overview | ✅ Created |
| STATUS.md | Current status | ❌ Needed |
| ROADMAP.md | Development timeline | ❌ Needed |
| apps/ | Individual app concepts | ❌ Needed |
| architecture.md | Technical details | ❌ Needed |

---

## Questions for Harley

1. **Which apps are priority?** (start with 1-3)
2. **Platform preference?** (PWA vs native)
3. **Any apps I missed?**
4. **Community Tools — is this the same as Tool Library app, or separate?**

---

## Provenance

```
---
Generated by: Z (Manager AI)
Context versions: START.md v1.0, CONSTITUTION.md v1.0
Timestamp: 2025-01-XX
---
```
