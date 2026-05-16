# Make Bad Output Mechanically Hard

## Metadata

- Name: `Make Bad Output Mechanically Hard`
- ID: `make-bad-output-mechanically-hard`
- Summary: Repeated review failures usually belong in a tool, type, schema, template, lint, or
  checklist instead of another reminder. Encode stable rejection criteria early, but keep escape
  hatches when legitimate exceptions are common.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, tooling, quality`
- Related: `prefer-tools-over-prompts, make-invalid-states-hard-to-express`

## Problem

Some bad outputs are predictable: unsafe types in the wrong layer, unwrapped errors, unaligned
tables, missing context, or style shapes the maintainer keeps rejecting. Repeating prose guidance
does not reliably prevent those failures.

## Preferred Move

Move repeatable rejection criteria into the cheapest enforcement layer: type system, API shape,
lint, formatter, test, schema, template, or review checklist. Make the unwanted output fail early or
look obviously out of place.

## Tradeoff

Mechanical checks can overconstrain design if they encode taste before the preference is stable. Add
escape hatches or keep the rule advisory when legitimate exceptions are common.

## Agent Instruction

When a rejected pattern can be detected or prevented mechanically, propose the enforcement point and
apply it if the scope is small. Prefer checks that fail before review.

## Examples

Bad: a policy lives only in review memory.

```text
Do not use untyped maps for fixed configuration.
```

Good: the boundary shape makes the policy hard to violate.

```rust
pub struct Toolchain {
    pub rust: Version,
    pub cargo_nextest: Version,
}
```
