# Rust Prefer Small Clear Shapes

## Metadata

- Name: `Prefer Small Clear Shapes`
- ID: `RUST-PREFER-SMALL-CLEAR-SHAPES`
- Summary: Favor small functions, narrow structs, and simple enums that keep live facts local for
  readers. Do not split cohesive logic into fragments that force more navigation than understanding.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Prefer small functions, narrow structs, and simple enums.

## Why

Small functions, narrow structs, and simple enums reduce the number of fields, branches, lifetimes,
and invariants a reader must hold at once. The goal is local clarity, not arbitrary line-count
reduction.

## Helps

Helps keep the number of live fields, branches, parameters, and invariants small enough for readers
to understand locally.

## Limits

Do not split code into tiny pieces that force more jumping than understanding. Keep cohesive logic
together when the parts change and are read together.

## Agent Instruction

Prefer small functions, narrow structs, and simple enums to reduce live fields, branches, lifetimes,
and invariants.

## Mechanisms

Extract named helpers, narrow structs, split enum responsibilities, reduce parameter lists, and move
unrelated state to the concept that owns it.

## References

- [Microsoft Pragmatic Rust Guidelines: prefer simple
  abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
- [Ed Page Rust Style: code organization](https://epage.github.io/dev/rust-style/)
