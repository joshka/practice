# Test Split Unrelated Assertions

## Metadata

- ID: `TEST-SPLIT-UNRELATED-ASSERTIONS`
- Status: `reviewed`
- Domain: `test-failures`
- Depth: `compact`

## Rule

Keep unrelated assertions separate when failure diagnosis matters.

## Why

One test that checks parsing, formatting, ordering, error display, and cleanup may stop at the first
failure and hide the real scope of the regression. Separate unrelated assertions when the failure
modes require different fixes or explanations.

## Helps

- Makes failures local to one behavior and prevents one broken check from masking another.

## Limits

Keep related assertions together when they describe one contract and the combined output is clearer.
Split when the assertions diagnose different behavior.

## Agent Instruction

Split unrelated assertions because one failing check would hide the real scope or cause of a
regression.

## Mechanisms

Supported by named test cases, table-driven tests with case labels, focused regression tests, and
assertion helpers that report the behavior under test.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
