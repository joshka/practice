# Docs Avoid Generated Prose Tells

## Metadata

- ID: `DOCS-AVOID-GENERATED-PROSE-TELLS`
- Legacy ID: `R-0513`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Avoid generated-prose tells.

## Why

Generated prose often sounds polished while hiding that it did not learn the project voice. Phrases
such as "seamless," "robust," repeated summary sentences, teaching-order narration, and generic
contrast language make technical docs feel less trustworthy because they avoid naming the concrete
behavior.

## Helps

- Preserves local voice, keeps docs dense, and makes claims easier to verify.

## Limits

Do not remove useful friendliness or explanation just because a sentence is smooth. Cut the
generated tell when it replaces concrete behavior, evidence, or tradeoff language.

## Agent Instruction

Avoid generated-prose tells because generated prose often sounds polished while hiding that it did not
learn the project voice.

## Mechanisms

Supported by prose review passes, local style guides, examples from accepted docs, and review
checklists that call out vague or templated wording.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
