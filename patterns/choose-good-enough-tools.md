# Choose Good Enough Tools

## Metadata

- Name: `Choose Good Enough Tools`
- ID: `choose-good-enough-tools`
- Summary: Tooling choices can become a distraction when the available tool is already adequate for
  the risk. Prefer the simplest tool that gives trustworthy feedback, upgrading only when accuracy,
  repeatability, or scale requires it.
- Status: `reviewed`
- Audience: `both`
- Topics: `tooling, judgment, pragmatism`
- Tags: `tooling, local-conventions, agent-workflow, reviewability`
- Related: `prefer-in-distribution-tools, encode-nonfunctional-requirements`

## Problem

Tool choice can consume more energy than the work itself. Software options often look equally
capable from the outside, have fuzzy consequences, and come with confident but contradictory advice.
Agents can amplify this by exploring every plausible category instead of selecting a workable path.

## Preferred Move

Define the actual constraints, then choose a tool that is good enough for those constraints and easy
for this repo to operate. Prefer familiarity, ecosystem fit, inspectability, and maintenance cost
over theoretical optimality when the difference between options is not decisive.

## Tradeoff

Do not use "good enough" to excuse a tool that violates a hard requirement. Security, latency,
portability, licensing, accessibility, and team expertise can make a tool clearly wrong.

## Agent Instruction

When asked to choose a tool, state the constraints and pick the simplest option that satisfies them.
Avoid broad tool surveys unless the choice is genuinely constrained by unknowns.

## Examples

Bad: the decision starts with the tool universe.

```text
I compared twelve job queue systems and three workflow engines before deciding how to run one
nightly cleanup task.
```

Good: the decision starts with the actual constraints.

```text
This task runs once per night, can retry from the beginning, and only needs repo-local logs. A
cron-triggered command is enough until we need durable step recovery.
```

## References

| Source                                | Use      | Note                                                     |
| ------------------------------------- | -------- | -------------------------------------------------------- |
| [No Best Tool For The Job][best-tool] | `adapts` | Many software choices are too close for a single "best." |

[best-tool]: https://frantic.im/best-tool/
