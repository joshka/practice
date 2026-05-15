# Rust Use Honest Minimum Dependencies

## Metadata

- ID: `RUST-USE-HONEST-MINIMUM-DEPENDENCIES`
- Legacy ID: `R-0243`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use the lowest honest compatible dependency requirement.

## Why

The manifest should state the lowest compatible dependency versions the crate honestly supports.
Overstating minimums reduces downstream flexibility; understating them breaks minimal-version builds
when newer APIs are used.

## Helps

Helps downstream users with older compatible dependency graphs build the crate without unnecessary
version pressure.

## Limits

Raise the minimum when a newer API, behavior fix, security patch, feature, or MSRV interaction is
actually required.

## Agent Instruction

Use the lowest honest compatible dependency requirement because the manifest should state the lowest
compatible dependency versions the crate honestly supports.

## Mechanisms

Set the manifest requirement to the lowest version that provides the APIs used, run minimal-version
checks where practical, and keep routine updates in the lockfile.

## References

- [Cargo Book: specifying
  dependencies](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
- [Cargo minimal-versions README](https://github.com/foresterre/cargo-minimal-versions#readme)
