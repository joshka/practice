# Label Doc Claims By Evidence

## Metadata

- Name: `Label Doc Claims By Evidence`
- ID: `label-doc-claims-by-evidence`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, evidence, review`
- Related: `write-docs-as-contracts, report-verification-honestly`

## Problem

Documentation can sound more certain than the evidence behind it. A hunch, a local observation, a
benchmark, a contract, and an upstream rule require different reader trust, but prose often presents
them with the same confidence.

## Preferred Move

Match the claim to the evidence. State contracts as contracts, measurements as measurements,
observations as observations, and preferences as preferences. If the evidence is weak, narrow the
claim or name the uncertainty. Replace ranking words with the concrete property that earns the
claim.

## Tradeoff

Do not turn every sentence into an academic citation exercise. Stable project rules and obvious code
facts can be stated directly. Label claims when the difference affects design, review, operations,
performance, security, compatibility, or future maintenance.

## Agent Instruction

When writing or revising docs, inspect strong words such as `always`, `never`, `guarantees`,
`secure`, `fast`, `safe`, `best`, and `easiest`. Keep them only when the doc points to the
contract, test, measurement, or source that supports them.

## Examples

Bad: the doc overstates a preference as a universal fact.

```markdown
This layout is always faster and prevents review confusion.
```

Good: the doc states the evidence and keeps the claim narrow.

```markdown
In this crate, grouping the parser helpers reduced review churn because reviewers could inspect the
validation path without jumping between modules.
```

## References

| Source                            | Use      | Note                                             |
| --------------------------------- | -------- | ------------------------------------------------ |
| [Google excessive claims][claims] | `adapts` | Strong claims need enough support for readers.   |
| [GitHub PR guidance][pr-review]   | `adapts` | Review context should explain purpose and scope. |

[claims]: https://developers.google.com/style/excessive-claims
[pr-review]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes
