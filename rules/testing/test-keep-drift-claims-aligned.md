# Test Keep Drift Claims Aligned

## Metadata

- ID: `TEST-KEEP-DRIFT-CLAIMS-ALIGNED`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Keep support claims, fixtures, docs, examples, and API paths aligned with drift tests.

## Why

Support matrices, fixtures, docs, examples, and public API paths often drift independently. Drift
tests should check the claim and the artifacts that carry it so a doc does not promise a parser,
platform, or feature path the code no longer supports.

## Helps

- Keeps user-facing support claims tied to executable evidence.

## Limits

Do not make drift checks so broad that every wording edit breaks tests. Check stable claims,
generated lists, examples, and paths that users depend on.

## Agent Instruction

Use drift tests to keep support claims, fixtures, docs, examples, and public API paths aligned.

## Mechanisms

Supported by generated docs checks, fixture inventories, API path tests, support-matrix validation,
and link or example checks in CI.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
