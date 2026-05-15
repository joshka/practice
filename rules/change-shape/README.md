# Change Shape

Change-shape rules cover one-purpose changes, small follow-ups, generated artifacts, dependency
churn, ownership, and structure-versus-behavior review boundaries.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`CHANGE-AVOID-UNNECESSARY-DEPENDENCY-CHURN`](change-avoid-unnecessary-dependency-churn.md). Do
  not include dependency churn unless it is necessary for the task. Dependency updates change
  lockfiles, feature graphs, minimum versions, build output, and downstream compatibility. Helps:
  Keeps dependency risk reviewable and prevents unrelated lockfile movement from obscuring the task.
- [`CHANGE-IDENTIFY-OWNING-MODULE-BEFORE-EDITING`](change-identify-owning-module-before-editing.md).
  Identify the owning module before editing. Editing the first file that mentions a behavior can put
  new logic in a caller, facade, test helper, or adapter that does not own the concept. Helps:
  Reduces scattered fixes and makes future readers find the behavior where they expect it.
- [`CHANGE-ISOLATE-CONTROVERSIAL-CHANGES`](change-isolate-controversial-changes.md). Isolate
  controversial changes. Formatting, renames, API breaks, dependency changes, unsafe code, large
  rewrites, and behavior changes all invite different review questions. Helps: Keeps contentious
  decisions explicit and makes reverting or revising them cheaper.
- [`CHANGE-MINIMAL-BUT-COMPLETE`](change-minimal-but-complete.md). Keep each change minimal but
  complete. A change that is too large hides risk, but a change that is too small can leave
  reviewers with an unexplained half-step. Helps: Gives reviewers a coherent unit that can be
  understood, validated, and reverted.
- [`CHANGE-PIN-BEHAVIOR-WITH-EARLY-TESTS`](change-pin-behavior-with-early-tests.md). Use early test
  changes to pin existing behavior when that makes behavior changes easier to review. Before
  changing messy behavior, an early test can document what the system currently does. Helps: Makes
  behavior changes safer and clarifies whether later diffs preserve or intentionally change existing
  behavior.
- [`CHANGE-PREFER-SMALL-FOLLOW-UPS`](change-prefer-small-follow-ups.md). Prefer small follow-up
  changes over overloaded changes. When a change uncovers adjacent cleanup, docs drift, naming
  issues, or broader refactoring, folding all of it into the current diff can hide the original
  purpose. Helps: Preserves review focus while still capturing useful nearby work.
- [`CHANGE-PRESERVE-UNOWNED-WORK`](change-preserve-unowned-work.md). Preserve unowned work. A
  working tree can contain edits from the user, another agent, generated state, or an earlier
  in-progress change. Helps: Protects parallel work and keeps the current diff accountable for only
  the files it owns.
- [`CHANGE-SEPARATE-STRUCTURE-FROM-BEHAVIOR`](change-separate-structure-from-behavior.md). Keep
  structure changes separate from behavior changes when the combined diff obscures review. Structure
  changes ask reviewers to confirm the code means the same thing; behavior changes ask them to
  confirm the system now does the right new thing. Helps: Makes reviews sharper and makes
  structure-only changes easier to revert if they were wrong.
- [`CHANGE-SYNC-GENERATED-ARTIFACTS`](change-sync-generated-artifacts.md). Keep generated artifacts
  in sync when they are part of the review surface. Generated files, lockfiles, snapshots, API
  listings, and agent packs are part of the review surface when they are checked into the repo.
  Helps: Prevents drift between source inputs and generated outputs.
- [`CHANGE-TREAT-AND-AS-SCOPE-WARNING`](change-treat-and-as-scope-warning.md). Treat `and` in a
  change description as a scope warning. A change titled "fix parser and update docs and clean API"
  often contains multiple review units. Helps: Catches accidental scope creep before the diff
  becomes hard to split.
- [`CHANGE-USE-ONE-PURPOSE-PER-CHANGE`](change-use-one-purpose-per-change.md). Use one purpose per
  change. One-purpose changes let reviewers ask one main question: did this accomplish the stated
  goal? Helps: Improves review speed, revertability, and historical understanding of why code
  changed.
