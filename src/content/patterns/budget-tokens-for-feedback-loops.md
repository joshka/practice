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
- Tags: `agent-workflow, agent-context, verification, feedback-loops`
- Related: `close-the-agent-loop, spend-human-attention-on-ambiguity`

## Problem

Agent work can spend its budget on implementation and repeated narration, leaving too little for
validation and handoff. It can also spend more on repeated reviews than their findings justify.
Both failures increase maintainer work.

## Preferred Move

Budget agent tokens for feedback loops that improve outcomes: validation, review, security scans,
garbage collection, documentation checks, and harness evals. Measure the value of the loop by
quality, throughput, and reduced human attention, alongside the user's time and token limits.

Give each pass a distinct question and stopping condition. Continue after a new defect, changed
artifact, or uncovered contract warrants another check. Once the agreed gates pass, stop repeating
unchanged checks or collecting equivalent reviews. Keep detailed evidence in one place and report
only decisions, meaningful changes, and unresolved limits in coordination updates.

## Tradeoff

Treat a budget as a ceiling, not a target to consume. Extra capacity can fund a useful check, but
does not justify another pass without an expected finding or decision. Do not skip required gates
to save tokens; if a hard limit prevents completion, report the unfinished checks explicitly.

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
