# Preserve Error Context

## Metadata

- Name: `Preserve Error Context`
- ID: `preserve-error-context`
- Summary: Errors often lose the facts a caller needs when they cross module, process, support, or
  user boundaries. Preserve stable kinds and actionable context so callers can retry, report,
  recover, or correlate the failure without parsing generic text.
- Status: `reviewed`
- Audience: `both`
- Topics: `errors, boundaries, review`
- Related: `write-actionable-error-messages, test-observable-behavior`

## Problem

Errors often lose the facts a caller needs when they cross a function, module, process, support, or
user boundary. A specific failure becomes a generic string, source errors disappear, diagnostic
identifiers are dropped, or the caller must parse text to decide whether to retry, report, or
recover.

## Preferred Move

Carry the stable error kind and recoverable context across the boundary. Preserve facts such as the
field name, resource ID, upstream status, retry hint, correlation ID, or source error when those
facts help someone act.

Pair this with [Write Actionable Error Messages](write-actionable-error-messages.md) when the
visible message itself needs user, operator, or support guidance.

## Tradeoff

Not every internal detail should become public contract. Keep sensitive, noisy, or unstable
diagnostics out of public error shapes and put them in logs, admin surfaces, or debugging context
instead. Do not hide the only useful fact in logs when the caller needs that fact to recover.

## Agent Instruction

When mapping or wrapping errors, preserve the stable kind and actionable context. Do not replace a
specific failure with a generic string unless callers truly cannot act on the detail.

## Examples

Bad: the error shape cannot carry the field or source error.

```rust
pub enum ApiError {
    BadRequest(String),
}
```

Good: the error shape preserves the stable kind and the field the caller can fix.

```rust
pub enum ApiError {
    MissingField {
        field: &'static str,
        source: ParseError,
    },
}
```

## References

| Source                | Use        | Note                                                 |
| --------------------- | ---------- | ---------------------------------------------------- |
| [Rust API][rust-api]  | `supports` | Error types should be meaningful and well-behaved.   |
| [Microsoft][ms]       | `adapts`   | Error structs can carry upstream causes and context. |

[rust-api]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-good-err
[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-ERRORS-CANONICAL-STRUCTS
