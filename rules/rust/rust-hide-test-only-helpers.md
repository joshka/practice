# Rust Hide Test Only Helpers

## Metadata

- ID: `RUST-HIDE-TEST-ONLY-HELPERS`
- Legacy ID: `R-0231`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep test-only helpers out of the normal public API.

## Why

Test-only helpers should not become production API or crate-wide concepts by accident. Keeping them
behind `#[cfg(test)]`, in test modules, or in test support crates prevents callers and docs from
depending on scaffolding.

## Helps

Helps keep normal APIs free of fixtures, shortcuts, and constructors that exist only to make tests
convenient.

## Limits

Expose test support deliberately when downstream users need it, such as a `test-support` feature,
fixtures crate, or documented integration-testing helper.

## Agent Instruction

Keep test-only helpers out of the normal public API because test-only helpers should not become
production API or crate-wide concepts by accident.

## Mechanisms

Put helpers under `#[cfg(test)]`, dev-dependencies, integration-test modules, or explicitly named
test-support features instead of normal public modules.

## References

- [Rust Book: test organization](https://doc.rust-lang.org/book/ch11-03-test-organization.html)
- [Cargo Book: features](https://doc.rust-lang.org/cargo/reference/features.html)
