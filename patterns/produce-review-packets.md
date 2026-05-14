# Produce Review Packets

## Metadata

- Name: `Produce Review Packets`
- ID: `produce-review-packets`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, review, verification`
- Related: `review-proof-not-just-code, report-verification-honestly`

## Problem

Human reviewers lose time when an agent hands off only a diff. The reviewer has to reconstruct the
goal, acceptance criteria, verification evidence, risk, and remaining judgment calls before deciding
whether the work is mergeable.

## Preferred Move

Package the work for review. Include the change summary, acceptance evidence, commands run, known
risks, and the artifact that best proves user-facing behavior: tests, logs, screenshots, recordings,
benchmarks, specialist review, or deployment notes.

## Tradeoff

Do not turn every tiny edit into a release dossier. The packet should be proportional to the risk
and should reduce review work, not bury the reviewer in generic ceremony.

## Agent Instruction

Before asking for review, produce a compact review packet with the goal, proof, verification, and
remaining risk. Prefer concrete artifacts over confidence language.

## Examples

Bad: the handoff asks the reviewer to inspect everything from scratch.

```text
Implemented the checkout fix.
```

Good: the handoff carries the evidence needed to review quickly.

```text
Fixed checkout retry after payment intent refresh.

Proof:
- Added a regression test that fails on main and passes here.
- Ran the checkout smoke test against Stripe test mode.
- Captured a 45-second recording of the retry path completing.

Risk: did not exercise Apple Pay because the local browser cannot provision that flow.
```

## References

| Source                             | Use        | Note                                                                 |
| ---------------------------------- | ---------- | -------------------------------------------------------------------- |
| [Symphony README][symphony-readme] | `supports` | Agent work is handed off with proof such as CI and walkthroughs.     |
| [Symphony blog][symphony-blog]     | `supports` | Human review becomes artifact review instead of session supervision. |
| [OpenAI autonomy loop][autonomy]   | `supports` | Higher autonomy depends on validation and review evidence.           |

[autonomy]: https://openai.com/index/harness-engineering/#increasing-levels-of-autonomy
[symphony-blog]: https://openai.com/index/open-source-codex-orchestration-symphony/
[symphony-readme]: https://github.com/openai/symphony#readme
