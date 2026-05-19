# Follow Local Conventions

## Metadata

- Name: `Follow Local Conventions`
- ID: `follow-local-conventions`
- Summary: Inconsistent style and structure make each change feel like a new design decision. Start
  from nearby patterns and only diverge when the local convention cannot support the current need.
- Status: `reviewed`
- Audience: `both`
- Topics: `workflow, review, agents`
- Tags: `local-conventions, change-shape, reviewability`
- Related: `preserve-unowned-work, small-reviewable-chunks`

## Problem

A change can be technically plausible while still fighting the repository it lands in. Generic
preferences, remembered framework patterns, or examples from another project can override local
naming, helper APIs, tests, and workflow unless the contributor checks the repo first.

## Preferred Move

Read local instructions and nearby code before applying general guidance. Prefer established local
helpers, naming, file layout, and verification commands when they are deliberate and still serve the
change.

## Tradeoff

Local conventions can be stale or unsafe. When a local pattern conflicts with correctness,
security, or an explicit user request, make the conflict visible and use the narrower exception
instead of silently rewriting the project style.

## Agent Instruction

Follow repository instructions and nearby conventions first. If they conflict with your general
defaults, name the conflict and use the local rule unless it is unsafe or impossible.
