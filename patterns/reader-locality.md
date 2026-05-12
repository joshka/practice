# Reader Locality

## Metadata

- Name: `Reader Locality`
- ID: `reader-locality`
- Status: `reviewed`
- Audience: `both`
- Topics: `readability, refactoring, organization`
- Related: `small-reviewable-chunks, separate-structure-from-behavior`

## Problem

A change can reduce line count while increasing the number of jumps a maintainer must make. Weak
helpers, distant types, and generic modules force readers to reconstruct context before they can
understand one local workflow.

## Preferred Move

Keep related concepts near the code that gives them meaning. Extract or move code only when the new
name, contract, and location reduce the reader's live context.

## Tradeoff

Strong reusable concepts can live farther away when their contract is clear enough that callers do
not need to inspect the implementation. Do not use locality to justify leaving unrelated
responsibilities fused together.

## Agent Instruction

Before extracting or moving code, check whether the new location reduces reader context. Keep weak
helpers near their caller and prefer local clarity over generic organization.

## References

| Source          | Use        | Note                                              |
| --------------- | ---------- | ------------------------------------------------- |
| [epage][epage]  | `supports` | Weak abstractions should stay close to their use. |

[epage]: https://epage.github.io/dev/rust-style/
