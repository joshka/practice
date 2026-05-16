# Change Avoid Unnecessary Dependency Churn

## Metadata

- Name: `Avoid Unnecessary Dependency Churn`
- ID: `CHANGE-AVOID-UNNECESSARY-DEPENDENCY-CHURN`
- Summary: Keep package, manifest, and lockfile movement out of unrelated work. Separate dependency
  changes make build, compatibility, and downstream risk reviewable on their own.
- Status: `reviewed`
- Domain: `change-shape`
- Depth: `compact`

## Rule

Do not include dependency churn unless it is necessary for the task.

## Why

Dependency updates change lockfiles, feature graphs, minimum versions, build output, and downstream
compatibility. If that churn rides along with an unrelated feature or doc fix, reviewers must
separate package-manager noise from the actual behavior change.

## Helps

- Keeps dependency risk reviewable and prevents unrelated lockfile movement from obscuring the task.

## Limits

Include dependency changes when the task requires a new API, security fix, or compatibility repair.
Otherwise leave lockfile refreshes and manifest minimum changes to their own review unit.

## Agent Instruction

Avoid dependency churn unless it is necessary for the task; dependency updates change lockfiles,
feature graphs, minimum versions, build output, and downstream compatibility.

## Mechanisms

Supported by focused jj changes, dependency-update PRs, `cargo tree`, minimal-version checks, and
diff review that separates manifest, lockfile, and source changes.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
