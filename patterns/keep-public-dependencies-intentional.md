# Keep Public Dependencies Intentional

## Metadata

- Name: `Keep Public Dependencies Intentional`
- ID: `keep-public-dependencies-intentional`
- Status: `reviewed`
- Audience: `both`
- Topics: `api-design, dependencies, rust`
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

## References

| Source                      | Use      | Note                                                        |
| --------------------------- | -------- | ----------------------------------------------------------- |
| [M-SIMPLE-ABSTRACTIONS][ms] | `adapts` | Public APIs should avoid exposing nested generic machinery. |

[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS
