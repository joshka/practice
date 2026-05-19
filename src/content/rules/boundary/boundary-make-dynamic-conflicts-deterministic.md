# Boundary Make Dynamic Conflicts Deterministic

## Metadata

- Name: `Make Dynamic Conflicts Deterministic`
- ID: `BOUNDARY-MAKE-DYNAMIC-CONFLICTS-DETERMINISTIC`
- Summary: Define stable ordering, duplicate handling, priority, or override policy for dynamic
  registrations. Deterministic conflict behavior prevents hash order or load timing from changing
  which plugin, guest, generated item, or handler wins.
- Status: `reviewed`
- Domain: `boundary`
- Tags: `boundary-correctness, validation-policy, state-transitions, tooling`
- Related: `make-validation-policy-explicit, make-state-transitions-explicit`

## Rule

Make dynamic registration conflicts deterministic and explicit.

## Why

Dynamic registration from plugins, generated code, guests, or config can produce duplicate names,
ordering conflicts, or shadowed handlers. If conflict resolution depends on hash order or load
timing, behavior changes between runs.

## Helps

- Makes extension systems predictable and diagnosable.

## Limits

Some systems intentionally allow priority or override order. Document and test that policy instead
of leaving conflicts accidental.

## Agent Instruction

Make dynamic registration conflicts deterministic and explicit because dynamic registration from
plugins, generated code, guests, or config can produce duplicate names, ordering conflicts, or
shadowed handlers.

## Mechanisms

Supported by deterministic sort keys, duplicate-name errors, priority fields, provenance tracking,
conflict tests, and startup diagnostics.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
