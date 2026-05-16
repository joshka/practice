# Rust Keep Rustdoc And Readme Examples Aligned

## Metadata

- Name: `Keep Rustdoc and README Examples Aligned`
- ID: `RUST-KEEP-RUSTDOC-AND-README-EXAMPLES-ALIGNED`
- Summary: Keep README, Rustdoc, generated docs, and example directories teaching the same current
  usage contract. Aligned examples prevent users from guessing which import path or lifecycle is
  correct.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep README examples, Rustdoc examples, generated README content, and example directories aligned.

## Why

Rust crates often teach the same API in several places. When examples drift, users cannot tell
which import path, feature flag, error behavior, or lifecycle pattern is current.

The Rust API Guidelines treat crate-level docs, item examples, metadata, and release notes as part
of the user-facing package story. README examples, crate Rustdoc, generated README content, and
`examples/` should therefore agree on the current contract even when each artifact serves a
different reader task.

## Helps

- Helps public documentation present one coherent usage contract.

## Limits

Examples can differ by audience or depth. Keep the contract, imports, feature assumptions, and
visible behavior consistent. Prefer generating repeated snippets from one source when the project
already has that machinery.

## Agent Instruction

Update README, crate Rustdoc, doctests, and example projects together for Rust public example
changes that teach the same contract.

## Mechanisms

Supported by doctests, README generation, example builds, docs builds with warnings denied, and
markdown lint.

## References

- [Rustdoc: documentation tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
- [Rust API Guidelines: Documentation](https://rust-lang.github.io/api-guidelines/documentation.html)
- [Rule: DOCS-ALIGN-README-AND-CRATE-RUSTDOC](../documentation/docs-align-readme-and-crate-rustdoc.md)
