# Review Preserve Durable Answers Near Source

## Metadata

- Name: `Preserve Durable Answers Near Source`
- ID: `REVIEW-EXPLAIN-CONTROVERSIAL-CHOICES-INLINE`
- Summary: Treat capable reviewer questions about non-obvious code as documentation signals.
  Preserve the durable answer at the closest appropriate source boundary so future readers do not
  have to rediscover it.
- Status: `reviewed`
- Domain: `review`
- Tags: `reviewability, reader-locality`
- Related: `reader-locality, run-source-explanation-pass, keep-docs-near-their-subject,
  private-context-is-not-shared-context, RUST-AVOID-OVERCOMMENTING-TRIVIAL-CODE`

## Rule

When a capable reviewer has to ask how or why non-obvious code works, treat the question as a
documentation signal. Preserve the durable part of the answer at the closest source boundary that
owns it.

## Why

A capable reviewer is a useful proxy for future maintainers and agents. If that reviewer cannot
derive an important explanation from the code and its nearby contracts, later readers will probably
repeat the same investigation without the benefit of the review conversation.

The question is evidence, not an automatic request for a comment. Clearer naming or structure may
remove the mystery. When the answer carries stable knowledge that code cannot express cleanly,
preserving it at the owning boundary turns temporary review context into shared source context.

## Helps

- Makes reviewer confusion an explicit check for missing source context.
- Preserves invariants, sequencing constraints, surprising conditions, plausible-but-wrong
  simplifications, and failure modes where future changes encounter them.
- Routes behavior, contracts, mental models, and change-specific rationale to artifacts that can
  keep each kind of explanation accurate.

## Limits

First prefer clearer naming, control flow, types, or structure when they make the behavior evident
without hiding a useful local story. Do not preserve trivial or one-off confusion, taste
preferences, incidental implementation details, speculative rationale, or explanations likely to
drift without a stable contract.

Choose the artifact by the answer's job:

- Use a local code comment for an invariant, parser or event sequence, surprising condition,
  plausible-but-wrong simplification, or failure mode that remains non-obvious in clear code.
- Use a test to preserve observable behavior and a regression boundary.
- Use item Rustdoc for a caller-facing contract and module or crate docs for a shared mental model.
- Use PR or commit prose only for change-specific context that does not need to remain beside the
  resulting source.

A review question is not proof that ordinary readers need prose. Answer the immediate question, then
keep only the stable knowledge whose absence would make a future reader infer or rediscover
something material. Do not add comments that translate syntax or narrate straightforward code.

## Agent Instruction

Use capable reviewer questions about non-obvious code as documentation signals. Prefer clearer code;
otherwise preserve the durable answer in the nearest comment, test, Rustdoc, module docs, or change
narrative that owns it.

## Mechanisms

Supported by review replies that distinguish immediate clarification from durable knowledge, code
comments, behavior tests, Rustdoc, module docs, review packets, and PR or commit narratives.

## References

- [Google Engineering Practices: How to write code review
  comments](https://google.github.io/eng-practices/review/reviewer/comments.html)
- [Google Engineering Practices: What to look for in a code
  review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
- [Keep Docs Near Their Subject](../../patterns/keep-docs-near-their-subject.md)
- [Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Rust Avoid Overcommenting Trivial
  Code](../rust/rust-avoid-overcommenting-trivial-code.md)
