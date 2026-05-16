# Make Parameters Explicit

## Metadata

- Name: `Make Parameters Explicit`
- ID: `make-parameters-explicit`
- Summary: Hidden configuration, time, randomness, globals, or environment reads make behavior hard
  to reason about and test. Gather ambient data at the outer boundary, then pass typed inputs or a
  cohesive context to the inner operation.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api-design, parameters`
- Related: `make-side-effects-visible, limit-live-context`

## Problem

Hidden inputs make behavior hard to reason about and hard to test. A function that reads ambient
configuration, environment variables, global state, current time, random numbers, or untyped maps
forces callers to infer what the operation depends on from implementation details.

## Preferred Move

Pass the required inputs explicitly at the boundary where the behavior is chosen. Split functions
when needed: one layer gathers ambient data, and a smaller inner layer receives typed parameters
that state the real dependency.

## Tradeoff

Do not thread parameters through every layer blindly. If many functions merely forward a value they
do not use, introduce a cohesive context type or move the operation closer to the owner of that
dependency.

## Agent Instruction

When behavior depends on ambient inputs, make those inputs visible in the function signature or in a
named context type. Keep ambient reads at the outer boundary and make the inner behavior testable
with explicit values.

## Examples

Bad: the rule depends on environment and wall-clock time hidden inside the function.

```rust
pub fn should_publish(pattern: &Pattern) -> bool {
    let min_score = env::var("MIN_PUBLISH_SCORE")
        .ok()
        .and_then(|value| value.parse().ok())
        .unwrap_or(80);

    pattern.score_at(SystemTime::now()) >= min_score
}
```

Good: the boundary gathers ambient data, and the rule receives its real inputs.

```rust
pub struct PublishInputs {
    pub min_score: u32,
    pub now: SystemTime,
}

pub fn should_publish(pattern: &Pattern, inputs: PublishInputs) -> bool {
    pattern.score_at(inputs.now) >= inputs.min_score
}
```

## References

| Source                             | Use      | Note                                                        |
| ---------------------------------- | -------- | ----------------------------------------------------------- |
| [Tidy First, Ch. 10][tidy-ch10]    | `adapts` | Hidden inputs are clearer when passed through a boundary.   |
| [C-CALLER-CONTROL][caller-control] | `adapts` | APIs should leave ownership and placement choices visible.  |

[caller-control]: https://rust-lang.github.io/api-guidelines/flexibility.html#c-caller-control
[tidy-ch10]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch10.html
