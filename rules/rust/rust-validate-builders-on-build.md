# Rust Validate Builders On Build

## Metadata

- ID: `RUST-VALIDATE-BUILDERS-ON-BUILD`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Builder `build` methods should validate cross-field invariants and return errors when construction
can fail.

## Why

Builders spread configuration across multiple calls. Cross-field rules often become visible only
when all fields are known, so validation belongs at the point that turns partial configuration into
a usable value.

The Pragmatic Rust Guidelines recommend builders for complex construction because they let callers
name optional inputs and keep initialization readable. That benefit disappears if `build` returns a
value whose cross-field invariants were never checked.

## Helps

- Helps keep partially configured builders flexible while keeping constructed values valid.

## Limits

Use infallible `build` when defaults and setters make invalid states impossible. Prefer typed state
builders only when the invariant is important enough to justify extra API complexity. Keep setter
methods cheap and defer validation only when a field cannot be judged independently.

## Agent Instruction

Validate Rust builder cross-field invariants in `build` and return an error when construction can
fail.

## Mechanisms

Supported by constructor tests, invalid-combination tests, and examples that show fallible builder
construction.

## References

- [Rule: RUST-USE-BUILDERS-FOR-OPTIONAL-OR-VALIDATED-FIELDS](rust-use-builders-for-optional-or-validated-fields.md)
- [Microsoft Pragmatic Rust Guidelines: Complex Type Construction has
  Builders](https://microsoft.github.io/rust-guidelines/guidelines/checklist/index.html)
- [Rust API Guidelines: predictable APIs](https://rust-lang.github.io/api-guidelines/predictability.html)
