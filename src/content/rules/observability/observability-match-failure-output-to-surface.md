# Observability Match Failure Output To Surface

## Metadata

- Name: `Match Failure Output To Surface`
- ID: `OBSERVABILITY-MATCH-FAILURE-OUTPUT-TO-SURFACE`
- Summary: Choose a failure-output surface that lets the affected user notice, understand, and act
  on the failure. Inline errors, alerts, toasts, banners, persistent status, CLI stderr, API
  responses, and support artifacts have different affordances and failure modes.
- Related: `write-actionable-error-messages, observability-surface-durable-failures,
  observability-keep-diagnostics-retention-safe, test-prove-command-construction-and-display`
- Status: `draft`
- Domain: `observability`
- Tags: `observability, errors, failure-output`

## Rule

Match failure output to the product surface and consequence.

## Why

The same failure can need different presentation on different surfaces. A field validation error is
usually more useful near the field. A background sync failure may need a persistent status row. A
destructive desktop operation may need an alert, an action, and details. A CLI diagnostic may need
stderr and a meaningful exit state, while machine-readable stdout remains stable for scripts. These
are product decisions, not universal component rules. If the output is too far from the affected
item, too transient, inaccessible, or mixed into the wrong channel, the message can be accurate and
still unusable.

## Helps

- Makes user-facing failures discoverable, actionable, accessible, and compatible with automation.

## Limits

Do not make every failure modal, persistent, or verbose. Let the product context and consequence set
the surface: transient informational events can stay lightweight, while failures that block work,
change saved state, require retry, affect support, or become script contracts usually need more
durable or structured presentation.

## Agent Instruction

Choose the failure surface by consequence and product context. Verify that fixable, durable,
interactive, command-line, API, and support-facing failures expose the needed information where the
affected audience can actually use it.

## Mechanisms

Supported by UI component guidelines, accessibility checks, end-to-end tests for visible recovery,
CLI stdout/stderr and exit-code tests, API problem-detail schemas, support-report fields, and
review that names the surface where the failure appears.

## References

- [Pattern: Write Actionable Error
  Messages](../../patterns/write-actionable-error-messages.md)
- [NN/g: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [NN/g: 10 Design Guidelines for Reporting Errors in
  Forms](https://www.nngroup.com/articles/errors-forms-design-guidelines/)
- [NN/g: Status Trackers and Progress
  Updates](https://www.nngroup.com/articles/status-tracker-progress-update/)
- [NN/g: Why So Many Info Tips Are Bad](https://www.nngroup.com/articles/info-tips-bad/)
- [Carbon Design System: Notifications](https://carbondesignsystem.com/components/notification/usage/)
- [Command Line Interface Guidelines](https://clig.dev/)
- [Fuchsia CLI Guidelines](https://fuchsia.dev/fuchsia-src/development/api/cli)
- [Microsoft .NET CLI Design
  Guidance](https://learn.microsoft.com/en-us/dotnet/standard/commandline/design-guidance)
- [Rustc Dev Guide:
  Diagnostics](https://rustc-dev-guide.rust-lang.org/diagnostics.html)
- [Clang Internals: Diagnostics
  Subsystem](https://clang.llvm.org/docs/InternalsManual.html#the-diagnostics-subsystem)
