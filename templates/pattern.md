# Pattern Template

Use this template for small, referenceable guidance units. Replace bracketed text before publishing
an entry.

## Metadata

- Name: `[Human-readable name]`
- ID: `[stable-kebab-case-id]`
- Status: `[draft | reviewed]`
- Audience: `[humans | agents | both]`
- Topics: `[comma-separated topics]`
- Related: `[related stable IDs, if any]`

## Problem

Describe the concrete pressure, failure mode, or review concern that makes this guidance relevant.
Prefer observable signals over abstract categories.

## Preferred Move

State the action to take. Keep this section direct enough that it can be quoted in review or copied
into an implementation note.

## Tradeoff

Explain when the move is limited, too costly, or likely to create a worse problem. Include the
counter-signal that should make someone choose a different move.

## Agent Instruction

Write the compact operational instruction for a coding agent. It should name the expected action,
the scope limit, and the evidence or validation the agent should report.

## References

List durable sources only when they help frame, validate, or contrast the guidance.

Use an aligned table for source notes. Tables may exceed the normal 100-column prose limit when
alignment improves readability.

| Source         | Use         | Note                                    |
| -------------- | ----------- | --------------------------------------- |
| `[link label]` | `[purpose]` | `[relevant idea, contrast, or context]` |

`Use` means:

- `supports`: the source reinforces a preference already held here.
- `adapts`: the source is useful, but this repo reshapes it for local practice.
- `differs`: this repo intentionally chooses a different rule or tradeoff.
