# Agent Prefer In Distribution Tools

## Metadata

- Name: `Prefer In-Distribution Tools`
- ID: `AGENT-PREFER-IN-DISTRIBUTION-TOOLS`
- Summary: Use standard project commands, supported CLIs, and documented workflows before inventing
  ad hoc tool paths. Familiar tools reduce misuse and make agent output easier to rerun.
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Prefer in-distribution tools for agent-facing work.

## Why

Agents are more reliable with tools that match their trained and tested workflow. For repo
operations, prefer standard CLI commands, project scripts, and well-supported formatter or test
tools before inventing ad hoc shell pipelines or UI workflows.

## Helps

- Reduces tool misuse and makes commands easier for humans to rerun.

## Limits

Use specialized tools when they are the project standard or the only reliable way to inspect the
artifact. The point is predictable operation, not lowest common denominator tooling.

## Agent Instruction

Prefer in-distribution tools for agent-facing work because trained and tested tool paths tend to be
more reliable.

## Mechanisms

Supported by documented repo commands, `just` or script wrappers, `cargo` workflows, `jj` aliases,
markdownlint, and generated checks.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
