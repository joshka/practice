# Test Cover Public Examples With Doctests

## Metadata

- ID: `TEST-COVER-PUBLIC-EXAMPLES-WITH-DOCTESTS`
- Name: `Cover Public Examples with Doctests`
- Summary: Compile public documentation examples as doctests when they do not need fragile state.
  Executable examples catch stale guidance, reserving no-run or ignored examples for real limits.
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Cover public examples with doctests when they can compile without fragile assumptions.

## Why

Public examples teach users and agents how to call the API. Doctests catch stale imports, renamed
methods, changed feature flags, and examples that no longer compile after API movement.

## Helps

- Keeps documentation examples executable and aligned with public API shape.

## Limits

Use `no_run`, `ignore`, or explanatory prose when examples require external services, credentials,
timing, or platform state. Prefer compiling examples when practical.

## Agent Instruction

Use doctests for public examples that teach humans and agents how to call the API and can compile
without fragile assumptions.

## Mechanisms

Supported by `cargo test --doc`, Rustdoc attributes, docs.rs-style builds, example fixtures, and CI
jobs that treat doctest failures as documentation drift.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
