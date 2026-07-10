# Markdown And Docs Agent Instructions

## Metadata

- Name: `Markdown And Docs Agent Instructions`
- ID: `agent-markdown-docs-instructions`
- Summary: `Compact documentation instructions for agents editing Markdown, Rustdoc, READMEs,
  review notes, or adjacent narrative. The snippet focuses on current behavior, local voice, page
  purpose, drift repair, and markdownlint-compatible formatting.`
- Status: `reviewed`
- Audience: `agents`
- Topics: `documentation, markdown, rustdoc, review-handoff`
- Tags: `documentation, rustdoc, review-handoff, source-truth, ai`
- Related: `guides/markdown-documentation.md, guides/documentation-workflow.md,
  rules/documentation/docs-own-ai-assisted-prose.md, principles/docs-are-contracts.md`

Use this snippet in repos where agents edit Markdown, Rustdoc, README files, or review narrative.

```markdown
## Documentation Work

Write docs that state current behavior, explain contracts and tradeoffs, and preserve local voice.
Choose the documentation job before editing: local correction, page coherence, repo map, reference
contract, or review handoff.

For agent efficiency, load this snippet for ordinary docs edits. Add the documentation rule domain
or documentation workflow guide when choosing pass depth, repairing drift, or reviewing risk. Use
the full documentation doctrine only for broad rewrites, de-AI-ification passes, or documentation
audits where the extra context is worth the token cost.

Keep user docs task-first. Put maintainer context, reference detail, and decision records behind the
first reading path. Do not create placeholder docs without durable content.

Write technical docs, not marketing, coaching, or chat. Pick the page mode first and keep one
dominant mode per page. Front-load the point, name the actor, prefer active voice, and use present
tense unless accuracy requires otherwise.

Use descriptive headings on reference pages, indexes, and landing pages. Reserve imperative headings
for procedures, checklists, and tutorials where the heading names a real step.

On navigation surfaces, name the destination, decision, artifact, or work area. Avoid directing the
reader with phrases like "start here," "use this when," or "open this guide." Hide catalog mechanics
such as rule prefixes, generated indexes, card behavior, and source layout unless citation,
automation, or contribution workflow depends on them.

Use prose for relationships, causality, and tradeoffs. Use lists for steps, fields, options, and
enumerations. Do not atomize explanation into one-sentence fragments by default.

Cut page narration, interface narration, teaching-order commentary, throat-clearing, unearned
ranking words, vague praise, stock AI word choice, contrast templates, self-answered questions,
false suspense, forced analogies, vague attribution, invented labels, repeated summaries, bold-first
bullets, unsupported precision, hedged neutrality, apology phrasing, permission phrasing, vague
action verbs, and link-hub prose. If a draft is smooth but low-signal, merge sections, cut
repetition, restore prose continuity, and add concrete detail.
Treat AI-assisted drafts as raw material: verify claims, restore local voice, keep useful detail,
and cut generated-sounding prose instead of merely disclosing provenance.

When changing behavior, search nearby docs, examples, Rustdoc, and agent instructions for drift.
Update them in the same review unit or report explicit follow-up.
Treat English descriptions near code as contracts that code, tests, examples, and agents implement
against. If docs and code disagree, identify which side is intended behavior and repair the other.

Use Markdown that passes `markdownlint-cli2`: prose around 100 columns, blank lines around headings,
lists, and code blocks, fenced code blocks with languages, `1.` numbered lists, and aligned tables.
Use `patterns/prefer-100-column-prose-wrap.md` when the 100-column preference needs rationale.

Canonical guides:

- `guides/markdown-documentation.md`
- `guides/documentation-workflow.md`
- `rules/documentation/docs-own-ai-assisted-prose.md`
- `principles/docs-are-contracts.md`
```
