# Avoid Boolean Flag Parameters

## Metadata

- Name: `Avoid Boolean Flag Parameters`
- ID: `avoid-boolean-flag-parameters`
- Summary: Behavioral boolean flags make call sites depend on hidden ordering and branch semantics.
  Distinguish them from boolean domain data, then prefer named operations, enums, options types, or
  builders when the caller selects behavior.
- Status: `reviewed`
- Audience: `both`
- Topics: `api-design, rust, readability`
- Tags: `boundary-correctness, validation-policy, public-api, reader-locality`
- Related: `make-invalid-states-hard-to-express, reader-locality`

## Problem

A behavioral boolean flag tells a function which policy, mode, or operation the caller wants.
`render(input, true)` or `open(path, false)` makes the reader remember parameter order, defaults, and
branch semantics before they can understand the call.

Not every boolean parameter is a behavioral flag. Boolean domain data records a fact, such as an
executable bit, before-or-after presence, or an already-derived predicate. The design problem begins
when the caller selects behavior and the call boundary erases the name of that choice.

## Preferred Move

Inspect call sites, not only declarations. Literal arguments, multiple booleans, and meaningful
names lost across the call boundary are the strongest signals that the interface hides behavior.

Choose the replacement that matches how the choice is used:

- Split operations when the flag selects distinct commands.
- Use an enum when one mode travels through multiple layers.
- Use an options type when callers make several independent choices.
- Use a no-argument builder method for a default-off capability.
- Hide a private boolean helper behind named operations when shared implementation needs the flag.

Make the caller's choice visible in domain language. For options types, prefer a struct literal so
field names travel with their values; `RenderOptions::new(true, false)` only relocates the ambiguity.

## Tradeoff

Keep a boolean when it represents domain data rather than caller-selected behavior. An
already-named boolean source can also remain readable at the call site. A hidden private helper can
accept a boolean when named public operations are its only callers. Parameterized tests can use
booleans when descriptive case names explain each combination.

Do not introduce a one-off enum that merely renames `true` and `false` without creating a durable
concept. The extra type is useful only when its name and variants reduce the context callers and
maintainers must remember.

## Agent Instruction

First classify a boolean parameter as domain data or caller-selected behavior. For behavior, inspect
call sites for literals, multiple booleans, and lost names, then use named operations or an explicit
choice shape when they make the calls self-explanatory.

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

Good: an options struct literal names several independent choices at the call site.

```rust
pub struct RenderOptions {
    pub include_drafts: bool,
    pub parallel: bool,
}

pub fn render_report(input: ReportInput, options: RenderOptions) -> Report {
    todo!()
}

let report = render_report(
    input,
    RenderOptions {
        include_drafts: true,
        parallel: false,
    },
);
```

Good: a no-argument builder method names a default-off capability.

```rust
let report = RenderRequest::new(input).include_drafts().render();
```

## References

| Source                         | Use        | Note                                                   |
| ------------------------------ | ---------- | ------------------------------------------------------ |
| [Flag Argument][flag-argument] | `supports` | Named operations can share a hidden flag helper.       |
| [C-CTOR][ctor]                 | `adapts`   | Builders fit APIs with multiple construction options.  |
| [M-INIT-BUILDER][ms]           | `adapts`   | Complex construction should expose named choices.      |

[ctor]: https://rust-lang.github.io/api-guidelines/predictability.html#c-ctor
[flag-argument]: https://martinfowler.com/bliki/FlagArgument.html
[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-INIT-BUILDER
