# Software Change Preferences

## Metadata

- Name: `Software Change Preferences`
- ID: `software-change-preferences`
- Summary: Software-change guidance covers broad preferences for change size, structure,
  validation, review artifacts, commit history, and handoff. It favors small coherent changes,
  explicit tradeoffs, and evidence matched to the changed surface.
- Status: `reviewed`
- Audience: `both`
- Topics: `change-shape, review, validation, handoff, source-control`
- Tags: `change-shape, reviewability, verification, review-handoff`
- Related: `change-shape-controls-review-cost, small-reviewable-chunks, produce-review-packets`

This guide covers broad preferences for change size, structure, validation, and handoff. More
specific Rust, code-shape, documentation, and jj guidance can add detail later without duplicating
these defaults.

## Core Preference

Prefer changes that reduce reader burden while preserving behavior. A good change makes the
important concept, boundary, or rule easier to see from the code and easier to verify from the
handoff.

Optimize for:

- Local reasoning over distant reconstruction.
- Observable behavior over private implementation shape.
- Small reviewable chunks over broad mixed diffs.
- Explicit tradeoffs over unspoken cleverness.
- Honest verification over implied confidence.

## Change Shape

Start by identifying the smallest coherent unit that can be reviewed on its own. A chunk can be a
structure-preserving refactor, a behavior change, a documentation update, or a pattern entry, but it
should not mix unrelated decisions.

### Scope

Keep scope narrow enough that a reviewer can name the change's purpose without reconstructing the
whole branch:

- Use one feature, bug fix, or documentation purpose per change.
- Do not include unrelated refactors.
- Do not include dependency churn unless it is necessary for the task.
- Do not commit binary artifacts; use Git LFS, release assets, PR uploads, CI artifacts, or external
  storage for large opaque outputs.
- Do not move broad modules unless the reader path improves.
- Do not add speculative public API for future features.

Use
[Avoid Speculative Public API][speculative-api] when a change wants to expose names, types, or
extension points before the current need is real.

Use [Use One Purpose Per Change][one-purpose], [Avoid Unnecessary Dependency
Churn][dependency-churn], and [Keep Binaries Out Of Source Control][binary-artifacts] when scope
pressure would mix unrelated work or opaque artifacts into the same review.

### Follow-Ups And Generated Output

When a change reveals separate cleanup, note it or put it in a separate change rather than widening
the current diff. Keep generated artifacts in sync when they are part of the review surface, but edit
the durable source instead of generated output when release tooling owns the generated artifact. Use
[Respect Generated Artifact Ownership][generated-ownership] when the durable fix belongs in the
source input, template, generator config, or release metadata.

Use [Small Reviewable Chunks][small-chunks] when a change could grow into multiple review concerns.
When structure and behavior can be separated cleanly, land the structure change first and verify it
before changing behavior.
Use [Code Shape][code-shape] when the main decision is how to reduce live context, limit change
radius, preserve reversibility, or clarify cohesion and coupling.
Use [Prefer Small Follow Ups][small-follow-ups], [Sync Generated Artifacts][sync-generated], and
[Separate Structure From Behavior][structure-behavior] when follow-up work, generated output, or
refactoring boundaries affect review shape.

## Local Context

Read the repo before applying general preferences. Local instructions, existing helpers, naming
schemes, tests, and version-control workflow usually contain information that a general guide cannot
know.

### Ownership

Before editing, identify the owning module, the adjacent modules it depends on, and the test style
already used for the behavior. That local map keeps a general preference from overriding the shape
the codebase already uses.

Use [Identify Owning Module Before Editing][owning-module] before changing code whose local owner,
neighbors, or test style are not yet clear.

### Local Fit

Prefer the existing style when it is coherent. If the existing shape is actively making the change
harder to understand, improve the local structure, but keep that improvement scoped to the same
concept.

Use [Follow Local Conventions][local-conventions] when general guidance and project shape might
conflict. Use [Separate Discovery From Editing][discovery-editing] when the local shape is not clear
enough to edit confidently.

## Working Copy Care

Assume unowned edits belong to someone. Do not revert, rewrite, or absorb work just because it makes
the current diff look cleaner.

Use [Preserve Unowned Work][preserve-work] when a shared working copy has pre-existing edits or
changes appear while work is in progress.
Use [Change Preserve Unowned Work][change-preserve-work] when this needs compact change-shape rule
wording.

## Verification

Choose verification by the risk of the change. Formatting changes need formatting checks, signature
changes need type or build checks, behavior changes need tests or smoke checks that exercise the
changed path.

### Change-Specific Proof

Choose validation by starting with the narrowest useful command before editing, then widening proof
as the risk of the change grows:

- Run focused tests for touched behavior.
- Run the project gate when practical.
- Run Markdown linting for Markdown-only or doc-heavy changes.
- Report validation gaps directly.

Use [Choose Validation By Risk][validation-risk] and [Run Fast Format And Lint Gates
Early][fast-gates] when selecting the first useful check for a change.

### Generated And Visible Output

Validate changes against the surface users receive, not only the source that generated it:

- Validate template changes against generated output, not only the template source.
- Regenerate affected reference projects when templates change.
- Run checks inside generated projects when generated projects are what users receive.
- Smoke-test interactive flows when event loops, terminal setup, or terminal teardown changed.
- Attach screenshots, GIFs, or before/after context when visible UI output changed.
- Document manual verification when CLI or TUI behavior lacks automated coverage.

Use [Match Evidence To Surface][evidence-surface] when template, generated-project, CLI, TUI,
rendered, parser, public API, or performance changes need proof from the surface users receive.
Use [Prove Command Construction And Display][command-proof], [Cover Navigation
Boundaries][navigation-tests], and [Run Docs As First Class Gate][docs-gate] when command output,
terminal navigation, or docs are the user-visible surface.

For optimization work, use one change per optimization idea. Record the hypothesis and expected
mechanism before touching hot code, run correctness before timing, and keep failed ideas useful by
recording why the evidence did not support them.

Do not make keep/revert decisions from one short benchmark run. Use increasingly expensive evidence
only when the previous step justifies it: counters, phase timers, per-case rows, hot-function maps,
microbenchmarks, profilers, and assembly inspection. Record exact commands, versions, hashes,
environment, corpus, raw samples, and interpretation for benchmark results worth comparing later.

Never run benchmarks in parallel when timing data matters.

Use [Measure Goal Change Compare][perf-measure], [Run Correctness First][perf-correctness],
[Avoid Single Run Conclusions][perf-single-run], [Record Benchmark Provenance][perf-provenance],
and [Run Timing Benchmarks Sequentially][perf-sequential] when optimization work affects review
shape or validation cost.

Use [Smallest Trustworthy Verification][smallest-check] to choose the cheapest credible check. Use
[Report Verification Honestly][honest-verification] to distinguish what ran, what failed, and what
was not checked.

## Review Artifacts

Use issues for review-sized slices. Each issue should include the problem, scope, out-of-scope
work, behavior references, and acceptance criteria.
Use [Define Slices In Issues][issue-slices] when the issue itself needs to make a future review
unit clear.

### Issues And Discussion

For non-obvious work, start with an issue before opening the review change. Use the issue to discuss
use cases, constraints, requirements, prior art, solution tradeoffs, and maintenance load before the
patch asks reviewers to judge implementation details. Do not mix problem discovery, solution
selection, and implementation review when they need separate decisions. Use
[Separate Discovery Selection Implementation][review-decision-layers] when the problem, design
choice, and patch correctness need different review artifacts.

When a discussion is long, summarize it for reviewer decisions. Avoid low-signal status comments:
if there is a status change, update the issue, PR checklist, handoff, or other source of truth
instead of nudging reviewers. Use [Update Source Of Truth][review-source-truth] when an issue, PR,
checklist, or handoff should own the current state.

Treat review as a two-way discussion. When a reviewer asks about intent, tradeoffs, risk, behavior,
API shape, or alternatives, answer the question instead of only pushing new code; use
[Answer Questions Before Code][review-answer-questions] for that review pattern. Leave review
threads unresolved for the reviewer unless the resolution is unambiguous, and use
[Let Reviewers Resolve Threads][review-threads] when comment ownership affects review clarity.

### Plans

Use implementation plans for multi-phase work. A useful plan records current state, desired end
state, non-goals, approach, phases, automated verification, and manual verification. Use
[Make Plans Versioned Artifacts][versioned-plans] when a plan needs review, history, or resumption
outside the chat thread.

### Prototype Rebuilds

When rebuilding from a prototype or prior implementation, classify what is being reused:
externally visible behavior, evidence, replaceable shape, or load-bearing boundary.

Treat names, helper placement, crate boundaries, and document shape as replaceable unless they carry
a domain constraint.

Discuss load-bearing boundaries before replacing them. A smaller local API is not automatically
better if it centralizes an open-ended domain or removes room for independent growth.

Record prototype boundary review in the issue, PR notes, or ADR when the implementation depends on
earlier work.

Use [Classify Prototype Reuse][prototype-reuse] when a rebuild depends on behavior, evidence, or
boundaries discovered in a prototype.

### PR Narrative

Use PR descriptions or review packets to explain the summary, design notes, user-facing surface,
tests or validation, reference material, and follow-up.

For code changes that need technical narration, include the problem, mental model, non-goals,
tradeoffs, architecture impact, observability impact, validation, and documentation deltas. Describe
behavior and intent rather than walking through the diff line by line.

Label speculation as inferred or unknown. Link critical claims to evidence such as tests, call
sites, runtime behavior, source documentation, or generated artifacts.

Use [Explain PR Problem Model And Proof][pr-proof], [Explain Controversial Choices
Inline][inline-choices], [Label Speculation As Inferred Or Unknown][label-speculation], and
[Make Review Artifacts Standalone][standalone-review] when review narrative needs to preserve
reasoning for readers who did not see the discussion.

PR descriptions should name the generated surface that changed: generated samples should state which
generation commands ran, templates should state which templates changed, and feature-flag changes
should name the affected features.

### Durable Decisions

Use ADRs for durable decisions. Reach for them when a decision changes package boundaries, ownership
boundaries, parser architecture, policy, registry purpose, release scope, or another long-lived
shape.

Use ADRs when changing a load-bearing boundary that future changes will have to route through.

Use [Use ADRs For Boundaries And Ownership][adr-boundaries] when a decision changes long-lived
ownership, policy, parser, package, or registry shape.

## Commit History

Commit messages and jj descriptions are part of the change. They should help future readers
understand why the change exists and what decision it captured.

### Atomicity

A change is atomic when it can stand on its own: it fulfills one purpose, is minimal but complete,
and builds, formats, and passes its relevant tests when considered separately. Watch for scope
warnings such as `and` in the change description, dead code inside the diff, or fix-up changes after
CI or review that show the original change was not complete.

Use [Minimal But Complete][minimal-complete], [Treat And As Scope Warning][and-warning], and [Use
One Purpose Per Change][one-purpose] when shaping a change that needs to stand on its own.

### Review Path

Shape the review path so the important behavior change is easy to follow. Early test changes can
pin existing behavior before the patch changes it, and small refactor changes can act as guideposts
through a larger behavior change. Split refactors from behavior changes when the combined diff would
force reviewers to reverse engineer what changed, make each change's intent visible in its summary,
and isolate controversial changes so review attention does not starve unrelated work. Avoid
dependency changes that only make sense if a later controversial change lands.

Use [Commit Messages For History][commit-history] when setting jj descriptions or preparing
published commits. Follow the repository's commit convention; use Conventional Commits only where
the repo has already adopted that spec.
Use [Pin Behavior With Early Tests][early-tests] and [Isolate Controversial
Changes][controversial-changes] when the review path needs guidepost tests or a separate lane for a
risky decision.

## Related Guidance

Use [Change Shape Rules][change-rules] for compact instructions about change size, generated
artifacts, dependency churn, ownership, and structure-versus-behavior boundaries. The deeper reason
is [Change Shape Controls Review Cost][review-cost]: small coherent changes keep review effort tied
to the decision being made.

Use [Testing And Verification Rules][testing-rules] and
[Tests Should Explain Failures][test-proof] when choosing proof for behavior changes. Use
[Keep Binaries Out Of Source Control][binary-artifacts] before adding opaque artifacts to history,
and use [Mechanisms][mechanisms] when the change needs tooling, CI, lint, jj, or release support.

## Review Questions

### Review Change Shape

- Does this change have one coherent purpose?
- Did it reduce what a reader must remember?
- Did it preserve behavior or name the behavior change clearly?
- Did it follow local project conventions before general preference?
- Did it avoid overwriting unowned work?

### Review Verification

- Did verification target the likely failure?
- For performance work, did correctness run before timing and did benchmark evidence include enough
  provenance to compare later?
- Does the handoff say what actually ran?

### Review Artifact

- Does the review artifact name scope, non-scope, evidence, and follow-up?
- Does the review artifact explain the mental model, architecture impact, observability impact, and
  documentation delta when those changed?
- If this comes from a prototype, did the review separate behavior, evidence, replaceable shape, and
  load-bearing boundaries?

[commit-history]: ../patterns/commit-messages-for-history.md
[code-shape]: code-shape.md
[adr-boundaries]: ../rules/review/review-use-adrs-for-boundaries-and-ownership.md
[and-warning]: ../rules/change-shape/change-treat-and-as-scope-warning.md
[binary-artifacts]: ../rules/source/source-keep-binaries-out-of-source-control.md
[change-preserve-work]: ../rules/change-shape/change-preserve-unowned-work.md
[change-rules]: ../rules/change-shape/README.md
[command-proof]: ../rules/testing/test-prove-command-construction-and-display.md
[controversial-changes]: ../rules/change-shape/change-isolate-controversial-changes.md
[dependency-churn]: ../rules/change-shape/change-avoid-unnecessary-dependency-churn.md
[discovery-editing]: ../patterns/separate-discovery-from-editing.md
[docs-gate]: ../rules/testing/test-run-docs-as-first-class-gate.md
[early-tests]: ../rules/change-shape/change-pin-behavior-with-early-tests.md
[evidence-surface]: ../rules/testing/test-match-evidence-to-surface.md
[fast-gates]: ../rules/testing/test-run-fast-format-and-lint-gates-early.md
[generated-ownership]: ../rules/change-shape/change-respect-generated-artifact-ownership.md
[honest-verification]: ../patterns/report-verification-honestly.md
[inline-choices]: ../rules/review/review-explain-controversial-choices-inline.md
[issue-slices]: ../rules/review/review-define-slices-in-issues.md
[label-speculation]: ../rules/review/review-label-speculation-as-inferred-or-unknown.md
[local-conventions]: ../patterns/follow-local-conventions.md
[mechanisms]: ../mechanisms/README.md
[minimal-complete]: ../rules/change-shape/change-minimal-but-complete.md
[navigation-tests]: ../rules/testing/test-cover-navigation-boundaries.md
[one-purpose]: ../rules/change-shape/change-use-one-purpose-per-change.md
[owning-module]: ../rules/change-shape/change-identify-owning-module-before-editing.md
[perf-correctness]: ../rules/performance/perf-run-correctness-first.md
[perf-measure]: ../rules/performance/perf-measure-goal-change-compare.md
[perf-provenance]: ../rules/performance/perf-record-benchmark-provenance.md
[perf-sequential]: ../rules/performance/perf-run-timing-benchmarks-sequentially.md
[perf-single-run]: ../rules/performance/perf-avoid-single-run-conclusions.md
[preserve-work]: ../patterns/preserve-unowned-work.md
[pr-proof]: ../rules/review/review-explain-pr-problem-model-and-proof.md
[prototype-reuse]: ../rules/review/review-classify-prototype-reuse.md
[review-cost]: ../principles/change-shape-controls-review-cost.md
[review-answer-questions]: ../rules/review/review-answer-questions-before-code.md
[review-decision-layers]: ../rules/review/review-separate-discovery-selection-implementation.md
[review-source-truth]: ../rules/review/review-update-source-of-truth.md
[review-threads]: ../rules/review/review-let-reviewers-resolve-threads.md
[small-chunks]: ../patterns/small-reviewable-chunks.md
[small-follow-ups]: ../rules/change-shape/change-prefer-small-follow-ups.md
[smallest-check]: ../patterns/smallest-trustworthy-verification.md
[speculative-api]: ../rules/change-shape/change-avoid-speculative-public-api.md
[standalone-review]: ../rules/review/review-make-review-artifacts-standalone.md
[structure-behavior]: ../rules/change-shape/change-separate-structure-from-behavior.md
[sync-generated]: ../rules/change-shape/change-sync-generated-artifacts.md
[test-proof]: ../principles/tests-should-explain-failures.md
[testing-rules]: ../rules/testing/README.md
[validation-risk]: ../rules/testing/test-choose-validation-by-risk.md
[versioned-plans]: ../patterns/make-plans-versioned-artifacts.md
