# Software Change Preferences

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

Use one feature, bug fix, or documentation purpose per change.
Do not include unrelated refactors.
Do not include dependency churn unless it is necessary for the task.
Do not commit binary artifacts; use Git LFS, release assets, PR uploads, CI artifacts, or external
storage for large opaque outputs.
Do not move broad modules unless the reader path improves.
Do not add speculative public API for future features.
If a change reveals separate cleanup, note it or put it in a separate change.
Prefer small follow-up changes over overloaded commits.
Keep generated artifacts in sync when they are part of the review surface.
Do not edit generated changelogs when release tooling owns them.

Use [Small Reviewable Chunks][small-chunks] when a change could grow into multiple review concerns.
When structure and behavior can be separated cleanly, land the structure change first and verify it
before changing behavior.
Use [Code Shape][code-shape] when the main decision is how to reduce live context, limit change
radius, preserve reversibility, or clarify cohesion and coupling.

## Local Context

Read the repo before applying general preferences. Local instructions, existing helpers, naming
schemes, tests, and version-control workflow usually contain information that a general guide cannot
know.

Identify the owning module before editing.
Identify adjacent modules that the owning module depends on.
Identify the test style already used for the behavior.
Prefer the existing style when it is coherent.
Improve local structure when the existing shape is actively making the change harder to understand.
Keep that improvement scoped to the same concept.

Use [Follow Local Conventions][local-conventions] when general guidance and project shape might
conflict. Use [Separate Discovery From Editing][discovery-editing] when the local shape is not clear
enough to edit confidently.

## Working Copy Care

Assume unowned edits belong to someone. Do not revert, rewrite, or absorb work just because it makes
the current diff look cleaner.

Use [Preserve Unowned Work][preserve-work] when a shared working copy has pre-existing edits or
changes appear while work is in progress.

## Verification

Choose verification by the risk of the change. Formatting changes need formatting checks, signature
changes need type or build checks, behavior changes need tests or smoke checks that exercise the
changed path.

Decide the narrowest useful validation command before editing.
Run focused tests for touched behavior.
Run the project gate when practical.
Run Markdown linting for Markdown-only or doc-heavy changes.
Report validation gaps directly.
Validate template changes against generated output, not only the template source.
Regenerate affected reference projects when templates change.
Run checks inside generated projects when generated projects are what users receive.
Smoke-test interactive flows when event loops, terminal setup, or terminal teardown changed.
Attach screenshots, GIFs, or before/after context when visible UI output changed.
Document manual verification when CLI or TUI behavior lacks automated coverage.

For optimization work, use one change per optimization idea. Record the hypothesis and expected
mechanism before touching hot code, run correctness before timing, and keep failed ideas useful by
recording why the evidence did not support them.

Do not make keep/revert decisions from one short benchmark run. Use increasingly expensive evidence
only when the previous step justifies it: counters, phase timers, per-case rows, hot-function maps,
microbenchmarks, profilers, and assembly inspection. Record exact commands, versions, hashes,
environment, corpus, raw samples, and interpretation for benchmark results worth comparing later.

Never run benchmarks in parallel when timing data matters.

Use [Smallest Trustworthy Verification][smallest-check] to choose the cheapest credible check. Use
[Report Verification Honestly][honest-verification] to distinguish what ran, what failed, and what
was not checked.

## Review Artifacts

Use issues for review-sized slices. Each issue should include the problem, scope, out-of-scope
work, behavior references, and acceptance criteria.

For non-obvious work, start with an issue before opening the review change.
Use the issue to discuss use cases, constraints, requirements, prior art, and solution tradeoffs.
Do not mix problem discovery, solution selection, and implementation review when they need separate
decisions.
When a discussion is long, summarize it for reviewer decisions.
Summaries should cover use cases, requirements, project constraints, prior art, solution tradeoffs,
and maintenance load.
Avoid low-signal status comments.
If there is a status change, update the source of truth instead of nudging reviewers.
Treat review as a two-way discussion.
Answer reviewer questions instead of only pushing new code.
Leave review threads unresolved for the reviewer unless the resolution is unambiguous.

Use implementation plans for multi-phase work. A useful plan records current state, desired end
state, non-goals, approach, phases, automated verification, and manual verification.

When rebuilding from a prototype or prior implementation, classify what is being reused:
externally visible behavior, evidence, replaceable shape, or load-bearing boundary.

Treat names, helper placement, crate boundaries, and document shape as replaceable unless they carry
a domain constraint.

Discuss load-bearing boundaries before replacing them. A smaller local API is not automatically
better if it centralizes an open-ended domain or removes room for independent growth.

Record prototype boundary review in the issue, PR notes, or ADR when the implementation depends on
earlier work.

Use PR descriptions or review packets to explain the summary, design notes, user-facing surface,
tests or validation, reference material, and follow-up.

For code changes that need technical narration, include the problem, mental model, non-goals,
tradeoffs, architecture impact, observability impact, validation, and documentation deltas. Describe
behavior and intent rather than walking through the diff line by line.

Label speculation as inferred or unknown. Link critical claims to evidence such as tests, call
sites, runtime behavior, source documentation, or generated artifacts.

PRs that touch generated samples should state which generation commands ran.
PRs that touch templates should state which templates changed.
PRs that touch feature flags should name the affected features.

Use ADRs for durable decisions. Reach for them when a decision changes package boundaries, ownership
boundaries, parser architecture, policy, registry purpose, release scope, or another long-lived
shape.

Use ADRs when changing a load-bearing boundary that future changes will have to route through.

## Commit History

Commit messages and jj descriptions are part of the change. They should help future readers
understand why the change exists and what decision it captured.

Each change should be minimal but complete.
Each change should fulfill a single purpose.
Each change should build, format, and pass its relevant tests when considered on its own.
The word `and` in a change description is a warning sign that the change may have two purposes.
Dead code inside a change is a warning sign that the change is not complete.
Fix-up changes after CI or review are a warning sign that the original change was not atomic.
Use early test changes to reproduce the existing behavior when that makes the behavior change easier
to review.
Structure test diffs so they emphasize the key behavior change and minimize noise.
Split refactors from behavior changes when the combined diff would force reviewers to reverse
engineer what changed.
Use small refactor changes as guideposts through a larger behavior change.
Make each change's intent visible in its summary.
Isolate controversial changes so review attention does not starve unrelated work.
Do not create a dependency change that only makes sense if the later controversial change lands.

Use [Commit Messages For History][commit-history] when setting jj descriptions or preparing
published commits. Follow the repository's commit convention; use Conventional Commits only where
the repo has already adopted that spec.

## Related Guidance

Use [Change Shape Rules][change-rules] for compact instructions about change size, generated
artifacts, dependency churn, ownership, and structure-versus-behavior boundaries. Use
[Change Shape Controls Review Cost][review-cost] for the reasoning behind small coherent changes.
Use [Testing And Verification Rules][testing-rules] and [Tests Should Explain Failures][test-proof]
when choosing proof for behavior changes. Use
[Keep Binaries Out Of Source Control][binary-artifacts] before adding opaque artifacts to history.
Use [Mechanisms][mechanisms] when the change needs tooling, CI, lint, jj, or release support.

## Review Questions

- Does this change have one coherent purpose?
- Did it reduce what a reader must remember?
- Did it preserve behavior or name the behavior change clearly?
- Did it follow local project conventions before general preference?
- Did it avoid overwriting unowned work?
- Did verification target the likely failure?
- For performance work, did correctness run before timing and did benchmark evidence include enough
  provenance to compare later?
- Does the handoff say what actually ran?
- Does the review artifact name scope, non-scope, evidence, and follow-up?
- Does the review artifact explain the mental model, architecture impact, observability impact, and
  documentation delta when those changed?
- If this comes from a prototype, did the review separate behavior, evidence, replaceable shape, and
  load-bearing boundaries?

[commit-history]: ../patterns/commit-messages-for-history.md
[code-shape]: code-shape.md
[binary-artifacts]: ../rules/source/source-keep-binaries-out-of-source-control.md
[change-rules]: ../rules/change-shape/README.md
[discovery-editing]: ../patterns/separate-discovery-from-editing.md
[honest-verification]: ../patterns/report-verification-honestly.md
[local-conventions]: ../patterns/follow-local-conventions.md
[mechanisms]: ../mechanisms/README.md
[preserve-work]: ../patterns/preserve-unowned-work.md
[review-cost]: ../principles/change-shape-controls-review-cost.md
[small-chunks]: ../patterns/small-reviewable-chunks.md
[smallest-check]: ../patterns/smallest-trustworthy-verification.md
[test-proof]: ../principles/tests-should-explain-failures.md
[testing-rules]: ../rules/testing/README.md
