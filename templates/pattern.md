# Pattern Template

Use this template for small, referenceable guidance units. Replace bracketed text before publishing
an entry.

## Metadata

- Name: `[Human-readable name]`
- ID: `[stable-kebab-case-id]`
- Summary: `[two-to-four sentence scan summary]`
- Status: `draft`
- Audience: `[humans | agents | both]`
- Topics: `[comma-separated topics]`
- Tags: `[comma-separated cluster tags]`
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

## Examples

Include examples when they make the pattern easier to recognize or apply. Prefer one compact bad
example and one compact good example over a large catalog.

Bad examples should show the failure mode. Good examples should show the preferred move. Keep both
small enough that the reader can see the difference without reconstructing a project.
Omit examples when the problem cannot be made obvious from the snippet itself.

When a pattern is about API or implementation shape, prefer examples that show the definition being
introduced or changed, not only the call site. Include call sites only when the caller experience is
the point of the pattern.

Use the code fence language that makes the distinction clearest. Prefer `diff` blocks when the
pattern is about reviewing a change between versions, such as separating structure from behavior.

## References

List durable sources only when they help frame, validate, or contrast the guidance.

Before publishing a pattern, check relevant source catalogs for support or contrast. Common starting
points include Rust API Guidelines, Microsoft Pragmatic Rust Guidelines, Ed Page Rust Style, official
language/framework docs, and durable design or documentation sources.
Do not use "Local" or similar "because I said so" entries as references. Omit the reference table
when no durable source is useful.
Use repo-relative links in prose or `Related` metadata for navigation, not as justification rows in
`References`.
Write the pattern in this repo's own voice. Do not copy or closely paraphrase upstream wording; use
source links to support, adapt, or contrast the guidance.

Change `Status` to `reviewed` only after maintainer review.

Use an aligned table for source notes. Tables may exceed the normal 100-column prose limit when
alignment improves readability.

| Source         | Use         | Note                                    |
| -------------- | ----------- | --------------------------------------- |
| `[link label]` | `[purpose]` | `[relevant idea, contrast, or context]` |

`Use` means:

- `supports`: the source reinforces a preference already held here.
- `adapts`: the source is useful, but this repo reshapes it for local practice.
- `differs`: this repo intentionally chooses a different rule or tradeoff.
