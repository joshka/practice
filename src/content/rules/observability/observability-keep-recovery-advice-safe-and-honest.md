# Observability Keep Recovery Advice Safe And Honest

## Metadata

- Name: `Keep Recovery Advice Safe and Honest`
- ID: `OBSERVABILITY-KEEP-RECOVERY-ADVICE-SAFE-AND-HONEST`
- Summary: Give recovery advice only when the program knows enough to make it safe. Report observed
  facts, label uncertainty, and avoid destructive, security-weakening, or policy-bypassing next
  steps unless the current state proves they are appropriate.
- Related: `write-actionable-error-messages, observability-preserve-operation-context-in-errors,
  observability-keep-diagnostics-retention-safe, boundary-report-provider-diagnostics`
- Status: `draft`
- Domain: `observability`
- Tags: `observability, errors, failure-output, security-privacy`

## Rule

Keep recovery advice safe and honest.

## Why

Helpful-looking messages can create worse failures when they guess the cause or recommend unsafe
actions. If the program only knows that an upstream request failed, a local process exited nonzero,
a plugin returned an error, or a background job stopped, the failure output should make the observed
fact and a safe diagnostic handle available. Do not claim a network issue, permission
problem, invalid credential, or corrupt file unless that is what the program actually observed.
Do not suggest deletion, force flags, credential changes, policy bypasses, broad retries, or access
changes unless the program knows those steps are safe for the current state.

## Helps

- Prevents recovery text from causing data loss, security regressions, policy bypasses, or false
  debugging trails.

## Limits

Do not withhold useful next steps just because they are not guaranteed to work. It is acceptable to
say "retry later" or "check your connection" when that is the safe next action, but distinguish
observed facts from likely causes and avoid presenting guesses as diagnosis.

## Agent Instruction

Give next steps only when the program knows they are safe; otherwise make the observed failure,
uncertainty, and diagnostic handle available for support or debugging.

## Mechanisms

Supported by typed error causes, source chains, retry policy tests, destructive-action guards,
provider diagnostic mapping, redaction checks, bug-report IDs, and review that asks whether the
message observed or guessed the cause.

## References

- [Pattern: Write Actionable Error
  Messages](../../patterns/write-actionable-error-messages.md)
- [NN/g: User Control and
  Freedom](https://www.nngroup.com/articles/user-control-and-freedom/)
- [Microsoft: Error Message
  Guidelines](https://learn.microsoft.com/en-us/windows/win32/debug/error-message-guidelines)
- [Microsoft: Actionable Error
  Messages](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-error-handling-guidelines)
- [GOV.UK Design System: Error
  Message](https://design-system.service.gov.uk/components/error-message/)
- [VA.gov Content Style Guide: Error
  Messages](https://design.va.gov/content-style-guide/error-messages/)
