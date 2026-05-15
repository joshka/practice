# Boundary Track Dynamic Registration Provenance

## Metadata

- ID: `BOUNDARY-TRACK-DYNAMIC-REGISTRATION-PROVENANCE`
- Legacy ID: `R-0317`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Track provenance for registrations from extensions, guests, or generated code.

## Why

When extensions, guests, generated code, or config register handlers, commands, routes, or tools,
later conflicts and failures need to identify where each registration came from. Provenance turns an
anonymous entry into a debuggable one.

## Helps

- Makes dynamic systems auditable and easier to debug after registration conflicts or failures.

## Limits

Do not store sensitive source details. Keep provenance to stable names, versions, paths, owners, or
generated identifiers that support debugging.

## Agent Instruction

Track provenance for extension, guest, generated-code, or config registrations so conflicts and
failures identify their source.

## Mechanisms

Supported by registration metadata, source IDs, version fields, conflict errors, diagnostics tables,
and tests for duplicate or shadowed registrations.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
