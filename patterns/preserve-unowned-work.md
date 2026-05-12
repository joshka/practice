# Preserve Unowned Work

## Metadata

- Name: `Preserve Unowned Work`
- ID: `preserve-unowned-work`
- Status: `reviewed`
- Audience: `agents`
- Topics: `workflow, version-control, agents`
- Related: `follow-local-conventions, small-reviewable-chunks`

## Problem

Shared working copies can contain edits made by someone else or by an earlier task. Treating those
edits as cleanup noise can lose work, widen the diff, or make review history misleading.

## Preferred Move

Check the working-copy state before editing. Reread files before patching them, work around
unrelated edits, and keep your change focused on files and lines needed for the current chunk.

## Tradeoff

Preserving unowned work can leave a stack less tidy than a clean rewrite. If another change blocks
the task, stop and ask for direction instead of guessing which work should win.

## Agent Instruction

Do not overwrite, revert, or absorb changes you did not make. If unowned work blocks the requested
change, report the conflict and ask how to proceed.
