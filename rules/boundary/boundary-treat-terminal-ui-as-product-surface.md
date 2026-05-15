# Boundary Treat Terminal Ui As Product Surface

## Metadata

- ID: `BOUNDARY-TREAT-TERMINAL-UI-AS-PRODUCT-SURFACE`
- Legacy ID: `R-0323`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Treat terminal UI as a product surface with platform-specific contracts.

## Why

Terminal UI is not just debug output. Layout, input handling, scroll behavior, color, small
viewports, and platform differences form a user-facing contract that can regress like any GUI or
API.

## Helps

- Makes terminal behavior reviewable and protects users from layout and interaction regressions.

## Limits

Do not require full visual testing for tiny internal terminal tools. Treat terminal UI as product
surface when users rely on it repeatedly or across platforms.

## Agent Instruction

Treat terminal UI as a product surface with platform-specific contracts because terminal UI is not just
debug output.

## Mechanisms

Supported by snapshot tests, viewport fixtures, manual screenshots, platform notes, keyboard-event
tests, and rendered-output review.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
