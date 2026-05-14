# Keep Name Current

## Metadata

- Name: `Keep Name Current`
- ID: `keep-name-current`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, naming, maintenance`
- Related: `reader-locality, separate-structure-from-behavior`

## Problem

Names become stale when responsibility changes. A stale name forces readers to choose between
trusting the word and reading the implementation.

## Preferred Move

Rename code when its responsibility changes. Keep broad renames separate from behavior changes when
the rename would otherwise hide the rule change.

## Tradeoff

Public names, serialized names, and widely used APIs have compatibility cost. Rename them only with
the migration and communication that the boundary requires.

## Agent Instruction

When code changes responsibility, update the name so future readers do not rely on stale
vocabulary. Separate broad renames from behavior changes.

## Examples

Bad: the name still says "active" after the rule becomes visibility.

```rust
let active_patterns = patterns
    .iter()
    .filter(|pattern| pattern.status().is_visible());
```

Good: the name follows the current responsibility.

```rust
let visible_patterns = patterns
    .iter()
    .filter(|pattern| pattern.status().is_visible());
```

## References

| Source                         | Use        | Note                                              |
| ------------------------------ | ---------- | ------------------------------------------------- |
| [Rename Variable][rename-var]  | `supports` | Rename when a name no longer communicates intent. |
| [C-COMMON-TRAITS][common]      | `adapts`   | Rust APIs should use names callers recognize.     |

[common]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-common-traits
[rename-var]: https://refactoring.com/catalog/renameVariable.html
