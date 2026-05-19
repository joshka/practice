# Test Cover Local Logic With Unit Tests

## Metadata

- ID: `TEST-COVER-LOCAL-LOGIC-WITH-UNIT-TESTS`
- Name: `Cover Local Logic with Unit Tests`
- Summary: Use unit tests for small local logic such as parsing helpers and policy branches.
  They give fast precise feedback, while boundary behavior still needs higher-level tests.
- Status: `reviewed`
- Domain: `testing`
- Tags: `testing, reader-locality, verification`
- Related: `test-prove-contracts-not-trivia, boundary-separate-pure-core-from-effects`

## Rule

Cover local logic with unit tests.

## Why

Small pure logic is cheapest to test close to where it lives. Unit tests can cover parsing helpers,
state transitions, formatting decisions, and policy branches without setting up the full public
integration path.

## Helps

- Gives fast, precise feedback for local contracts and edge cases.

## Limits

Unit tests are not enough for behavior that depends on public integration, feature flags,
filesystem, terminal, network, or external provider boundaries. Add higher-level tests for those
surfaces.

## Agent Instruction

Cover local logic with unit tests because small pure logic is cheapest to test close to where it lives.

## Mechanisms

Supported by module tests, table cases, focused fixtures, pure helper extraction, and assertions
that compare meaningful values rather than implementation details.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
