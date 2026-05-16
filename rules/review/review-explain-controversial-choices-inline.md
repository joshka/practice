# Review Explain Controversial Choices Inline

## Metadata

- ID: `REVIEW-EXPLAIN-CONTROVERSIAL-CHOICES-INLINE`
- Status: `reviewed`
- Domain: `review`
- Depth: `compact`

## Rule

Explain controversial implementation choices next to the code or artifact where reviewers will see
them.

## Why

Some decisions are easiest to understand at the exact line, file, generated artifact, or config
boundary where the reviewer pauses. A PR body can explain the overall model, but a local inline note
can prevent reviewers from rediscovering why a surprising dependency, unsafe block, performance
tradeoff, generated output, policy exception, or temporary compatibility shape exists.

## Helps

- Turns likely review objections into explicit decision points.
- Keeps the PR narrative from becoming a long map of every local exception.
- Preserves context for future readers who land on a specific changed line or file.

## Limits

Do not annotate every ordinary choice. Inline explanation is useful for surprising or risky
decisions, not for restating obvious code or defending taste preferences.

## Agent Instruction

Place short inline notes beside surprising review decisions so reviewers see the rationale at the
line, file, generated artifact, or config boundary where the concern appears.

## Mechanisms

Supported by PR review comments, file comments, code comments for durable rationale, review packets,
and PR templates that ask for controversial choices or local exceptions.

## References

- [GitHub Docs: Commenting on a pull
  request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request)
- [GitHub Docs: Reviewing proposed changes in a pull
  request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request)
- [Review Explain PR Problem Model And Proof](review-explain-pr-problem-model-and-proof.md)
- [Write PR Narrative](../../patterns/write-pr-narrative.md)
