# Remediate Doc Drift

## Metadata

- Name: `Remediate Doc Drift`
- ID: `remediate-doc-drift`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, maintenance, correctness`
- Related: `write-docs-as-contracts, keep-docs-near-their-subject`

## Problem

Documentation drifts when behavior changes but the nearby explanation, examples, or review guidance
do not. Readers then learn the old system from the docs and the new system from debugging.

## Preferred Move

Treat stale docs as broken contracts. Update, remove, or explicitly retire the stale claim near the
behavior change. Prefer checkable examples and current-state wording so future drift is easier to
catch. When a public API slice introduces behavior, include enough local docs, examples, or links
for a user and reviewer to understand that slice without waiting for a later docs pass.

## Tradeoff

Some historical context belongs in changelogs, migration notes, or release posts. Keep that context
when readers need history, but do not let product, API, or workflow docs depend on unexplained time
markers.

## Agent Instruction

When changing behavior, search nearby docs, examples, and agent instructions for stale claims.
Update the docs in the same review unit or report the drift as explicit follow-up work. Do not
defer caller-facing examples for newly exposed behavior unless the review notes explain why.

## Examples

Bad: the behavior changed, but the doc still describes the old command.

```diff
 fn import_table(name: TableName, tables: &mut Tables) -> Result<(), ImportError> {
+    reject_duplicate_name(&name, tables)?;
     tables.insert(name);
     Ok(())
 }
```

Good: the behavior and doc move together.

```diff
- The importer accepts duplicate table names and keeps the last one.
+ The importer rejects duplicate table names before building the typed config.

 fn import_table(name: TableName, tables: &mut Tables) -> Result<(), ImportError> {
+    reject_duplicate_name(&name, tables)?;
     tables.insert(name);
     Ok(())
 }
```

## References

| Source                          | Use        | Note                                             |
| ------------------------------- | ---------- | ------------------------------------------------ |
| [Rustdoc tests][doctests]       | `supports` | Checkable examples can catch stale examples.     |
| [Google timeless docs][current] | `adapts`   | Current-state docs reduce maintenance ambiguity. |

[current]: https://developers.google.com/style/timeless-documentation
[doctests]: https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html
