# Test Prove Contracts Not Trivia

## Metadata

- ID: `TEST-PROVE-CONTRACTS-NOT-TRIVIA`
- Name: `Prove Contracts Not Trivia`
- Summary: Write tests around observable contracts instead of private helper trivia.
  This preserves refactoring freedom unless the detail is itself the promised behavior.
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Prove contracts with tests, not implementation trivia.

## Why

Tests that lock down private helper order, incidental formatting, or intermediate variables make
refactoring expensive without proving user-visible behavior. Tests should protect contracts:
outputs, errors, invariants, side effects, and compatibility promises.

## Helps

- Keeps tests useful through refactoring and focused on behavior that matters.

## Limits

Implementation-detail tests are useful when the implementation detail is the contract, such as a
wire format, sort order, allocation guarantee, or documented algorithm property.

## Agent Instruction

Prove contracts with tests, not implementation trivia that makes refactoring expensive without
proving user-visible behavior.

## Mechanisms

Supported by public-surface tests, invariant tests, snapshot review, API examples, and review that
asks what contract each test protects.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
