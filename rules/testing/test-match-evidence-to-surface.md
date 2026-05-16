# Test Match Evidence To Surface

## Metadata

- ID: `TEST-MATCH-EVIDENCE-TO-SURFACE`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Match validation evidence to the changed surface.

## Why

A change to rendered docs, terminal layout, parser output, public API, or performance needs evidence
from that surface. A unit test may prove local logic while failing to show that the actual
user-facing page, screen, byte output, or API still works.

## Helps

- Makes validation persuasive because the proof matches what changed.

## Limits

Do not run every possible surface check for every edit. Pick the narrowest evidence that would catch
the likely failure.

## Agent Instruction

Match validation evidence to the changed surface because a change to rendered docs, terminal layout,
parser output, public API, or performance needs evidence from that surface.

## Mechanisms

Supported by doctests, snapshots, screenshots, integration tests, byte-level assertions, benchmark
output, rendered docs, and command-output fixtures.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
