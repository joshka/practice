# Reconstruct Rationale Before Writing

## Metadata

- Name: `Reconstruct Rationale Before Writing`
- ID: `reconstruct-rationale-before-writing`
- Summary: Explanations become plausible stories when writers infer intent from current code and
  consult history only to fill gaps. Reconstruct the decision from present behavior, introducing
  and corrective changes, tests, measurements, and discussion before drafting the durable account.
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, evidence, history, rationale`
- Tags: `documentation, source-truth, reviewability, ai`
- Related: `label-doc-claims-by-evidence, DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION,
  commit-messages-for-history`

## Problem

Code shows what executes, but often underdetermines why one design was chosen over another. A writer
who begins with the implementation can produce a coherent explanation that was never the project's
reason. Looking up one old change afterward tends to decorate or confirm that story instead of
testing it.

History creates a second failure mode when it becomes the published structure. A chronological list
of changes makes readers reconstruct the current model themselves. Most readers need to know how the
system works now, why this form remains useful, and what they could break by changing it.

## Preferred Move

Separate research order from writing order.

Research the decision before drafting its rationale:

1. Establish current behavior from code, tests, contracts, and observable output.
1. Find the change that introduced the technique or representation.
1. Follow later changes that corrected, restricted, reverted, replaced, or retuned it.
1. Read full commit messages, review discussion, linked tests, benchmarks, incident notes, and
   nearby maintainer discussion when they materially affect the decision.
1. Record the problem each change addressed, the alternative it replaced, and what its evidence
   actually isolated.
1. Reconcile the resulting account with today's implementation. Separate surviving rationale,
   later drift, conventional practice, measured behavior, and unresolved inference.

Then write from the present outward. Make the current mechanism, contract, or tradeoff the subject.
Use history to support that explanation, identify a failed alternative, or warn about a regression
path. Keep chronology only when sequence itself explains the current behavior.

Scope research so evidence stays connected to the code. For large systems, inspect one subsystem or
line-bounded group with its path-scoped history rather than loading the whole repository history at
once. Give extra attention to introducing changes and recent corrections; neither age nor recency
alone determines explanatory value.

## Select Evidence Deliberately

Start with the current implementation, important callers and callees, and relevant tests. Record the
questions the present code cannot answer before opening historical sources. This keeps research tied
to a real explanatory gap.

Use scoped history as a high-recall index, then select evidence by causal value:

- changes that introduced the concept or representation;
- recent changes that define its present shape;
- fixes, reverts, removals, and changes that added or removed guards;
- measurements or incidents that explain a performance, safety, or compatibility constraint; and
- decisions in callers, generated inputs, or neighboring modules that constrain the local code.

Line attribution can identify changes behind surviving code, but it favors the last rewrite and
cannot reveal deleted checks or abandoned alternatives. Folder history can over-select mechanical
changes and miss a decision made elsewhere. Use both as discovery aids rather than treating either
as the decision record.

For discussions, search using change identifiers, dates, test names, and the vocabulary of the code.
Read enough adjacent context to distinguish proposals, experiments in progress, failed results,
jokes, and retrospective explanations. Discussion supplies context and stated intent; it does not
override the resulting code or later corrections.

Keep a compact evidence ledger. For each useful source, record the claim, the affected mechanism,
the alternative or problem it addresses, and whether it supplies current behavior, stated intent,
measurement, convention, inference, or unresolved conflict. Summarize one evidence packet before
opening the next.

## Attention Limits

Batch by coherent mechanism, using line counts only as an attention budget. Split a small but
historically dense area by decision, and combine small files when they implement one concept. Large
raw history or discussion dumps consume attention without guaranteeing that the relevant causal
thread remains visible.

Watch for these research failures:

- Recency is not relevance; introducing changes and middle regression fixes may explain more than
  the latest edit.
- A broad rewrite can replace line attribution without replacing the rationale.
- A pull request description can be incomplete, mistaken, retrospective, or copied from another
  implementation.
- A passing combined test measures the complete changed configuration, not each term or proposed
  cause independently.
- Nearby discussion can concern another experiment, and confident speculation remains speculation.
- A standard external explanation can hide the project's different representation or policy.
- More evidence can create false confidence when it has not been reduced to explicit claims and
  reconciled with the present code.

## Evidence Boundaries

A passing combined change supports the changed system under that test. It does not prove every
constant, branch, or optimization independently. A benchmark supports the measured configuration,
not every proposed cause. A maintainer explanation supports stated intent, while current behavior
still comes from the code and tests.

When the evidence stops, narrow the claim or state what remains unknown. Do not turn words such as
`intentional`, `deliberate`, `workaround`, `safe`, `faster`, or `required` into facts without a
contract, measurement, or attributable decision that earns them.

## Tradeoff

This process costs more than translating code into prose. Use it where rationale affects
correctness, performance, compatibility, safety, architecture, operational behavior, or likely
future changes. Straightforward contracts and mechanics do not need an archaeological record.

Private discussions can supply missing context, but durable docs should carry the useful reasoning
without naming discovery tools or requiring access to a private archive. Link a stable source when
readers can use it and the provenance materially improves the claim.

## Agent Instruction

Before documenting non-obvious rationale, identify the current explanatory gap, then reconstruct the
decision from current behavior, introducing and corrective history, tests, measurements, and
relevant discussion. Keep evidence in bounded, claim-labeled packets. Write the final explanation
from the current mechanism outward; use history as evidence, not as the reader's required narrative,
and state where the evidence stops.

## Example

Bad: chronology leaves the reader to infer the current design.

```text
Change A introduced a shared cache. Change B altered its key. Change C removed one field.
```

Good: the current decision leads, while history explains the constraint.

```text
The cache keys entries by normalized input because callers may spell the same request differently.
An earlier raw-input key fragmented those entries and reduced the measured hit rate. Keep
normalization before lookup when changing the request path; the available benchmark compared the
complete key change and does not isolate each normalization rule.
```

## References

| Source                                                  | Use        | Note                                                        |
| ------------------------------------------------------- | ---------- | ----------------------------------------------------------- |
| [Diataxis: explanation][diataxis]                       | `adapts`   | Explanation connects facts and gives reasons.               |
| [Rust project: stability without stagnation][stability] | `supports` | Historical tradeoffs can explain present compatibility.     |
| [Git: submitting patches][git-patches]                  | `adapts`   | Commit messages should explain motivation and consequences. |

[diataxis]: https://diataxis.fr/explanation/
[git-patches]: https://git-scm.com/docs/SubmittingPatches
[stability]: https://blog.rust-lang.org/2014/10/30/Stability/
