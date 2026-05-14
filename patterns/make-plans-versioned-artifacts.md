# Make Plans Versioned Artifacts

## Metadata

- Name: `Make Plans Versioned Artifacts`
- ID: `make-plans-versioned-artifacts`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, planning, documentation`
- Related: `define-good-before-delegating, preserve-agent-context-coherence`

## Problem

Plans in chat are hard to review, update, cite, or resume. For larger work, important decisions and
progress can vanish into transient conversation history.

## Preferred Move

For complex or long-running work, put the plan in the repo as a versioned artifact. Include the
goal, constraints, acceptance criteria, progress, decisions, and open questions. Keep small changes
lightweight, but make large plans reviewable outside the chat thread.

## Tradeoff

Do not create plan documents for obvious one-step edits. Use a versioned plan when the work spans
multiple sessions, has meaningful risk, needs human review before execution, or will guide multiple
agents.

## Agent Instruction

When work is complex enough that the plan itself needs review, create or update a checked-in plan.
Keep the plan current as decisions change.

## Examples

Bad: the only plan is buried in the thread.

```text
I'll do the migration in six phases...
```

Good: the plan is reviewable and resumable.

```text
Added `docs/plans/import-migration.md` with scope, acceptance criteria, phase status, and the
decision log.
```

## References

| Source                                      | Use        | Note                                                    |
| ------------------------------------------- | ---------- | ------------------------------------------------------- |
| [OpenAI knowledge system][knowledge-system] | `supports` | Plans can be first-class repo artifacts with history.   |

[knowledge-system]: https://openai.com/index/harness-engineering/#we-made-repository-knowledge-the-system-of-record
