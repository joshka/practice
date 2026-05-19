# Make The Change Easy First

## Metadata

- Name: `Make The Change Easy First`
- ID: `make-the-change-easy-first`
- Summary: Some changes are risky because the path to make or verify them is unnecessarily hard.
  First add the smallest harness, boundary, helper, tool, or runbook that makes the real change
  cheaper to understand and review.
- Status: `reviewed`
- Audience: `both`
- Topics: `refactoring, workflow, tooling`
- Tags: `change-shape, tooling, reviewability`
- Related: `separate-structure-from-behavior, prefer-tools-over-prompts`

## Problem

Some changes feel hard because the system makes the desired path slow, risky, or unpleasant. Pushing
through that friction can produce a larger, riskier diff than first improving the path.

## Preferred Move

When the change is blocked by friction, first make the change easier: add a test harness, improve a
tool, clarify a boundary, extract a helper, write a runbook, or simplify the workflow. Then make the
now-easy behavior change as a separate reviewable unit when practical.
Prepare first when the benefit is immediate: the code becomes easier to understand or the next
behavior change becomes cheaper to make and review.

## Tradeoff

Do not spend unbounded time building infrastructure for a one-off task. Make the path easier when the
friction is repeated, risk-reducing, or necessary to validate the real change.
If the preparatory work is large and the payoff is not immediate, record it for later instead of
letting the current change become an infrastructure project.

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

| Source                          | Use        | Note                                                     |
| ------------------------------- | ---------- | -------------------------------------------------------- |
| [Opening Mail][mail]            | `adapts`   | Tools can make unpleasant work easier and more reliable. |
| [Tidy First, Ch. 21][tidy-ch21] | `supports` | Prepare first when the current change benefits directly. |

[mail]: https://frantic.im/opening-mail/
[tidy-ch21]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch21.html
