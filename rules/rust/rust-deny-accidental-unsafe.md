# Rust Deny Accidental Unsafe

## Metadata

- ID: `RUST-DENY-ACCIDENTAL-UNSAFE`
- Legacy ID: `R-0235`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Deny accidental unsafe code when the crate does not need unsafe.

## Why

If a crate does not need unsafe, accidental unsafe blocks should fail loudly. A crate-level lint
makes the safety policy executable so unsafe does not enter through a helper, dependency workaround,
or generated snippet unnoticed.

## Helps

Helps crates that intend to be safe Rust catch accidental unsafe introductions during review and CI.

## Limits

Do not deny unsafe in crates that intentionally provide low-level primitives unless the unsafe
surface is confined to specific modules with their own policy.

## Agent Instruction

Deny accidental unsafe code in crates that do not need unsafe so unsafe blocks fail loudly.

## Mechanisms

Use `#![forbid(unsafe_code)]` or `#![deny(unsafe_code)]` at the crate or module level and document
exceptions where unsafe is part of the crate purpose.

## References

- [Rust Reference: lint check
  attributes](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes)
- [Rust Reference: unsafe blocks](https://doc.rust-lang.org/reference/unsafe-blocks.html)
