# Test Avoid Opaque Boolean Assertions

## Metadata

- ID: `TEST-AVOID-OPAQUE-BOOLEAN-ASSERTIONS`
- Status: `reviewed`
- Domain: `test-failures`
- Depth: `compact`

## Rule

Avoid boolean assertions for values with multiple failure causes.

## Why

An assertion like `assert!(items.contains(x))` or `assert!(result.is_ok())` can fail for many
reasons while showing little useful state. Comparing the actual collection, error variant, or whole
struct tells the next maintainer what changed.

## Helps

- Makes CI and agent failures easier to diagnose from the first failure message.

## Limits

Boolean assertions are fine for genuinely binary conditions. Use richer comparisons when multiple
causes can make the boolean false.

## Agent Instruction

Avoid boolean assertions for values with multiple failure causes because an assertion like
`assert!(items.contains(x))` or `assert!(result.is_ok())` can fail for many reasons while showing
little useful state.

## Mechanisms

Supported by `assert_eq!`, pretty assertions, snapshot tests, custom assertion helpers, and tests
that include useful actual values in failure output.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
