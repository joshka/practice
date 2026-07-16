# Separate Technique From Example Policy

## Metadata

- Name: `Separate Technique From Example Policy`
- ID: `DOCS-SEPARATE-TECHNIQUE-FROM-EXAMPLE-POLICY`
- Summary: Training examples should distinguish the library or framework technique being taught
  from application-specific policy. Explain the policy's rationale, tradeoffs, and meaningful edge
  cases, then tell readers what to reuse and what to reconsider.
- Status: `draft`
- Domain: `documentation`
- Tags: `documentation, examples, source-truth, reader-locality`
- Related: `DOCS-DISTINGUISH-EXAMPLE-ROLES, DOCS-PROVE-REAL-USE-WITH-EXAMPLES,
  keep-docs-near-their-subject`

## Rule

Separate the technique an example teaches from the application policy it chooses.

## Why

A substantial integration example necessarily makes decisions beyond the library or framework API.
It may choose retry limits, buffering, resize behavior, authorization fallback, persistence, error
recovery, or scheduling policy so the example behaves like a complete application. Readers can
mistake those incidental decisions for framework requirements when the source presents every choice
at the same level.

A training-quality example makes five things findable:

- the library or framework technique being demonstrated;
- the application policy selected for this example;
- the rationale and tradeoffs behind that policy;
- edge cases that materially shape the implementation;
- which parts readers should reuse and which they should reconsider for their own application.

The distinction should also appear in source ownership. Framework setup can remain visible at the
integration boundary, while domain policy belongs in named application concepts instead of being
hidden inside schedule, router, widget, or callback wiring.

For a web-service example, a compact teaching note might say:

```markdown
## Technique

The router and middleware stack show how requests enter the framework and receive shared context.

## Example Policy

This service keeps idempotency records for 24 hours and retries upstream timeouts twice. Those are
application choices: the window bounds storage, while the retry limit favors latency over recovery.

## Reuse And Reconsider

Reuse the router and middleware ownership shape. Reconsider the idempotency window, retry limit,
authorization fallback, and persistence layer for the target service.
```

## Helps

- Prevents readers from cargo-culting application decisions as framework requirements.
- Preserves realistic examples without hiding the policy that makes them realistic.
- Gives maintainers a place to explain edge cases without narrating every implementation line.
- Makes source boundaries reinforce the example's teaching goal.

## Limits

Do not add five headings to a focused snippet whose policy is obvious or irrelevant. One sentence,
an item comment, or a module note can carry the distinction when the example is small.

Do not label ordinary language mechanics or one-off temporary values as policy. Explain decisions
that a reasonable application might choose differently and edge cases that materially affect the
shape. Keep the main technique visible instead of turning the example into an architecture essay.

## Agent Instruction

For substantial training examples, label the reusable technique and application policy, explain the
policy's tradeoffs and edge cases, and state what readers should reuse or reconsider.

## Mechanisms

Supported by example README sections, crate or module docs, source comments at policy boundaries,
example inventories, doctests for reusable API paths, and review that traces policy out of framework
orchestration into its owning concept.

## References

- [The rustdoc book: How to write documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
- [Rust API Guidelines: Documentation examples](https://rust-lang.github.io/api-guidelines/documentation.html#all-items-have-a-rustdoc-example-c-example)
- [Diataxis: Tutorials](https://diataxis.fr/tutorials/)
