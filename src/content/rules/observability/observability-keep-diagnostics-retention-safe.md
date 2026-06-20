# Observability Keep Diagnostics Retention Safe

## Metadata

- Name: `Keep Diagnostics Retention Safe`
- ID: `OBSERVABILITY-KEEP-DIAGNOSTICS-RETENTION-SAFE`
- Summary: Match diagnostic detail to its audience and retention period. Redact or summarize
  sensitive values while preserving enough operation context to debug.
- Related: `avoid-secret-or-private-log-context, keep-secrets-out-of-context,
  contain-observability-policy, write-actionable-error-messages`
- Status: `reviewed`
- Domain: `observability`
- Tags: `observability, security-privacy, failure-output`

## Rule

Keep diagnostics safe for their retention boundary.

## Why

Diagnostics that are safe in a local debug log may be unsafe in long-lived telemetry, CI artifacts,
PR comments, or user-visible error reports. Retention and audience determine what values,
identifiers, paths, and payloads can be recorded.

When a visible failure message needs raw detail, prefer a safe diagnostic handle, details
disclosure, support bundle, or redacted summary over exposing sensitive payloads inline.

## Helps

- Keeps debugging useful while reducing privacy, compliance, and accidental disclosure risk.

## Limits

Do not remove all useful context in the name of safety. Redact or summarize sensitive values while
preserving operation, category, and recovery detail.

## Agent Instruction

Keep diagnostics safe for their retention boundary, especially telemetry, CI artifacts, PR comments,
and user-visible reports.

## Mechanisms

Supported by redaction helpers, logging policy, structured fields with safe values, telemetry
review, and tests for secret or PII leaks.

## References

- [Pattern: Log At Owned Boundaries](../../patterns/log-at-owned-boundaries.md)
- [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [OWASP Logging Cheat
  Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
