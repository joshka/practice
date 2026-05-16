# Budget Tokens For Feedback Loops

## Metadata

- Name: `Budget Tokens For Feedback Loops`
- ID: `budget-tokens-for-feedback-loops`
- Summary: Long-running agent work can exhaust context before validation, review, or handoff
  happens. Reserve space for feedback loops by summarizing durable state and avoiding unnecessary
  transcript growth.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, evaluation, budgeting`
- Tags: `agent-workflow, agent-context, verification`
- Related: `close-the-agent-loop, spend-human-attention-on-ambiguity`

## Problem

Token spend is easy to treat as waste when it is measured like a software bill instead of as part of
the cost of doing work. Under-spending on review agents, cleanup loops, evals, and verification can
leave human attention as the bottleneck.

## Preferred Move

Budget agent tokens for feedback loops that improve outcomes: validation, review, security scans,
garbage collection, documentation checks, and harness evals. Measure the value of the loop by
quality, throughput, and reduced human attention, not by raw token volume.

## Tradeoff

Do not Goodhart token consumption. A token floor is useful only when it funds a loop with a clear
purpose and evidence of value. If the loop stops improving outcomes, change or remove it.

## Agent Instruction

When proposing an agent loop, state what signal the token spend buys and how its effectiveness will
be judged. Avoid treating token volume itself as success.

## Examples

Bad: token spend becomes the metric.

```text
Run more agents until the weekly token budget is used.
```

Good: token spend funds a measurable feedback loop.

```text
Run the nightly docs-drift and security-review agents. Track actionable findings, false positives,
and human review time saved.
```

## References

| Source                          | Use      | Note                                                         |
| ------------------------------- | -------- | ------------------------------------------------------------ |
| [OpenAI scarce attention][time] | `adapts` | Human time and attention are treated as the scarce resource. |

[time]: https://openai.com/index/harness-engineering/#redefining-the-role-of-the-engineer
