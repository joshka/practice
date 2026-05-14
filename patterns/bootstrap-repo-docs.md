# Bootstrap Repo Docs

## Metadata

- Name: `Bootstrap Repo Docs`
- ID: `bootstrap-repo-docs`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, repositories, onboarding`
- Related: `document-system-mental-models, use-agents-md-as-map`

## Problem

New or newly-documented repositories often start with scattered notes or an overbuilt doc tree. Both
make readers guess where to begin, what is authoritative, and which conventions are real.

## Preferred Move

Start with a small durable map: what the repo is for, how to build or validate it, where the
important concepts live, how contributors should work, and which docs are canonical. Put user,
maintainer, and decision records in different layers so the first reading path stays light. Add
deeper docs only when there is stable content to put behind the map.

## Tradeoff

Do not create placeholder pages to satisfy an imagined structure. Empty docs teach readers that the
map is unreliable. It is better to name the missing doc in a plan than to publish a hollow page.

## Agent Instruction

When bootstrapping repo docs, create the minimum useful entry points and link to real content. Avoid
placeholder files; capture planned docs in a roadmap or issue until they have durable substance. Do
not front-load maintainer context in onboarding docs.

## Examples

Bad: the repo has a large empty tree.

```text
docs/
  architecture.md
  api.md
  operations.md
  testing.md
```

Good: the repo has a small map with real entry points.

```text
README.md
AGENTS.md
guides/
  validation.md
  release.md
references/
  doc-plan.md
```

## References

| Source                         | Use      | Note                                                   |
| ------------------------------ | -------- | ------------------------------------------------------ |
| [Diataxis applying][applying]  | `adapts` | Documentation maps should follow reader needs.         |
| [Rust API crate docs][crate]   | `adapts` | Crate-level docs should orient readers to the library. |

[applying]: https://diataxis.fr/application/
[crate]: https://rust-lang.github.io/api-guidelines/documentation.html#c-crate-doc
