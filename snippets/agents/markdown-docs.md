# Markdown And Docs Agent Instructions

Use this snippet in repos where agents edit Markdown, Rustdoc, README files, or review narrative.

```markdown
## Documentation Work

Write docs that state current behavior, explain contracts and tradeoffs, and preserve local voice.
Choose the documentation job before editing: local correction, page coherence, repo map, reference
contract, or review handoff.

Keep user docs task-first. Put maintainer context, reference detail, and decision records behind the
first reading path. Do not create placeholder docs without durable content.

When changing behavior, search nearby docs, examples, Rustdoc, and agent instructions for drift.
Update them in the same review unit or report explicit follow-up.

Use Markdown that passes `markdownlint-cli2`: prose around 100 columns, blank lines around headings,
lists, and code blocks, fenced code blocks with languages, `1.` numbered lists, and aligned tables.

Canonical guides:

- `guides/markdown-documentation.md`
- `guides/documentation-workflow.md`
```
