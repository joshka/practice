# Document System Mental Models

## Metadata

- Name: `Document System Mental Models`
- ID: `document-system-mental-models`
- Summary: Systems with implicit concepts force readers to reconstruct how parts fit together from
  scattered implementation details. Document the mental model that explains ownership, flow,
  boundaries, and vocabulary before listing procedures.
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, architecture, mental-models`
- Tags: `documentation, source-truth, agent-context`
- Related: `write-docs-as-contracts, choose-doc-type`

## Problem

Large systems become hard to change when every reader has to rediscover boundaries, data flow,
lifecycle, ownership, persistence, and failure behavior from scattered implementation details.
Locally readable code can still leave the system-level model implicit.

## Preferred Move

Write short module, crate, or guide-level notes that explain how the pieces fit together. Capture
the stable model: what owns what, what crosses the boundary, what is persisted, what can retry, what
must happen in order, and what assumptions downstream code relies on.

## Tradeoff

Do not write speculative architecture essays. Keep the note close to the code or guide it explains,
and update it when the model changes. If the model is still unstable, mark the uncertainty instead
of freezing a guess.

## Agent Instruction

When a change depends on system behavior that is not obvious from a single function, add or update a
nearby mental-model note. Report the boundary, lifecycle, side effects, and assumptions that the
note now captures.

## Examples

Bad: the module doc names the topic but leaves the reader to reconstruct the workflow.

```rust
//! Background job processing.
```

Good: the module doc gives the next reader the shape of the system.

```rust
//! Background job processing.
//!
//! Workers claim jobs by marking a database row as leased, then acknowledge the
//! row only after the handler commits its side effects. Failed jobs keep their
//! lease until it expires, so handlers must be safe to retry.
```

## References

| Source                                      | Use        | Note                                                           |
| ------------------------------------------- | ---------- | -------------------------------------------------------------- |
| [Diátaxis explanation context][context]     | `supports` | Explanation carries the context and rationale behind behavior. |
| [Diátaxis reference structure][structure]   | `adapts`   | Reference should respect the structure of the machinery.       |
| [Rustdoc components][rustdoc-components]    | `supports` | Component docs are the expected place for public context.      |

[context]: https://diataxis.fr/explanation/#provide-context
[structure]: https://diataxis.fr/reference/#respect-the-structure-of-the-machinery
[rustdoc-components]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html#documenting-components
