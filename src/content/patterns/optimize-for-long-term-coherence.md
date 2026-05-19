# Optimize For Long Term Coherence

## Metadata

- Name: `Optimize For Long Term Coherence`
- ID: `optimize-for-long-term-coherence`
- Summary: Agent-produced work can satisfy a prompt while weakening the system's future concepts,
  names, boundaries, and tests. Choose the smallest change that preserves long-term direction
  without using coherence as an excuse for speculative architecture.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, maintainability, design`
- Tags: `change-shape, reader-locality, source-truth`
- Related: `reader-locality, small-reviewable-chunks`

## Problem

Agent-produced work can satisfy the immediate prompt while making the next hundred changes harder.
The failure is not only local correctness; it is losing the thread of the system's names, concepts,
boundaries, tests, and documentation over time.

## Preferred Move

Prefer changes that preserve the system's long-term shape. Keep concepts coherent, names stable,
contracts documented, tests meaningful, and review units small. Ask whether the change makes future
work easier to understand, extend, and verify.

## Tradeoff

Do not use future coherence as an excuse for speculative architecture. Choose the smallest change
that improves or preserves the system's direction, and leave larger redesigns as explicit follow-up
work.

## Agent Instruction

Before handing off, check whether the change fits the repo's existing concepts and will remain easy
to build on. Report any future-coherence risk instead of treating the prompt as the whole success
criteria.

## Examples

Bad: the implementation satisfies the feature by adding another parallel concept.

```text
Added a second workflow loader because it was faster than adapting the existing loader.
```

Good: the implementation extends the existing concept boundary.

```text
Extended the existing workflow loader with the new step type and kept validation in the same
boundary as the other workflow policy checks.
```
