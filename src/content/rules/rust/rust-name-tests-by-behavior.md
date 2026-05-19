# Rust Name Tests By Behavior

## Metadata

- Name: `Name Tests By Behavior`
- ID: `RUST-NAME-TESTS-BY-BEHAVIOR`
- Summary: Name tests after the behavior, boundary, or regression they protect so failure output is
  useful before a reader opens the body. Keep names concise and let module context carry repeated
  setup details.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, testing, failure-output, reviewability`
- Related: `tests-should-explain-failures, test-optimize-failure-output`

## Rule

Name Rust tests by the behavior they protect.

## Why

Test names are the first diagnostic readers see when a Rust test fails. Names that only repeat the
function under test, such as `test_parse`, force readers to open the body before they know what
contract broke.

Behavior-oriented names describe the expected outcome, boundary, or regression: accepted input,
rejected shape, preserved state, cleanup behavior, feature interaction, or visible error. That makes
failures useful in CI output and helps future maintainers decide whether a refactor preserved the
right contract.

## Helps

- Helps test output explain the broken behavior before a reader opens the test body.

## Limits

Keep names concise. A short module name plus a behavior-focused test name is usually better than a
sentence-length function name.

## Agent Instruction

Name Rust tests for the behavior, boundary, or regression they protect, not just the function under
test.

## Mechanisms

Supported by test review, failure-output review, and regression tests named after the broken
contract.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rule: TEST-OPTIMIZE-FAILURE-OUTPUT](../test-failures/test-optimize-failure-output.md)
