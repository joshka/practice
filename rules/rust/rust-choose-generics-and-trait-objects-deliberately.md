# Rust Choose Generics And Trait Objects Deliberately

## Metadata

- Name: `Choose Generics and Trait Objects Deliberately`
- ID: `RUST-CHOOSE-GENERICS-AND-TRAIT-OBJECTS-DELIBERATELY`
- Summary: Pick generics, stored type parameters, or trait objects for the variation they actually
  model. The choice affects compile cost, object safety, lifetimes, and caller ergonomics.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use generics, stored generic parameters, and trait objects deliberately.

## Why

Generics, stored type parameters, and trait objects trade off monomorphization, API complexity,
object safety, compile times, and caller ergonomics. Choose the shape because it expresses the
variation, not because abstraction feels more flexible.

## Helps

Helps APIs expose the right kind of variation without surprising callers with compile-time cost,
object-safety constraints, allocation, or lifetime complexity.

## Limits

Generics are usually right for caller-chosen types and zero-cost abstraction. Trait objects are
usually right for heterogeneous storage, dynamic plugins, or smaller public signatures.

## Agent Instruction

Choose generics, stored type parameters, and trait objects deliberately because they trade off
monomorphization, object safety, compile time, and ergonomics.

## Mechanisms

Compare call-site ergonomics, monomorphization, object safety, lifetime bounds, storage needs, and
expected extension points before choosing the abstraction shape.

## References

- [Rust Book: trait objects](https://doc.rust-lang.org/book/ch18-02-trait-objects.html)
- [Rust Book: generic data types](https://doc.rust-lang.org/book/ch10-01-syntax.html)
