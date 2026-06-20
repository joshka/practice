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
- [`OBSERVABILITY-KEEP-RECOVERY-ADVICE-SAFE-AND-HONEST`](observability-keep-recovery-advice-safe-and-honest.md).
  Give recovery advice only when the program knows enough to make it safe. Report observed facts,
  label uncertainty, and avoid destructive, security-weakening, or policy-bypassing next steps
  unless the current state proves they are appropriate.
- [`OBSERVABILITY-LOG-AT-OWNED-BOUNDARIES`](observability-log-at-owned-boundaries.md). Emit logs
  where the code still knows the operation, intent, input class, and external boundary. That
  placement gives useful context without duplicating noise through every layer.
- [`OBSERVABILITY-MATCH-FAILURE-OUTPUT-TO-SURFACE`](observability-match-failure-output-to-surface.md).
  Choose a failure-output surface that lets the affected user notice, understand, and act on the
  failure. Inline errors, alerts, toasts, banners, persistent status, CLI stderr, API responses, and
  support artifacts have different affordances and failure modes.
- [`OBSERVABILITY-PRESERVE-OPERATION-CONTEXT-IN-ERRORS`](observability-preserve-operation-context-in-errors.md).
  Carry the operation, resource, provider, input class, and policy context that explain a failure.
  Stable identifiers and sanitized summaries shorten debugging without exposing payloads.
- [`OBSERVABILITY-SURFACE-DURABLE-FAILURES`](observability-surface-durable-failures.md). Give
  persistent failures a stable status, error surface, or retry path instead of only an ephemeral UI
  log. Users and maintainers need something actionable after the moment passes.
