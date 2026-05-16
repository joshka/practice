# Move Declaration And Initialization Together

## Metadata

- Name: `Move Declaration And Initialization Together`
- ID: `move-declaration-and-initialization-together`
- Summary: A value declared before it is valid makes readers track an empty slot and its future
  assignment. Declare values where they become meaningful, using immutable locals and narrow scopes
  unless evaluation order requires more care.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, readability, state`
- Related: `limit-live-context, reader-locality, use-explaining-variable`

## Problem

A variable that exists before it has a meaningful value creates a temporary mystery. The reader must
track an empty slot, scan forward for assignment, and check whether the value can be observed before
it becomes valid.
This is one instance of a broader live-context problem: the longer a fact is in scope, the longer a
reader has to consider whether it can affect later code.

## Preferred Move

Declare a value where it becomes known. Prefer immutable locals and narrow scopes so a name starts
life with meaning.
Preserve evaluation order, but move each declaration as close as practical to the expression that
gives it a valid value and the code that uses it.

## Tradeoff

Some language constructs, cleanup paths, or ownership constraints require broader scope. Do not
duplicate expensive work or contort control flow only to narrow a variable.
If moving the declaration requires manually tracking too many ordering constraints, take a smaller
step or add a test first; this cleanup should not quietly change execution order.

## Agent Instruction

Move local declarations to the point where their value becomes meaningful. Avoid placeholder values
that readers must remember across unrelated work.

## Examples

Bad: the name exists before it has a valid value.

```rust
let mut slug = None;

if let Some(input) = request.slug() {
    slug = Some(Slug::parse(input)?);
}

let pattern = load_pattern(slug.ok_or(Error::MissingSlug)?)?;
```

Good: the value is declared when it becomes available.

```rust
let input = request.slug().ok_or(Error::MissingSlug)?;
let slug = Slug::parse(input)?;

let pattern = load_pattern(slug)?;
```

## References

| Source                          | Use      | Note                                                         |
| ------------------------------- | -------- | ------------------------------------------------------------ |
| [Tidy First, Ch. 7][tidy-ch7]   | `adapts` | Keep declaration and initialization close, preserving order. |

[tidy-ch7]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch07.html
