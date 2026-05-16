# Test Optimize Failure Output

## Metadata

- Name: `Optimize Failure Output`
- ID: `TEST-OPTIMIZE-FAILURE-OUTPUT`
- Summary: Design tests so failures include expected values, actual values, inputs, and contract
  context where that helps repair. Useful output shortens CI and agent debugging loops.
- Related: `tests-should-explain-failures, test-observable-behavior,
  smallest-trustworthy-verification`
- Status: `reviewed`
- Domain: `test-failures`
- Tags: `testing, failure-output, errors, reviewability`

## Rule

Optimize tests for useful failure output.

## Why

A passing test is useful, but a failing test is where maintainers and agents spend repair time.
Tests should fail with the expected and actual values, relevant input, and enough context to
identify the broken contract without rerunning under a debugger.

## Helps

- Shortens repair loops and makes regression failures actionable in CI logs.

## Limits

Do not turn tests into verbose diagnostics when the failure is already obvious. Add output where it
changes the speed or reliability of repair.

## Agent Instruction

Optimize tests for useful failure output because a passing test is useful, but a failing test is where
maintainers and agents spend repair time.

## Mechanisms

Supported by whole-value comparisons, snapshots, named table cases, custom messages with input
context, and regression tests that preserve useful failure shape.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
