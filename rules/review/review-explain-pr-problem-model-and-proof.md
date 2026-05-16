# Review Explain PR Problem Model And Proof

## Metadata

- ID: `REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`
- Status: `reviewed`
- Domain: `review`
- Depth: `compact`

## Rule

Explain the problem, mental model, tradeoffs, validation, and docs impact in PR descriptions.

## Why

Reviewers should not have to reverse-engineer the intent from the diff. A good PR description tells
them what problem to look for, which model makes the diff make sense, what tradeoffs were accepted,
which commands or manual checks provide evidence, and whether docs, examples, or agent instructions
changed with the behavior.

## Helps

- Reduces reviewer guesswork, speeds review, and leaves future maintainers a useful explanation of
  why the change exists.

## Limits

Do not write a session diary. Include rejected options only when they explain an otherwise
surprising design choice, risk, or follow-up.

## Agent Instruction

Explain the problem, mental model, tradeoffs, validation, and docs impact so reviewers do not
reverse-engineer intent from the diff.

## Mechanisms

Supported by PR templates, review packets, validation checklists, docs-impact sections, and inline
comments for decisions that are easiest to understand next to the changed code.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Ed Page: PR style](https://epage.github.io/dev/pr-style/)
- [GitHub Docs: helping others review your
  changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes)
