# Change Sync Generated Artifacts

## Metadata

- ID: `CHANGE-SYNC-GENERATED-ARTIFACTS`
- Status: `reviewed`
- Domain: `change-shape`
- Depth: `compact`

## Rule

Keep generated artifacts in sync when they are part of the review surface.

## Why

Generated files, lockfiles, snapshots, API listings, and agent packs are part of the review surface
when they are checked into the repo. Leaving them stale makes the source change look complete while
the generated consumer-facing artifact disagrees.

## Helps

- Prevents drift between source inputs and generated outputs.

## Limits

Do not regenerate broad artifacts unrelated to the change. Run the narrow generator or explain why
the artifact is intentionally unchanged.

## Agent Instruction

Update them with the source change because checked-in generated files, lockfiles, snapshots, API
listings, or agent packs are review surfaces.

## Mechanisms

Supported by generator scripts, `--check` modes, snapshot tests, lockfile checks, API diff tools,
and PR validation that reports regenerated files.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
