# Avoid Secret Or Private Log Context

## Metadata

- Name: `Avoid Secret Or Private Log Context`
- ID: `avoid-secret-or-private-log-context`
- Summary: Diagnostics can outlive their request and move through systems with different access
  rules. Record safe identifiers and classifications at the boundary that understands data
  sensitivity, using explicit protected workflows for rare sensitive evidence.
- Status: `reviewed`
- Audience: `both`
- Topics: `logging, privacy, security`
- Tags: `security-privacy, observability, agent-context`
- Related: `keep-secrets-out-of-context, log-at-owned-boundaries`

## Problem

Logs, traces, metrics, error reports, and agent transcripts can outlive the request that produced
them and move through systems with different access rules. Including secrets, tokens, raw payloads,
private user data, or proprietary context can turn diagnostics into a data leak.

## Preferred Move

Log stable identifiers, classifications, counts, error kinds, and correlation IDs instead of raw
secret or private values. Redact, hash, tokenize, or omit sensitive context at the boundary that
knows the data classification.

## Tradeoff

Some incidents require sensitive evidence. Capture it only through an explicit, access-controlled
workflow with retention and audit expectations. Do not smuggle sensitive data into ordinary logs
because it is convenient during debugging.

## Agent Instruction

When adding diagnostics, classify the context before recording it. Avoid logging secrets, tokens,
raw private payloads, connection strings, source code, or user-sensitive fields; prefer safe
identifiers and redacted summaries.

## Examples

Bad: the log stores the credential-bearing header.

```rust
warn!(
    authorization = %request.authorization_header(),
    "request rejected by auth middleware",
);
```

Good: the log records the decision and correlation fields without the secret.

```rust
warn!(
    request_id = %request.id(),
    auth_scheme = %request.auth_scheme(),
    reason = "expired_token",
    "request rejected by auth middleware",
);
```

## References

| Source                            | Use        | Note                                             |
| --------------------------------- | ---------- | ------------------------------------------------ |
| [OWASP data to exclude][exclude]  | `supports` | Sensitive values should be removed or protected. |
| [OWASP logging vocabulary][vocab] | `adapts`   | Security events need useful but safe context.    |

[exclude]: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#data-to-exclude
[vocab]: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html
