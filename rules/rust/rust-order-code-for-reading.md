# Rust Order Code For Reading

## Metadata

- ID: `RUST-ORDER-CODE-FOR-READING`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Order Rust code by execution order or conceptual dependency order.

## Why

File order is a reading interface. Readers should encounter the main concept, public API, or caller
before the helpers when that makes the story easier to follow. Random helper-first ordering makes
readers jump around before they know what the file is for.

Ed Page's Rust style guide frames source as technical writing and names several ordering rules:
central item first, caller before callee, public before private, and inherent impls near the type.
Those are not mechanical absolutes; they are ways to make the file's outline visible to a skimming
reader.

## Helps

- Helps modules read top-to-bottom and keeps helpers in context.

## Limits

Use judgment when trait impl grouping, macro constraints, generated code, or local convention makes
another order clearer. If two ordering rules conflict, choose the order that best reduces jumping
for the expected reader of that file.

## Agent Instruction

Arrange Rust modules so public or central items appear before helpers and reading order follows
execution or conceptual dependency.

## Mechanisms

Supported by source review, file moves, and module-level documentation that names the central
concept.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Ed Page Rust Style: File structure](https://epage.github.io/dev/rust-style/#file-structure)
- [Rule: RUST-CENTRAL-ITEM-FIRST](rust-central-item-first.md)
