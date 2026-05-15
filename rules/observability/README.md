# Observability And Failure

Observability rules cover owned logging boundaries, durable failure visibility, diagnostic context,
failure states, and safe telemetry retention.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`OBSERVABILITY-DISTINGUISH-FAILURE-STATES`](observability-distinguish-failure-states.md).
  Distinguish partial, aborted, timed-out, denied, failed, and completed states. A timeout,
  permission denial, user abort, partial write, and provider failure need different recovery paths.
  Helps: Improves retry behavior, user support, and post-failure diagnosis.
- [`OBSERVABILITY-KEEP-DIAGNOSTICS-RETENTION-SAFE`](observability-keep-diagnostics-retention-safe.md).
  Keep diagnostics safe for their retention boundary. Diagnostics that are safe in a local debug log
  may be unsafe in long-lived telemetry, CI artifacts, PR comments, or user-visible error reports.
  Helps: Keeps debugging useful while reducing privacy, compliance, and accidental disclosure risk.
- [`OBSERVABILITY-LOG-AT-OWNED-BOUNDARIES`](observability-log-at-owned-boundaries.md). Log at owned
  boundaries. The best diagnostic point is usually where code still knows the operation, caller
  intent, input class, and external system boundary. Helps: Produces logs that identify the
  responsible operation without duplicating noise at every layer.
- [`OBSERVABILITY-PRESERVE-OPERATION-CONTEXT-IN-ERRORS`](observability-preserve-operation-context-in-errors.md).
  Preserve operation context in errors. An error such as "not found" or "permission denied" is
  rarely enough. Helps: Shortens debugging by carrying the missing operation and resource context
  with the failure.
- [`OBSERVABILITY-SURFACE-DURABLE-FAILURES`](observability-surface-durable-failures.md). Do not hide
  durable failures only in UI logs. A durable failure that only appears in an ephemeral UI log can
  disappear before a maintainer or user can act. Helps: Makes persistent failures visible after the
  immediate UI event is gone.
