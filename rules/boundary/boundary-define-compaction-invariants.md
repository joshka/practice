# Boundary Define Compaction Invariants

## Metadata

- ID: `BOUNDARY-DEFINE-COMPACTION-INVARIANTS`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Define explicit budget and cut-point invariants for compaction.

## Why

Compaction deletes, summarizes, or moves information. Without explicit budget and cut-point
invariants, a compactor can drop required context, keep too much, or produce nondeterministic
summaries that later agents treat as authoritative.

## Helps

- Makes summarization, pruning, and context-window management testable and reviewable.

## Limits

Do not over-model throwaway local trimming. Define invariants when compaction output will guide
future execution, review, or persistence.

## Agent Instruction

Define explicit budget and cut-point invariants before compaction deletes, summarizes, or moves
information.

## Mechanisms

Supported by token budgets, stable cut markers, before/after fixtures, invariant tests, and logs
that report what was kept, summarized, or discarded.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
