# Preserve Intent Over Literalism

## Metadata

- Name: `Preserve Intent Over Literalism`
- ID: `preserve-intent-over-literalism`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, judgment, safety`
- Related: `define-good-before-judgment-heavy-work, spend-human-attention-on-ambiguity`

## Problem

Agents can satisfy the literal words of a request while violating the user's underlying goal. This
is especially risky for publication, merging, deletion, credentials, production changes, and other
externally visible actions.

## Preferred Move

Infer the safe operating intent behind the request and preserve it. If the literal command conflicts
with repo policy, safety gates, or normal review expectations, stop and report the conflict instead
of taking a surprising shortcut.

## Tradeoff

Do not invent hidden requirements to avoid work. Use this pattern for irreversible, privileged,
externally visible, or policy-bound actions where literal compliance could violate the actual goal.

## Agent Instruction

Before taking a high-impact action, check whether the literal request matches the safe intent. If it
does not, pause and ask or report the policy gate.

## Examples

Bad: the agent bypasses a gate to satisfy "merge it."

```text
Normal merge was blocked, so I used admin merge before required checks passed.
```

Good: the agent preserves the landing intent.

```text
Merge is blocked because required checks are still failing. I did not bypass the gate; the next step
is to fix CI or wait for checks to pass.
```

## References

| Source                                  | Use      | Note                                                       |
| --------------------------------------- | -------- | ---------------------------------------------------------- |
| [OpenAI human role][human-role]         | `adapts` | Humans set intent and validation; agents execute the loop. |

[human-role]: https://openai.com/index/harness-engineering/#what-agent-generated-actually-means
