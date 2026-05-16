# Change Shape

Change-shape rules cover one-purpose changes, small follow-ups, generated artifacts, dependency
churn, ownership, and structure-versus-behavior review boundaries.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`CHANGE-AVOID-SPECULATIVE-PUBLIC-API`](change-avoid-speculative-public-api.md). Add public
  surfaces only when current or accepted callers need them. Waiting for concrete pressure keeps
  compatibility commitments smaller and easier to validate.
- [`CHANGE-AVOID-UNNECESSARY-DEPENDENCY-CHURN`](change-avoid-unnecessary-dependency-churn.md). Keep
  package, manifest, and lockfile movement out of unrelated work. Separate dependency changes make
  build, compatibility, and downstream risk reviewable on their own.
- [`CHANGE-IDENTIFY-OWNING-MODULE-BEFORE-EDITING`](change-identify-owning-module-before-editing.md).
  Find the component that owns the concept before adding or moving logic. That keeps invariants,
  tests, and future maintenance close to the responsible code.
- [`CHANGE-ISOLATE-CONTROVERSIAL-CHANGES`](change-isolate-controversial-changes.md). Put risky or
  contentious moves in their own review unit when they can stand alone. This lets reviewers approve,
  reject, or revise the decision without incidental cleanup attached.
- [`CHANGE-MINIMAL-BUT-COMPLETE`](change-minimal-but-complete.md). Keep the diff as small as the
  purpose allows while including the evidence that purpose needs. Reviewers should see one coherent
  unit they can understand, validate, and revert.
- [`CHANGE-PIN-BEHAVIOR-WITH-EARLY-TESTS`](change-pin-behavior-with-early-tests.md). Add
  characterization tests before changing messy behavior when the existing contract is unclear. The
  baseline separates intentional behavior changes from accidental drift.
- [`CHANGE-PREFER-SMALL-FOLLOW-UPS`](change-prefer-small-follow-ups.md). Move adjacent cleanup or
  broader improvements into focused follow-up changes when the current diff can stand alone. This
  preserves review focus while still capturing useful work.
- [`CHANGE-PRESERVE-UNOWNED-WORK`](change-preserve-unowned-work.md). Treat nearby edits from users,
  agents, generators, or earlier changes as outside your ownership unless the task says otherwise.
  Adapting around them protects parallel work and context.
- [`CHANGE-RESPECT-GENERATED-ARTIFACT-OWNERSHIP`](change-respect-generated-artifact-ownership.md).
  Fix generated outputs through their source inputs, templates, metadata, or generator configuration
  whenever those own the result. Hand edits are durable only when the tool workflow explicitly
  supports curation.
- [`CHANGE-SEPARATE-STRUCTURE-FROM-BEHAVIOR`](change-separate-structure-from-behavior.md). Split
  refactoring or layout changes from behavior changes when the combined diff obscures intent.
  Separate review units make meaning preservation and new behavior easier to check.
- [`CHANGE-SYNC-GENERATED-ARTIFACTS`](change-sync-generated-artifacts.md). Update checked-in
  generated outputs when their source inputs change and they are part of review. Keeping them
  aligned prevents consumers from seeing stale artifacts.
- [`CHANGE-TREAT-AND-AS-SCOPE-WARNING`](change-treat-and-as-scope-warning.md). Use compound change
  descriptions as a prompt to inspect whether the work has more than one purpose. The word is not a
  rule, but it catches scope creep while splitting is still cheap.
- [`CHANGE-USE-ONE-PURPOSE-PER-CHANGE`](change-use-one-purpose-per-change.md). Shape each change
  around one review question and one reason for existing. Related tests, docs, and generated files
  can travel with it when they support that same purpose.
