# Boundary Make Policy Boundaries Explicit

## Metadata

- Name: `Make Policy Boundaries Explicit`
- ID: `BOUNDARY-MAKE-POLICY-BOUNDARIES-EXPLICIT`
- Summary: Route writes, network calls, shell execution, publication, telemetry, redaction, and
  credential use through a visible policy decision before effects run. Callers can then understand
  allowed, denied, redacted, fallback, preserved, and unsupported outcomes.
- Status: `reviewed`
- Domain: `boundary`
- Tags: `boundary-correctness, validation-policy, side-effects, security-privacy`
- Related: `make-validation-policy-explicit, contain-observability-policy, prove-security-impact`

## Rule

Route policy-sensitive side effects through an explicit policy boundary.

## Why

Filesystem writes, network calls, shell execution, external publication, telemetry, redaction,
credential use, and user-visible changes can be technically valid while still being disallowed for
the current actor, profile, environment, or approval state. If the policy decision is hidden inside
the effectful operation, callers cannot predict whether the operation will run, be denied, be
redacted, fall back, or require approval.

An explicit policy boundary gives the operation a visible decision point before the side effect
happens. It also gives tests and logs a stable place to prove allowed, denied, redacted, fallback,
preserved, and unsupported outcomes.

## Helps

- Makes access, privacy, publication, and approval decisions reviewable before side effects run.
- Gives callers actionable denial, redaction, fallback, and approval behavior.

## Limits

Do not build a policy framework for a tiny internal helper with no meaningful external effect. Use
this rule when the operation touches external systems, durable state, secrets, user-visible output,
or resources controlled by a caller, profile, organization, or security boundary.

## Agent Instruction

Route policy-sensitive side effects through an explicit policy boundary before execution, and make
allowed, denied, redacted, fallback, preserved, and unsupported outcomes visible to callers.

## Mechanisms

Supported by policy objects, authorization checks, approval gates, redaction helpers, dry-run modes,
typed denial errors, audit logs, and policy-outcome tests.

## References

- [Boundary Give Tools Identity Policy And Limits](boundary-give-tools-identity-policy-and-limits.md)
- [Test Cover Policy Outcomes](../testing/test-cover-policy-outcomes.md)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP Developer Guide: Enforce Access Controls](https://devguide.owasp.org/en/04-design/02-web-app-checklist/07-access-controls/)
