# Observability Distinguish Failure States

## Metadata

- ID: `OBSERVABILITY-DISTINGUISH-FAILURE-STATES`
- Legacy ID: `R-0603`
- Status: `reviewed`
- Domain: `observability`
- Depth: `compact`

## Rule

Distinguish partial, aborted, timed-out, denied, failed, and completed states.

## Why

A timeout, permission denial, user abort, partial write, and provider failure need different
recovery paths. Collapsing them into one generic error makes retry logic, support messages, and
incident review guess at what actually happened.

## Helps

- Improves retry behavior, user support, and post-failure diagnosis.

## Limits

Do not expose internal state distinctions that callers cannot act on. Preserve distinctions that
change recovery, messaging, metrics, or debugging.

## Agent Instruction

Distinguish partial, aborted, timed-out, denied, failed, and completed states because they need
different recovery paths.

## Mechanisms

Supported by typed errors, explicit status enums, structured logs, retry policy tests, and metrics
that keep terminal states distinct.

## References

- [Pattern: Log At Owned Boundaries](../../patterns/log-at-owned-boundaries.md)
- [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [OWASP Logging Cheat
  Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
