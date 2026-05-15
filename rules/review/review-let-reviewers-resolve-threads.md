# Review Let Reviewers Resolve Threads

## Metadata

- ID: `REVIEW-LET-REVIEWERS-RESOLVE-THREADS`
- Legacy ID: `R-0903`
- Status: `reviewed`
- Domain: `review`
- Depth: `compact`

## Rule

Let reviewers resolve review threads unless resolution is unambiguous.

## Why

Resolving a review thread is a communication act, not just a UI cleanup. If the author resolves a
thread after a nontrivial change, the reviewer may miss the chance to confirm that the concern was
actually addressed. Letting the reviewer resolve keeps ownership with the person who raised the
question.

## Helps

- Preserves reviewer trust and prevents important concerns from disappearing before they are
  rechecked.

## Limits

Resolve only clearly mechanical threads yourself, such as typo fixes or duplicate comments, and
leave a short note when the resolution might not be obvious from the diff.

## Agent Instruction

Let reviewers resolve review threads unless resolution is unambiguous; thread resolution is a
communication act, not just a UI cleanup.

## Mechanisms

Supported by review-thread discipline, explicit "addressed in ..." replies, follow-up commits that
name the concern, and PR summaries that call out remaining reviewer-owned threads.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Ed Page: PR style](https://epage.github.io/dev/pr-style/)
- [GitHub Docs: helping others review your
  changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes)
