# Private Context And Review Artifacts

Review artifact rules cover issue slices, PR narratives, ADRs, speculation labels, thread ownership,
and artifacts that stand alone without private session context.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`REVIEW-ANSWER-QUESTIONS-BEFORE-CODE`](review-answer-questions-before-code.md). Answer reviewer
  questions before or alongside the code changes that address them. This keeps intent, tradeoffs,
  and unresolved choices visible instead of burying the reasoning in a new patch.
- [`REVIEW-CLASSIFY-PROTOTYPE-REUSE`](review-classify-prototype-reuse.md). Classify whether a
  rebuild is reusing behavior, evidence, replaceable internal shape, or load-bearing boundaries.
  That separation helps preserve proven compatibility while discarding prototype scaffolding.
- [`REVIEW-DEFINE-SLICES-IN-ISSUES`](review-define-slices-in-issues.md). Shape issues around
  review-sized slices with clear outcomes. Coherent slices reduce scope creep and give maintainers
  or agents a practical unit of work without losing the larger purpose.
- [`REVIEW-EXPLAIN-CONTROVERSIAL-CHOICES-INLINE`](review-explain-controversial-choices-inline.md).
  Treat capable reviewer questions about non-obvious code as documentation signals. Preserve the
  durable answer at the closest appropriate source boundary so future readers do not have to
  rediscover it.
- [`REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`](review-explain-pr-problem-model-and-proof.md). Use
  PR descriptions to explain the problem, mental model, tradeoffs, validation, and documentation
  impact. Reviewers can then evaluate the diff against stated intent instead of reverse-engineering
  it.
- [`REVIEW-LABEL-SPECULATION-AS-INFERRED-OR-UNKNOWN`](review-label-speculation-as-inferred-or-unknown.md).
  Mark review claims as observed, inferred, assumed, or unknown when the evidence level matters.
  Clear labels keep guesses from hardening into false project knowledge.
- [`REVIEW-LET-REVIEWERS-RESOLVE-THREADS`](review-let-reviewers-resolve-threads.md). Leave
  nontrivial review threads for the reviewer to resolve after they confirm the concern was
  addressed. Authors should only close unambiguous mechanical threads, because resolution carries
  communication ownership.
- [`REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`](review-make-review-artifacts-standalone.md). Put the
  needed problem, decision, context, validation, and risk in the issue, PR, commit, or handoff
  itself. Standalone artifacts make review and future debugging possible without private session
  context.
- [`REVIEW-SEPARATE-DISCOVERY-SELECTION-IMPLEMENTATION`](review-separate-discovery-selection-implementation.md).
  Split problem discovery, solution selection, and implementation review when they require different
  decisions. This keeps design debate out of patch correctness review once scope or direction is
  still unsettled.
- [`REVIEW-UPDATE-SOURCE-OF-TRUTH`](review-update-source-of-truth.md). Put durable status changes in
  the owning issue, PR description, checklist, plan, or handoff instead of posting low-signal
  comments. Updating the source of truth reduces notification churn and makes the current state
  discoverable.
- [`REVIEW-USE-ADRS-FOR-BOUNDARIES-AND-OWNERSHIP`](review-use-adrs-for-boundaries-and-ownership.md).
  Record durable ownership, API, storage, topology, runtime, or service-boundary decisions in ADRs.
  A decision record gives later contributors a stable tradeoff to affirm, revise, or replace.
