# Spend Human Attention On Ambiguity

## Metadata

- Name: `Spend Human Attention On Ambiguity`
- ID: `spend-human-attention-on-ambiguity`
- Summary: Agent throughput can exceed the maintainer's ability to review and steer. Delegate
  execution and inspection, but reserve human attention for ambiguous goals, taste, architecture,
  risk, and the systems that make future delegation safer.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, prioritization, review`
- Related: `small-reviewable-chunks, define-good-before-judgment-heavy-work`

## Problem

Agent throughput can create more work than the maintainer can review. Human attention is still the
scarce resource, especially for ambiguous goals, product judgment, new architecture, and decisions
where the acceptance criteria are not yet known.

## Preferred Move

Use agents for execution, inspection, mechanical cleanup, and well-specified changes. Spend human
attention on choosing goals, resolving ambiguity, setting taste and constraints, reviewing high-risk
outputs, and improving the systems that make future agent work safer.

## Tradeoff

Do not abdicate judgment just because a task is easy to delegate. If the output changes product
direction, security posture, public API, or long-term architecture, keep a human decision point in
the loop.

## Agent Instruction

Before doing broad work, identify which decisions need human attention and which parts are safe to
execute mechanically. Ask for review at the ambiguity boundary, not after burying it in a large diff.

## Examples

Bad: the agent consumes review attention on a large ambiguous bundle.

```text
I redesigned the onboarding flow, changed the data model, and updated the API because it seemed
cleaner.
```

Good: the agent separates execution from the human decision.

```text
I found three onboarding data-model options and recommend option two. Once chosen, the migration and
tests are mechanical.
```
