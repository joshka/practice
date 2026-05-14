# Observability And Failure

Status: `reviewed`

This guide collects preferences for Rust and service boundaries where failures need to be
understandable after the fact. Use it with [Boundary Correctness][boundary],
[Markdown And Documentation][docs], and [Software Change Preferences][change].

Failure handling is not only about returning the right type. A good failure path preserves what the
caller can act on and records enough safe context for the owner of the operation to diagnose what
happened.

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

## Rust API Shape

Reusable Rust libraries should expose errors that downstream code can reason about. Application
boundaries can aggregate errors for reporting, but library and service contracts should not force
callers to parse prose, inspect broad dynamic errors, or depend on private logging side effects.

Prefer enum or struct errors with owned context and source errors where useful. Keep display text
human-readable, but make the stable contract the type and fields. For HTTP-style boundaries,
machine-readable problem details can carry the external contract while internal errors preserve
source context.

## Review Questions

- Who needs to act on this failure: caller, operator, support person, maintainer, or user?
- Does the error type preserve a stable kind, useful fields, and source context?
- Which boundary owns the operation and has enough context to log or count it?
- Will this failure be logged once with correlation fields, or repeatedly as it bubbles up?
- Are logs, metrics, traces, and error reports safe for their retention and access rules?
- Could a caller recover, retry, branch, or show a useful message without parsing prose?
- Does documentation name important failure, panic, safety, or recovery contracts?

[boundary]: boundary-correctness.md
[change]: software-change-preferences.md
[docs]: markdown-documentation.md
[observable-failures]: ../patterns/make-failures-observable.md
[observability-policy]: ../patterns/contain-observability-policy.md
[owned-logs]: ../patterns/log-at-owned-boundaries.md
[private-log-context]: ../patterns/avoid-secret-or-private-log-context.md
[structured-errors]: ../patterns/return-structured-errors.md
