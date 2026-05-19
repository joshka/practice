# Agent Keep Durable Context On Disk

## Metadata

- Name: `Keep Durable Context on Disk`
- ID: `AGENT-KEEP-DURABLE-CONTEXT-ON-DISK`
- Summary: Store project facts, accepted decisions, and long-lived operating notes in files instead
  of relying on chat context. Durable context makes future sessions and reviews resumable.
- Related: `use-disk-as-context-sink, prefer-durable-summaries,
  private-context-is-not-shared-context`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, agent-context, source-truth, documentation`

## Rule

Keep durable context on disk.

## Why

Prompt context disappears, compacts, or becomes invisible to future sessions. Durable project facts,
review decisions, task plans, and operating notes should live in files when they need to guide later
agents or human reviewers.

## Helps

- Prevents accepted guidance from being trapped in one chat and makes long-running work resumable.

## Limits

Do not commit private scratch state or local-only checkout facts. Put local steering in ignored
files and public guidance in durable docs only after it is generalized.

## Agent Instruction

Keep durable context on disk because prompt context disappears, compacts, or becomes invisible to
future sessions.

## Mechanisms

Supported by `AGENTS.md`, checked guides, ignored `AGENTS.override.md`, `.plans` files for local
work, ADRs, and generated snippets.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
