# Rust Maintainability

This guide applies the repo's software-change preferences to Rust code. Prefer Rust that is easy to
read locally, hard to misuse, and honest about behavior, performance, and error boundaries.

Use this guide with [Software Change Preferences](software-change-preferences.md) and
[Code Shape](code-shape.md), not instead of them.

## Core Preference

Prefer reader-first Rust that still respects ownership, performance, and API compatibility. A Rust
change is better when it reduces the number of concepts, fields, lifetimes, jumps, and hidden
invariants a maintainer must hold at once.

Use [Reader Locality][reader-locality] when extraction, module movement, or helper placement affects
how much context a reader must reconstruct.
Use [Code Shape][code-shape] when the change is primarily about live context, extraction,
structure/behavior separation, reversible structure, cohesion, coupling, naming, or local
expression shape.

## Concepts And Types

Extract a type or helper when it names a real concept and reduces downstream reasoning. Avoid
wrapper types, tuple structs, or parameter bags that are constructed only to be immediately
destructured.

Prefer types that make invalid states hard to express when the invariant is repeated, meaningful,
and useful across a boundary. Keep a guard clause or local validation when the rule is one-off and a
new type would add ceremony without reducing risk.

Use [Test Observable Behavior][test-behavior] before trusting a refactor that moves concepts around.

## Functions And Control Flow

Keep functions small enough to fit in a maintainer's head. Longer functions are acceptable when
their visual paragraphs map directly to meaningful phases.

Prefer named locals for important calls, side-effectful operations, and values whose role matters to
the reader. Use iterators for pure transformations and explicit loops for mutation, control flow, or
important side effects.

Use [Separate Structure From Behavior][structure-behavior] when a rename, move, extraction, or
formatting pass can be reviewed independently from a behavior change.

## Modules And Visibility

Modules should represent concepts, not arbitrary file-size cuts. Put the central type, trait, or
workflow near the top, keep inherent impls close to their type, and make re-exports deliberate.

Use the smallest visibility that protects real invariants and keeps refactors cheap. Avoid
visibility ceremony that only makes the code look more layered.

## API Boundaries

Public APIs should be predictable, narrow, and hard to misuse. Prefer standard conversion traits
over ad hoc conversion names when the standard trait expresses the relationship. Keep dependencies
out of public types unless the dependency is part of the abstraction.

Use Conventional Commits only when the repo already follows that spec; otherwise keep jj
descriptions and commits in the canonical Chris Beams and Tim Pope style from
[Commit Messages For History][commit-history].

## Errors

Rust error types should preserve enough context for callers to act. Application boundaries may use
broad error types; reusable libraries should expose intentional errors with stable kinds and
recoverable context.

Use [Preserve Error Context][error-context] when wrapping or mapping errors. Use
[Write Actionable Error Messages][actionable-errors] when the visible message needs to help a user,
operator, caller, or support person make progress.

## Testing

Tests should protect observable behavior rather than private implementation shape. Prefer focused
unit tests, golden tests, round trips, property tests, or integration checks based on the changed
surface and likely failure.

Use [Smallest Trustworthy Verification][smallest-check] to pick the cheapest credible check and
[Report Verification Honestly][honest-verification] in the handoff.

## Performance

Prefer clarity first, then measure. Do not add caching, concurrency, allocation tricks, or unsafe
code from a guess alone. Keep hot-path changes small enough to benchmark directly, and document
intentional performance-sensitive shapes where future maintainers will see them.

Unsafe code should have a narrow purpose, a nearby safety argument, and tests or review evidence
that protect the invariant.

## Dependency Changes

Prefer the widest honest semver-compatible requirement that preserves the crate's intended behavior
and downstream integration shape. Use lockfile updates for newer compatible releases, and raise
`Cargo.toml` minimums only when a newer minimum is actually required.

Keep maintenance-only dependency updates separate from changes that may alter parsing, trait
behavior, MSRV, feature behavior, or public API semantics.

## Agent Snippet

For copyable `AGENTS.md` guidance, use [Rust Agent Instructions][rust-snippet].

## Review Questions

- Does this name a real Rust concept or just move code?
- Are ownership and borrowing relationships visible at the call site?
- Does the type make invalid states harder to express?
- Did the change improve locality or fragment understanding?
- Did tests protect observable behavior instead of private shape?
- Are error kinds, context, and recovery paths visible at the boundary?
- Is a performance-sensitive choice measured or clearly documented?
- Did dependency requirements change only when the minimum truly changed?

## References

| Source                      | Use      | Note                                                        |
| --------------------------- | -------- | ----------------------------------------------------------- |
| [C-VALIDATE][validate]      | `adapts` | Prefer argument types that rule out bad inputs.             |
| [C-CONV-TRAITS][conv]       | `adapts` | Standard conversion traits keep APIs interoperable.         |
| [C-GOOD-ERR][errors]        | `adapts` | Error types should be meaningful and well-behaved.          |
| [M-SIMPLE-ABSTRACTIONS][ms] | `adapts` | Public APIs should avoid exposing nested generic machinery. |
| [epage Rust Style][epage]   | `adapts` | Reader-locality and Rust code-shape guidance.               |

[actionable-errors]: ../patterns/write-actionable-error-messages.md
[conv]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-conv-traits
[commit-history]: ../patterns/commit-messages-for-history.md
[code-shape]: code-shape.md
[epage]: https://epage.github.io/dev/rust-style/
[errors]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-good-err
[error-context]: ../patterns/preserve-error-context.md
[honest-verification]: ../patterns/report-verification-honestly.md
[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS
[reader-locality]: ../patterns/reader-locality.md
[rust-snippet]: ../snippets/agents/rust.md
[smallest-check]: ../patterns/smallest-trustworthy-verification.md
[structure-behavior]: ../patterns/separate-structure-from-behavior.md
[test-behavior]: ../patterns/test-observable-behavior.md
[validate]: https://rust-lang.github.io/api-guidelines/dependability.html#c-validate
