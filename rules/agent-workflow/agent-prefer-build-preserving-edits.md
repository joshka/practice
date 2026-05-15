# Agent Prefer Build Preserving Edits

## Metadata

- ID: `AGENT-PREFER-BUILD-PRESERVING-EDITS`
- Legacy ID: `R-0823`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Prefer build-preserving edits when the route stays natural.

## Why

A long period of broken build state hides which edit caused the failure and makes agent recovery
harder. When practical, refactor and change code in slices that keep tests or at least compilation
close to green after each step.

## Helps

- Improves bisectability, local recovery, and confidence during multi-step edits.

## Limits

Some migrations need a short broken interval. Do not contort the design just to preserve
buildability; use this preference when the natural route allows it.

## Agent Instruction

Prefer build-preserving edits on natural paths so failures stay close to the edit that caused them.

## Mechanisms

Supported by small jj changes, compiler checks, focused tests after each slice, feature flags,
compatibility shims, and temporary adapters that can be removed later.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
