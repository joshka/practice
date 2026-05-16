# Rust Group Module Imports

## Metadata

- ID: `RUST-GROUP-MODULE-IMPORTS`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Prefer grouped module imports over one-import-per-line style.

## Why

Grouped module imports keep related names together and make dependencies easier to scan.
One-import-per-line style can exaggerate churn and hide that several imports come from the same
conceptual module.

## Helps

Helps readers see dependency shape by module and reduces churn from one-import-per-line edits.

## Limits

Follow local convention when the crate intentionally uses single-item imports, especially where
rustfmt or team style is already settled.

## Agent Instruction

Prefer grouped module imports over one-import-per-line style because grouped module imports keep
related names together and make dependencies easier to scan.

## Mechanisms

Group imports by source module, let rustfmt normalize ordering, and avoid expanding grouped imports
unless doing so clarifies conflicting names or public re-exports.

## References

- [Ed Page Rust Style: imports](https://epage.github.io/dev/rust-style/)
- [rustfmt configuration](https://rust-lang.github.io/rustfmt/)
