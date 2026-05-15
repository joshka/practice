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
such as "seamless," "robust," repeated summary sentences, teaching-order narration, generic
contrast language, and component-centered navigation copy make technical docs feel less trustworthy
because they avoid naming the concrete behavior.

On documentation sites, generated tells often appear as "cards map," "pages carry," "domains
expose," "the full map," or "how X should be reasoned about." These phrases narrate the catalog or
the UI instead of naming the reader's destination, decision, artifact, or work area.

## Helps

- Preserves local voice, keeps docs dense, and makes claims easier to verify.

## Limits

Do not remove useful friendliness or explanation just because a sentence is smooth. Cut the
generated tell when it replaces concrete behavior, evidence, tradeoff language, or a direct
navigation label.

## Agent Instruction

Avoid generated-prose tells, including component-centered navigation copy, that replace concrete
behavior, evidence, tradeoffs, or direct labels.

## Mechanisms

Supported by prose review passes, local style guides, examples from accepted docs, and review
checklists that call out vague or templated wording.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Docs Hide Catalog Mechanics](docs-hide-catalog-mechanics.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
