# Docs Distinguish Example Roles

## Metadata

- Name: `Distinguish Example Roles`
- ID: `DOCS-DISTINGUISH-EXAMPLE-ROLES`
- Summary: `Name whether an example is focused, canonical, survey, integration, or showcase work.
  That role controls how complete, copyable, and validated the example must be.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, examples, verification`
- Related: `DOCS-PROVE-REAL-USE-WITH-EXAMPLES, DOCS-MARK-NONCOMPILING-EXAMPLES-HONESTLY`

## Rule

Distinguish example roles instead of treating every example as the same kind of proof.

## Why

Examples answer different reader questions. A small focused example teaches one concept, a canonical
workflow shows the shortest complete path, a survey example shows breadth, an integration sketch
shows ownership structure, and an interactive showcase proves a runnable surface. Blending those
roles makes examples either too small to prove the workflow or too large to teach the local rule.

## Helps

- Keeps example sets from becoming a pile of generic snippets.
- Makes review ask whether an example is canonical, illustrative, broad, integrative, or
  interactive.
- Helps maintainers decide which examples must compile, which examples can be sketches, and which
  examples need explicit opt-in behavior.

## Limits

Do not create a taxonomy for a tiny page with one obvious example. Some examples can serve multiple
roles, but the primary role should still be clear enough that readers know how much to trust and
reuse it.

## Agent Instruction

Name the example's primary role before expanding it; keep focused, canonical, survey, integration,
and showcase examples from collapsing into one generic snippet.

## Mechanisms

Supported by example inventories, README review, docs.rs example review, doctest coverage for
copyable public examples, and labels that separate canonical examples from illustrative sketches.

## References

- [Diataxis: the map](https://diataxis.fr/map/)
- [Rust API Guidelines: Documentation](https://rust-lang.github.io/api-guidelines/documentation.html)
- [Docs Prove Real Use With Examples](docs-prove-real-use-with-examples.md)
- [Docs Show Side Effects In Live Examples](docs-show-side-effects-in-live-examples.md)
