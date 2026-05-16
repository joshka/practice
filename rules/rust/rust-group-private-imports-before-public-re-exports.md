# Rust Group Private Imports Before Public Re Exports

## Metadata

- ID: `RUST-GROUP-PRIVATE-IMPORTS-BEFORE-PUBLIC-RE-EXPORTS`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Group private imports before public re-exports.

## Why

Private imports and public re-exports answer different questions. Grouping private `use` statements
before `pub use` exports lets readers separate implementation dependencies from the crate or module
API being presented.

## Helps

Helps separate implementation dependencies from the public discovery surface exposed through `pub
use`.

## Limits

Small modules can keep imports together when there is no meaningful public surface. Split once
re-exports start acting as API documentation.

## Agent Instruction

Group private imports before public re-exports because private imports and public re-exports answer
different questions.

## Mechanisms

Place private `use` statements before public `pub use` groups, add a blank line between groups, and
keep re-export lists intentional and reviewable.

## References

- [Rust Reference: use
  declarations](https://doc.rust-lang.org/reference/items/use-declarations.html)
- [Ed Page Rust Style: imports](https://epage.github.io/dev/rust-style/)
