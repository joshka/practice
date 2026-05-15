# Rust Document Current Implemented Behavior

## Metadata

- ID: `RUST-DOCUMENT-CURRENT-IMPLEMENTED-BEHAVIOR`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Document current implemented Rust behavior, not aspirations.

## Why

Rustdoc and README examples are part of a crate's public contract. If docs describe planned support,
future compatibility, or unimplemented behavior as available API, callers will write code against a
contract the crate does not actually satisfy.

Planned behavior can still be useful, but it should be labeled as scope, roadmap, non-goal, or
future work. Current behavior should be written in present tense and backed by examples or tests
when users are expected to rely on it.

## Helps

- Helps crate docs stay truthful about what users can depend on today.

## Limits

Design documents and tracking issues may describe future work. Keep that material clearly separate
from public API docs that users treat as current behavior.

## Agent Instruction

Write Rust public docs in present tense for implemented behavior; label planned behavior as future
work or scope.

## Mechanisms

Supported by doctests, README/Rustdoc alignment checks, release review, and issue or roadmap links
for planned behavior.

## References

- [Rule: DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION](../documentation/docs-state-current-behavior-not-aspiration.md)
- [Rust API Guidelines: Documentation](https://rust-lang.github.io/api-guidelines/documentation.html)
