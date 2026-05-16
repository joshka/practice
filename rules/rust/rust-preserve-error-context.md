# Rust Preserve Error Context

## Metadata

- Name: `Preserve Error Context`
- ID: `RUST-PRESERVE-ERROR-CONTEXT`
- Summary: Wrap and model errors so callers can see the operation, relevant input, source cause, and
  recovery signal. Avoid flattening failures into broad strings or generic variants that remove
  actionable context.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Preserve enough Rust error context for callers to act.

## Why

Mapping every failure to a broad string or generic variant loses the operation, input, source
error, and recovery signal. Reusable crates need stable error kinds and recoverable context so
callers can log, retry, report, or branch correctly.

The standard `Error` trait supports source chaining because the visible error and the underlying
cause often answer different questions. Preserve both levels when wrapping failures: the outer error
should name the operation or domain failure, while the source should keep lower-level diagnostic
detail.

## Helps

- Helps callers diagnose failures and preserve error chains without depending on private details.

## Limits

Applications may use broader error wrappers at outer boundaries. Public library errors should still
surface intentional categories and useful context. Avoid exposing unstable private error types just
to keep every detail typed.

## Agent Instruction

Preserve Rust error source, operation, and recoverable context while wrapping or mapping failures.

## Mechanisms

Supported by `std::error::Error::source`, error enum review, invalid-input tests, and snapshot
review for visible messages.

## References

- [Rust standard library: Error](https://doc.rust-lang.org/std/error/trait.Error.html)
- [Rust API Guidelines: Function docs include error, panic, and safety
  considerations](https://rust-lang.github.io/api-guidelines/documentation.html#c-failure)
- [Pattern: Preserve Error Context](../../patterns/preserve-error-context.md)
