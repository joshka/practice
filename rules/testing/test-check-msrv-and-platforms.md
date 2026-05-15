# Test Check MSRV And Platforms

## Metadata

- ID: `TEST-CHECK-MSRV-AND-PLATFORMS`
- Legacy ID: `R-0423`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Run MSRV and platform checks when the crate declares them.

## Why

MSRV and platform support are public compatibility claims. A crate that declares support for an
older Rust version, Windows terminal behavior, or Unix-only paths needs checks that prove those
claims still hold after dependency and API changes.

## Helps

- Keeps support claims aligned with reality and catches accidental platform or toolchain
  regressions.

## Limits

Do not run expensive platform matrices for crates that do not make platform promises. Match checks
to documented support and release risk.

## Agent Instruction

Run MSRV and platform checks for crates that publish those compatibility claims.

## Mechanisms

Supported by pinned toolchain CI, `rust-version` checks, platform matrices, cargo metadata review,
and release-support documentation.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
