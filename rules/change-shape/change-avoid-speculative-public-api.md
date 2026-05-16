# Change Avoid Speculative Public API

## Metadata

- Name: `Avoid Speculative Public API`
- ID: `CHANGE-AVOID-SPECULATIVE-PUBLIC-API`
- Summary: Add public surfaces only when current or accepted callers need them. Waiting for concrete
  pressure keeps compatibility commitments smaller and easier to validate.
- Status: `reviewed`
- Domain: `change-shape`
- Depth: `compact`

## Rule

Do not add public API for future features before the need is real.

## Why

Public API turns a local guess into a contract that users, downstream integrations, examples, tests,
docs, and compatibility promises may start depending on. Speculative API often preserves the wrong
shape: names, parameter order, return types, extension points, and error behavior chosen before the
real use case has put pressure on the design.

Waiting for a concrete use keeps the first public shape smaller and easier to explain. It also lets
maintainers validate the API against actual callers instead of designing around imagined future
requirements.

## Helps

- Prevents accidental compatibility commitments to unused names, types, and extension points.
- Keeps review focused on the current behavior rather than a guessed future design.

## Limits

Some foundation work is legitimate when a near-term feature has accepted requirements, migration
pressure, or external compatibility constraints. In that case, keep the API as narrow as the known
caller needs, mark experimental surfaces clearly where appropriate, and document the evidence for
adding it now.

## Agent Instruction

Avoid speculative public API; add public names, types, extension points, and compatibility promises
only for concrete current needs or explicitly accepted near-term requirements.

## Mechanisms

Supported by issue-scoped acceptance criteria, public API review, experimental API labels,
compatibility notes, downstream-use searches, and follow-up issues for deferred extension points.

## References

- [Public API Changes Have Downstream Cost](../../principles/public-api-changes-have-downstream-cost.md)
- [Fowler: Yagni](https://martinfowler.com/bliki/Yagni.html)
- [Rust API Guidelines: public APIs are stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
- [Cargo SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html)
