# Rust Avoid Broad Context And Callbacks

## Metadata

- ID: `RUST-AVOID-BROAD-CONTEXT-AND-CALLBACKS`
- Legacy ID: `R-0215`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Avoid broad context objects and callback-heavy control flow.

## Why

Broad context objects and callback-heavy flows hide which inputs, effects, and ordering a function
needs. In Rust this often fights ownership and lifetimes while making readers chase control flow
through closures instead of seeing the data path locally.

## Helps

Helps readers see a function's real inputs, outputs, lifetimes, and side effects without tracing a
context bag or callback chain through distant code.

## Limits

Broad context objects can be useful at application boundaries, plugin systems, dependency injection
seams, or framework integration points when the contract is named and stable.

## Agent Instruction

Avoid broad context objects and callback-heavy control flow because broad context objects and
callback-heavy flows hide which inputs, effects, and ordering a function needs.

## Mechanisms

Replace context bags with explicit parameters, split callbacks into named operations, return values
instead of mutating hidden state, and move orchestration to a narrow owner.

## References

- [Rust API Guidelines: caller controls where to copy and place
  data](https://rust-lang.github.io/api-guidelines/flexibility.html#c-caller-control)
- [Microsoft Pragmatic Rust Guidelines: prefer simple
  abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
