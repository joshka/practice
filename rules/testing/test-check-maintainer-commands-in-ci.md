# Test Check Maintainer Commands In CI

## Metadata

- ID: `TEST-CHECK-MAINTAINER-COMMANDS-IN-CI`
- Name: `Check Maintainer Commands in CI`
- Summary: Put documented maintainer commands, or intentionally stronger equivalents, in CI.
  This keeps local instructions honest while leaving slow or credentialed checks to special jobs.
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Check the same commands in CI that maintainers are expected to run locally.

## Why

If the README or maintainer guide says to run `cargo test`, `cargo doc`, `markdownlint-cli2`, or a
release check, CI should exercise the same command or an intentionally stronger equivalent.
Otherwise local guidance and actual merge gates drift apart.

## Helps

- Keeps contributor instructions honest and prevents maintainers from relying on checks that CI
  never runs.

## Limits

Some commands are too slow, platform-specific, or credential-dependent for every PR. Put those in
scheduled, release, or manual workflows and document the difference.

## Agent Instruction

If the README or maintainer guide says to run `cargo test`, `cargo doc`, `markdownlint-cli2`, or a
release check, CI should exercise the same command or an intentionally stronger equivalent, check
the same commands in CI that maintainers are expected to run locally.

## Mechanisms

Supported by CI workflows, local script wrappers, `just` recipes, required checks, scheduled jobs,
and README validation sections.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
