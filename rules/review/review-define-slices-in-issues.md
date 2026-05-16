# Review Define Slices In Issues

## Metadata

- Name: `Define Slices in Issues`
- ID: `REVIEW-DEFINE-SLICES-IN-ISSUES`
- Summary: Shape issues around review-sized slices with clear outcomes. Coherent slices reduce scope
  creep and give maintainers or agents a practical unit of work without losing the larger purpose.
- Status: `reviewed`
- Domain: `review`
- Tags: `reviewability, change-shape, review-handoff`
- Related: `small-reviewable-chunks, cap-change-radius, define-good-before-judgment-heavy-work`

## Rule

Define review-sized slices in issues.

## Why

Issues are often the first place a future PR gets shaped. If an issue asks for "fix docs and clean
up the API and improve tests," the eventual change is likely to become a mixed review with unclear
stopping points. Naming slices such as "document current behavior," "add failing regression test,"
or "introduce additive API" lets the work land in pieces that reviewers can understand.

## Helps

- Keeps issues actionable, prevents accidental scope creep, and gives agents a clear unit of work.

## Limits

Do not split work so finely that each issue loses the reason it exists. A slice should still have a
coherent user, maintainer, or review outcome.

## Agent Instruction

Define review-sized slices in issues because issues are often the first place a future PR gets shaped.

## Mechanisms

Supported by issue templates, task checklists, milestone notes, and follow-up issue links that keep
large efforts reviewable without hiding the overall objective.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Ed Page: PR style](https://epage.github.io/dev/pr-style/)
- [GitHub Docs: helping others review your
  changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes)
