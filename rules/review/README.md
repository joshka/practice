# Private Context And Review Artifacts

Review artifact rules cover issue slices, PR narratives, ADRs, speculation labels, thread ownership,
and artifacts that stand alone without private session context.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`REVIEW-DEFINE-SLICES-IN-ISSUES`](review-define-slices-in-issues.md). Define review-sized slices
  in issues. Issues are often the first place a future PR gets shaped. Helps: Keeps issues
  actionable, prevents accidental scope creep, and gives agents a clear unit of work.
- [`REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`](review-explain-pr-problem-model-and-proof.md).
  Explain the problem, mental model, tradeoffs, validation, and docs impact in PR descriptions.
  Reviewers should not have to reverse-engineer the intent from the diff. Helps: Reduces reviewer
  guesswork, speeds review, and leaves future maintainers a useful explanation of why the change
  exists.
- [`REVIEW-LABEL-SPECULATION-AS-INFERRED-OR-UNKNOWN`](review-label-speculation-as-inferred-or-unknown.md).
  Label speculation as inferred or unknown. Review notes often mix facts, traces, guesses, and
  model-based conclusions. Helps: Makes risk visible, keeps review discussion precise, and helps
  future readers decide what still needs verification.
- [`REVIEW-LET-REVIEWERS-RESOLVE-THREADS`](review-let-reviewers-resolve-threads.md). Let reviewers
  resolve review threads unless resolution is unambiguous. Resolving a review thread is a
  communication act, not just a UI cleanup. Helps: Preserves reviewer trust and prevents important
  concerns from disappearing before they are rechecked.
- [`REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`](review-make-review-artifacts-standalone.md). Make
  issues, PRs, commit messages, and review handoffs stand alone. Issues, PR descriptions, commit
  messages, and agent handoffs are read by people who did not see the chat, scratch notes, local
  plan, or discarded attempts. Helps: Makes review possible without private context and leaves
  durable reasoning for future debugging, archaeology, and follow-up work.
- [`REVIEW-USE-ADRS-FOR-BOUNDARIES-AND-OWNERSHIP`](review-use-adrs-for-boundaries-and-ownership.md).
  Use ADRs for durable boundary and ownership decisions. Some decisions outlive the PR that
  introduces them: module ownership, public API boundaries, storage formats, source-control
  topology, runtime responsibility, and service or crate boundaries. Helps: Preserves architectural
  context, reduces repeated debate, and gives future changes a decision to affirm, revise, or
  replace.
