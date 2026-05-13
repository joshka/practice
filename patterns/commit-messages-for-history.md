# Commit Messages For History

## Metadata

- Name: `Commit Messages For History`
- ID: `commit-messages-for-history`
- Status: `reviewed`
- Audience: `both`
- Topics: `version-control, jj, review`
- Related: `small-reviewable-chunks, report-verification-honestly`

## Problem

A change can be reviewable today but hard to understand later if its commit message only names the
files touched or repeats the diff. Future readers use history through compact views, blame, bisect,
reverts, and remote UI summaries; weak messages make those tools less useful.

## Preferred Move

Use the Chris Beams and Tim Pope commit-message style for jj descriptions and published commits:

- Write a short imperative subject, aiming for about 50 characters.
- Capitalize the subject and omit trailing punctuation.
- Add a blank line before the body when a body is needed.
- Wrap body prose at 72 columns.
- Use the body to explain the reason, context, and consequences of the change.
- Use Conventional Commits when the repository has adopted that spec.

The subject should complete the sentence: "If applied, this change will ...".

Choose the commit format by repository convention. If the repo uses Conventional Commits, keep the
type and optional scope prefix while applying the same subject/body discipline. If the repo has no
structured commit format, default to the canonical Chris Beams and Tim Pope shape without adding a
prefix. Do not introduce Conventional Commits into a repo just because this guidance mentions it.

## Tradeoff

Not every change needs a body. A tiny typo fix or mechanical update can use a one-line subject when
the diff carries all necessary context. A small diff can still deserve a longer message when the
background, constraint, or decision is significant. Add a body when the reason, tradeoff, or
review-relevant consequence would otherwise be lost.

## Agent Instruction

When setting a jj description or preparing a published commit, use a short imperative subject and a
72-column body when context matters. If the repo uses Conventional Commits, keep the conventional
prefix while preserving the same subject/body discipline. Otherwise use the canonical unprefixed
style. Explain why the change exists and what it changes; do not use the body as a file-by-file diff
summary.

## Examples

Bad: the subject repeats the files and the body adds no context.

```text
Update docs

Changed README.md and AGENTS.md.
```

Good: the subject states the change and the body carries the context future readers need. Wrap the
body at 72 columns.

```text
Document pattern review status

Patterns now start as drafts because reviewed needs to mean
maintainer-accepted, not merely written. The distinction matters as the
catalog grows and agents add new entries in small batches.

This keeps later readers from treating generated text as settled
guidance before it has been checked against the repo voice and source
policy.

The change also updates the template so new patterns carry the safer
default without requiring each future task to remember the rule.
```

## References

| Source                         | Use      | Note                                                                 |
| ------------------------------ | -------- | -------------------------------------------------------------------- |
| [Chris Beams][beams]           | `adapts` | Seven-rule style, including reason and context in the message body.  |
| [Tim Pope][pope]               | `adapts` | Compact subject/body model, 50/72 formatting, and tooling rationale. |
| [Conventional Commits][cc]     | `adapts` | Structured commit prefixes for projects that use them.               |

[beams]: https://cbea.ms/git-commit/
[pope]: https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[cc]: https://www.conventionalcommits.org/
