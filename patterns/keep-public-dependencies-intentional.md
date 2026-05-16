# Keep Public Dependencies Intentional

## Metadata

- Name: `Keep Public Dependencies Intentional`
- ID: `keep-public-dependencies-intentional`
- Summary: Public dependencies shape downstream compatibility, API expectations, and maintenance
  cost. Add or raise them only when the public behavior needs that requirement, using lockfile
  updates for ordinary compatible refreshes.
- Status: `reviewed`
- Audience: `both`
- Topics: `api-design, dependencies, rust`
- Tags: `dependencies, public-api, rust, change-shape`
- Related: `prefer-standard-conversions, preserve-error-context`

## Problem

A dependency becomes part of a crate's public contract when its types appear in public APIs. That
can force downstream users to care about another crate's versions, feature flags, traits, and
semver behavior even when the dependency was only an implementation detail.

## Preferred Move

Keep dependency types out of public APIs unless the dependency is part of the abstraction. Use local
types, standard library types, or conversion boundaries when the dependency should stay private.

## Tradeoff

Exposing a dependency type can be correct when interoperability is the point of the API. If the
public contract is intentionally shaped around another crate, document that dependency as part of
the abstraction and preserve compatibility carefully.

## Agent Instruction

Before exposing a dependency type publicly, decide whether downstream users should depend on that
crate as part of the API. If not, keep the dependency behind a local type or conversion boundary.

## Examples

Bad: a library exposes `anyhow` in its public API, so downstream users lose a stable crate-owned
error contract.

```rust
pub fn parse(input: &str) -> anyhow::Result<Pattern> {
    todo!()
}
```

Good: the public API exposes a crate-owned error type. The library can still use `anyhow`
internally if that does not leak across the public boundary.

```rust
pub fn parse(input: &str) -> Result<Pattern, ParseError> {
    todo!()
}
```

## References

| Source                      | Use      | Note                                                        |
| --------------------------- | -------- | ----------------------------------------------------------- |
| [M-SIMPLE-ABSTRACTIONS][ms] | `adapts` | Public APIs should avoid exposing nested generic machinery. |

[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS
