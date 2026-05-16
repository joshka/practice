# Rust Review As Future Maintainer

## Metadata

- Name: `Review As Future Maintainer`
- ID: `RUST-REVIEW-AS-FUTURE-MAINTAINER`
- Summary: Review Rust changes for the reader who will debug, extend, or release the code later, not
  only for immediate correctness. Favor maintainable API shape, docs, tests, and error behavior over
  changes that merely compile.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Review Rust changes from the perspective of a future maintainer who did not write the code.

## Why

Rust changes can compile and pass tests while leaving future readers with vague ownership,
surprising visibility, hidden side effects, unclear errors, or brittle feature behavior. Reviewing
as a future maintainer keeps the focus on the next person who must debug, extend, or release the
crate.

Ed Page's Rust style guide frames code as technical writing for reviewers and future debuggers. A
Rust review should therefore evaluate the reading path as well as the compiler path: where the main
concept appears, what invariants are visible, and whether the public contract matches the code.

## Helps

- Helps review prioritize correctness, public API clarity, documentation truth, and maintainability.

## Limits

Do not turn every review into a broad rewrite. Name the concrete cause when a module is hard to
read and keep fixes scoped to the owning concept. Prefer findings that identify a future failure
mode over taste-only comments.

## Agent Instruction

Review Rust changes for the future maintainer: name readability causes, public API risks, docs
truth, and validation gaps concretely.

## Mechanisms

Supported by code review findings with file references, focused checks, diff summaries, and
residual-risk handoffs.

## References

- [Rule: REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE](../review/review-make-review-artifacts-standalone.md)
- [Ed Page Rust Style: Principles](https://epage.github.io/dev/rust-style/#principles)
- [Pattern: Review Proof Not Just Code](../../patterns/review-proof-not-just-code.md)
