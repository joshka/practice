# Markdown And Docs Agent Instructions

Use this snippet in repos where agents edit Markdown, Rustdoc, README files, or review narrative.

```markdown
## Documentation Work

Write docs that state current behavior, explain contracts and tradeoffs, and preserve local voice.
Choose the documentation job before editing: local correction, page coherence, repo map, reference
contract, or review handoff.

Keep user docs task-first. Put maintainer context, reference detail, and decision records behind the
first reading path. Do not create placeholder docs without durable content.

Write technical docs, not marketing, coaching, or chat. Pick the page mode first and keep one
dominant mode per page. Front-load the point, name the actor, prefer active voice, and use present
tense unless accuracy requires otherwise.

Use prose for relationships, causality, and tradeoffs. Use lists for steps, fields, options, and
enumerations. Do not atomize explanation into one-sentence fragments by default.

Cut page narration, teaching-order commentary, throat-clearing, unearned ranking words, vague
praise, AI contrast templates, repeated summaries, and link-hub prose. If a draft is smooth but
low-signal, merge sections, cut repetition, restore prose continuity, and add concrete detail.

When changing behavior, search nearby docs, examples, Rustdoc, and agent instructions for drift.
Update them in the same review unit or report explicit follow-up.
Treat English descriptions near code as contracts that code, tests, examples, and agents implement
against. If docs and code disagree, identify which side is intended behavior and repair the other.

Use Markdown that passes `markdownlint-cli2`: prose around 100 columns, blank lines around headings,
lists, and code blocks, fenced code blocks with languages, `1.` numbered lists, and aligned tables.

Canonical guides:

- `guides/markdown-documentation.md`
- `guides/documentation-workflow.md`
- `principles/docs-are-contracts.md`
```
