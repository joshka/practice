# Test Validate Declared Minimum Dependency Versions

## Metadata

- ID: `TEST-VALIDATE-DECLARED-MINIMUM-DEPENDENCY-VERSIONS`
- Legacy ID: `R-0431`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Validate declared minimum dependency versions.

## Why

Cargo manifests communicate the minimum compatible versions a downstream project may resolve. If the
crate uses APIs introduced after the declared minimum, users with minimal resolution fail even
though normal lockfile tests pass.

## Helps

- Keeps dependency requirements honest and protects downstream minimal-version builds.

## Limits

Minimal-version checks can be slow or affected by transitive ecosystem issues. Use `--direct` or
targeted checks when the direct dependency floor is the relevant contract.

## Agent Instruction

Validate declared minimum dependency versions because cargo manifests communicate the minimum
compatible versions a downstream project may resolve.

## Mechanisms

Supported by `cargo minimal-versions check --direct`, direct minimal-resolution jobs, manifest
review, dependency automation configured with `increase-if-necessary`, and lockfile-only update PRs.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
