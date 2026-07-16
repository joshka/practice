# Keep Docs Near Their Subject

## Metadata

- Name: `Keep Docs Near Their Subject`
- ID: `keep-docs-near-their-subject`
- Summary: Documentation drifts when it is far from the code, policy, or workflow it explains. Let
  shared rationale rise to the nearest stable owner while item docs retain their local contracts,
  differences, edge cases, and side effects.
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, locality, maintenance`
- Tags: `documentation, source-truth, local-conventions`
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

Apply documentation gravity to shared rationale:

- Rationale shared by a type's methods belongs on the type.
- Rationale shared by enum variants belongs on the enum; variant docs explain their differences.
- Rationale shared by several types belongs on the module.
- Cross-module flow and design rationale belong at the crate root or in a focused guide.
- Item docs explain the local contract, exception, edge case, side effect, or override.

Move an explanation upward only as far as its audience and subject remain the same. Leave a concise
local statement and link when non-linear readers still need the contract at the item they reached.

## Tradeoff

Do not force every idea into the smallest possible scope. Cross-cutting principles belong in a guide
or pattern when duplicating them near every call site would create drift. Choose the location that
keeps the owning source clear.

Do not hoist item-specific obligations into broad prose that callers may never find. Shared rationale
can have one canonical owner while local contracts repeat the small fact needed to use an item
safely.

## Agent Instruction

When adding docs, move shared rationale to the nearest stable type, enum, module, crate, or guide;
keep local contracts and differences on the affected item and link to canonical detail.

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
