# Observability Preserve Operation Context In Errors

## Metadata

- Name: `Preserve Operation Context in Errors`
- ID: `OBSERVABILITY-PRESERVE-OPERATION-CONTEXT-IN-ERRORS`
- Summary: Carry the operation, resource, provider, input class, and policy context that explain a
  failure. Stable identifiers and sanitized summaries shorten debugging without exposing payloads.
- Status: `reviewed`
- Domain: `observability`
- Depth: `compact`

## Rule

Preserve operation context in errors.

## Why

An error such as "not found" or "permission denied" is rarely enough. The next maintainer needs to
know the operation, resource identity, provider, input class, and relevant policy so they can tell
whether the bug is data, configuration, permissions, or code.

## Helps

- Shortens debugging by carrying the missing operation and resource context with the failure.

## Limits

Do not attach sensitive payloads or huge values. Prefer stable identifiers, categories, and
sanitized summaries.

## Agent Instruction

Preserve operation context in errors because an error such as "not found" or "permission denied" is
rarely enough.

## Mechanisms

Supported by error enums, context wrappers, `Display` implementations, structured diagnostics, and
regression tests for error messages where callers rely on them.

## References

- [Pattern: Log At Owned Boundaries](../../patterns/log-at-owned-boundaries.md)
- [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [OWASP Logging Cheat
  Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
