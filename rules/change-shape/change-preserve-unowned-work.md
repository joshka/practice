# Change Preserve Unowned Work

## Metadata

- ID: `CHANGE-PRESERVE-UNOWNED-WORK`
- Status: `reviewed`
- Domain: `change-shape`
- Depth: `compact`

## Rule

Preserve unowned work.

## Why

A working tree can contain edits from the user, another agent, generated state, or an earlier
in-progress change. Reformatting, reverting, or moving that work because it is nearby violates
ownership and can destroy context outside the task.

## Helps

- Protects parallel work and keeps the current diff accountable for only the files it owns.

## Limits

If unowned work blocks validation or editing, inspect it and adapt. Ask before removing, reverting,
or rewriting work that is not clearly part of your task.

## Agent Instruction

Preserve unowned work because a working tree can contain edits from the user, another agent, generated
state, or an earlier in-progress change.

## Mechanisms

Supported by `jj status`, path-scoped diffs, fresh jj changes for new tasks, ownership notes in
handoffs, and review of touched files before finalizing.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
