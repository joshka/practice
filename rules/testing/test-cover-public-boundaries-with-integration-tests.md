# Test Cover Public Boundaries With Integration Tests

## Metadata

- ID: `TEST-COVER-PUBLIC-BOUNDARIES-WITH-INTEGRATION-TESTS`
- Legacy ID: `R-0408`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Cover public behavior across module boundaries with integration tests.

## Why

Public behavior can break across module, crate, feature, or adapter boundaries even when unit tests
pass. Integration tests prove that the pieces compose through the API shape users actually call.

## Helps

- Catches wiring, visibility, feature, and cross-module regressions at the user-facing boundary.

## Limits

Keep integration tests focused on public contracts. Use unit tests for dense local logic so
integration tests do not become slow duplicates.

## Agent Instruction

Use integration tests for public behavior that can break across modules, crates, features, or
adapters despite passing unit tests.

## Mechanisms

Supported by `tests/` integration tests, example crates, feature-specific integration jobs, public
API fixtures, and end-to-end command tests where appropriate.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
