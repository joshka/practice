# Review Answer Questions Before Code

## Metadata

- ID: `REVIEW-ANSWER-QUESTIONS-BEFORE-CODE`
- Status: `reviewed`
- Domain: `review`
- Depth: `compact`

## Rule

Answer reviewer questions instead of only pushing new code.

## Why

Review is a discussion about correctness, maintainability, and intent. A code push can fix the
immediate diff while leaving the reviewer unsure whether the question was understood, whether an
alternative was considered, or whether the remaining behavior is deliberate. That uncertainty often
causes another round of review even when the code is now acceptable.

Answering the question makes the decision visible. Sometimes the answer is "changed as suggested."
Sometimes it is a short explanation of why another approach was chosen. Either way, future readers
can see the reasoning instead of inferring it from a later diff.

## Helps

- Reduces repeated review rounds caused by unanswered concerns.
- Preserves design reasoning that would otherwise disappear into a patch update.

## Limits

Do not turn every small nit into a long thread. For obvious mechanical fixes, a short acknowledgement
or the code change itself can be enough. Use explicit answers when the reviewer asked about intent,
tradeoffs, risk, behavior, API shape, or alternatives.

## Agent Instruction

Answer reviewer questions before or with code updates so intent, tradeoffs, and remaining choices
are visible instead of buried in a new patch.

## Mechanisms

Supported by reply comments, review packets, PR description updates, inline follow-up notes,
decision links, and handoffs that separate what changed from what was intentionally left unchanged.

## References

- [Review Explain PR Problem Model And Proof](review-explain-pr-problem-model-and-proof.md)
- [Review Make Review Artifacts Standalone](review-make-review-artifacts-standalone.md)
- [Google Engineering Practices: How to handle reviewer comments](https://google.github.io/eng-practices/review/developer/handling-comments.html)
