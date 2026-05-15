# Test Check Important Feature Combinations

## Metadata

- ID: `TEST-CHECK-IMPORTANT-FEATURE-COMBINATIONS`
- Legacy ID: `R-0422`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Test all features and important feature combinations.

## Why

Rust feature flags can change public API, optional dependencies, cfg-gated docs, and compile paths.
Testing only the default feature set can miss that `no-default-features`, `all-features`, or
important feature pairs no longer compile or no longer expose the documented API.

## Helps

- Catches feature-gated regressions before downstream users combine features differently than the
  maintainer did.

## Limits

Do not test every theoretical feature combination when the matrix explodes. Choose default,
no-default, all-features, each-feature, and important known interactions based on risk.

## Agent Instruction

Test all features and important feature combinations because rust feature flags can change public API,
optional dependencies, cfg-gated docs, and compile paths.

## Mechanisms

Supported by `cargo hack`, selected CI matrices, feature-specific doctests, `cargo tree -e
features`, and documented feature support policy.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
