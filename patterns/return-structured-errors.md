# Return Structured Errors

## Metadata

- Name: `Return Structured Errors`
- ID: `return-structured-errors`
- Summary: String-only errors hide the stable facts callers need for branching, retrying, logging,
  and support. Return structured error values with machine-readable kinds and context, then render
  audience-specific messages at the boundary.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, errors, api-design`
- Related: `preserve-error-context, write-actionable-error-messages`

## Problem

String errors and broad catch-all errors make callers parse prose or give up. The user-visible
message may be good enough for a person, but code still needs a stable kind, recoverable fields,
source error, and sometimes a correlation or instance identifier.

## Preferred Move

Return errors with structure at API boundaries. Use enums, structs, problem-detail objects, error
kinds, source chains, and typed fields so callers can branch, retry, show useful messages, or attach
support context without parsing text.

## Tradeoff

Applications can aggregate errors internally when no caller can act on the variants. Reusable
libraries and public service boundaries should not expose only `anyhow::Error`, `String`, or
unstructured JSON when callers need stable behavior.

## Agent Instruction

When designing an error boundary, include stable error kind, actionable fields, source context, and
correlation or instance identity when needed. Keep display text helpful, but do not make prose the
only machine-readable contract.

## Examples

Bad: callers can only inspect text.

```rust
pub fn load_pattern(id: PatternId) -> Result<Pattern, String> {
    repository::load(id).map_err(|err| format!("could not load pattern: {err}"))
}
```

Good: callers can match the kind and preserve the source.

```rust
pub enum LoadPatternError {
    NotFound { id: PatternId },
    Repository { id: PatternId, source: RepositoryError },
}

pub fn load_pattern(id: PatternId) -> Result<Pattern, LoadPatternError> {
    repository::load(id).map_err(|source| LoadPatternError::Repository { id, source })
}
```

## References

| Source                    | Use        | Note                                                     |
| ------------------------- | ---------- | -------------------------------------------------------- |
| [C-GOOD-ERR][rust-error]  | `supports` | Error types should be meaningful and well-behaved.       |
| [RFC 9457][problem]       | `adapts`   | HTTP APIs can expose machine-readable problem details.   |

[problem]: https://www.rfc-editor.org/rfc/rfc9457.html
[rust-error]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-good-err
