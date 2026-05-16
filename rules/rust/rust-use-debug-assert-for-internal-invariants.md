# Rust Use Debug Assert For Internal Invariants

## Metadata

- Name: `Use Debug Assert For Internal Invariants`
- ID: `RUST-USE-DEBUG-ASSERT-FOR-INTERNAL-INVARIANTS`
- Summary: Use debug assertions for internal invariants that should hold if nearby code is correct.
  Do not use them for caller validation or safety requirements that must be enforced in release
  builds.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, validation-policy, failure-output`
- Related: `make-invalid-states-hard-to-express, rust-document-public-panic-contracts`

## Rule

Use `debug_assert!` for internal invariants that should be checked during development.

## Why

Some invariants indicate programmer mistakes inside the crate rather than ordinary caller-facing
errors. `debug_assert!` documents those assumptions and catches violations in debug builds without
turning every internal invariant into runtime error handling.

This matches the Pragmatic Rust distinction between programming bugs and ordinary errors: bugs are
not recovery paths for callers, while fallible input or environment behavior should be modeled as
errors. `debug_assert!` is useful when the invariant is internal and checking it in release builds
would be unnecessary or too expensive.

## Helps

- Helps distinguish internal correctness assumptions from recoverable public errors.

## Limits

Do not use `debug_assert!` for validating untrusted input, public preconditions that must always be
enforced, or safety requirements that unsafe code relies on in release builds. If release behavior
would become unsound or externally wrong when the assertion is disabled, use ordinary validation.

## Agent Instruction

Use `debug_assert!` for internal Rust invariants, not for public validation or safety requirements.

## Mechanisms

Supported by tests, debug builds in CI where useful, and review of panic/error boundaries.

## References

- [Rust standard library: debug_assert](https://doc.rust-lang.org/std/macro.debug_assert.html)
- [Microsoft Pragmatic Rust Guidelines:
  Checklist](https://microsoft.github.io/rust-guidelines/guidelines/checklist/index.html)
- [Rule: RUST-DOCUMENT-PUBLIC-PANIC-CONTRACTS](rust-document-public-panic-contracts.md)
