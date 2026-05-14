# Make State Transitions Explicit

## Metadata

- Name: `Make State Transitions Explicit`
- ID: `make-state-transitions-explicit`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api-design, state`
- Related: `make-invalid-states-hard-to-express, strengthen-cohesion`

## Problem

Lifecycle state becomes fragile when callers mutate fields directly or coordinate several updates by
hand. The transition rule is spread across status fields, timestamps, events, persistence, and
validation checks that must move together.

## Preferred Move

Represent state transitions as named operations. Put the precondition, state update, emitted event,
and returned error in the method or function that owns the transition. Use enums or transition
types when the domain has a closed set of states.

## Tradeoff

Do not hide ordinary field updates behind ceremony when there is no lifecycle rule. The transition
operation should protect an invariant, emit a meaningful event, or make an invalid transition hard
to express.

## Agent Instruction

When a change mutates lifecycle fields, look for the state transition being performed. Introduce or
use a named transition operation when multiple facts must change together or invalid transitions are
possible.

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
