# Test Run Docs As First Class Gate

## Metadata

- ID: `TEST-RUN-DOCS-AS-FIRST-CLASS-GATE`
- Name: `Run Docs as a First-Class Gate`
- Summary: Treat documentation checks as real validation for examples, links, commands, and claims.
  Prose-only edits may need less proof, but API-facing docs should fail before stale guidance ships.
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Run docs as a first-class validation job.

## Why

Docs contain commands, examples, feature claims, public API paths, and Rustdoc links. Treating docs
as a secondary check lets stale examples and broken rendered docs ship even when code tests pass.

## Helps

- Keeps documentation, examples, and public API contracts aligned with code.

## Limits

Small prose-only edits may only need markdown lint and link review. Run stronger docs gates when
examples, Rustdoc, features, or public behavior claims change.

## Agent Instruction

Run docs as a first-class validation job because docs contain commands, examples, feature claims,
public API paths, and Rustdoc links.

## Mechanisms

Supported by `markdownlint-cli2`, `cargo test --doc`, `cargo doc --no-deps`, docs.rs-style builds,
link checks, and rendered-doc review.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
