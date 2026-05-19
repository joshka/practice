# Keep Structure Reversible

## Metadata

- Name: `Keep Structure Reversible`
- ID: `keep-structure-reversible`
- Summary: Early structure can harden into unnecessary abstraction before the design is proven.
  Prefer arrangements that are easy to inline, split, merge, or rename until the underlying concept
  earns permanence.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, refactoring, design`
- Tags: `change-shape, reviewability, reader-locality`
- Related: `separate-structure-from-behavior, small-reviewable-chunks`

## Problem

Tidying toward an uncertain design can accidentally create a durable contract. A public type,
module boundary, serialization shape, or compatibility layer is harder to undo than a local helper
or private rename.
Structure creates useful optionality only when it lowers the cost of likely future changes;
premature contracts can spend that option before the evidence exists.
Some structure moves become effectively irreversible when they propagate through public APIs,
serialized data, many call sites, or deployment topology.

## Preferred Move

Prefer reversible structure moves while evidence is still forming. Rename, group, move, extract a
private helper, or clarify a local boundary before creating public APIs or data formats. Ask what it
would cost to back the structure out if the next change disproves it.
Treat local structure as a way to test design understanding. It should make code relationships
clearer without making callers depend on an unproven shape.
For large irreversible moves, build reversibility first: narrow feature-flag checks, keep adapters
small, prototype against production-like constraints, and prevent the decision from spreading before
it has evidence.

## Tradeoff

Some decisions must become durable before release or coordination. Reversibility is not an excuse to
avoid a real compatibility decision; it is a way to keep learning cheap while the shape is still
private.
Do not optimize only for future options. Shipping current behavior still matters, and a reversible
structure move is only worthwhile when it helps comprehension, review, or likely follow-on changes.
Treat irreversible decisions more deliberately than reversible ones. Do not spend the same review
budget on a private helper extraction that you would spend on a public protocol or service split.

## Agent Instruction

When reshaping code toward an uncertain design, choose the smallest reversible structure move. Avoid
creating public compatibility promises until the design has evidence.

## Examples

Bad: a public type is introduced before the shape has proven itself.

```rust
pub struct SearchDocument {
    pub title: String,
    pub summary: String,
    pub tags: Vec<String>,
}
```

Good: the uncertain shape stays private and can move later.

```rust
fn search_text(pattern: &Pattern) -> String {
    [pattern.title(), pattern.summary(), &pattern.tags().join(" ")].join(" ")
}
```

## References

| Source                          | Use      | Note                                                    |
| ------------------------------- | -------- | ------------------------------------------------------- |
| [Tidy First, Ch. 22][tidy-ch22] | `adapts` | Design creates elements, relationships, and benefits.   |
| [Tidy First, Ch. 23][tidy-ch23] | `adapts` | Code shape affects which future changes stay cheap.     |
| [Tidy First, Ch. 24][tidy-ch24] | `adapts` | Design work trades current cost for future flexibility. |
| [Tidy First, Ch. 28][tidy-ch28] | `adapts` | Reversible decisions deserve a different pace.          |

[tidy-ch22]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch22.html
[tidy-ch23]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch23.html
[tidy-ch24]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch24.html
[tidy-ch28]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch28.html
