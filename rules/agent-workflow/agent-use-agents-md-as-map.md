# Agent Use Agents Md As Map

## Metadata

- ID: `AGENT-USE-AGENTS-MD-AS-MAP`
- Legacy ID: `R-0811`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Use `AGENTS.md` as a map, not the whole manual.

## Why

`AGENTS.md` becomes hard to use when it tries to contain every rule, example, and exception.
Treating it as a map keeps startup context compact while pointing agents to deeper guides,
mechanisms, and local overrides when the task needs them.

## Helps

- Keeps agent instructions scannable and reduces context bloat without losing durable guidance.

## Limits

Inline critical safety rules that must always be visible. Link deeper detail when the rule is
task-specific or too long for every agent run.

## Agent Instruction

Use `AGENTS.md` to route agents to deeper guides because a full rule set would make the file hard to
scan.

## Mechanisms

Supported by short root `AGENTS.md` files, guide links, snippets, local override files, and agent
packs generated from reviewed rules.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
