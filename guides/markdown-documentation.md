# Markdown And Documentation

This guide captures how documentation should be shaped in this repo and in downstream project
guidance. Prefer docs that reduce rediscovery, carry contracts clearly, and stay easy to lint,
review, and reuse.

Use this guide with [Software Change Preferences](software-change-preferences.md).

## Markdown Style

Write Markdown that is easy to read in source form and easy to diff.

- Wrap prose around 100 columns.
- Put a blank line after headings.
- Put a blank line before and after lists, blockquotes, and fenced code blocks.
- Use fenced code blocks with a language tag.
- Use `1.` markers for numbered lists.
- Format tables with aligned columns.
- Let table rows exceed the prose line limit when alignment improves readability.

Run:

```bash
markdownlint-cli2 "**/*.md"
```

The repo config links directly to the upstream lint rules it customizes.

## Docs As Contracts

Treat docs, comments, and Rustdoc as part of the behavioral surface. If behavior changes, update the
nearby docs in the same review unit. If a doc is wrong, fix the doc or the behavior intentionally;
do not leave drift for the next reader.

Good docs explain purpose, constraints, invariants, edge cases, side effects, and recovery paths.
Weak docs repeat names, signatures, or ordinary control flow.

Use [Preserve Error Context][error-context] and [Write Actionable Error Messages][actionable-errors]
when documenting failures that cross user, caller, operator, or support boundaries.

## Choose The Doc Type

Separate documentation jobs instead of mixing every reader need into one page.

- Tutorials teach by doing.
- How-to guides help a reader complete a task.
- Reference docs state exact names, options, defaults, and contracts.
- Explanation docs carry rationale, tradeoffs, and mental models.

Use Diátaxis as a framing tool, not as a rigid taxonomy. The point is to keep the document's primary
job obvious.

## Rustdoc

Rustdoc should document contracts, not narrate implementation.

For crates and modules, include the purpose, boundaries, key concepts, feature flags, constraints,
and important non-goals when they matter.

For public items, include the first-sentence summary plus relevant sections:

- `# Examples`
- `# Errors`
- `# Panics`
- `# Safety`
- `# Performance`

Prefer examples that compile. Use `no_run` when compilation matters but running requires external
systems. Use `ignore` only when the example cannot be made checkable.

## Examples

Examples should make the pattern, contract, or workflow easier to recognize. Prefer compact bad and
good examples when the contrast clarifies the rule.

Omit examples when the problem cannot be made obvious from the snippet itself. For API or
implementation-shape guidance, show the definition being introduced or changed. For review-unit
guidance, use `diff` blocks when the change itself is the point.

Use [Test Observable Behavior][test-behavior] when examples imply behavior that should be protected
by tests.

## Sources And References

References support, adapt, or contrast this repo's guidance. They do not supply the prose. Write in
this repo's voice and avoid copying or closely paraphrasing upstream text.

Use direct links to the relevant upstream section instead of broad root links. Omit the references
section when no durable source is useful.

## Review Questions

- Does the document have one primary job?
- Does the first paragraph state the useful point?
- Does the doc explain a contract, constraint, or tradeoff instead of restating names?
- Are examples small enough to understand without reconstructing a project?
- Are Markdown tables aligned?
- Did behavior changes update nearby docs?
- Do source links point to the relevant upstream section?

## References

| Source                 | Use      | Note                                                  |
| ---------------------- | -------- | ----------------------------------------------------- |
| [markdownlint][mdlint] | `adapts` | Lintable Markdown conventions and configurable rules. |
| [Diátaxis][diataxis]   | `adapts` | Framework for separating documentation jobs.          |
| [Rustdoc][rustdoc]     | `adapts` | Rust documentation conventions and section structure. |

[actionable-errors]: ../patterns/write-actionable-error-messages.md
[diataxis]: https://diataxis.fr/
[error-context]: ../patterns/preserve-error-context.md
[mdlint]: https://github.com/DavidAnson/markdownlint
[rustdoc]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html
[test-behavior]: ../patterns/test-observable-behavior.md
