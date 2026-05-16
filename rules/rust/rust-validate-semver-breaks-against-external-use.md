# Rust Validate Semver Breaks Against External Use

## Metadata

- ID: `RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Validate semver-breaking changes against real external use.

## Why

Semver tools can detect many API breaks, but real downstream code shows how the public surface is
actually used. Validate breaking changes against external examples or known users before assuming
migration cost is acceptable.

## Helps

Helps distinguish theoretical API cleanup from real downstream breakage, especially for library
crates with examples, tutorials, and external dependents.

## Limits

External usage searches are evidence, not veto power. Security, soundness, correctness, or strategic
API repair can justify a break with clear release notes.

## Agent Instruction

Validate semver-breaking changes against real external use because semver tools can detect many API
breaks, but real downstream code shows how the public surface is actually used.

## Mechanisms

Use public API diff tools, crater-like checks where available, reverse-dependency searches, example
builds, migration notes, and explicit semver labeling.

## References

- [Cargo Book: SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html)
- [cargo-semver-checks README](https://github.com/obi1kenobi/cargo-semver-checks#readme)
