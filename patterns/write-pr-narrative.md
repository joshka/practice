# Write PR Narrative

## Metadata

- Name: `Write PR Narrative`
- ID: `write-pr-narrative`
- Status: `reviewed`
- Audience: `both`
- Topics: `review, documentation, collaboration`
- Related: `produce-review-packets, report-verification-honestly`

## Problem

A pull request can contain correct code and still waste reviewer attention. Without purpose,
context, review order, risk, and verification, reviewers must reconstruct the story from the diff.
Future readers also lose the reasoning that connects a changelog entry, issue, commit, or bug hunt
back to the decision.

## Preferred Move

Write the PR narrative as a review guide. State the purpose, the shape of the change, the risky or
interesting decisions, user-facing surface, reference material used, how to review it, what was
verified, and what remains out of scope or follow-up. Frame the narrative around the decision the
reviewer needs to make, not only around the work already done.

## Tradeoff

Do not write a long essay for a tiny obvious change. Scale the narrative to the review burden. A
one-line summary can be enough when the diff is small, low-risk, and locally obvious.

## Agent Instruction

When preparing a review handoff, describe the change as part of the work. Include purpose, notable
decisions, user-facing surface, verification, follow-up, and any recommended review path through the
files. Call out deferred work, untested paths, and places where the implementation diverged from
prior discussion.

## Examples

Bad: the PR body repeats the title.

```markdown
Fix parser.
```

Good: the PR body gives the reviewer a path.

```markdown
Teach the config parser to reject duplicate table names before constructing the typed config.

Review `parser.rs` first for the new duplicate detection, then `error.rs` for the public error
variant. The user-facing surface is the new `DuplicateTable` error. Verified with
`cargo test -p config`. Follow-up: add migration-guide wording before the next release.
```

## References

| Source                      | Use        | Note                                                   |
| --------------------------- | ---------- | ------------------------------------------------------ |
| [epage PR style][epage-pr]  | `adapts`   | PRs should prepare reviewers and preserve reasoning.   |
| [GitHub PR guidance][pr]    | `supports` | PRs should give reviewers context and review guidance. |
| [GitHub issue links][links] | `adapts`   | PR narrative can connect the change to tracked work.   |

[epage-pr]: https://epage.github.io/dev/pr-style/
[links]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests
[pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes
