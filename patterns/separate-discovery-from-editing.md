# Separate Discovery From Editing

## Metadata

- Name: `Separate Discovery From Editing`
- ID: `separate-discovery-from-editing`
- Summary: Editing while still discovering the system can bake early misunderstandings into the
  diff. Read enough to find the ownership, constraints, and likely change shape before making
  scoped edits.
- Status: `reviewed`
- Audience: `agents`
- Topics: `workflow, agents, review`
- Tags: `agent-workflow, change-shape, reviewability`
- Related: `follow-local-conventions, preserve-unowned-work`

## Problem

Exploration can turn into edits before the contributor understands the local shape. The first
plausible fix then reflects a guess, not the repository's actual contracts, conventions, and
failure modes.

## Preferred Move

Inspect the relevant files, instructions, tests, and current working-copy state before changing
tracked files. Start editing only after the target chunk and likely verification path are clear.

## Tradeoff

Tiny mechanical edits may not need a long discovery pass. Keep exploration proportional to risk,
but do enough reading to avoid inventing structure from one isolated example.

## Agent Instruction

Do a targeted read-only pass before editing. Summarize what context controls the change, then patch
only the confirmed scope.

## Examples

Bad: the first plausible file shape becomes the implementation.

```text
Created a new helpers module before reading the existing module layout.
```

Good: exploration identifies the local owner before editing.

```text
Read AGENTS.md, nearby modules, and tests; patched the existing workspace path helper.
```
