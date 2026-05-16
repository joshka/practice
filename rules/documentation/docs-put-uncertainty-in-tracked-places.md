# Docs Put Uncertainty In Tracked Places

## Metadata

- Name: `Put Uncertainty in Tracked Places`
- ID: `DOCS-PUT-UNCERTAINTY-IN-TRACKED-PLACES`
- Summary: `Keep user docs focused on current truth and move unresolved direction to issues, ADRs,
  or roadmaps. Track speculation where it can be decided instead of implying a promise.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, source-truth, reviewability`
- Related: `document-intentional-non-goals, DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION`

## Rule

Put uncertainty in issues, ADRs, or roadmaps rather than burying it in user docs.

## Why

User docs should describe what is true now. If uncertainty about future design, incomplete support,
or possible direction is buried in user-facing prose, readers may treat it as either a promise or a
warning without knowing whether the project has committed to it.

## Helps

- Keeps user docs authoritative while preserving uncertainty in places where it can be tracked and
  resolved.

## Limits

Document known limitations that affect current use. Move speculation about future shape, unresolved
tradeoffs, or possible support to issues, ADRs, or roadmaps.

## Agent Instruction

Put uncertainty in issues, ADRs, or roadmaps rather than user docs that should describe current
truth.

## Mechanisms

Supported by issue links, ADRs, roadmap entries, support matrices, and docs review that
distinguishes current limitations from future plans.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
