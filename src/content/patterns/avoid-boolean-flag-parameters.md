# Avoid Boolean Flag Parameters

## Metadata

- Name: `Avoid Boolean Flag Parameters`
- ID: `avoid-boolean-flag-parameters`
- Summary: Boolean parameters make call sites depend on hidden ordering and branch semantics.
  Prefer named operations, enums, options types, or builders when the choice is part of the API
  contract.
- Status: `reviewed`
- Audience: `both`
- Topics: `api-design, rust, readability`
- Tags: `boundary-correctness, validation-policy, public-api, reader-locality`
- Related: `make-invalid-states-hard-to-express, reader-locality`

## Problem

A boolean argument often hides the meaning of a choice at the call site. `render(input, true)` or
`open(path, false)` makes the reader remember parameter order, defaults, and branch semantics before
they can understand the call.

## Preferred Move

Use a named operation, enum, options type, or builder when the choice is part of the API contract.
Make the call site state the mode in domain language instead of encoding it as `true` or `false`.

## Tradeoff

A local private helper can keep a boolean when the call sites are adjacent and the name already
makes the choice obvious. Do not introduce an enum for a one-off branch that has not become a real
API concept.

## Agent Instruction

When a boolean parameter makes the call site ambiguous, replace it with a named operation or explicit
choice type. Keep a boolean only when nearby call sites remain self-explanatory.

## Examples

Bad: the API publishes an unnamed boolean choice.

```rust
pub fn render_report(input: ReportInput, include_drafts: bool) -> Report {
    todo!()
}
```

Good: an enum names the mode when one operation has several legitimate modes.

```rust
pub enum RenderMode {
    Preview,
    Final,
}

pub fn render_report(input: ReportInput, mode: RenderMode) -> Report {
    todo!()
}
```

Good: split operations when the boolean was really selecting two different commands.

```rust
pub fn render_preview(input: ReportInput) -> Report {
    todo!()
}

pub fn render_final(input: ReportInput) -> Report {
    todo!()
}
```

Good: an options type or builder names several independent choices.

```rust
pub struct RenderOptions {
    pub include_drafts: bool,
    pub format: RenderFormat,
}

pub fn render_report(input: ReportInput, options: RenderOptions) -> Report {
    todo!()
}
```

## References

| Source                | Use      | Note                                                   |
| --------------------- | -------- | ------------------------------------------------------ |
| [C-CTOR][ctor]        | `adapts` | Builders fit APIs with multiple construction options.  |
| [M-INIT-BUILDER][ms]  | `adapts` | Complex construction should expose named choices.      |

[ctor]: https://rust-lang.github.io/api-guidelines/predictability.html#c-ctor
[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-INIT-BUILDER
