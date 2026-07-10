# Rust Choose Generics And Trait Objects Deliberately

## Metadata

- Name: `Choose Generics and Trait Objects Deliberately`
- ID: `RUST-CHOOSE-GENERICS-AND-TRAIT-OBJECTS-DELIBERATELY`
- Summary: Pick generics, stored type parameters, or trait objects for the variation they actually
  model. The choice affects compile cost, object safety, lifetimes, and caller ergonomics.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, public-api, performance, reader-locality`
- Related: `make-parameters-explicit, public-api-changes-have-downstream-cost`

## Rule

Use generics, stored generic parameters, and trait objects deliberately.

## Why

These choices put variation in different places, so they create different costs.

A generic function lets each caller choose a concrete type. Monomorphization enables static dispatch
and optimization, but can increase compile time and machine-code size. Bounds also become part of the
caller's contract and error surface.

A stored type parameter makes the choice part of the containing type's identity. The parameter and
its bounds then spread through fields, constructors, return types, and wrappers. This is useful when
each value has a fixed implementation, but awkward when callers do not care or need heterogeneous
storage.

A trait object erases the concrete type, allowing runtime selection and heterogeneous storage. The
cost is pointer indirection, dynamic dispatch, ownership and lifetime bounds, and a dyn-compatible
trait with fewer available method shapes.

The wrong choice can therefore spread complexity through an API or constrain its future evolution.
Choose the shape that matches where variation belongs, not the one that merely appears flexible.

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

- [Rust Compiler Development Guide: monomorphization](https://rustc-dev-guide.rust-lang.org/backend/monomorph.html)
- [Rust Reference: dyn compatibility](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility)
- [Rust Book: trait objects](https://doc.rust-lang.org/book/ch18-02-trait-objects.html)
- [Rust Book: generic data types](https://doc.rust-lang.org/book/ch10-01-syntax.html)
