# Keep One Authoritative Owner Per Fact

## Metadata

- Name: `Keep One Authoritative Owner Per Fact`
- ID: `BOUNDARY-KEEP-ONE-AUTHORITATIVE-OWNER-PER-FACT`
- Summary: Give each state fact one definite authority and derive other views from it where
  practical. Cached, persisted, or adapter-specific projections may duplicate a fact only when
  their source and invalidation or reconciliation contract are explicit.
- Status: `draft`
- Domain: `boundary`
- Tags: `boundary-correctness, state-transitions, ownership, source-truth`
- Related: `strengthen-cohesion, source-coherence-review,
  BOUNDARY-IDENTIFY-ANEMIC-STATE-MACHINES`

## Rule

Give each fact one authoritative owner; derive or explicitly invalidate every other representation.

## Why

Redundant state turns one update into a synchronization protocol. A score and stored level, a status
variant and `is_running` flag, or an optional deadline and `timed_out` flag can disagree even when
each field looks reasonable by itself. The same failure occurs across types when a UI, adapter,
cache, and domain model each act as though their copy is authoritative.

Prefer the representation that naturally owns the transition. Derive cheap deterministic facts from
it, expose read-only projections for other layers, and route runtime mutation through one owner. For
example, `JobState::Running { deadline }` can answer whether a job is running and whether its deadline
has elapsed; separate `is_running`, `timeout_active`, and status fields should not independently make
those claims.

A projection is not a second authority. A rendering snapshot, database materialized view, search
index, adapter record, or measured performance cache may duplicate source data when it identifies:

- the authoritative source;
- the operation, version, event, or key that refreshes or invalidates it;
- whether stale reads are allowed and for how long;
- how missing, partial, or failed refreshes recover;
- tests or measurements that justify the duplicate representation.

## Helps

- Prevents flags, timers, status variants, caches, and adapters from disagreeing about the same fact.
- Removes synchronization branches for values that can be derived from existing state.
- Makes mutation, invalidation, stale-read behavior, and recovery boundaries reviewable.
- Preserves useful projections without weakening the authoritative domain model.

## Limits

Related fields are not necessarily duplicate facts. A job's status, start time, and attempt count can
have different meanings and retention needs even though one transition updates them together.

Persisted denormalization, offline replicas, distributed ownership, and interoperability boundaries
may require several writable representations. In those cases, define authority by scope and make
conflict resolution or reconciliation part of the model. Do not claim one global authority when the
system deliberately supports concurrent authorities.

Do not replace a measured cache with repeated expensive computation merely to remove duplication.
Keep the cache and document its invalidation contract. Conversely, an undocumented cache is not
justified by calling it a projection.

## Agent Instruction

Identify the authority for each duplicated fact; derive other views or document their refresh,
staleness, and reconciliation contract before keeping writable projections.

## Mechanisms

Supported by [Source Coherence Review](../../mechanisms/source-coherence-review.md), constructor and
transition review, cache-key or version tests, stale-read tests, and assertions that projections are
updated or invalidated at the authoritative mutation boundary.

## References

- [React: Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure)
- [Redux Fundamentals: Single Source of Truth](https://redux.js.org/tutorials/fundamentals/part-2-concepts-data-flow#single-source-of-truth)
- [PostgreSQL: Materialized Views](https://www.postgresql.org/docs/current/rules-materializedviews.html)
