# Agent Prefer Tools Over Prompts

## Metadata

- Name: `Prefer Tools Over Prompts`
- ID: `AGENT-PREFER-TOOLS-OVER-PROMPTS`
- Summary: Move repeated instructions into tools, checks, templates, or durable guides. Tooling
  catches failures even when prompts are short, compacted, or interpreted differently.
- Related: `prefer-tools-over-prompts, teach-agents-through-tools,
  make-bad-output-mechanically-hard`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, tooling, automation, documentation`

## Rule

Prefer tools and checks over repeated prompting.

## Why

If the same instruction must be repeated to every agent, it belongs in a tool, check, template, or
guide. Tools reduce memory burden and catch failures even when the prompt is short, compacted, or
interpreted differently.

## Helps

- Converts repeated steering into durable enforcement and frees human attention for ambiguous
  decisions.

## Limits

Not every preference should become a tool. Keep judgment-heavy guidance as prose when automation
would reject valid cases or create busywork.

## Agent Instruction

Prefer tools and checks over repeated prompting; put repeated instructions in a tool, check,
template, or guide.

## Mechanisms

Supported by lint configs, generators, test helpers, CI gates, templates, snippets, repo scripts,
and audit commands.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
