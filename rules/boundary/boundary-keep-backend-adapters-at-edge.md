# Boundary Keep Backend Adapters At Edge

## Metadata

- Name: `Keep Backend Adapters At Edge`
- ID: `BOUNDARY-KEEP-BACKEND-ADAPTERS-AT-EDGE`
- Summary: Keep provider-specific terminal, storage, network, and runtime APIs in adapter layers at
  the boundary. Core logic stays stable and testable while real backend differences remain modeled
  instead of hidden behind a false common API.
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Keep backend adapters at the edge.

## Why

Backend-specific APIs for terminals, storage, network providers, or runtimes spread quickly if they
enter core logic. Keeping adapters at the edge lets the core model stay stable while each backend
handles its own translation and limits.

## Helps

- Reduces coupling to specific providers and makes alternate backends easier to test or add.

## Limits

Do not hide meaningful backend differences behind a fake common API. Model shared core behavior
separately from backend-specific capabilities.

## Agent Instruction

Keep backend adapters at the edge because backend-specific APIs for terminals, storage, network
providers, or runtimes spread quickly if they enter core logic.

## Mechanisms

Supported by adapter modules, feature-gated integrations, core domain types, backend fixtures, and
tests that exercise translation at the edge.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
