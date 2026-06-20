# Test Prove Contracts Not Trivia

## Metadata

- ID: `TEST-PROVE-CONTRACTS-NOT-TRIVIA`
- Name: `Prove Contracts Not Trivia`
- Summary: Write tests around observable contracts instead of private helper trivia.
  This preserves refactoring freedom unless the detail is itself the promised behavior, such as a
  stable user-facing output contract.
- Status: `reviewed`
- Domain: `testing`
- Tags: `testing, public-api, verification`
- Related: `test-observable-behavior, tests-should-explain-failures,
  write-actionable-error-messages`

## Rule

Prove contracts with tests, not implementation trivia.

## Why

Tests that lock down private helper order, incidental formatting, or intermediate variables make
refactoring expensive without proving user-visible behavior. Tests should protect contracts:
outputs, errors, invariants, side effects, and compatibility promises.

For user-facing error messages, test the stable facts users and callers rely on: operation, affected
item, impact classification, recovery affordance, diagnostic handle, and machine-readable contract.
Avoid freezing full prose unless exact wording is the public contract.

## Helps

- Keeps tests useful through refactoring and focused on behavior that matters.

## Limits

Implementation-detail tests are useful when the implementation detail is the contract, such as a
wire format, sort order, allocation guarantee, documented algorithm property, exact CLI output, or
localized UI copy that must not drift.

## Agent Instruction

Prove contracts with tests, not implementation trivia that makes refactoring expensive without
proving user-visible behavior.

## Mechanisms

Supported by public-surface tests, invariant tests, targeted message assertions, snapshot review,
API examples, and review that asks what contract each test protects.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
