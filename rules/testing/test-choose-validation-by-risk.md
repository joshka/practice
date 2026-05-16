# Test Choose Validation By Risk

## Metadata

- ID: `TEST-CHOOSE-VALIDATION-BY-RISK`
- Name: `Choose Validation by Risk`
- Summary: Match the amount and kind of validation to the changed surface and failure cost.
  Cheap checks come first, but risky or uncertain behavior needs targeted evidence.
- Status: `reviewed`
- Domain: `testing`
- Tags: `testing, verification, validation-policy, reviewability`
- Related: `smallest-trustworthy-verification, review-proof-not-just-code`

## Rule

Choose validation by risk.

## Why

Different changes need different proof. A typo may need markdown lint; a parser change may need
fixtures and fuzzing; a public API change may need doctests, integration tests, and semver checks.
Validation should match the surface and failure cost.

## Helps

- Avoids both under-testing risky work and over-testing low-risk edits.

## Limits

When risk is uncertain, run the cheap checks first and add targeted checks around the uncertainty.
Do not use a broad test suite as a substitute for thinking about the specific risk.

## Agent Instruction

Choose validation by risk because different changes need different proof.

## Mechanisms

Supported by validation plans, risk-based PR checklists, focused test commands, skipped-check notes,
and rule-specific mechanisms.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
