# Choose Doc Type

## Metadata

- Name: `Choose Doc Type`
- ID: `choose-doc-type`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, structure, review`
- Related: `write-docs-as-contracts`

## Problem

A document becomes hard to use when it mixes learning, task steps, reference facts, and rationale in
the same flow. Readers looking for one job have to sift through the others.

## Preferred Move

Choose the document's primary job before drafting. Use tutorial shape for learning, how-to shape for
task completion, reference shape for exact facts, and explanation shape for rationale and tradeoffs.

## Tradeoff

Small docs can combine jobs when the combined result is still easy to scan. Split or relabel the doc
when one reader need starts hiding another.

## Agent Instruction

Before drafting a guide, name its primary documentation job. Keep reference tables, task steps, and
rationale in separate sections when mixing them would slow the reader down.

## Examples

Bad: a task guide starts with conceptual history before giving the command.

````md
## Why Markdown Linting Matters

Markdown linting grew out of...

## Running The Check
````

Good: a how-to starts with the goal and command, then links to rationale.

````md
## Run Markdown Lint

```bash
markdownlint-cli2 "**/*.md"
```
````

## References

| Source                          | Use        | Note                                                 |
| ------------------------------- | ---------- | ---------------------------------------------------- |
| [Diátaxis tutorials][tutorials] | `supports` | Tutorials serve learning-by-doing.                   |
| [Diátaxis how-to][how-to]       | `supports` | How-to guides are organized around completing tasks. |
| [Diátaxis reference][reference] | `supports` | Reference docs optimize for exact facts.             |
| [Diátaxis explanation][explain] | `supports` | Explanation docs carry rationale and context.        |

[tutorials]: https://diataxis.fr/tutorials/
[how-to]: https://diataxis.fr/how-to-guides/
[reference]: https://diataxis.fr/reference/
[explain]: https://diataxis.fr/explanation/
