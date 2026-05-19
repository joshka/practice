# Rust Prefer Constructors And Conversion Traits

## Metadata

- Name: `Prefer Constructors And Conversion Traits`
- ID: `RUST-PREFER-CONSTRUCTORS-AND-CONVERSION-TRAITS`
- Summary: Use inherent constructors and standard conversion traits to show whether construction
  builds, validates, converts, borrows, allocates, or can fail. Prefer public fields only when direct
  construction is truly part of the contract.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, validation-policy, public-api, boundary-correctness`
- Related: `prefer-standard-conversions, make-invalid-states-hard-to-express`

## Rule

Prefer inherent constructors or trait implementations for construction.

## Why

Construction should tell callers whether they are building a new value, validating input, converting
between representations, or borrowing a view. Inherent constructors and standard conversion traits
carry those expectations better than ad hoc helper names.

## Helps

Helps callers discover how values are created and whether construction validates, converts, borrows,
allocates, or can fail.

## Limits

Use public fields for simple data carriers when direct construction is part of the contract. Use
named constructors when invariants or policy matter.

## Agent Instruction

Prefer constructors or conversion traits that show whether callers are building, validating,
converting, or borrowing values.

## Mechanisms

Prefer inherent `new` or domain-named constructors, implement `From`, `TryFrom`, `AsRef`, or
`Borrow` when they match standard semantics, and avoid surprising conversion traits.

## References

- [Rust API Guidelines: conversions use standard
  traits](https://rust-lang.github.io/api-guidelines/interoperability.html#c-conv-traits)
- [Rust API Guidelines: constructors are static inherent
  methods](https://rust-lang.github.io/api-guidelines/predictability.html#c-ctor)
