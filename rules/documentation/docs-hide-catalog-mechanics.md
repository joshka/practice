# Docs Hide Catalog Mechanics

## Metadata

- ID: `DOCS-HIDE-CATALOG-MECHANICS`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Hide catalog mechanics unless citation, automation, or contribution workflow depends on them.

## Why

Rule IDs, prefixes, domains, generated indexes, source layout, and UI containers are useful
maintenance machinery, but they are usually not the reader's task. Public navigation copy that says
"each domain groups rules by the prefix used in rule IDs" or "each card maps a recurring work area"
makes readers parse the catalog model before they can choose the right page.

Lead with the reader-facing grouping: documentation, Rust APIs, testing, review, source control, or
agent workflow. Mention IDs, prefixes, domains, or generated structure only when the reader needs
them for stable links, review comments, agent snippets, or repository contribution work.

## Helps

- Keeps site copy oriented around work areas and artifacts instead of implementation taxonomy.

## Limits

Catalog mechanics are appropriate in maintainer docs, contribution guides, generator docs, and rule
authoring instructions. They are also appropriate when explaining stable IDs, generated snippets, or
source layout is the point of the page.

## Agent Instruction

Lead with reader-facing work areas and artifacts; mention rule IDs, prefixes, domains, generated
indexes, source layout, or UI containers only for citation, automation, or contribution workflow.

## Mechanisms

Supported by landing-page review, generated-index review, maintainer-doc separation, and copy checks
that flag UI-container actors such as "cards," "domains," "pages," or "sections" in user-facing
navigation prose.

## References

- [Docs Match Page Shape To Reader Task](docs-match-page-shape-to-reader-task.md)
- [Docs Use Concrete Details](docs-use-concrete-details.md)
- [Diataxis: reference](https://diataxis.fr/reference/)
