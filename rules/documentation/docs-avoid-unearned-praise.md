# Docs Avoid Unearned Praise

## Metadata

- Name: `Avoid Unearned Praise`
- ID: `DOCS-AVOID-UNEARNED-PRAISE`
- Summary: `Replace vague ranking words with observable behavior, evidence, or tradeoffs. Use
  evaluative claims only when the basis is explicit enough for readers to verify.`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Avoid unearned ranking and vague praise.

## Why

Words such as "simple," "powerful," "best," and "easy" are often unearned unless the doc states the
comparison or tradeoff. Vague praise makes a reader ask what was measured, what alternative is
worse, and whether the claim is marketing instead of documentation.

## Helps

- Keeps claims credible and replaces praise with observable behavior, constraints, or tradeoffs.

## Limits

Use evaluative language when the basis is explicit, such as a measured benchmark, a concrete feature
comparison, or a stated design goal. Otherwise prefer the fact that makes the thing useful.

## Agent Instruction

Avoid unearned ranking and vague praise because words such as "simple," "powerful," "best," and "easy"
are often unearned unless the doc states the comparison or tradeoff.

## Mechanisms

Supported by wording review, evidence labels, source-backed comparison tables, and PR review that
asks broad claims to name their basis.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
