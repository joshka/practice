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
action verbs, evidence-disclaimer templates, empty `current`/`complete`/`combined` scaffolding, and
link-hub prose. Start a new paragraph when the subject, explanatory level, evidence type, or
maintainer warning changes. If a draft is smooth but low-signal, merge sections, cut repetition,
restore prose continuity, and add concrete detail.
Treat AI-assisted drafts as raw material: verify claims, restore local voice, keep useful detail,
and cut generated-sounding prose instead of merely disclosing provenance. If the process is
described, distinguish model generation from human prompting, steering, evaluation, correction, and
endorsement accurately.

When documenting non-obvious design rationale, inspect current behavior, introducing and corrective
history, tests, measurements, and relevant discussion before drafting. Write from the current
mechanism outward. Use history to support the explanation, identify a rejected alternative, or warn
about a regression rather than making chronology the reader's route to the present design.

For broad source-explanation work, define scope and completion gates before editing. Audit small
helpers, formulas, producers, return paths, edge branches, and low-level contracts instead of
sampling. Track both file coverage and size-weighted progress. If review exposes a systematic miss,
add it to the checklist and repeat that check across completed areas.

Keep temporary plans, progress records, and research notes outside the published change unless they
are durable project documentation. Report progress proactively after small batches and wave
boundaries, including completed scope, weighted coverage, unresolved questions, and the next area.
When the pass is documentation-only, verify that executable tokens, configuration, generated
artifacts, and unrelated formatting did not change; use a language-aware comparison when practical.

Trace claims through every producer, wrapper, trait implementation, return path, feature gate, and
indirect effect that can change their meaning. Distinguish counters from weighted statistics, cached
results from associated hints, exact conditions from the risks they approximate, and textbook
guarantees from the work the implementation actually performs.

For unsafe code, separate an unsafe API's caller contract, the proof at each unsafe operation, and
the invariant enforced by a safe wrapper. Current caller discipline does not prove a broader safe
signature sound. Consolidate shared safety reasoning at its owner instead of repeating boilerplate.

Make the checkout a self-contained reading environment for the stated audience. Establish the
system's end-to-end map, ownership, vocabulary, and required domain fundamentals before detailed
comments depend on them. Explain the local implementation beside the code; use specifications,
papers, history, and discussion for evidence or optional depth rather than as prerequisites. Prove
completion with reader comprehension questions, not comment count alone.

Give each broad review pass a named purpose. Promote a systematic finding into the checklist and
repeat it across completed scope. Once declared gates and systematic misses are resolved, stop when
another pass produces only repeated findings or alternate wording with no material reader benefit.

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
- `patterns/reconstruct-rationale-before-writing.md`
- `patterns/run-source-explanation-pass.md`
- `rules/documentation/docs-own-ai-assisted-prose.md`
- `principles/docs-are-contracts.md`
```
