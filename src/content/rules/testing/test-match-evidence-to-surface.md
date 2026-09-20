# Test Match Evidence To Surface

## Metadata

- ID: `TEST-MATCH-EVIDENCE-TO-SURFACE`
- Name: `Match Evidence to Surface`
- Summary: Validate the actual changed surface, such as rendered docs, API behavior, or byte output.
  The narrowest relevant proof is more persuasive than unrelated broad test success.
- Status: `reviewed`
- Domain: `testing`
- Tags: `testing, verification, reviewability`
- Related: `smallest-trustworthy-verification, report-verification-honestly`

## Rule

Match validation evidence to the changed surface.

## Why

A change to rendered docs, terminal layout, parser output, public API, or performance needs evidence
from that surface. A unit test may prove local logic while failing to show that the actual
user-facing page, screen, byte output, or API still works.

For UI changes, exercise a complete user task in the built application. Check the relevant loading,
success, empty, failure, cancellation, and recovery states. Inspect layout with realistic content,
window sizes, appearances, selection, and keyboard focus where those affect the changed workflow.
Screenshots show appearance; interaction and state transitions need their own checks. A source
field for a progress value does not prove that users can see it while work is running.

For release artifacts, inspect and exercise the packaged output when packaging is in scope.
Checkout tests cannot establish that fixtures, assets, or linked documentation reached the archive.

## Helps

- Makes validation persuasive because the proof matches what changed.

## Limits

Do not run every possible surface check for every edit. Pick the narrowest evidence that would catch
the likely failure.

## Agent Instruction

Validate the changed surface directly: exercise UI workflows in the built app, check consumer
configurations for API changes, and inspect packaged output for release changes. State what each
check proves; passing local tests does not establish product acceptance.

## Mechanisms

Supported by doctests, snapshots, screenshots, integration tests, byte-level assertions, benchmark
output, rendered docs, and command-output fixtures.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
