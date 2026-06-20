# Observability And Failure

## Metadata

- Name: `Observability And Failure`
- ID: `observability-and-failure`
- Summary: Observability and failure guidance covers Rust and service boundaries where failures
  need to be understandable after the fact. It favors structured errors, owned logging boundaries,
  distinct failure states, safe diagnostics, and enough context for the owner to act.
- Status: `reviewed`
- Audience: `both`
- Topics: `observability, errors, logging, diagnostics, privacy`
- Tags: `observability, errors, failure-output, security-privacy`
- Related: `tests-should-explain-failures, make-failures-observable,
  contain-observability-policy`

This guide collects preferences for Rust and service boundaries where failures need to be
understandable after the fact. Use it with [Boundary Correctness][boundary],
[Markdown And Documentation][docs], and [Software Change Preferences][change].

Failure handling is not only about returning the right type. A good failure path preserves what the
caller can act on and records enough safe context for the owner of the operation to diagnose what
happened.

When a failure reaches a user, operator, support person, or reviewer, the visible output is part of
the product surface. Use [Write Actionable Error Messages][actionable-errors] when an error,
warning, or diagnostic needs to name the attempted operation, affected item, impact, next step, and
support handle without becoming verbose prose. Use [Match Failure Output To Surface][surface-output]
when the decision is where and how the failure should appear. Use [Keep Recovery Advice Safe and
Honest][safe-recovery] when the cause, retry path, or suggested next step could be guessed or risky.

## Core Preference

Prefer failure paths that preserve structure for callers and produce useful diagnostic signals at
owned boundaries. Do not make people reconstruct the operation, input class, source error, or
correlation trail from a generic message.

Use [Return Structured Errors][structured-errors] when callers need stable error kinds, fields,
source chains, or problem details. Use [Make Failures Observable][observable-failures] when a
failure crosses a caller, operator, support, or production boundary and needs a diagnostic trail.

## Boundary Ownership

Observability policy belongs where the operation is owned. Request handlers, job runners, CLI
commands, persistence adapters, and domain services often know the useful operation name, retry
context, correlation ID, tenant or resource identity, and redaction rules.

Use [Contain Observability Policy][observability-policy] when helpers are deciding log severity,
metrics names, tracing shape, sampling, or redaction without owning the workflow. Use
[Log At Owned Boundaries][owned-logs] when the same failure would otherwise be logged by multiple
layers.

## Privacy And Diagnostic Context

Diagnostics move farther than the request that created them. Logs, traces, metrics, crash reports,
support bundles, CI artifacts, and agent transcripts can all cross access boundaries.

Use [Avoid Secret Or Private Log Context][private-log-context] before recording raw payloads,
headers, source snippets, tokens, connection strings, user data, or proprietary context. Prefer safe
identifiers, classifications, counts, and correlation fields.

Use [Keep Diagnostics Retention Safe][retention-safe] when logs, traces, metrics, crash reports, CI
artifacts, support bundles, or agent transcripts cross access or retention boundaries. This includes
deciding whether raw detail belongs inline, behind a details disclosure, in a support bundle, or only
in redacted diagnostic records.

## Rust API Shape

Reusable Rust libraries should expose errors that downstream code can reason about. Application
boundaries can aggregate errors for reporting, but library and service contracts should not force
callers to parse prose, inspect broad dynamic errors, or depend on private logging side effects.

Prefer enum or struct errors with owned context and source errors where useful. Keep display text
human-readable, but make the stable contract the type and fields. For HTTP-style boundaries,
machine-readable problem details can carry the external contract while internal errors preserve
source context.

Use [Preserve Operation Context In Errors][operation-context] when an error needs the operation,
resource, input class, or source chain to stay useful after it crosses a boundary.

For event-driven or agentic systems, diagnostics are part of the durable state model. Tool failures,
provider stream failures, policy denials, reload failures, replay rejection, compaction failures,
resource load failures, and startup repair should emit structured diagnostics that include safe
provenance and enough operation context to reproduce or explain the failure.

Partial, aborted, timed-out, denied, failed, and completed are different states. Model them
explicitly when downstream code, replay, support, or UI rendering must distinguish them.

Do not hide failures only in UI logs. If a UI, worker, or extension observes a failure that changes
durable system state, the core event or diagnostic stream should carry that fact.

Use [Distinguish Failure States][failure-states] and [Surface Durable
Failures][durable-failures] when retry, support, replay, UI, or background-task behavior depends on
the exact failure state.

## Related Guidance

Use [Observability Rules][observability-rules] for compact failure, logging, diagnostic context, and
retention instructions. Use [Boundary Rules][boundary-rules] when failure state crosses parsing,
provider, async, tool, or state-transition boundaries. Use [Testing And Benchmarking][test-mechanism]
when diagnostics need proof from integration tests, fixtures, or replay cases.

## Review Questions

### Failure Contract

- Who needs to act on this failure: caller, operator, support person, maintainer, or user?
- Does the error type preserve a stable kind, useful fields, and source context?
- Which boundary owns the operation and has enough context to log or count it?
- Will this failure be logged once with correlation fields, or repeatedly as it bubbles up?

### Diagnostics

- Are logs, metrics, traces, and error reports safe for their retention and access rules?
- Could a caller recover, retry, branch, or show a useful message without parsing prose?
- Does the visible failure output appear on the right surface for that audience and consequence?
- Is the suggested recovery step based on observed state rather than a guessed cause?
- Does documentation name important failure, panic, safety, or recovery contracts?
- Are partial, aborted, timed-out, denied, failed, and completed states distinguishable?
- Are diagnostics durable enough for replay, support, or future debugging without exposing secrets?

[boundary]: boundary-correctness.md
[boundary-rules]: ../rules/boundary/README.md
[change]: software-change-preferences.md
[actionable-errors]: ../patterns/write-actionable-error-messages.md
[docs]: markdown-documentation.md
[durable-failures]: ../rules/observability/observability-surface-durable-failures.md
[failure-states]: ../rules/observability/observability-distinguish-failure-states.md
[observable-failures]: ../patterns/make-failures-observable.md
[observability-rules]: ../rules/observability/README.md
[observability-policy]: ../patterns/contain-observability-policy.md
[operation-context]: ../rules/observability/observability-preserve-operation-context-in-errors.md
[owned-logs]: ../patterns/log-at-owned-boundaries.md
[private-log-context]: ../patterns/avoid-secret-or-private-log-context.md
[retention-safe]: ../rules/observability/observability-keep-diagnostics-retention-safe.md
[safe-recovery]: ../rules/observability/observability-keep-recovery-advice-safe-and-honest.md
[structured-errors]: ../patterns/return-structured-errors.md
[surface-output]: ../rules/observability/observability-match-failure-output-to-surface.md
[test-mechanism]: ../mechanisms/testing-and-benchmarking.md
