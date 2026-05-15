# Test Write Regression Tests For Bug Fixes

## Metadata

- ID: `TEST-WRITE-REGRESSION-TESTS-FOR-BUG-FIXES`
- Legacy ID: `R-0410`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Write regression tests for bug fixes unless impractical.

## Why

A bug fix without a regression test can silently revert later, especially when the original failure
was an edge case, integration path, or user-reported behavior. The test should fail before the fix
and explain the broken contract after it is repaired.

## Helps

- Preserves user-reported fixes and gives future maintainers a precise failure when the bug returns.

## Limits

Skip or defer the test only when the bug is impractical to reproduce safely. In that case, document
the reason and use the closest practical validation.

## Agent Instruction

Write regression tests for bug fixes that could silently revert, especially edge cases, integration
paths, and user-reported behavior.

## Mechanisms

Supported by failing-first regression tests, minimized fixtures, issue-linked test names, snapshots,
integration tests, and handoff notes when reproduction is impractical.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
