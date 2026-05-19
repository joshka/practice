# Test Keep Slow Checks Out Of PR CI

## Metadata

- ID: `TEST-KEEP-SLOW-CHECKS-OUT-OF-PR-CI`
- Name: `Keep Slow Checks out of PR CI`
- Summary: Keep long fuzzing, exhaustive matrices, and noisy benchmarks out of required PR CI.
  Fast gates preserve review flow, while heavier checks belong in release or scheduled validation.
- Status: `reviewed`
- Domain: `testing`
- Tags: `testing, automation, reviewability, performance`
- Related: `budget-tokens-for-feedback-loops, test-choose-validation-by-risk`

## Rule

Keep slow fuzzing, long benchmarks, and exhaustive compatibility checks out of required PR CI unless
they are fast and deterministic.

## Why

Required PR CI should give fast, reliable feedback. Long fuzz runs, exhaustive feature matrices, and
noisy benchmarks can block unrelated work or train contributors to ignore failures when they are
part of the default gate.

## Helps

- Keeps normal review fast while preserving heavier checks for release or scheduled validation.

## Limits

Run slow checks in PR CI when they are the only trustworthy gate for a high-risk change or when they
have become fast and deterministic enough for the normal loop.

## Agent Instruction

Keep slow fuzzing, long benchmarks, and exhaustive compatibility checks outside required PR CI
unless they are fast and deterministic.

## Mechanisms

Supported by scheduled CI, release workflows, manual dispatch jobs, labeled heavy-check jobs, and PR
summaries that report which heavy checks did or did not run.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
