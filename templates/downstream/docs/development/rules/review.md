# Private Context And Review Artifacts

Generated from the canonical `development-preferences` rule catalog. Do not edit copied rule
text by hand; update the source repo and recopy this file.

## Instructions

- `REVIEW-DEFINE-SLICES-IN-ISSUES`: Define review-sized slices in issues because issues are often
  the first place a future PR gets shaped.
- `REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`: Explain the problem, mental model, tradeoffs,
  validation, and docs impact so reviewers do not reverse-engineer intent from the diff.
- `REVIEW-LABEL-SPECULATION-AS-INFERRED-OR-UNKNOWN`: Label speculation as inferred or unknown
  because review notes often mix facts, traces, guesses, and model-based conclusions.
- `REVIEW-LET-REVIEWERS-RESOLVE-THREADS`: Let reviewers resolve review threads unless resolution is
  unambiguous; thread resolution is a communication act, not just a UI cleanup.
- `REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`: Make issues, PRs, commit messages, and handoffs stand
  alone for readers who did not see the chat, notes, plan, or discarded attempts.
- `REVIEW-USE-ADRS-FOR-BOUNDARIES-AND-OWNERSHIP`: Use ADRs for decisions that outlive a PR, such as
  ownership, API boundaries, storage formats, runtime responsibility, and service or crate
  boundaries.
