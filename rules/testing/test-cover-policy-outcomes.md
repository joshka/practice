# Test Cover Policy Outcomes

## Metadata

- ID: `TEST-COVER-POLICY-OUTCOMES`
- Name: `Cover Policy Outcomes`
- Summary: Test allowed, denied, redacted, fallback, and unsupported policy outcomes.
  Policy value lives at decision boundaries, so assert caller-visible behavior instead of internals.
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Cover allowed, denied, redacted, and fallback behavior in policy tests.

## Why

Policy code is most useful at its decision boundaries: allowed, denied, redacted, fallback,
preserved, and unsupported. Testing only the allowed path misses the cases where security, privacy,
compatibility, or user messaging matters most.

## Helps

- Makes access, privacy, compatibility, and fallback behavior explicit and reviewable.

## Limits

Avoid coupling tests to policy internals. Assert the observable decision, redaction, error, or
fallback that callers rely on.

## Agent Instruction

Cover allowed, denied, redacted, fallback, preserved, and unsupported outcomes in policy tests.

## Mechanisms

Supported by table-driven policy tests, fixtures for each decision class, redaction assertions, and
explicit denied/unsupported error checks.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
