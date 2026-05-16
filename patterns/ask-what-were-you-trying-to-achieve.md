# Ask What Were You Trying To Achieve

## Metadata

- Name: `Ask What Were You Trying To Achieve`
- ID: `ask-what-were-you-trying-to-achieve`
- Summary: `Recover the original intent before judging a surprising design. Separating purpose
  from mechanism makes it easier to preserve useful constraints while replacing stale structure.`
- Status: `reviewed`
- Audience: `both`
- Topics: `refactoring, legacy-code, collaboration`
- Related: `preserve-intent-over-literalism, document-intentional-non-goals`

## Problem

Legacy code often looks strange because the original constraints are invisible. Asking "why is this
built this way?" can make people defend the current mechanism instead of recovering the original
intent and deciding whether that intent still matters.

## Preferred Move

Ask what the previous design was trying to achieve. Separate intent from means, then compare the
original goal with current product, operational, and maintenance needs. Preserve, replace, or remove
the mechanism based on that comparison.

## Tradeoff

Do not use this as a way to avoid direct critique. Once intent is understood, be clear about whether
the current design still serves it.

## Agent Instruction

When encountering surprising code, infer or ask for the intended outcome before refactoring it. In
the handoff, distinguish the preserved intent from the implementation you changed.

## Examples

Bad: the review question starts with blame and invites post-hoc justification.

```text
Why is there a separate Redis cluster just for this one job queue?
```

Good: the question recovers the decision context.

```text
What was this separate Redis cluster trying to achieve: isolation, rollout speed, reliability, or
alignment with another team?
```

## References

| Source                                    | Use        | Note                                                    |
| ----------------------------------------- | ---------- | ------------------------------------------------------- |
| [What Were You Trying To Achieve][no-why] | `supports` | Intent is more useful than defending the current means. |

[no-why]: https://frantic.im/no-why/
