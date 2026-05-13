# Prefer Standard Conversions

## Metadata

- Name: `Prefer Standard Conversions`
- ID: `prefer-standard-conversions`
- Status: `reviewed`
- Audience: `both`
- Topics: `api-design, rust, interoperability`
- Related: `keep-public-dependencies-intentional`

## Problem

Ad hoc conversion methods can make an API harder to predict. Callers must learn project-specific
names for relationships Rust already models with `From`, `TryFrom`, `AsRef`, `Borrow`, `Deref`, or
iterator traits.

## Preferred Move

Use standard conversion traits when they honestly express the relationship and preserve expected
semantics. Prefer project-specific method names only when the conversion has domain behavior,
side effects, lossy semantics, or surprising costs that the standard trait would hide.

## Tradeoff

Do not implement a standard trait just to look idiomatic. If the operation can fail, allocate
surprisingly, lose information, or depend on context, use a clearer domain method or `TryFrom`
instead of forcing `From`.

## Agent Instruction

Before adding a custom conversion method, check whether a standard Rust conversion trait fits the
semantics. Use the standard trait when it is honest; use a named method when the conversion has
domain-specific behavior or surprising costs.

## Examples

Bad: a project-specific constructor names a standard parsing relationship.

```rust
impl PatternId {
    pub fn from_string(input: &str) -> Result<Self, PatternIdError> {
        todo!()
    }
}
```

Good: parsing from text implements the standard `FromStr` trait.

```rust
impl FromStr for PatternId {
    type Err = PatternIdError;

    fn from_str(input: &str) -> Result<Self, Self::Err> {
        todo!()
    }
}

let id: PatternId = input.parse()?;
```

## References

| Source                 | Use        | Note                                                   |
| ---------------------- | ---------- | ------------------------------------------------------ |
| [C-CONV-TRAITS][api]   | `supports` | Conversion traits should follow ecosystem conventions. |
| [std::convert][std]    | `supports` | Standard conversion traits define expected semantics.  |

[api]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-conv-traits
[std]: https://doc.rust-lang.org/std/convert/index.html
