# Docs Document Lifecycle And Side Effects

## Metadata

- ID: `DOCS-DOCUMENT-LIFECYCLE-AND-SIDE-EFFECTS`
- Legacy ID: `R-0518`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Document lifecycle, ownership, side effects, feature flags, platform assumptions, and compatibility
when callers need them.

## Why

APIs that open files, spawn tasks, touch terminals, allocate resources, mutate global state, enable
feature flags, or depend on platform behavior create obligations for callers. If those obligations
are not documented, examples can compile while still teaching unsafe cleanup, ownership, or
compatibility assumptions.

## Helps

- Makes caller obligations visible and reduces misuse around runtime, platform, feature, and cleanup
  behavior.

## Limits

Do not narrate internal implementation. Document the lifecycle, side effects, and compatibility
facts a caller must know to use or maintain the API correctly.

## Agent Instruction

Document lifecycle, ownership, side effects, feature flags, platform assumptions, and compatibility
for APIs that create caller obligations.

## Mechanisms

Supported by Rustdoc contract sections, live-resource examples, feature tables, platform notes,
doctests, and integration tests that exercise the documented lifecycle.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
