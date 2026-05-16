# Strengthen Cohesion

## Metadata

- Name: `Strengthen Cohesion`
- ID: `strengthen-cohesion`
- Summary: A concept becomes harder to understand when its data, rules, and behavior are scattered
  or bundled with unrelated concerns. Move elements that change for the same reason toward one
  named owner, while separating nearby code that belongs to another concept.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, architecture, readability`
- Tags: `reader-locality, change-shape, ownership`
- Related: `reader-locality, cap-change-radius`

## Problem

A concept becomes harder to understand when its data, validation, transitions, and behavior are
split across files or types that do not make sense independently. The reader has to assemble one
idea from unrelated technical categories.
Change gets more expensive when coupled elements are scattered and uncoupled elements are bundled
together only because they share a file, layer, or framework bucket.

## Preferred Move

Move related data and behavior toward one named concept when they change together. Put rules beside
the state they protect, and give the cohesive unit a name that explains the domain role.

When several functions, fields, or modules repeatedly change for the same reason, make that
relationship visible as a smaller containing element. When nearby code does not change for that
reason, move it toward the concept it actually belongs to.

## Tradeoff

Cohesion is not a license to build a large mixed module. Split responsibilities that do not change
together, and preserve framework layout where it carries useful convention.
Move one element at a time when the evidence is incomplete. Large reorganizations can hide the
specific coupling that made the change valuable.

## Agent Instruction

When facts and behavior always change together, move them toward one named concept instead of
scattering them by technical category. Report what concept now owns the rule and what expected
change made that grouping valuable.

## Examples

Bad: callers mutate lifecycle fields directly.

```rust
pattern.status = Status::Published;
pattern.published_at = Some(now);
events.push(Event::Published { at: now });
```

Good: the cohesive concept owns the transition.

```rust
let pattern = pattern.publish(now)?;
```

## References

| Source                          | Use      | Note                                                     |
| ------------------------------- | -------- | -------------------------------------------------------- |
| [M-SIMPLE-ABSTRACTIONS][ms]     | `adapts` | APIs should expose simple concepts, not machinery.       |
| [Tidy First, Ch. 32][tidy-ch32] | `adapts` | Keep code that moves together under a clear owner.       |

[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS
[tidy-ch32]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch32.html
