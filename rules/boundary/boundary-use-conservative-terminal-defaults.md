# Boundary Use Conservative Terminal Defaults

## Metadata

- ID: `BOUNDARY-USE-CONSERVATIVE-TERMINAL-DEFAULTS`
- Legacy ID: `R-0324`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Use conservative terminal defaults.

## Why

Terminals vary in color support, width, input behavior, fonts, and accessibility settings.
Conservative defaults reduce the chance that a UI is unreadable, clipped, or unusable on common
terminals before users configure anything.

## Helps

- Improves first-run usability and cross-terminal compatibility.

## Limits

Advanced styling and interaction can be opt-in or capability-detected. Defaults should remain safe
for small viewports, limited color, and ordinary keyboard input.

## Agent Instruction

Use conservative terminal defaults because terminals vary in color support, width, input behavior,
fonts, and accessibility settings.

## Mechanisms

Supported by capability detection, fallback styles, minimum viewport tests, no-color modes,
saturating layout arithmetic, and manual checks in common terminals.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
