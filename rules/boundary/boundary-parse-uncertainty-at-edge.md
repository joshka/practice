# Boundary Parse Uncertainty At Edge

## Metadata

- Name: `Parse Uncertainty At Edge`
- ID: `BOUNDARY-PARSE-UNCERTAINTY-AT-EDGE`
- Summary: Parse and validate raw strings, JSON, CLI args, provider responses, and user input at
  the boundary before passing values inward. Core logic receives typed invariants, while
  domain-specific checks that require later context remain explicit policy decisions.
- Status: `reviewed`
- Domain: `boundary`
- Tags: `boundary-correctness, validation-policy, errors, source-truth`
- Related: `parse-dont-validate, make-validation-policy-explicit, label-doc-claims-by-evidence`

## Rule

Push uncertainty to the boundary, then pass trusted values inward.

## Why

Raw strings, JSON, CLI args, provider responses, and user input contain uncertainty. Parse and
validate them at the edge so inner code receives typed values with known invariants instead of
repeating defensive checks everywhere.

## Helps

- Concentrates validation policy and reduces invalid states in core logic.

## Limits

Some validation depends on domain context that is only available later. Parse structural uncertainty
early and make later policy checks explicit.

## Agent Instruction

Push uncertainty to the boundary, then pass trusted values inward from parsed strings, JSON, CLI
args, provider responses, and user input.

## Mechanisms

Supported by `FromStr`, `TryFrom`, parser types, validation errors, newtypes with invariants, and
tests for accepted and rejected inputs.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
