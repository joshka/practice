# Agent Suggest Local Override Files

## Metadata

- Name: `Suggest Local Override Files`
- ID: `AGENT-SUGGEST-LOCAL-OVERRIDE-FILES`
- Summary: Put checkout-only facts in ignored override files instead of shared guidance. Local
  overrides keep machine-specific steering useful without leaking it to every contributor.
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Suggest ignored agent override files for local-only repo context.

## Why

Some agent instructions are true only for one checkout: local jj topology, ignored plan directories,
machine-specific paths, or temporary repo notes. Suggesting an ignored override file keeps those
facts useful without committing them into public guidance for every contributor.

## Helps

- Separates local steering from shared policy and reduces accidental leakage of machine-specific
  state.

## Limits

Do not hide durable project rules in local overrides. Promote guidance into checked docs when it
should apply to other contributors or future clones.

## Agent Instruction

Suggest ignored override files for checkout-only facts such as local jj topology, plan directories,
machine paths, or temporary repo notes.

## Mechanisms

Supported by globally ignored `AGENTS.override.md`, `.git/info/exclude`, repo `AGENTS.md`
instructions that mention local overrides, and audits for private path leaks.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
