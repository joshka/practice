# Keep Docs Near Their Subject

## Metadata

- Name: `Keep Docs Near Their Subject`
- ID: `keep-docs-near-their-subject`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, locality, maintenance`
- Related: `write-docs-as-contracts, document-system-mental-models`

## Problem

Docs drift when the information lives far from the thing it explains. Readers also lose time when
API contracts, workflow steps, system rationale, and implementation constraints are scattered across
unrelated files.

## Preferred Move

Put documentation at the nearest stable boundary where readers will look for it. Use Rustdoc for
public API contracts, module or crate docs for component models, guide pages for workflows and
policies, and pattern entries for reusable review language. Link outward instead of duplicating a
large explanation in multiple places.

## Tradeoff

Do not force every idea into the smallest possible scope. Cross-cutting principles belong in a guide
or pattern when duplicating them near every call site would create drift. Choose the location that
keeps the owning source clear.

## Agent Instruction

When adding docs, choose the nearest stable owner for the information. Avoid duplicating long
guidance; link to the canonical guide or pattern when the detail already exists.

## Examples

Bad: a public API contract is hidden in a distant guide.

```md
## Import Notes

`load_profile` writes the normalized profile to disk before returning.
```

Good: the contract appears at the API boundary that callers inspect.

```rust
/// Loads a profile and writes the normalized form to disk before returning.
pub fn load_profile(path: &Path) -> Result<Profile, ProfileError> {
    todo!()
}
```

## References

| Source                                    | Use        | Note                                                         |
| ----------------------------------------- | ---------- | ------------------------------------------------------------ |
| [Diátaxis reference structure][structure] | `adapts`   | Reference docs should follow the structure of the machinery. |
| [Rustdoc components][rustdoc-components]  | `supports` | Component docs are where Rust readers inspect API behavior.  |

[structure]: https://diataxis.fr/reference/#respect-the-structure-of-the-machinery
[rustdoc-components]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html#documenting-components
