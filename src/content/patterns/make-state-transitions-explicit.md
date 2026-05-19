# Make State Transitions Explicit

## Metadata

- Name: `Make State Transitions Explicit`
- ID: `make-state-transitions-explicit`
- Summary: Lifecycle rules become fragile when status fields, timestamps, events, and validation
  checks are coordinated by hand. Give meaningful transitions a named owner that holds the
  preconditions, state update, event, and error behavior together.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api-design, state`
- Tags: `state-transitions, boundary-correctness, reader-locality`
- Related: `make-invalid-states-hard-to-express, strengthen-cohesion`

## Problem

Lifecycle state becomes fragile when callers mutate fields directly or coordinate several updates by
hand. The transition rule is spread across status fields, timestamps, events, persistence, and
validation checks that must move together.

A cluster of functions can also be an anemic state machine: the code has states, events, guards, and
transitions, but no type or module owns the machine. Each caller has to reconstruct which transitions
are allowed and which side effects belong to them.

## Preferred Move

Represent state transitions as named operations. Put the precondition, state update, emitted event,
and returned error in the method or function that owns the transition. Use enums or transition
types when the domain has a closed set of states.

When scattered functions form a state machine, name the machine and give it a small owner. The owner
does not need to be large, but it should make the states, legal transitions, and transition effects
visible in one place.

Common places to look are auth flows, UI state, workflow runners, import pipelines, retry loops, and
payment or publishing lifecycles. These often start as "just a few helpers" and become a state
machine once cases, retries, failure modes, and recovery paths accumulate.

## Tradeoff

Do not hide ordinary field updates behind ceremony when there is no lifecycle rule. The transition
operation should protect an invariant, emit a meaningful event, or make an invalid transition hard
to express.

## Agent Instruction

When a change mutates lifecycle fields, look for the state transition being performed. Introduce or
use a named transition operation when multiple facts must change together or invalid transitions are
possible. If several functions collectively encode states and events, call out the state machine and
consider giving it an owner.

## Examples

Bad: callers must remember every field and event involved in publishing.

```rust
pattern.status = Status::Published;
pattern.published_at = Some(now);
events.push(PatternEvent::Published { at: now });
```

Good: the aggregate owns the transition and its preconditions.

```rust
impl Pattern {
    pub fn publish(&mut self, now: SystemTime) -> Result<PatternEvent, PublishError> {
        if self.status != Status::Reviewed {
            return Err(PublishError::NotReviewed);
        }

        self.status = Status::Published;
        self.published_at = Some(now);
        Ok(PatternEvent::Published { at: now })
    }
}
```

## References

| Source                      | Use      | Note                                              |
| --------------------------- | -------- | ------------------------------------------------- |
| [C-VALIDATE][validate]      | `adapts` | APIs should enforce validity where practical.     |
| [M-SIMPLE-ABSTRACTIONS][ms] | `adapts` | Public APIs should expose simple domain concepts. |

[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS
[validate]: https://rust-lang.github.io/api-guidelines/dependability.html#c-validate
