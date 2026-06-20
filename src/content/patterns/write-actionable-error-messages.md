# Write Actionable Error Messages

## Metadata

- Name: `Write Actionable Error Messages`
- ID: `write-actionable-error-messages`
- Summary: Accurate error messages can still leave users, operators, callers, or support unable to
  act. Design failure output so the audience can find the attempted operation, affected item, known
  cause, impact, next step, and diagnostic handle when those facts matter.
- Status: `reviewed`
- Audience: `both`
- Topics: `errors, documentation, support`
- Tags: `errors, failure-output, public-api`
- Related: `preserve-error-context, test-observable-behavior,
  observability-match-failure-output-to-surface, observability-surface-durable-failures,
  observability-keep-diagnostics-retention-safe,
  observability-keep-recovery-advice-safe-and-honest`

## Problem

An error message can be technically accurate and still leave the audience stuck. Generic failures,
missing causes, vague recovery advice, or absent correlation details create dead ends for users,
callers, operators, and support. The maintainer knows the workflow and source error; the person
seeing the message may only know the operation they attempted and the state the program left behind.

## Preferred Move

Design the failure output for the boundary where it appears. The exact wording, structure, tone,
and component choice are product decisions. The goal is that the audience can find the useful facts
for that boundary:

- What operation was attempted?
- Which item, path, command, package, setting, account, field, or external system was affected?
- What failed or what state changed?
- Why did it happen, when that can be known or honestly inferred?
- What was the impact: blocked, skipped, degraded, fallback, warning-only, or informational?
- What can the user, caller, operator, or support person do next?
- What identifier, raw diagnostic detail, link, or bug-report context can connect the visible
  message to logs or support?

Avoid dead ends. If the immediate audience cannot fix the problem, make the next escalation path or
correlation information available so the visible failure can be connected to diagnostic detail.

Do not treat the checklist as a copy template. A product may express these facts as one sentence,
field-level helper text, a notification body, action labels, a details disclosure, a status record,
structured API fields, or a support bundle. The guidance is about which information should be
available, not the prose shape used to present it.

Use [Match Failure Output To Surface][surface] for where and how the message should appear. Use
[Surface Durable Failures][durable] when a transient message is not enough. Use [Keep Recovery
Advice Safe and Honest][safe-recovery] when the cause or next step is uncertain or risky. Use [Keep
Diagnostics Retention Safe][retention] when raw details, logs, support artifacts, or telemetry may
cross access boundaries.

## Tradeoff

When the state is obvious, a single precise line can be better than verbose prose. Add impact, next
step, or diagnostic detail when it changes what the audience should do next or what a maintainer can
diagnose later.

User-facing messages should not expose sensitive, noisy, or unstable internals. Keep private detail
in logs, admin surfaces, or debugging context, but carry enough concrete context in the visible
message for someone to make progress.

## Agent Instruction

When changing an error, warning, or diagnostic message, make sure the audience can find the
attempted operation, affected item, changed state or failure, known impact, safe next step, and
support diagnostic handle when those facts matter. Keep obvious states concise, and do not replace
useful diagnostics with friendly but dead-end prose.

## Review Checklist

Use this checklist when reviewing the content of user-facing errors, warnings, and diagnostics:

- Does the message name the attempted operation rather than only the low-level failure?
- Does it identify the affected path, command, package, setting, account, field, provider, or
  external system?
- Does it say what failed or what state changed in terms the target audience understands?
- Does it explain why only when the program actually knows why?
- Does it distinguish blocked, skipped, degraded, fallback, warning-only, and informational states?
- Does it give a safe next step when one is known?
- Does it preserve command output, correlation IDs, raw diagnostics, bug-report details, or links
  when the visible message alone is not enough?
- Does it avoid dead-end phrases such as "failed", "not installed", or "invalid" when the
  operation-specific consequence is known?
- Does it avoid over-correcting into prose that repeats obvious state or hides the important noun?

## Illustrative Examples

These examples show missing and present information, not required copy style.

Bad: the message says the operation failed but gives the user no next step or diagnostic handle.

```text
Something went wrong.
```

Good: the message names the failed action, gives a next step, and includes a support correlation
identifier.

```text
We could not import contacts.csv because the email column is missing. Add an email column and try
again. If this keeps failing, contact support with request ID req_123.
```

Bad: the message reports an installed-state fact but hides the operation-specific consequence.

```text
foo is not installed.
```

Good: the message connects the missing dependency to the attempted operation and gives a safe next
step.

```text
Could not build docs because `foo` is not installed.
Next: install `foo` or rerun with `--no-diagrams` to skip diagram generation.
```

Bad: the message points at the user instead of the affected field and recovery path.

```text
Invalid input.
```

Good: the message names the field, the rule, and the fix.

```text
Expiration date must be after today's date. Enter a later date to schedule the report.
```

## References

| Source                       | Use        | Note                                                                  |
| ---------------------------- | ---------- | --------------------------------------------------------------------- |
| [NN/g Error Guidelines]      | `supports` | Error messages should be visible, constructive, precise, and concise. |
| [NN/g Error Rubric]          | `adapts`   | Useful review dimensions: visibility, communication, and efficiency.  |
| [NN/g Heuristics]            | `supports` | Users need to recognize, diagnose, recover, and stay informed.        |
| [Microsoft Error Guidelines] | `supports` | Name what happened, why, the user impact, and a solution.             |
| [GOV.UK Error Message]       | `supports` | State what went wrong, keep input, and write specific fixes.          |
| [VA.gov Error Messages]      | `supports` | Use clear direct messages with a concrete call to action.             |

[durable]: ../rules/observability/observability-surface-durable-failures.md
[GOV.UK Error Message]: https://design-system.service.gov.uk/components/error-message/
[Microsoft Error Guidelines]: https://learn.microsoft.com/en-us/windows/win32/debug/error-message-guidelines
[NN/g Error Guidelines]: https://www.nngroup.com/articles/error-message-guidelines/
[NN/g Error Rubric]: https://www.nngroup.com/articles/error-messages-scoring-rubric/
[NN/g Heuristics]: https://www.nngroup.com/articles/ten-usability-heuristics/
[retention]: ../rules/observability/observability-keep-diagnostics-retention-safe.md
[safe-recovery]: ../rules/observability/observability-keep-recovery-advice-safe-and-honest.md
[surface]: ../rules/observability/observability-match-failure-output-to-surface.md
[VA.gov Error Messages]: https://design.va.gov/content-style-guide/error-messages/
