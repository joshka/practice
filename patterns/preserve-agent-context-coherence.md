# Preserve Agent Context Coherence

## Metadata

- Name: `Preserve Agent Context Coherence`
- ID: `preserve-agent-context-coherence`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, context, workflow`
- Related: `small-reviewable-chunks, separate-discovery-from-editing`

## Problem

Unrelated work pollutes the session's attention, working-copy state, and handoff narrative. Even
with long context windows, the useful context for one task can become harder to find when the agent
mixes separate goals in one thread or change.

## Preferred Move

Keep a session and jj change focused on one coherent purpose. For unrelated questions,
investigations, or edits, start a side session, side note, or fresh jj change instead of folding the
new work into the current context.

## Tradeoff

Small follow-ups that complete the same review unit should stay together. Split only when the new
work has a different owner, validation path, or review decision.

## Agent Instruction

Before accepting unrelated work into the current thread or change, decide whether it belongs in a
fresh context. If you split it, name the relationship and preserve the current change's purpose.

## Examples

Bad: the agent mixes a doc review, a Rust refactor, and a publication workflow in one change.

```text
Updated docs, refactored parser ownership, and pushed main.
```

Good: the agent keeps the current chunk coherent and starts a new one for the next topic.

```text
Finished the documentation pattern batch. Started a fresh jj change for coding-agent guidance.
```
