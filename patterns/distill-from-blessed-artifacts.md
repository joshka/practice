# Distill From Blessed Artifacts

## Metadata

- Name: `Distill From Blessed Artifacts`
- ID: `distill-from-blessed-artifacts`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, discovery, examples`
- Related: `follow-local-conventions, document-system-mental-models`

## Problem

Prompts and plans are usually underspecified. A repository's accepted code, tests, docs, examples,
and reviews often carry thousands of small quality decisions that are not written down as explicit
rules.

## Preferred Move

Before producing a significant change, inspect representative artifacts that the maintainer already
accepts as good. Extract the patterns behind them: naming shape, error style, test granularity,
documentation tone, API boundaries, and workflow conventions. Apply the inferred principle, not
only the literal example.

## Tradeoff

Do not cargo-cult a local artifact when it is stale, inconsistent, or outside the current domain.
When examples conflict, prefer current nearby code and report the conflict instead of inventing a
private style guide.

## Agent Instruction

Use accepted local artifacts as high-density context. State which artifacts shaped the change and
which reusable principles you inferred from them.

## Examples

Bad: the agent follows the prompt literally and ignores the repo's established shape.

```text
Implemented a new parser with a custom error enum and snapshot tests because the prompt asked for
"a parser."
```

Good: the agent extracts the surrounding pattern before implementing.

```text
Matched the existing parser modules: a typed config boundary, thiserror errors with operation
context, and table-driven tests for valid and invalid inputs.
```
