# Review Classify Prototype Reuse

## Metadata

- ID: `REVIEW-CLASSIFY-PROTOTYPE-REUSE`
- Legacy ID: `R-0706`
- Status: `draft`
- Domain: `review`
- Depth: `compact`

## Rule

Classify what a rebuild reuses from a prototype or prior implementation.

## Why

Prototype rebuilds can blur four different kinds of reuse: externally visible behavior, evidence
from tests or production use, replaceable internal shape, and load-bearing boundaries. Treating all
prototype details as either disposable or authoritative makes review harder. A name, helper layout,
crate boundary, or document shape may be accidental, while a protocol behavior, migration path, or
integration boundary may be the reason the prototype worked.

Classifying reuse lets reviewers preserve the parts that carry evidence or compatibility while
replacing the parts that were only scaffolding.

## Helps

- Prevents rewrites from discarding proven behavior or preserving accidental structure.
- Makes load-bearing boundaries visible before a smaller local API removes needed growth room.

## Limits

Do not turn every small cleanup into architecture archaeology. Use this rule when a change rebuilds,
ports, replaces, or extracts behavior from an existing prototype, spike, prior implementation, or
legacy component. Record uncertain classifications as inferred or unknown instead of overstating
evidence.

## Agent Instruction

Classify prototype reuse as behavior, evidence, replaceable shape, or load-bearing boundary before
changing the boundary.

## Mechanisms

Supported by issue notes, ADRs for durable boundaries, comparison tests, migration plans, review
packets, and explicit non-goals for prototype-only shape.

## References

- [Review Use ADRs For Boundaries And Ownership](review-use-adrs-for-boundaries-and-ownership.md)
- [Review Label Speculation As Inferred Or Unknown](review-label-speculation-as-inferred-or-unknown.md)
- [Martin Fowler: Sacrificial Architecture](https://martinfowler.com/bliki/SacrificialArchitecture.html)
- [Martin Fowler: Branch By Abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html)
