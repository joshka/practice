# Review Update Source Of Truth

## Metadata

- Name: `Update Source of Truth`
- ID: `REVIEW-UPDATE-SOURCE-OF-TRUTH`
- Summary: Put durable status changes in the owning issue, PR description, checklist, plan, or
  handoff instead of posting low-signal comments. Updating the source of truth reduces notification
  churn and makes the current state discoverable.
- Status: `reviewed`
- Domain: `review`
- Depth: `compact`

## Rule

Update the source of truth instead of posting low-signal status comments.

## Why

Status comments can be useful when they change what reviewers know. They become noise when they only
say that work is ongoing, restate that someone should review, or duplicate information that belongs
in the issue body, PR description, checklist, milestone, commit, or review packet. The next reader
then has to reconstruct state from a comment stream instead of the artifact that owns the decision.

Updating the source of truth keeps the current scope, blocker, acceptance state, and next action in
one durable place. It also reduces notification churn and makes future agents or maintainers load
the right artifact instead of scanning for the latest nudge.

## Helps

- Keeps review state discoverable from the artifact that owns it.
- Reduces notification noise and comment archaeology.

## Limits

Use comments when a person needs a direct answer, a decision needs visible acknowledgement, or a
temporary blocker should notify reviewers. Even then, update the owning issue, PR description,
checklist, or plan when the status should remain true after the notification is read.

## Agent Instruction

Update the owning issue, PR description, checklist, plan, or handoff for durable status changes;
avoid comments that only nudge reviewers or restate current progress.

## Mechanisms

Supported by issue bodies, PR descriptions, task checklists, project fields, milestones, review
packets, and handoffs that name the current blocker, next action, and acceptance state.

## References

- [Review Make Review Artifacts Standalone](review-make-review-artifacts-standalone.md)
- [GitHub Docs: About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [GitHub Docs: About task lists](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-tasklists)
- [GitHub Docs: Helping others review your changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes)
