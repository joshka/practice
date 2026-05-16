# Review Separate Discovery Selection Implementation

## Metadata

- ID: `REVIEW-SEPARATE-DISCOVERY-SELECTION-IMPLEMENTATION`
- Status: `reviewed`
- Domain: `review`
- Depth: `compact`

## Rule

Separate problem discovery, solution selection, and implementation review when they need different
decisions.

## Why

Some work is not ready for one implementation PR. The team may still be discovering the problem,
choosing among designs, or deciding whether the change belongs in scope at all. If those decisions
are folded into implementation review, reviewers have to evaluate the problem statement, tradeoffs,
architecture, and patch correctness at the same time.

Separating the decision layers gives each artifact a cleaner job. Issues and design notes can carry
use cases, constraints, prior art, and alternatives. Implementation reviews can then focus on
whether the accepted direction was executed correctly.

## Helps

- Prevents implementation review from becoming a hidden design-selection meeting.
- Makes problem statements, chosen direction, and patch correctness easier to review separately.

## Limits

Do not force extra process onto obvious fixes. Keep the decision layers together when the problem,
solution, and patch are small enough for one reviewer to judge directly. Split them when the design
choice, scope, or acceptance criteria are still under debate.

## Agent Instruction

Separate discovery, solution selection, and implementation review for unsettled scope or design; use
issues, design notes, or ADRs before asking reviewers to judge a patch.

## Mechanisms

Supported by issue discussions, design notes, ADRs, implementation plans, acceptance criteria,
non-goals, and PR narratives that link to the accepted direction.

## References

- [Pattern: Separate Discovery From Editing](../../patterns/separate-discovery-from-editing.md)
- [Review Explain PR Problem Model And Proof](review-explain-pr-problem-model-and-proof.md)
- [GitHub Docs: Helping others review your changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes)
- [Ed Page: PR style](https://epage.github.io/dev/pr-style/)
