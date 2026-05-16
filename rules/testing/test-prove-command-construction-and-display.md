# Test Prove Command Construction And Display

## Metadata

- ID: `TEST-PROVE-COMMAND-CONSTRUCTION-AND-DISPLAY`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Prove command construction and display behavior in tests.

## Why

Command-building code can be wrong in quoting, argument order, display redaction, environment
handling, or platform formatting while still invoking a happy path locally. Tests should prove both
the executed shape and the displayed shape when users or logs rely on them.

## Helps

- Prevents shell, display, redaction, and platform bugs in command-facing code.

## Limits

Do not assert incidental formatting that callers do not see. Test the command fields, display
string, or redaction contract that matters.

## Agent Instruction

Prove command construction and display behavior in tests because command-building code can be wrong
in quoting, argument order, display redaction, environment handling, or platform formatting while
still invoking a happy path locally.

## Mechanisms

Supported by structured command assertions, golden display output, platform-specific cases,
redaction tests, and no-shell argument-vector tests.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
