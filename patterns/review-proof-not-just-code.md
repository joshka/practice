# Review Proof Not Just Code

## Metadata

- Name: `Review Proof Not Just Code`
- ID: `review-proof-not-just-code`
- Summary: Code review is weaker when it inspects the diff without checking whether the claimed
  behavior was proven. Ask for the smallest trustworthy evidence that the change works and that the
  likely failure mode was covered.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, review, verification`
- Related: `define-good-before-judgment-heavy-work, report-verification-honestly`

## Problem

Reviewing only the diff wastes human attention on reconstructing whether the work satisfies the
goal. Agent-produced changes especially need evidence because the code may be correct-looking while
missing the user's intended outcome.

## Preferred Move

Ask for proof of work in the form that fits the change: failing and passing tests, screenshots,
videos, logs, traces, benchmark output, design notes, or a concise acceptance checklist. Review the
evidence and the decision points, not only the implementation.

## Tradeoff

Do not demand heavyweight artifacts for tiny changes. The proof should be the smallest trustworthy
evidence that the behavior changed as intended.

## Agent Instruction

Include the proof artifact or command output that demonstrates success. If proof is unavailable,
state what evidence is missing and why.

## Examples

Bad: the handoff asks the reviewer to infer success from the diff.

```text
Updated the import flow and cleaned up the retry helper.
```

Good: the handoff carries the review evidence.

```text
Added a test that fails on main when the import retry drops the last error. It passes with this fix;
the log excerpt shows the final retry error is now preserved.
```

## References

| Source                           | Use        | Note                                                           |
| -------------------------------- | ---------- | -------------------------------------------------------------- |
| [OpenAI autonomy loop][autonomy] | `supports` | Higher autonomy depends on agents proving and validating work. |

[autonomy]: https://openai.com/index/harness-engineering/#increasing-levels-of-autonomy
