# Make The Change Easy First

## Metadata

- Name: `Make The Change Easy First`
- ID: `make-the-change-easy-first`
- Status: `reviewed`
- Audience: `both`
- Topics: `refactoring, workflow, tooling`
- Related: `separate-structure-from-behavior, prefer-tools-over-prompts`

## Problem

Some changes feel hard because the system makes the desired path slow, risky, or unpleasant. Pushing
through that friction can produce a larger, riskier diff than first improving the path.

## Preferred Move

When the change is blocked by friction, first make the change easier: add a test harness, improve a
tool, clarify a boundary, extract a helper, write a runbook, or simplify the workflow. Then make the
now-easy behavior change as a separate reviewable unit when practical.

## Tradeoff

Do not spend unbounded time building infrastructure for a one-off task. Make the path easier when the
friction is repeated, risk-reducing, or necessary to validate the real change.

## Agent Instruction

If a requested change is risky because the workflow is missing a check, harness, or boundary,
propose the smallest preparatory improvement first. Keep preparatory work separate from behavior
changes when that improves review.

## Examples

Bad: the agent changes behavior without creating a way to validate it.

```text
Edited the import retry loop directly and manually inspected the diff.
```

Good: the agent first creates the path that makes the change safe.

```text
Added a failing retry-order test, then changed the retry loop so the behavior change is reviewable
against that test.
```

## References

| Source                    | Use        | Note                                                        |
| ------------------------- | ---------- | ----------------------------------------------------------- |
| [Opening Mail][mail]      | `adapts`   | Tools can make unpleasant work easier and more reliable.    |
| [Tidy First][tidy]        | `supports` | Structural preparation can make behavior changes safer.     |

[mail]: https://frantic.im/opening-mail/
[tidy]: https://books.google.com/books/about/Tidy_First.html?id=-WndEAAAQBAJ
