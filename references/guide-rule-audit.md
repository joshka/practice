# Guide Rule Audit

Status: `draft`

This audit records the guide-grouping and hidden-rule extraction pass. It is evidence for the
current state, not a substitute for maintainer review of draft rules.

## Objective Checklist

| Requirement                              | Evidence                                                                  | Status  |
| ---------------------------------------- | ------------------------------------------------------------------------- | ------- |
| Review guide grouping.                   | All non-Rust guides were inspected and grouped with smaller subsections.  | done    |
| Reduce long flat lists.                  | `scripts/audit_guidance.py` now fails long non-Rust guide bullet runs.    | done    |
| Extract hidden instructional ideas.      | Fourteen guide-only ideas became new draft rule pages.                    | done    |
| Justify extracted rules with sources.    | Each new rule has rationale, limits, mechanisms, and source links.        | done    |
| Feed rules into agent guidance.          | Core agent snippet and reviewed rule pack are checked by audit.           | partial |
| Validate generated and rendered outputs. | Guidance audit, Markdown lint, generator checks, and build pass.          | done    |

The partial item is intentional: repository policy keeps new rules as `draft` until the maintainer
accepts them. Draft rules are indexed for review, but the reviewed-rule agent pack omits them until
their status changes to `reviewed`.

## Completion Audit

The objective breaks down into these concrete deliverables:

- Review every guide's content grouping.
- Replace difficult long flat lists with shorter named groups.
- Look for guide-only instructional ideas that deserve rule, pattern, principle, or mechanism pages.
- Expand extracted ideas into justified pages with rationale, limits, examples or mechanisms, and
  source links where useful.
- Ensure accepted guide rules can inform overall agent guidance the same way reviewed Rust rules do.
- Validate that generated indexes, agent surfaces, Markdown, and the site are current.

## Prompt To Artifact Checklist

- "Review the guides" maps to the edited guide set under `guides/`, with non-Rust guide grouping
  evidence below and Rust treated as the existing exemplar checklist.
- "Long lists with no real grouping" maps to the grouped guide headings plus
  `scripts/audit_guidance.py`, which fails non-Rust guide pages with more than seven consecutive
  top-level bullets.
- "Guides are sources of actual rules, patterns, principles, mechanisms" maps to the extracted
  draft rules below, the generated `rules/README.md` indexes, and direct guide links to existing
  rules, patterns, principles, and mechanisms.
- "Every instructional idea that could be questioned should have a page" maps to the draft review
  queue and the coverage pass notes below. This is the least mechanically provable requirement:
  the repo can verify page shape, links, and generated surfaces, but deciding that every
  questionable guide sentence has a page remains maintainer judgment.
- "Rules in guide pages need to inform the overall agent guidelines" maps to
  `snippets/agents/core.md`, which links every guide and the reviewed rule pack, and to
  `snippets/agents/rules.md`, which is generated from reviewed rules only.
- "Capture, list, expand out to validated and justified rules docs that link to sources" maps to
  the fourteen new draft rule pages, their source-backed references, the domain indexes, and the
  validation commands listed below.

The current evidence supports most of the objective, but not final completion:

- Guide grouping reviewed: covered by the grouping evidence below, which names each non-Rust
  guide's groups.
- Long flat lists reduced: covered by `audit_guide_grouping`, which fails non-Rust guide bullet
  runs over 7.
- Hidden guide rules extracted: partially covered by the fourteen new draft rules listed below with
  origin guides.
- Extracted rules justified: covered by rule schema, link, and quality audits.
- Rules inform agent guidance: partially covered because `core.md` links guides and the reviewed
  rule pack, but draft rules are intentionally not in that pack yet.
- Generated surfaces current: covered by generator `--check` commands and `pnpm build`.

The incomplete parts are policy and coverage limits, not failing mechanics. The extracted ideas are
still `draft`, so they cannot enter the reviewed-rule agent pack until maintainer acceptance. Also,
the audit can prove that linked rule pages are valid and that long lists stay grouped, but it cannot
prove by itself that every possible guide sentence worth questioning has already been extracted.
The draft review queue below is therefore the remaining review checkpoint.

As a follow-up coverage pass, modal-language scans looked for guide instructions without nearby rule
links. That pass tightened direct links from:

- `guides/boundary-correctness.md` to existing boundary rules for upstream modeling, resource
  identity, dynamic registration, state machines, UI/app state, primary sources, backend adapters,
  tool execution, input classes, partial streams, and provider diagnostics.
- `guides/software-change-preferences.md` to existing performance rules for measurement sequence,
  correctness-before-timing, single-run skepticism, benchmark provenance, and sequential benchmark
  execution.
- `guides/code-shape.md` to existing refactoring rules for real variation, DRY limits, weak
  abstractions, local reasoning, linear stories, and side-effect loops.
- `guides/jj-workflow.md` to existing VCS rules for inspection, review lanes, shell quoting,
  noninteractive commands, exact mutation targets, publication, remote topology, Git boundaries, and
  operation-log recovery.
- `guides/markdown-documentation.md` to existing documentation, Rustdoc, and testing rules for
  Markdown linting, document type, scan path, prose shape, concrete claims, voice, source links,
  README/Rustdoc ownership, current behavior, comparisons, Rustdoc validation, docs.rs, examples,
  side effects, and doctests.
- `guides/observability-and-failure.md` to existing observability rules for diagnostics retention,
  operation context in errors, distinct failure states, and durable failure visibility.
- `guides/documentation-workflow.md` to existing documentation, review, and testing rules for
  generated-prose cleanup, concrete details, standalone review artifacts, and drift claim
  validation.
- `guides/coding-agents.md` to existing agent-workflow rules for objective setting, durable
  context, tools over prompts, build-preserving edits, workspace isolation, scoped capabilities,
  proof-focused handoffs, feedback loops, maintainer next options, and nonfunctional requirements.
- `guides/software-change-preferences.md` to existing change-shape, review, testing, performance,
  and source rules for one-purpose scope, dependency churn, binary artifacts, follow-ups, generated
  artifacts, owning modules, unowned work, validation by risk, visible output proof, review slices,
  PR narrative, ADRs, atomicity, and controversial changes.

## Grouping Evidence

The non-Rust guides now group long enumerations by topic:

- `guides/software-change-preferences.md`: scope, follow-ups, verification, review artifacts,
  commit history, and review questions.
- `guides/code-shape.md`: reader locality, local expression shape, abstraction, and review
  questions.
- `guides/boundary-correctness.md`: validation, lifecycle, inputs, effects, tool execution,
  providers, and review questions.
- `guides/observability-and-failure.md`: failure visibility, error contracts, diagnostics, and
  review questions.
- `guides/markdown-documentation.md`: document jobs, rule shape, reader path, Rustdoc, examples,
  references, and review questions.
- `guides/documentation-workflow.md`: evidence, voice, repo maps, review narrative, drift, and
  review questions.
- `guides/coding-agents.md`: objectives, context, guardrails, workspaces, verification, feedback,
  maintainer loops, coherence, and review questions.
- `guides/jj-workflow.md`: defaults, working copies, descriptions, command shape, bookmarks,
  GitHub handoff, recovery, and review questions.

The remaining allowed long bullet runs are in `guides/rust-maintainability.md`, where the Rust guide
is already the exemplar checklist that links compact rules directly. `scripts/audit_guidance.py`
now fails non-Rust guide pages that rebuild long flat top-level bullet runs.

## Extracted Draft Rules

- `guides/markdown-documentation.md`:
  [`DOCS-GROUP-RELATED-LIST-ITEMS`](../rules/documentation/docs-group-related-list-items.md)
- `guides/markdown-documentation.md`:
  [`DOCS-DISTINGUISH-EXAMPLE-ROLES`](../rules/documentation/docs-distinguish-example-roles.md)
- `guides/markdown-documentation.md`:
  [`DOCS-MAKE-GUIDANCE-REVIEW-STATE-VISIBLE`](../rules/documentation/docs-make-guidance-review-state-visible.md)
- `guides/documentation-workflow.md`:
  [`DOCS-REVIEW-CORRECTNESS-AND-RISK-FIRST`](../rules/documentation/docs-review-correctness-and-risk-first.md)
- `guides/documentation-workflow.md` and `guides/software-change-preferences.md`:
  [`REVIEW-EXPLAIN-CONTROVERSIAL-CHOICES-INLINE`](../rules/review/review-explain-controversial-choices-inline.md)
- `guides/code-shape.md`:
  [`REFACTORING-MAKE-EDGE-CASES-EXPLICIT`](../rules/refactoring/refactoring-make-edge-cases-explicit.md)
- `guides/boundary-correctness.md`:
  [`BOUNDARY-MAKE-POLICY-BOUNDARIES-EXPLICIT`](../rules/boundary/boundary-make-policy-boundaries-explicit.md)
- `guides/coding-agents.md`:
  [`AGENT-REVIEW-OUTPUT-AS-FUTURE-MAINTAINER`](../rules/agent-workflow/agent-review-output-as-future-maintainer.md)
- `guides/software-change-preferences.md`:
  [`REVIEW-CLASSIFY-PROTOTYPE-REUSE`](../rules/review/review-classify-prototype-reuse.md)
- `guides/software-change-preferences.md`:
  [`CHANGE-AVOID-SPECULATIVE-PUBLIC-API`](../rules/change-shape/change-avoid-speculative-public-api.md)
- `guides/software-change-preferences.md`:
  [`REVIEW-UPDATE-SOURCE-OF-TRUTH`](../rules/review/review-update-source-of-truth.md)
- `guides/software-change-preferences.md`:
  [`REVIEW-ANSWER-QUESTIONS-BEFORE-CODE`](../rules/review/review-answer-questions-before-code.md)
- `guides/software-change-preferences.md`:
  [`CHANGE-RESPECT-GENERATED-ARTIFACT-OWNERSHIP`](../rules/change-shape/change-respect-generated-artifact-ownership.md)
- `guides/software-change-preferences.md`:
  [`REVIEW-SEPARATE-DISCOVERY-SELECTION-IMPLEMENTATION`](../rules/review/review-separate-discovery-selection-implementation.md)

There are fifteen draft rules in the repository after this pass. Fourteen are new in this change; the
pre-existing draft is
[`DOCS-MATCH-PAGE-SHAPE-TO-READER-TASK`](../rules/documentation/docs-match-page-shape-to-reader-task.md).

## Draft Review Criteria

For each queued rule, maintainer review should decide:

- Whether the rule is durable enough to become `reviewed`, or should stay `draft`.
- Whether the rule should be accepted as written, narrowed, merged with another rule, or dropped.
- Whether the rule's rationale, limits, mechanisms, and references justify the instruction.
- Whether the compact agent instruction would help future agents act without overgeneralizing.
- Whether promotion requires nearby guide, snippet, template, or generated-index updates.

## Draft Review Queue

Maintainer review should decide whether each draft rule is accepted as written, narrowed, merged
with another rule, or dropped. The queue is:

- [`DOCS-GROUP-RELATED-LIST-ITEMS`](../rules/documentation/docs-group-related-list-items.md):
  from `guides/markdown-documentation.md`.
- [`DOCS-DISTINGUISH-EXAMPLE-ROLES`](../rules/documentation/docs-distinguish-example-roles.md):
  from `guides/markdown-documentation.md`.
- [`DOCS-MAKE-GUIDANCE-REVIEW-STATE-VISIBLE`](../rules/documentation/docs-make-guidance-review-state-visible.md):
  from `guides/markdown-documentation.md`.
- [`DOCS-REVIEW-CORRECTNESS-AND-RISK-FIRST`](../rules/documentation/docs-review-correctness-and-risk-first.md):
  from `guides/documentation-workflow.md`.
- [`REVIEW-EXPLAIN-CONTROVERSIAL-CHOICES-INLINE`](../rules/review/review-explain-controversial-choices-inline.md):
  from `guides/documentation-workflow.md` and `guides/software-change-preferences.md`.
- [`DOCS-MATCH-PAGE-SHAPE-TO-READER-TASK`](../rules/documentation/docs-match-page-shape-to-reader-task.md):
  pre-existing draft.
- [`REFACTORING-MAKE-EDGE-CASES-EXPLICIT`](../rules/refactoring/refactoring-make-edge-cases-explicit.md):
  from `guides/code-shape.md`.
- [`BOUNDARY-MAKE-POLICY-BOUNDARIES-EXPLICIT`](../rules/boundary/boundary-make-policy-boundaries-explicit.md):
  from `guides/boundary-correctness.md`.
- [`AGENT-REVIEW-OUTPUT-AS-FUTURE-MAINTAINER`](../rules/agent-workflow/agent-review-output-as-future-maintainer.md):
  from `guides/coding-agents.md`.
- [`REVIEW-CLASSIFY-PROTOTYPE-REUSE`](../rules/review/review-classify-prototype-reuse.md):
  from `guides/software-change-preferences.md`.
- [`CHANGE-AVOID-SPECULATIVE-PUBLIC-API`](../rules/change-shape/change-avoid-speculative-public-api.md):
  from `guides/software-change-preferences.md`.
- [`REVIEW-UPDATE-SOURCE-OF-TRUTH`](../rules/review/review-update-source-of-truth.md):
  from `guides/software-change-preferences.md`.
- [`REVIEW-ANSWER-QUESTIONS-BEFORE-CODE`](../rules/review/review-answer-questions-before-code.md):
  from `guides/software-change-preferences.md`.
- [`CHANGE-RESPECT-GENERATED-ARTIFACT-OWNERSHIP`](../rules/change-shape/change-respect-generated-artifact-ownership.md):
  from `guides/software-change-preferences.md`.
- [`REVIEW-SEPARATE-DISCOVERY-SELECTION-IMPLEMENTATION`](../rules/review/review-separate-discovery-selection-implementation.md):
  from `guides/software-change-preferences.md`.

## Agent Guidance Evidence

Agent-facing guidance has two layers:

- `snippets/agents/core.md` points agents to every reviewed guide, including non-Rust guide pages,
  and to the reviewed-rule pack for compact execution rules.
- `snippets/agents/rules.md` is generated from reviewed rules only.

That matches the Rust model for accepted material: reviewed rules become compact agent instructions,
and guide pages provide the higher-context map. The extracted rules will enter the generated
reviewed-rule pack after maintainer review and status promotion.
`scripts/audit_guidance.py` now verifies that the core agent snippet keeps those guide and rule-pack
links.

## Validation Evidence

The current pass has been validated with:

```bash
python3 scripts/audit_guidance.py
python3 scripts/audit_guidance.py --quality
python3 scripts/generate_rule_indexes.py --check
python3 scripts/generate_agent_rules.py --check
python3 scripts/generate_downstream_template.py --check
markdownlint-cli2 "**/*.md"
pnpm build
```

## Remaining Gate

Maintainer review is still required for the draft rules. For each accepted rule:

1. Update the rule `Status` metadata from `draft` to `reviewed`, or revise the rule and keep it in
   the draft queue.
1. Remove accepted rules from the `Draft Review Queue` in this audit.
1. Regenerate `rules/README.md`, the affected domain indexes, `snippets/agents/rules.md`, and the
   downstream rule template.
1. Rerun the validation commands above.

That promotion path is what completes the agent-guidance requirement: accepted rules enter the
reviewed rule pack, while rejected or unresolved ideas stay visible in the review queue.
