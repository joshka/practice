# Observability Log At Owned Boundaries

## Metadata

- ID: `OBSERVABILITY-LOG-AT-OWNED-BOUNDARIES`
- Status: `reviewed`
- Domain: `observability`
- Depth: `compact`

## Rule

Log at owned boundaries.

## Why

The best diagnostic point is usually where code still knows the operation, caller intent, input
class, and external system boundary. Logging too deep loses purpose; logging too high often loses
the exact provider, resource, or failure state.

## Helps

- Produces logs that identify the responsible operation without duplicating noise at every layer.

## Limits

Avoid logging the same failure at every call frame. Add context as errors cross boundaries, and emit
logs where the owning component can explain the event.

## Agent Instruction

Log at owned boundaries because the best diagnostic point is usually where code still knows the
operation, caller intent, input class, and external system boundary.

## Mechanisms

Supported by adapter-layer logs, structured error context, tracing spans, log-level policy, and
tests that assert important diagnostic fields.

## References

- [Pattern: Log At Owned Boundaries](../../patterns/log-at-owned-boundaries.md)
- [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [OWASP Logging Cheat
  Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
