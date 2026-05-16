# Rust Preserve Valid State On Failure

## Metadata

- Name: `Preserve Valid State On Failure`
- ID: `RUST-PRESERVE-VALID-STATE-ON-FAILURE`
- Summary: Keep values valid when fallible operations return errors so callers can retry, inspect, or
  drop them predictably. Use transactional updates or staging when partial mutation would expose a
  broken state.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Preserve the current usable state when refresh, parsing, I/O, or rendering preparation fails.

## Why

Partially applied failure paths can leave callers with neither the old valid state nor the new
state. Rust makes ownership explicit, but state transitions still need policy: read, normalize,
compare, and only then mutate when the new state is safe to publish.

The Rust API Guidelines example for `Read::read` highlights an important contract shape: when an
error is returned, callers need to know whether partial work happened. Stateful code should make the
same policy explicit and prefer preserving the previous usable state when a refresh cannot be fully
validated.

## Helps

- Helps stateful Rust code avoid corrupting usable state after fallible work.

## Limits

Destructive operations may intentionally invalidate state. Make that policy explicit and test the
failure path. When partial mutation is unavoidable, report enough detail for callers to recover or
rebuild state.

## Agent Instruction

Stage fallible Rust refresh, parse, I/O, or render work before mutating usable state.

## Mechanisms

Supported by state-transition tests, temporary values, transaction-like updates, and failure-path
review.

## References

- [Rule: BOUNDARY-READ-NORMALIZE-COMPARE-MUTATE](../boundary/boundary-read-normalize-compare-mutate.md)
- [Rust API Guidelines: Function docs include error, panic, and safety
  considerations](https://rust-lang.github.io/api-guidelines/documentation.html#c-failure)
- [Pattern: Make State Transitions Explicit](../../patterns/make-state-transitions-explicit.md)
