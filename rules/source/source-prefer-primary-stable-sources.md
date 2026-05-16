# Source Prefer Primary Stable Sources

## Metadata

- ID: `SOURCE-PREFER-PRIMARY-STABLE-SOURCES`
- Status: `reviewed`
- Domain: `source`
- Depth: `compact`

## Rule

Prefer primary or stable sources for durable guidance.

## Why

External references are most useful when they help a reader verify, compare, or challenge a rule.
For Rust guidance, that usually means sources such as the Rust API Guidelines, Rust Book, official
Cargo or rustdoc docs, Microsoft Pragmatic Rust Guidelines, or Ed Page's Rust and PR style notes.
Private repos, local paths, and transient session notes should not be the evidence a public rule
depends on.

## Helps

- Makes rules easier to audit, easier to justify in review, and less dependent on private memory.

## Limits

Not every preference has a good external source. Use citations to clarify or contrast an idea, not
to outsource judgment or decorate a rule that is intentionally local.

## Agent Instruction

Use primary or stable sources because a reader needs to verify, compare, or challenge durable guidance.

## Mechanisms

Supported by source-link review, internal link checks, stale-reference searches, and reference
tables that state whether this repo supports, adapts, or intentionally differs from a source.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Rust API Guidelines: public APIs are stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
- [Microsoft Pragmatic Rust Guidelines: prefer simple abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
