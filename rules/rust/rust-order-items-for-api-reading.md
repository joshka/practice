# Rust Order Items For API Reading

## Metadata

- ID: `RUST-ORDER-ITEMS-FOR-API-READING`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Order Rust items so the API is easy to read.

## Why

Item order is part of source readability. Imports should be minimal and grouped by meaning, public
items can come before private helpers when that helps readers find the API, and inherent impls
should usually sit near the type they explain.

Trait impls, helper functions, and private imports should support the main concept instead of
burying it. Ed Page's Rust style guide frames this as code-as-technical-writing: the order should
guide the reader through the file's story.

## Helps

- Helps readers scan modules for API, implementation, and type behavior without jumping around.

## Limits

Use judgment when macros, generated code, trait impl grouping, or local convention makes another
order clearer. Do not churn stable files solely to satisfy ordering preference.

## Agent Instruction

Order Rust imports, public items, inherent impls, trait impls, and helpers to make the file's API
story easy to scan.

## Mechanisms

Supported by rustfmt, import review, module review, and rendered Rustdoc review for public item
ordering.

## References

- [Ed Page Rust Style: File structure](https://epage.github.io/dev/rust-style/#file-structure)
- [Rule: RUST-CENTRAL-ITEM-FIRST](rust-central-item-first.md)
- [Rule: RUST-ORDER-CODE-FOR-READING](rust-order-code-for-reading.md)
