# Make Invalid States Hard To Express

## Metadata

- Name: `Make Invalid States Hard To Express`
- ID: `make-invalid-states-hard-to-express`
- Summary: Repeated validation spreads invariants across callers and lets unchecked values travel
  too far. Move the rule into a construction boundary or precise type when that reduces downstream
  reasoning without adding local ceremony.
- Status: `reviewed`
- Audience: `both`
- Topics: `api-design, correctness, rust`
- Tags: `boundary-correctness, validation-policy, state-transitions, public-api`
- Related: `avoid-boolean-flag-parameters, test-observable-behavior`

## Problem

Repeated validation asks every caller to remember the same rule before using a value safely. One
missed check can let an empty identifier, unparsed URL, invalid state transition, or unsupported
mode travel deeper into the system.

## Preferred Move

Move the invariant into the boundary where uncertain input becomes a trusted value. Use precise
types, constructors, parsers, or enums so downstream functions accept a representation that carries
the invariant in its type or construction path.

## Tradeoff

Do not wrap values that are constructed and immediately destructured. A precise type should reduce
downstream reasoning; it should not add ceremony around a value that stays local to one branch.

## Agent Instruction

When the same validation protects the same invariant in multiple places, consider a precise type or
construction boundary. Avoid wrapper types that do not reduce downstream checks.

## Examples

Bad: the API accepts raw strings, so every caller must remember that blank names are invalid.

```rust
pub fn publish_pattern(name: String) {
    todo!()
}
```

Good: uncertain input becomes a trusted value before it reaches the publishing API.

```rust
pub struct PatternName(String);

impl PatternName {
    pub fn parse(input: &str) -> Result<Self, PatternNameError> {
        todo!()
    }
}

pub fn publish_pattern(name: PatternName) {
    todo!()
}
```

## References

| Source                 | Use        | Note                                                     |
| ---------------------- | ---------- | -------------------------------------------------------- |
| [C-VALIDATE][validate] | `supports` | Prefer argument types that rule out bad inputs.          |
| [M-AVOID-WRAPPERS][ms] | `adapts`   | Avoid wrappers when they add API ceremony without value. |

[validate]: https://rust-lang.github.io/api-guidelines/dependability.html#c-validate
[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-AVOID-WRAPPERS
