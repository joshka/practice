# Rust Central Item First

## Metadata

- Name: `Central Item First`
- ID: `RUST-CENTRAL-ITEM-FIRST`
- Summary: Put the main type, trait, enum, or function before supporting details. Readers can learn
  the module's purpose before chasing helpers and adapters.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, reader-locality, public-api`
- Related: `reader-locality, RUST-ORDER-CODE-FOR-READING, RUST-ORDER-ITEMS-FOR-API-READING`

## Rule

Put the central item first and keep inherent impls near the type.

## Why

A Rust module is easier to read when the main type, trait, enum, or function appears before helpers.
Keeping inherent impls near the type lets readers learn the concept and its core operations before
diving into adapters, tests, or support code.

## Helps

Helps readers open a module and immediately find the type, trait, enum, or function the file exists
to define.

## Limits

Keep prerequisites first when they are tiny and necessary to understand the central item, such as a
private helper enum used directly in the type signature.

## Agent Instruction

Put the main Rust type, trait, enum, or function before helpers so readers find the module concept
first.

## Mechanisms

Place the central item near the top, keep inherent impls close to it, and move tests, adapters,
trait impls, and helpers after the main concept.

## References

- [Ed Page Rust Style: item organization](https://epage.github.io/dev/rust-style/)
