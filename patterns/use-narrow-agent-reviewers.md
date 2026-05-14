# Use Narrow Agent Reviewers

## Metadata

- Name: `Use Narrow Agent Reviewers`
- ID: `use-narrow-agent-reviewers`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, review, guardrails`
- Related: `make-bad-output-mechanically-hard, review-proof-not-just-code`

## Problem

General review prompts can miss important details or produce vague feedback. Review quality improves
when each reviewer has a specific guardrail, domain, or failure mode to inspect.

## Preferred Move

Use focused agent reviewers for narrow concerns: security, architecture boundaries, docs drift,
test quality, accessibility, performance, dependency risk, or release safety. Let each reviewer
produce targeted feedback that the primary agent can address.

## Tradeoff

Too many reviewers can create noise. Add a narrow reviewer when the concern is important,
repeatable, and easier to check with focused context than with one broad review pass.

## Agent Instruction

When a change has a specific risk, request or simulate a focused review for that risk. Keep the
reviewer's scope narrow and report which guardrail it checked.

## Examples

Bad: one generic reviewer is expected to catch every class of issue.

```text
Please review this PR.
```

Good: the review asks for the relevant guardrail.

```text
Run an architecture-boundary review for imports that cross from UI into repository code, then run a
docs-drift review for changed public behavior.
```

## References

| Source                              | Use        | Note                                                            |
| ----------------------------------- | ---------- | --------------------------------------------------------------- |
| [OpenAI agent review loop][reviews] | `adapts`   | Agent-to-agent review can move feedback handling into the loop. |

[reviews]: https://openai.com/index/harness-engineering/#redefining-the-role-of-the-engineer
