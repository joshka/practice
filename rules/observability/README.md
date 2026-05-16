# Observability And Failure

Observability rules cover owned logging boundaries, durable failure visibility, diagnostic context,
failure states, and safe telemetry retention.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`OBSERVABILITY-DISTINGUISH-FAILURE-STATES`](observability-distinguish-failure-states.md).
  Preserve status distinctions that change recovery, messaging, metrics, or debugging. Collapsing
  timeouts, denials, aborts, partial work, and failures makes callers guess.
- [`OBSERVABILITY-KEEP-DIAGNOSTICS-RETENTION-SAFE`](observability-keep-diagnostics-retention-safe.md).
  Match diagnostic detail to its audience and retention period. Redact or summarize sensitive values
  while preserving enough operation context to debug.
- [`OBSERVABILITY-LOG-AT-OWNED-BOUNDARIES`](observability-log-at-owned-boundaries.md). Emit logs
  where the code still knows the operation, intent, input class, and external boundary. That
  placement gives useful context without duplicating noise through every layer.
- [`OBSERVABILITY-PRESERVE-OPERATION-CONTEXT-IN-ERRORS`](observability-preserve-operation-context-in-errors.md).
  Carry the operation, resource, provider, input class, and policy context that explain a failure.
  Stable identifiers and sanitized summaries shorten debugging without exposing payloads.
- [`OBSERVABILITY-SURFACE-DURABLE-FAILURES`](observability-surface-durable-failures.md). Give
  persistent failures a stable status, error surface, or retry path instead of only an ephemeral UI
  log. Users and maintainers need something actionable after the moment passes.
