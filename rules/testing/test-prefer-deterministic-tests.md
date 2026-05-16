# Test Prefer Deterministic Tests

## Metadata

- ID: `TEST-PREFER-DETERMINISTIC-TESTS`
- Name: `Prefer Deterministic Tests`
- Summary: Prefer tests controlled by fixed inputs, clocks, ordering, and local state.
  Deterministic failures are reproducible, while real integration checks should be isolated by cost.
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Prefer deterministic tests over timing or external-state tests.

## Why

Tests that depend on timing, network state, random ordering, real clocks, or external services fail
for reasons unrelated to the code under review. Deterministic tests give agents and maintainers
failures they can reproduce and fix.

## Helps

- Reduces flaky CI and makes failures actionable.

## Limits

Some behavior needs real integration or timing validation. Isolate those checks, mark their cost,
and keep deterministic lower-level coverage for the core contract.

## Agent Instruction

Prefer deterministic tests over timing or external-state tests because tests that depend on timing,
network state, random ordering, real clocks, or external services fail for reasons unrelated to the
code under review.

## Mechanisms

Supported by fake clocks, seeded randomness, temp directories, mocked providers, local fixtures,
retry-free assertions, and quarantined live integration jobs.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
