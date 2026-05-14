# Preserve Local Doc Voice

## Metadata

- Name: `Preserve Local Doc Voice`
- ID: `preserve-local-doc-voice`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, style, agents`
- Related: `follow-local-conventions, preserve-intent-over-literalism`

## Problem

Generated or drive-by documentation edits often flatten a project's voice. The result may be
grammatical, but it loses local names, directness, emphasis, and the maintainer's way of explaining
tradeoffs.

## Preferred Move

Patch the smallest wording needed while preserving the document's existing voice. Prefer local
terms, heading style, example shape, section density, and level of formality unless the current
voice is unclear, inaccessible, or inconsistent with the audience. Put the useful point before
background and use lists only when enumeration helps.

## Tradeoff

Do not preserve local voice when it hides meaning, insults readers, relies on private jokes, or uses
ambiguous shorthand. In those cases, keep the document's intent and repair the voice deliberately.

## Agent Instruction

Before rewriting prose, read nearby paragraphs and match their level of directness, terminology, and
structure. Preserve the document's density and scan shape. Report when you intentionally depart from
the local voice and why.

## Examples

Bad: the edit replaces a concise local rule with generic filler.

```diff
- Keep the public error small; put recovery detail in the variant.
+ It is generally considered a best practice to thoughtfully design error handling behavior.
```

Good: the edit keeps the local voice and clarifies the rule.

```diff
- Keep the public error small; put recovery detail in the variant.
+ Keep the public error small; put caller recovery detail in the variant.
```

## References

| Source                        | Use      | Note                                                 |
| ----------------------------- | -------- | ---------------------------------------------------- |
| [Google voice and tone][tone] | `adapts` | Technical docs should stay clear, direct, and human. |

[tone]: https://developers.google.com/style/tone
