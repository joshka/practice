# Test Run Fast Format And Lint Gates Early

## Metadata

- ID: `TEST-RUN-FAST-FORMAT-AND-LINT-GATES-EARLY`
- Name: `Run Fast Format and Lint Gates Early`
- Summary: Run cheap format and lint gates early in the feedback loop.
  They remove mechanical failures quickly, but they do not replace validation of risky behavior.
- Status: `reviewed`
- Domain: `testing`
- Tags: `testing, tooling, automation, reviewability`
- Related: `close-the-agent-loop, test-keep-slow-checks-out-of-pr-ci`

## Rule

Run formatting and clippy early because they fail fast.

## Why

Formatting and lint failures are cheap to find and noisy to review. Running them early prevents a
long implementation or test run from ending with mechanical failures that could have been fixed
immediately.

## Helps

- Shortens feedback loops and keeps review focused on behavior instead of mechanics.

## Limits

Do not let lint polish displace higher-risk correctness validation. Run fast gates early, then still
run the checks that match the change.

## Agent Instruction

Run formatting and clippy early because those failures are cheap to find and noisy to review.

## Mechanisms

Supported by `cargo fmt --check`, `cargo clippy`, `markdownlint-cli2`, editor formatters, and CI
jobs that fail fast before slower suites.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
