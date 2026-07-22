# Test Avoid Opaque Boolean Assertions

## Metadata

- Name: `Avoid Opaque Boolean Assertions`
- ID: `TEST-AVOID-OPAQUE-BOOLEAN-ASSERTIONS`
- Summary: Prefer comparisons or richer assertions when a predicate hides state needed to diagnose
  the failure. The first failure should show the useful actual value.
- Related: `tests-should-explain-failures, test-optimize-failure-output, test-observable-behavior,
  write-actionable-error-messages`
- Status: `reviewed`
- Domain: `test-failures`
- Tags: `testing, failure-output, reviewability`

## Rule

Avoid boolean assertions when the predicate hides state needed to diagnose a failure.

## Why

An assertion like `assert!(items.contains(x))`, `assert!(items.is_empty())`, or
`assert!(result.is_ok())` can fail while showing little useful state. The condition is boolean, but
the collection contents, error variant, or whole struct often explains what changed. A comparison,
snapshot, or domain assertion can expose that state in the first failure.

## Helps

- Makes CI and agent failures easier to diagnose from the first failure message.

## Limits

Boolean assertions are fine when the boolean itself is the useful actual value. Prefer richer output
when a predicate hides state needed to diagnose why it was false.

Compare the whole value when the whole value is the contract. Use snapshots for structured or
rendered text that is easier to review as a whole. When only one property matters and whole-value
equality would be too strict, use a predicate that reports useful actual-value context or write a
small domain assertion helper.

A custom assertion message that shows the actual value is a useful fallback. Structured comparison
or snapshot output is generally stronger because it preserves expected-versus-actual structure and
can produce a focused diff.

Do not print values indiscriminately. For very large values or values containing sensitive data,
compact context or a boolean assertion may be the better tradeoff.

## Agent Instruction

Use boolean assertions when the boolean is the useful actual value. When a predicate hides
diagnostic state, choose a comparison, snapshot, contextual predicate, or small domain assertion
helper that exposes the relevant actual value without printing excessive or sensitive data.

## Mechanisms

Supported by `assert_eq!`, pretty assertions, snapshot tests, custom assertion helpers, and
contextual assertion messages that include useful actual values.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Clippy PR #17149: Add `assert_is_empty`
  lint](https://github.com/rust-lang/rust-clippy/pull/17149)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
