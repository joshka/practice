# Docs Compare Libraries Accurately

## Metadata

- ID: `DOCS-COMPARE-LIBRARIES-ACCURATELY`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Compare nearby libraries accurately and charitably.

## Why

Comparisons with nearby libraries affect trust. If a doc overstates another crate's weakness,
ignores its current API, or frames a tradeoff unfairly, readers learn that the project is arguing
rather than explaining when to choose which tool.

## Helps

- Makes comparison docs credible and helps users choose based on real constraints instead of
  positioning language.

## Limits

Do not add comparison sections unless users need them. When comparison is useful, compare current
documented behavior, not old memory or private preference.

## Agent Instruction

Compare nearby libraries accurately and charitably; inaccurate comparisons undermine trust.

## Mechanisms

Supported by source checks against upstream docs, dated comparison notes when needed, and review
that asks what claim a user can verify.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
