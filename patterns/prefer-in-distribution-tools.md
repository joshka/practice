# Prefer In Distribution Tools

## Metadata

- Name: `Prefer In Distribution Tools`
- ID: `prefer-in-distribution-tools`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, tooling, architecture`
- Related: `follow-local-conventions, deliver-context-just-in-time`

## Problem

Agents spend extra context and attention on unfamiliar languages, bespoke formats, unusual CLIs, and
rare frameworks. The more the repo diverges from common, well-documented conventions, the more local
instruction it needs to get ordinary work right.

## Preferred Move

Prefer boring, common, stable tools and formats when they meet the need. Use conventional command
shapes, standard help output, common project layouts, and widely represented language idioms so the
agent can spend attention on the domain problem.

## Tradeoff

Do not choose common tools when they are dishonest for the domain. Specialized tools are fine when
they encode real constraints, but document their use and provide local examples.

## Agent Instruction

When choosing tools or formats, prefer the conventional option unless there is a clear domain reason
to differ. If you choose the unusual option, document the reason and the local usage pattern.

## Examples

Bad: the repo invents a private command protocol for ordinary help.

```text
toolctl !!describe --topic build --shape dense-v2
```

Good: the tool follows a familiar command shape.

```bash
toolctl build --help
```

## References

| Source                                      | Use      | Note                                                         |
| ------------------------------------------- | -------- | ------------------------------------------------------------ |
| [OpenAI agent legibility][agent-legibility] | `adapts` | Boring, stable technologies are easier for agents to model.  |

[agent-legibility]: https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal
