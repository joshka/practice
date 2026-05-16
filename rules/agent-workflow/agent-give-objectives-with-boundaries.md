# Agent Give Objectives With Boundaries

## Metadata

- ID: `AGENT-GIVE-OBJECTIVES-WITH-BOUNDARIES`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Give agents objectives with boundaries, not brittle step lists.

## Why

A brittle step list can make an agent follow the wrong route even after the codebase shows a better
one. An objective with boundaries names the desired outcome, forbidden moves, relevant files, and
proof while leaving room to choose the local implementation path.

## Helps

- Preserves intent while letting the agent adapt to real repo structure and discovered constraints.

## Limits

Use explicit steps when the order is the safety property, such as a migration, release, or
destructive operation. Otherwise prefer outcome, scope, and constraints.

## Agent Instruction

Give agents objectives with boundaries so they can adapt to real repo structure without following
brittle step lists.

## Mechanisms

Supported by task briefs with objective, scope, non-goals, allowed tools, changed-file ownership,
and required validation.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
