# Rust Avoid Empty Wrapper Types

## Metadata

- ID: `RUST-AVOID-EMPTY-WRAPPER-TYPES`
- Legacy ID: `R-0206`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Avoid wrapper types that add no invariant, behavior, or ownership clarity.

## Why

A wrapper type should earn its name by adding an invariant, behavior, ownership boundary, or API
meaning. A tuple struct or newtype that only renames an existing value adds conversion cost and
another concept without helping the reader.

## Helps

Helps keep the type system meaningful by reserving new names for real invariants, ownership
boundaries, validation rules, or domain concepts.

## Limits

Use a wrapper when it prevents unit confusion, restricts construction, hides representation,
implements a trait coherently, or marks a boundary that callers need to see.

## Agent Instruction

Avoid wrapper types that add no invariant, behavior, or ownership clarity; a wrapper should earn its
name.

## Mechanisms

Look for validation constructors, private fields, trait implementations, serialization policy, or
ownership changes. If none exist, prefer the underlying type or a type alias.

## References

- [Rust API Guidelines: newtypes provide static
  distinctions](https://rust-lang.github.io/api-guidelines/type-safety.html#c-custom-type)
- [Microsoft Pragmatic Rust Guidelines: avoid wrapper types that add no
  value](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-AVOID-WRAPPERS)
