# Keep Automations Repo Owned

## Metadata

- Name: `Keep Automations Repo Owned`
- ID: `keep-automations-repo-owned`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, automation, runbooks`
- Related: `code-is-memory-of-process, keep-docs-near-their-subject`

## Problem

Automations become opaque when their real instructions live only in an app instance, schedule
configuration, or private prompt. They are hard to review, version, recover, and hand off.

## Preferred Move

Keep automation instructions in the repository whenever the workflow belongs to the project. The
scheduler prompt should be small and point to a reviewed runbook, script, or guide that the repo
owns.

## Tradeoff

Some secrets, credentials, schedules, or deployment wiring must live outside the repo. Keep those as
external configuration, but keep the workflow's intent and reviewed steps in version control.

## Agent Instruction

When creating or revising an automation, put the durable runbook or script in the repo and keep the
external automation prompt thin. Report which repo file owns the workflow.

## Examples

Bad: the app-owned automation contains the only copy of the workflow.

```text
Every Monday, inspect releases, decide if the binary needs rebuilding, run the upgrade, verify the
device, and message me if anything looks wrong.
```

Good: the app-owned automation delegates to a repo-owned runbook.

```text
You are the weekly upgrade agent. Follow docs/automations/weekly-upgrade.md.
```
