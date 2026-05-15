# Observability Surface Durable Failures

## Metadata

- ID: `OBSERVABILITY-SURFACE-DURABLE-FAILURES`
- Legacy ID: `R-0604`
- Status: `reviewed`
- Domain: `observability`
- Depth: `compact`

## Rule

Do not hide durable failures only in UI logs.

## Why

A durable failure that only appears in an ephemeral UI log can disappear before a maintainer or user
can act. Persistent problems such as failed syncs, denied permissions, invalid config, or
background-task failures need a stable status, error surface, or retry path.

## Helps

- Makes persistent failures visible after the immediate UI event is gone.

## Limits

Do not turn transient informational events into permanent alarms. Persist or surface failures that
affect correctness, user action, retry, or support.

## Agent Instruction

Do not hide durable failures only in UI logs because a durable failure that only appears in an
ephemeral UI log can disappear before a maintainer or user can act.

## Mechanisms

Supported by status fields, health checks, background task state, user-visible diagnostics, retry
queues, and logs linked to durable error records.

## References

- [Pattern: Log At Owned Boundaries](../../patterns/log-at-owned-boundaries.md)
- [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [OWASP Logging Cheat
  Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
