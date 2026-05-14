# Document Intentional Non Goals

## Metadata

- Name: `Document Intentional Non Goals`
- ID: `document-intentional-non-goals`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, scope, rationale`
- Related: `write-docs-as-contracts, document-system-mental-models`

## Problem

Maintainers repeat the same debate when the reason for not doing something is only held in memory.
The absence of a feature, abstraction, dependency, or validation rule can look accidental when it was
actually a deliberate scope decision.

## Preferred Move

Document intentional omissions when they are likely to be rediscovered. State the rejected direction,
the reason it is out of scope, and the signal that would justify revisiting it.

## Tradeoff

Do not write a non-goal for every ordinary omission. Use this pattern when the missing thing is
plausible, has already come up in review, or would be expensive to rediscover later.

## Agent Instruction

When a change intentionally avoids a plausible feature, abstraction, dependency, or compatibility
path, add a short non-goal or rationale note near the relevant guide, module, or API. Include the
revisit condition instead of making the decision sound permanent.

## Examples

Bad: the design leaves an obvious question unanswered.

```md
## Configuration

The tool reads project settings from `project.toml`.
```

Good: the doc records the scope boundary and revisit signal.

```md
## Configuration

The tool reads project settings from `project.toml`.

Non-goal: environment-variable configuration is intentionally omitted for now. Add it when there is
a concrete non-interactive deployment path that cannot write a project config file.
```

## References

| Source                                  | Use        | Note                                                         |
| --------------------------------------- | ---------- | ------------------------------------------------------------ |
| [Diátaxis explanation context][context] | `supports` | Explanation is where design reasons and alternatives belong. |

[context]: https://diataxis.fr/explanation/#provide-context
