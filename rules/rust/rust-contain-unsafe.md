# Rust Contain Unsafe

## Metadata

- ID: `RUST-CONTAIN-UNSAFE`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep unsafe small, wrapped, documented, and tested through the safe API.

## Why

Unsafe code concentrates obligations the compiler cannot check. Keeping unsafe blocks small,
documented, wrapped by safe APIs, and tested through safe behavior makes the invariant auditable and
reduces how much code must be trusted manually.

## Helps

Helps reviewers audit safety invariants locally and lets most tests exercise the unsafe behavior
through a safe public contract.

## Limits

Low-level crates may need more unsafe code, but the safety argument should still be localized and
attached to the abstraction that enforces it.

## Agent Instruction

Keep unsafe small, wrapped, documented, and tested through the safe API because unsafe concentrates
obligations the compiler cannot check.

## Mechanisms

Keep unsafe blocks small, document safety preconditions, wrap them in safe functions or types, add
focused tests, and run tools such as Miri where appropriate.

## References

- [Rust Reference: unsafe blocks](https://doc.rust-lang.org/reference/unsafe-blocks.html)
- [Rust API Guidelines: unsafe code documents
  invariants](https://rust-lang.github.io/api-guidelines/documentation.html#c-failure)
