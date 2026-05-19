# Code Is Memory Of Process

## Metadata

- Name: `Code Is Memory Of Process`
- ID: `code-is-memory-of-process`
- Summary: Code accumulates the history of decisions, shortcuts, and workflows that produced it.
  When changing it, preserve useful operational memory while removing obsolete process scars that no
  longer serve readers.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, automation, process`
- Tags: `source-truth, tooling, automation, agent-workflow`
- Related: `prefer-tools-over-prompts, prefer-durable-summaries`

## Problem

Manual process knowledge is fragile. If a workflow only lives in someone's memory, a chat thread, or
a one-off prompt, every future run depends on rediscovering the same steps and constraints.

## Preferred Move

Turn stable process knowledge into code, scripts, runbooks, tests, or checked templates. Use prose
to explain judgment and tradeoffs; use executable artifacts to preserve repeatable steps.

## Tradeoff

Do not automate a process before it is understood. For early exploration, write a short runbook or
checklist first, then promote the stable parts into code once the loop repeats.

## Agent Instruction

When a workflow repeats, ask what part of the process should become a checked artifact. Prefer a
small script, runbook, test, or template over another transient prompt.

## Examples

Bad: the process only exists in a chat message.

```text
Every Friday, remember to fetch the upstream release, rebuild the binary, test SSH reachability, and
then cut over production.
```

Good: the process has a durable entry point.

```text
docs/automations/weekly-upgrade.md describes the workflow, and
scripts/weekly-upgrade-check.sh verifies the canary before cutover.
```
