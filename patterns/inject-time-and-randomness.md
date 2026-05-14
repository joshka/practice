# Inject Time And Randomness

## Metadata

- Name: `Inject Time And Randomness`
- ID: `inject-time-and-randomness`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, testing, side-effects`
- Related: `make-parameters-explicit, test-observable-behavior`

## Problem

Time and randomness make code harder to test when they are read from inside the behavior being
checked. The caller cannot reproduce the boundary case, and the test must race the clock or accept
whatever random value appears.

## Preferred Move

Inject time, identifiers, random choices, and nonce-like values at the boundary where nondeterminism
is acceptable. Keep deterministic decision logic behind explicit parameters or a small trait only
when the operation needs a reusable source.

## Tradeoff

Do not introduce a broad clock or random-provider trait for one local value. Passing a timestamp,
seed, generated ID, or chosen value is often clearer than adding a mockable service.

## Agent Instruction

When adding behavior that reads time or randomness, keep nondeterminism at the edge. Pass explicit
values into the decision logic, or introduce a narrow provider only when multiple operations share
the same source.

## Examples

Bad: the decision reads the clock internally, so tests cannot choose the boundary instant.

```rust
pub fn is_expired(deadline: SystemTime) -> bool {
    SystemTime::now() >= deadline
}
```

Good: the caller supplies the instant used by the decision.

```rust
pub fn is_expired(deadline: SystemTime, now: SystemTime) -> bool {
    now >= deadline
}
```

## References

| Source                             | Use      | Note                                                  |
| ---------------------------------- | -------- | ----------------------------------------------------- |
| [SystemTime][system-time]          | `adapts` | Wall-clock time can move in ways callers must handle. |
| [C-CALLER-CONTROL][caller-control] | `adapts` | Callers should keep meaningful control over inputs.   |

[caller-control]: https://rust-lang.github.io/api-guidelines/flexibility.html#c-caller-control
[system-time]: https://doc.rust-lang.org/std/time/struct.SystemTime.html
