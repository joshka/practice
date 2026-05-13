# Write Actionable Error Messages

## Metadata

- Name: `Write Actionable Error Messages`
- ID: `write-actionable-error-messages`
- Status: `reviewed`
- Audience: `both`
- Topics: `errors, documentation, support`
- Related: `preserve-error-context, test-observable-behavior`

## Problem

An error message can be technically accurate and still leave the audience stuck. Generic failures,
missing causes, vague recovery advice, or absent correlation details create dead ends for users,
callers, operators, and support.

## Preferred Move

Write the message for the boundary where it appears. An actionable error should answer the useful
questions at that boundary:

- What happened?
- What went wrong?
- Why did it happen, when that can be known or honestly inferred?
- What can the user, caller, operator, or support person do next?
- What identifier or diagnostic context can connect the message to logs or support?

Avoid dead ends. If the immediate audience cannot fix the problem, give them the next escalation
path or the correlation information needed to connect the visible failure to diagnostic detail.

## Tradeoff

User-facing messages should not expose sensitive, noisy, or unstable internals. Keep private detail
in logs, admin surfaces, or debugging context, but carry enough concrete context in the visible
message for someone to make progress.

## Agent Instruction

When changing an error message, include what happened, what can be done next, and any correlation
information needed for support. Do not replace a useful diagnostic with friendly but dead-end prose.

## Examples

Bad: the message says the operation failed but gives the user no next step or diagnostic handle.

```text
Something went wrong.
```

Good: the message names the failed action, gives a next step, and includes a support correlation
identifier.

```text
We could not import contacts.csv because the email column is missing. Add an email column and try
again. If this keeps failing, contact support with request ID req_123.
```

## References

| Source        | Use      | Note                                                         |
| ------------- | -------- | ------------------------------------------------------------ |
| [Wix UX][wix] | `adapts` | Good error messages say what happened, why, and what to do.  |
| [HN][hn]      | `adapts` | Discussion stresses diagnostics, actionability, and support. |

[wix]: https://wix-ux.com/when-life-gives-you-lemons-write-better-error-messages-46c5223e1a2f
[hn]: https://news.ycombinator.com/item?id=48069032
