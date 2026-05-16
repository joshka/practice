# Name Coupling

## Metadata

- Name: `Name Coupling`
- ID: `name-coupling`
- Summary: Relationships between pieces are hard to judge when the reason they change together is
  unnamed. Describe the change pressure first, then decide whether the coupling belongs directly,
  behind a clearer owner, or across an explicit boundary.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, architecture, review`
- Related: `cap-change-radius, strengthen-cohesion`

## Problem

Two pieces can change together for a good reason, a bad reason, or an invisible reason. If the
relationship is unnamed, reviewers debate "decoupling" before they know whether the dependency is
beneficial domain structure or accidental shape.
The useful question is not whether two elements are related, but which expected edit would require
both pieces to move.

## Preferred Move

Name the coupling before adding or removing abstraction. Describe why the pieces change together,
then decide whether to keep the relationship direct, move it to a clearer owner, or introduce a
boundary.

Prefer naming the change pressure explicitly: "the wire format edit touches both sides,"
"publish policy changes touch these two modules," or "rendering-only edits should not reach this
type." That turns coupling from a vague smell into a reviewable design claim.

## Tradeoff

Decoupling has a cost. It can replace an honest dependency with a vague protocol, callback, trait,
or configuration seam that future readers still have to understand.
Reducing coupling for one category of edits can add machinery or create a different dependency
somewhere else. Do not decouple just to make a relationship disappear from the current file.

## Agent Instruction

Before decoupling or adding an abstraction, name the relationship between the pieces. State whether
the coupling is beneficial, accidental, or still uncertain, and name the future edit that would make
it costly.

## Examples

Bad: the service depends on the table shape directly, but the relationship is not named.

```rust
pub fn render_card(row: PatternRow) -> PatternCard {
    PatternCard {
        title: row.title,
        summary: row.summary,
        href: format!("/patterns/{}", row.slug),
    }
}
```

Good: the coupling is named as a catalog projection. Callers depend on the projection contract, not
on the persistence row.

```rust
pub struct CatalogPattern {
    title: String,
    summary: String,
    slug: PatternSlug,
}

impl From<PatternRow> for CatalogPattern {
    fn from(row: PatternRow) -> Self {
        Self {
            title: row.title,
            summary: row.summary,
            slug: row.slug,
        }
    }
}

impl CatalogPattern {
    pub fn card_href(&self) -> String {
        format!("/patterns/{}", self.slug)
    }
}
```

## References

| Source                          | Use      | Note                                                       |
| ------------------------------- | -------- | ---------------------------------------------------------- |
| [Tidy First, Ch. 29][tidy-ch29] | `adapts` | Coupling only matters when a likely edit has to propagate. |
| [Tidy First, Ch. 31][tidy-ch31] | `adapts` | Decoupling has its own cost and should not be automatic.   |

[tidy-ch29]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch29.html
[tidy-ch31]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch31.html
