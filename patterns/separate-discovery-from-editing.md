# Separate Discovery From Editing

## Metadata

- Name: `Separate Discovery From Editing`
- ID: `separate-discovery-from-editing`
- Status: `reviewed`
- Audience: `agents`
- Topics: `workflow, agents, review`
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
