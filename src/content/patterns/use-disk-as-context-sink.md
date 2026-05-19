# Use Disk As Context Sink

## Metadata

- Name: `Use Disk As Context Sink`
- ID: `use-disk-as-context-sink`
- Summary: Large pasted context is difficult to search, diff, summarize, and revisit. Put bulky or
  reusable context on disk so agents can pull the relevant slice while the thread stays focused on
  decisions and handoff.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, context, tooling`
- Tags: `agent-context, documentation, source-truth`
- Related: `prefer-durable-summaries, deliver-context-just-in-time`

## Problem

Large pasted context is hard to search, summarize, diff, and revisit. It also competes with the
current task for attention when most of the material is only occasionally relevant.

## Preferred Move

Put large or reusable context on disk in structured files. Let agents use search, parsers, scripts,
and summaries to pull the slice they need. Keep the thread focused on decisions and handoff rather
than raw bulk context.

## Tradeoff

Small, ephemeral context can stay in the prompt when writing a file would add ceremony. Move context
to disk when it is large, reusable, structured, or likely to be consulted by more than one session.

## Agent Instruction

When context is large or reusable, ask for or create a disk-backed source of truth. Use tools to
query it instead of trying to keep all details in the active conversation.

## Examples

Bad: the thread carries a giant table that the agent must reason over from memory.

```text
Here are 5,000 rows of dependency metadata pasted into chat...
```

Good: the data is on disk and queried as needed.

```text
dependencies.csv is checked in under references/. Use DuckDB or a small script to inspect the rows
needed for this decision.
```
