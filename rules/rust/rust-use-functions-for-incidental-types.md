# Rust Use Functions For Incidental Types

## Metadata

- Name: `Use Functions For Incidental Types`
- ID: `RUST-USE-FUNCTIONS-FOR-INCIDENTAL-TYPES`
- Summary: Prefer free or module functions when a type does not own the operation or invariant.
  Move behavior onto a type when the method relationship clarifies state, policy, or trait design.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Prefer regular functions over associated functions when the type name is incidental.

## Why

Associated functions imply the type owns the operation. When the type is only incidental to a
calculation, a regular function can keep ownership clearer and avoid turning utility behavior into a
misleading method family.

## Helps

Helps callers avoid chasing an irrelevant type just to find a stateless operation or one-off
transformation.

## Limits

Use inherent methods when the operation depends on type invariants, mutates owned state,
participates in trait design, or is central to the type's purpose.

## Agent Instruction

Prefer regular functions because a type name is incidental and does not own the operation or invariant.

## Mechanisms

Prefer free functions or module functions for stateless operations, parsing helpers, and incidental
grouping. Move behavior onto a type when the type owns the invariant.

## References

- [Microsoft Pragmatic Rust Guidelines: prefer simple
  abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
