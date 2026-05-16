# Markdown And Documentation

This guide captures how documentation should be shaped in this repo and in downstream project
guidance. Prefer docs that reduce rediscovery, carry contracts clearly, and stay easy to lint,
review, and reuse.

Use this guide with [Software Change Preferences](software-change-preferences.md).

## Markdown Style

Write Markdown that is easy to read in source form and easy to diff.

- Wrap prose around 100 columns.
- Put a blank line after headings.
- Put a blank line before and after lists, blockquotes, and fenced code blocks.
- Use fenced code blocks with a language tag.
- Use `1.` markers for numbered lists.
- Format tables with aligned columns.
- Let table rows exceed the prose line limit when alignment improves readability.

Run:

```bash
markdownlint-cli2 "**/*.md"
```

The repo config links directly to the upstream lint rules it customizes.

Use [Keep Markdown Lintable][markdown-lintable] when Markdown source format, table alignment, code
fences, or line wrapping affects review quality.

## Docs As Contracts

Treat docs, comments, and Rustdoc as part of the behavioral surface. If behavior changes, update the
nearby docs in the same review unit. If a doc is wrong, fix the doc or the behavior intentionally;
do not leave drift for the next reader.

Good docs explain purpose, constraints, invariants, edge cases, side effects, and recovery paths;
weak docs repeat names, signatures, or ordinary control flow.

Docs should explain purpose, assumptions, edge cases, and relationships instead of merely restating
names or signatures.

Prefer documentation that helps a human form the right mental model without reading every method in
the system. Code can be locally obvious and still hide behavior that matters at a larger scale:
ordering, ownership, lifecycle, persistence, retry behavior, external effects, compatibility rules,
and caller obligations. Capture that information near the API or workflow boundary where readers
look for it.

Good documentation also amortizes discovery. Humans and agents both spend time reconstructing
context from code when rationale is missing. Capture stable rationale, constraints, and system
behavior once during production so future work can start from a durable summary instead of
repeating the same scan.

Reusable guidance should [make its review state visible][guidance-status]. Start new patterns as
`draft`, and mark them `reviewed` only after the maintainer explicitly accepts the rule. Source
links justify, frame, or contrast the guidance; they do not supply the wording. Write durable
guidance in the repo's own voice, avoid copying or closely paraphrasing sources, and omit source
links when no durable source actually clarifies the idea.

Pattern-style guidance should expose the main decision quickly: the symptom, the preferred move, the
risk or limit, the example, and the agent instruction. Keep the compact form visible, then add only
the prose needed to make the tradeoff judgeable.

Use [Document System Mental Models][system-models], [Document Intentional Non Goals][non-goals],
[Make Side Effects Visible][side-effects], [Keep Docs Near Their Subject][doc-locality], and
[Prefer Durable Summaries][durable-summaries] when code needs durable context beyond a single API
contract.

Use [Preserve Error Context][error-context] and [Write Actionable Error Messages][actionable-errors]
when documenting failures that cross user, caller, operator, or support boundaries.

## Document Types

Separate documentation jobs instead of mixing every reader need into one page.

- Tutorials teach by doing.
- How-to guides help a reader complete a task.
- Reference docs state exact names, options, defaults, and contracts.
- Explanation docs carry rationale, tradeoffs, and mental models.

Use Diátaxis as a framing tool, not as a rigid taxonomy. The point is to keep the document's primary
job obvious.

Use [Choose Document Type][doc-type], [One Dominant Mode Per Page][one-mode], and [Match Page Shape
To Reader Task][page-shape] when a document is mixing tutorial, how-to, reference, explanation, or
decision-record jobs.

## Writing Rules

Use grouped, named lists when a checklist or rule cluster grows past easy scanning. A long flat
list can hide whether the page is about document mode, scan path, sentence shape, claim quality,
style limits, or evidence. Use [Group Related List Items][group-lists] when a list needs internal
structure, and use [Prose For Relationships, Lists For Enumeration][prose-lists] when bullets are
carrying explanation that belongs in paragraphs.

### Document Mode

- Write technical docs, not marketing, coaching, or chat.
- Pick the document mode before editing.
- Keep one dominant mode per page.
- Explain in explanation pages.
- Guide in setup and how-to pages.
- Describe in reference pages.
- Do not mix documentation modes without a reason.

### Scan Path

- Front-load the point in sentences and paragraphs.
- Use fewer, denser sections.
- Use headings for real topic clusters, not micro-points.
- Use descriptive headings on reference pages, indexes, and landing pages.
- Reserve imperative headings for procedures, checklists, and tutorials where the heading names a
  real step.
- Name destinations, decisions, artifacts, and work areas instead of directing the reader with
  phrases like `start here` or `use this when`.
- Hide catalog mechanics such as rule prefixes, generated indexes, card behavior, and source layout
  unless citation, automation, or contribution workflow depends on them.

Use [Front Load Useful Point][front-load], [Use Descriptive Headings][descriptive-headings], [Name
Destination Not Direction][destination-names], and [Hide Catalog Mechanics][catalog-mechanics] when
the reader's scan path depends on headings, first sentences, labels, or generated structure.

### Prose And Lists

- Use prose for relationships, causality, and tradeoffs.
- Use lists for steps, fields, options, and enumerations.
- Do not use lists as the default explanation format.
- Let a paragraph develop one idea.
- Do not atomize explanation into one-sentence fragments by default.
- Give each sentence one main burden.
- Do not combine explanation, qualification, anticipated confusion, and navigation in one sentence
  unless the page needs it.

Use [Write Technical Prose][technical-prose] and [Prose For Relationships, Lists For
Enumeration][prose-lists] when prose shape is hiding relationships, tradeoffs, or the main point.

### Concrete Claims

- Prefer concrete nouns.
- Prefer real paths.
- Prefer real defaults.
- Prefer real examples.
- Prefer explicit tradeoffs.

Use [Use Concrete Details][concrete-details] when a doc could name real paths, defaults, commands,
types, examples, or tradeoffs instead of generic wording.

### Voice And Style

#### Sentence Voice

- Name the actor.
- Prefer active voice.
- Prefer present tense unless accuracy requires another tense.
- Avoid vague praise words.
- Avoid invented abstractions.
- Avoid idioms when plain language is available.
- Cut filler and signposting.

#### Page Narration

- Do not narrate the page.
- Do not narrate the interface.
- Explain the system instead of explaining what the page will do.
- Avoid unearned ranking words.
- Use words like `simplest`, `easiest`, `best`, `fastest`, `safest`, and `usually` only when the
  page states the property that earns the claim.
- In explanation and reference pages, do not stage the reader through time.
- Use temporal staging only in actual procedures.
- Avoid contrast templates such as `not X, but Y`.
- Avoid punctuation as style signaling.
- Do not lean on repeated dashes or colon scaffolding.

Use [Avoid Unearned Praise][unearned-praise] and [Avoid Generated Prose Tells][generated-tells] when
voice, ranking words, page narration, or interface narration weakens technical clarity.

### Revision And Evidence

#### Local Revision

- Do not restate the same point in adjacent paragraphs at different intensity.
- Do not over-introduce sections.
- Do not over-summarize sections.
- Avoid mini-intros before every list.
- Avoid mini-summaries after every section unless they add meaning.

#### Evidence Links

- Link cleanly to deeper pages.
- Do not add bridge prose that explains the link more than the concept.
- Verify claims, defaults, recommendations, and examples against source and behavior.
- If a draft is smooth but low-signal, merge sections, cut repetition, restore prose continuity, and
  add specifics.

Use [Use Source Links As Support][source-links] and [Verify Commands Paths And Links][verify-links]
when a documentation change depends on source claims, commands, paths, defaults, or examples.

## Layering Rules

### Entry Points And Decisions

- Keep README files short enough to serve as entry points.
- Put purpose, quick start, compatibility, status, and next links in the README.
- Put detailed usage models in Rustdoc unless the material is maintainer-only.
- Put release, conformance, fuzzing, performance, and protocol coverage in maintainer docs.
- Put durable decisions and rejected alternatives in ADRs.

### Crate And Module Docs

- Use the crate root to teach the crate.
- Use the crate root to expose the primary path.
- Use the crate root to route readers to deeper modules.
- Include purpose, first example, primary entry points, module map, feature flags, lifecycle notes,
  current limitations, and next reading when they matter.
- Keep crate-level docs updated when adding public modules, widgets, commands, modes, or major
  behaviors.
- Keep crate README and crate-level Rustdoc focused on that crate's contract, caveats,
  configuration, examples, and source references.
- Keep support crate docs focused on the support crate's role.
- Link support crate docs back to core crates and workspace docs instead of duplicating the whole
  workspace inventory.

Use [README As Entry Point][readme-entry], [Align README And Crate Rustdoc][readme-rustdoc],
[Teach Crate From Crate Root][crate-root], and [Keep Markdown Outside Rustdoc
Purposeful][markdown-outside-rustdoc] when deciding which documentation surface owns a usage model,
API contract, or maintainer-only explanation.

### Links And Examples

- Link to runnable examples for interactive flows.
- Prefer reference-style links for Rust types when repeated inline links would distract from the
  doc comment.
- Prefer descriptive link text in sentence prose.
- Use path-only link text mainly in dense tables and inventories.
- Group link definitions near the end of Markdown documents when that keeps prose easier to scan.

### User-Facing Docs

- Keep user docs light and task-first.
- Do not front-load maintainer depth into onboarding.
- State current behavior, not aspirations.
- Put the useful answer before background.
- Prefer examples before theory in user docs.
- Document uncertainty in an issue, ADR, or roadmap item.
- Do not bury uncertainty in user docs.

Use [State Current Behavior Not Aspiration][current-behavior] and [Put Uncertainty In Tracked
Places][tracked-uncertainty] when user-facing docs are tempted to carry future plans or unresolved
questions.

### Comparisons And Ownership

- Compare nearby libraries accurately and charitably.
- Explain fit, scope, and tradeoffs instead of implying the local project is universally better.
- Prefer direct ownership and boundary statements over apologetic design justifications.

Use [Compare Libraries Accurately][compare-libraries] when documentation positions a project,
crate, or tool against nearby alternatives.

### Rustdoc Items And Validation

- For public Rust items, make the first sentence a concise action or return summary.
- Prefer prose for Rustdoc argument details; avoid parameter tables unless the API is truly tabular.
- Keep quick-start examples copy-pasteable under the stated feature flags and dependencies.
- Do not rely on undeclared transitive dependencies in examples.
- Verify example commands, file paths, and linked references are real before handing off docs.
- When updating downstream agent instructions, include the local lint command, line length, docs as
  contracts, and the canonical skill or guide for documentation work.

Use [Write Public Docs For Caller Tasks][public-docs], [Build Docs Like Users Read Them][build-docs],
[Mark Noncompiling Examples Honestly][noncompiling-examples], and [Validate Rust Docs As
Code][validate-rust-docs] when Rustdoc, examples, feature flags, or generated docs are part of the
review surface.

## Rustdoc

Rustdoc should document contracts, not narrate implementation.

For crates and modules, include the purpose, boundaries, key concepts, feature flags, constraints,
and important non-goals when they matter.

Important module docs should answer the ownership questions a future maintainer needs before
editing the area:

- What concept does this module own?
- Which adjacent concept does it intentionally not own?
- Which external assumptions shape the code?
- Where does new behavior in this area belong?

Short concrete module docs are usually better than long generic module docs.

For public items, include the first-sentence summary plus relevant sections:

- `# Examples`
- `# Errors`
- `# Panics`
- `# Safety`
- `# Performance`

Also document lifecycle, ownership, side effects, feature flags, platform assumptions, and
compatibility when callers need that contract. Public fields deserve the same standard as public
functions: meaning, valid values, defaults, invariants, and interactions with neighboring fields.

Prefer examples that compile. Use `no_run` when compilation matters but running requires external
systems. Use `ignore` only when the example cannot be made checkable.

Feature-gated examples should compile under the relevant feature set. If the crate uses generated
README content from crate-level Rustdoc, keep the Rustdoc source authoritative and regenerate the
README in the same change.

When a public facade is the canonical path, use Rustdoc attributes such as `#[doc(inline)]` so
readers land on the useful documentation from that path. Avoid public glob re-exports that make the
documentation surface harder to audit.

For docs.rs, configure metadata intentionally: enable relevant features, documented cfgs, and
platform-specific docs when those surfaces affect users. When README content is generated from
Rustdoc, treat the crate root as the source of truth and regenerate the README after crate-doc
changes. Keep Rustdoc citation style consistent when adding RFCs, specifications, or protocol
references.

Use [Write Rustdoc As API Contract][rustdoc-contract], [Document Feature Contracts][feature-docs],
[Keep Rustdoc And README Examples Aligned][rustdoc-readme], [Use Doc Inline For Canonical
Reexports][doc-inline], [Avoid Glob Reexports][glob-reexports], and [Configure Docs.rs][docs-rs]
when Rust documentation paths, feature-gated docs, generated README content, or docs.rs metadata are
part of the public surface.

## Examples

Examples should make the pattern, contract, or workflow easier to recognize. Prefer compact bad and
good examples when the contrast clarifies the rule.

Examples should be direct, readable, and practical. They should teach where output goes, who owns
cleanup, why a feature is enabled, and which reader need the example serves.

Different example roles should be visibly different in the source:

- Small focused examples teach one concept.
- Canonical workflow examples show the smallest complete workflow.
- Survey examples show breadth without requiring a live environment.
- Integration sketches teach ownership structure, not framework cleverness.
- Interactive showcases are opt-in, reversible, and explicit about where they should run.
- Large examples need a specific teaching reason.
- Example inventories distinguish canonical examples from sketches.

Omit examples when the problem cannot be made obvious from the snippet itself. For API or
implementation-shape guidance, show the definition being introduced or changed. For review-unit
guidance, use `diff` blocks when the change itself is the point.

For public APIs, prefer realistic examples over isolated constructor calls. A good example can teach
ownership, error handling, feature flags, lifecycle, protocol shape, or integration with a caller's
runtime. For protocol-facing APIs, include concrete representative inputs or outputs when bytes,
paths, headers, modes, coordinates, or compatibility rules are the contract.

For UI examples, show the visible behavior or point to a runnable example when static prose cannot
carry the interaction.

Examples that open live resources should make side effects and cleanup visible. Policy-sensitive,
persistent, external, or user-visible effects should be gated by policy, configuration, or explicit
opt-in; when live effects are not the point, default to encode-only, dry-run, buffered, or
non-persistent behavior.

Keep public examples small, deterministic, and copy-paste friendly. They should not rely on
undeclared transitive dependencies or a specific local repository unless the example is explicitly
illustrative. Use relative names unless the section is about absolute-name semantics.

Use [Test Observable Behavior][test-behavior] when examples imply behavior that should be protected
by tests.

Use [Distinguish Example Roles][example-roles], [Prove Real Use With Examples][real-examples],
[Show Side Effects In Live Examples][example-effects], and [Cover Public Examples With
Doctests][example-doctests] when examples need a clear role, need to prove a contract, show cleanup,
or stay executable.

## Sources And References

References support, adapt, or contrast this repo's guidance. They do not supply the prose. Write in
this repo's voice and avoid copying or closely paraphrasing upstream text.

Use direct links to the relevant upstream section instead of broad root links. Omit the references
section when no durable source is useful.

## Agent Snippet

For copyable `AGENTS.md` guidance, use [Markdown And Docs Agent Instructions][docs-snippet].

## Related Guidance

Use [Documentation Rules][doc-rules] for compact docs guidance and [Docs Are Contracts][docs-contracts]
for the reasoning behind treating docs as behavior-bearing artifacts. Use
[Rust Docs Validation][docs-validation] for Rustdoc, doctest, and docs.rs proof. Use
[External Source Ledger][source-ledger] when adding or evaluating recurring source families.

## Review Questions

### Page Job

- Does the document have one primary job?
- Does the first paragraph state the useful point?
- Does the doc explain a contract, constraint, or tradeoff instead of restating names?
- For pattern-style guidance, are the symptom, move, risk, example, and agent instruction visible?

### Evidence

- Are examples small enough to understand without reconstructing a project?
- Are Markdown tables aligned?
- Did behavior changes update nearby docs?
- Do source links point to the relevant upstream section?

## References

| Source                 | Use      | Note                                                  |
| ---------------------- | -------- | ----------------------------------------------------- |
| [markdownlint][mdlint] | `adapts` | Lintable Markdown conventions and configurable rules. |
| [Diátaxis][diataxis]   | `adapts` | Framework for separating documentation jobs.          |
| [Rustdoc][rustdoc]     | `adapts` | Rust documentation conventions and section structure. |

[actionable-errors]: ../patterns/write-actionable-error-messages.md
[diataxis]: https://diataxis.fr/
[build-docs]: ../rules/documentation/docs-build-docs-like-users-read-them.md
[catalog-mechanics]: ../rules/documentation/docs-hide-catalog-mechanics.md
[compare-libraries]: ../rules/documentation/docs-compare-libraries-accurately.md
[concrete-details]: ../rules/documentation/docs-use-concrete-details.md
[crate-root]: ../rules/rust/rust-teach-crate-from-crate-root.md
[current-behavior]: ../rules/documentation/docs-state-current-behavior-not-aspiration.md
[descriptive-headings]: ../rules/documentation/docs-use-descriptive-headings.md
[destination-names]: ../rules/documentation/docs-name-destination-not-direction.md
[doc-rules]: ../rules/documentation/README.md
[doc-inline]: ../rules/rust/rust-use-doc-inline-for-canonical-reexports.md
[doc-type]: ../rules/documentation/docs-choose-document-type.md
[docs-rs]: ../rules/rust/rust-configure-docs-rs.md
[docs-contracts]: ../principles/docs-are-contracts.md
[docs-snippet]: ../snippets/agents/markdown-docs.md
[docs-validation]: ../mechanisms/rust-docs-validation.md
[doc-locality]: ../patterns/keep-docs-near-their-subject.md
[durable-summaries]: ../patterns/prefer-durable-summaries.md
[error-context]: ../patterns/preserve-error-context.md
[example-doctests]: ../rules/testing/test-cover-public-examples-with-doctests.md
[example-effects]: ../rules/documentation/docs-show-side-effects-in-live-examples.md
[example-roles]: ../rules/documentation/docs-distinguish-example-roles.md
[feature-docs]: ../rules/rust/rust-document-feature-contracts.md
[front-load]: ../rules/documentation/docs-front-load-useful-point.md
[generated-tells]: ../rules/documentation/docs-avoid-generated-prose-tells.md
[glob-reexports]: ../rules/rust/rust-avoid-glob-reexports.md
[guidance-status]: ../rules/documentation/docs-make-guidance-review-state-visible.md
[group-lists]: ../rules/documentation/docs-group-related-list-items.md
[markdown-lintable]: ../rules/documentation/docs-keep-markdown-lintable.md
[markdown-outside-rustdoc]: ../rules/rust/rust-keep-markdown-outside-rustdoc-purposeful.md
[mdlint]: https://github.com/DavidAnson/markdownlint
[non-goals]: ../patterns/document-intentional-non-goals.md
[noncompiling-examples]: ../rules/documentation/docs-mark-noncompiling-examples-honestly.md
[one-mode]: ../rules/documentation/docs-one-dominant-mode-per-page.md
[page-shape]: ../rules/documentation/docs-match-page-shape-to-reader-task.md
[prose-lists]: ../rules/documentation/docs-prose-for-relationships-lists-for-enumeration.md
[public-docs]: ../rules/rust/rust-write-public-docs-for-caller-tasks.md
[readme-entry]: ../rules/documentation/docs-readme-as-entry-point.md
[readme-rustdoc]: ../rules/documentation/docs-align-readme-and-crate-rustdoc.md
[real-examples]: ../rules/documentation/docs-prove-real-use-with-examples.md
[rustdoc-contract]: ../rules/rust/rust-write-rustdoc-as-api-contract.md
[rustdoc-readme]: ../rules/rust/rust-keep-rustdoc-and-readme-examples-aligned.md
[rustdoc]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html
[side-effects]: ../patterns/make-side-effects-visible.md
[source-ledger]: ../references/
[source-links]: ../rules/documentation/docs-use-source-links-as-support.md
[system-models]: ../patterns/document-system-mental-models.md
[technical-prose]: ../rules/documentation/docs-write-technical-prose.md
[test-behavior]: ../patterns/test-observable-behavior.md
[tracked-uncertainty]: ../rules/documentation/docs-put-uncertainty-in-tracked-places.md
[unearned-praise]: ../rules/documentation/docs-avoid-unearned-praise.md
[validate-rust-docs]: ../rules/rust/rust-validate-rust-docs-as-code.md
[verify-links]: ../rules/documentation/docs-verify-commands-paths-and-links.md
