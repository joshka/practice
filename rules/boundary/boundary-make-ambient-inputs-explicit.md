# Boundary Make Ambient Inputs Explicit

## Metadata

- ID: `BOUNDARY-MAKE-AMBIENT-INPUTS-EXPLICIT`
- Legacy ID: `R-0304`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Make ambient inputs explicit.

## Why

Time, randomness, environment variables, current directories, locale, terminal size, network
clients, and process state can change behavior without appearing in function signatures. Making them
explicit improves tests and shows callers what influences the result.

## Helps

- Makes nondeterminism injectable and reduces hidden dependencies.

## Limits

Do not pass huge context objects everywhere. Inject the specific ambient input where tests,
portability, or reader understanding needs control.

## Agent Instruction

Make ambient inputs explicit because time, randomness, environment variables, current directories,
locale, terminal size, network clients, and process state can change behavior without appearing in
function signatures.

## Mechanisms

Supported by clock and RNG traits, config structs, explicit environment readers, terminal-size
parameters, temp directories, and deterministic tests.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
