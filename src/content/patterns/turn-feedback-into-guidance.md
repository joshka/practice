# Turn Feedback Into Guidance

## Metadata

- Name: `Turn Feedback Into Guidance`
- ID: `turn-feedback-into-guidance`
- Summary: Repeated steering can expose missing, unclear, unreached, or ignored guidance. Diagnose
  the failure, fix the current artifact, and repair the instruction or delivery mechanism that
  should prevent recurrence.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, feedback, process`
- Tags: `agent-workflow, automation, source-truth, feedback-loops`
- Related: `prefer-durable-summaries, report-verification-honestly`

## Problem

Repeated steering wastes maintainer attention. If the same correction is needed across sessions,
fixing one artifact has not repaired the recurring failure. The cause may be missing guidance,
unclear wording, poor discovery, or failure to apply an instruction that was already available.

## Preferred Move

When feedback reveals a reusable preference, update the system that should have prevented the miss.
That might be a pattern, guide, template, lint rule, test, snippet, or agent instruction. Fix the
current artifact and capture the generalized lesson at the right level.

### Check The Failure Before Adding A Rule

Read the instruction, the action it produced, the maintainer's correction, and the subsequent
result together. A task summary is a discovery aid, not enough evidence to diagnose the failure.
Check whether the relevant guidance was actually loaded; a listed skill or available guide does
not establish that the agent read it.

Distinguish four causes before choosing the repair:

- Missing guidance: add the smallest reusable instruction to the existing owner.
- Unclear guidance: add the trigger, decision, counterexample, or limit that was missing.
- Unreached guidance: repair the map, snippet, or generated copy that the task actually uses.
- Ignored guidance: improve execution or a mechanical check instead of repeating the same rule.

Keep successful cases in the sample. Preserve instructions that produced useful decisions, and
separate observed outcomes from claims that the guidance caused them. Include counterexamples and
task-specific constraints before generalizing one correction to all work.

Keep private task links and excerpts in a local review record. Published guidance should explain
the failure and preferred move without requiring access to the originating conversation. Record
which authored and generated surfaces changed so the next audit can check whether the fix reached
its users.

## Tradeoff

Do not turn every comment into a permanent rule. Capture feedback when it applies beyond the
current line, when it has repeated, or when failing to encode it will likely cost future review
time.

## Agent Instruction

When maintainer feedback points to a broader preference, propose or make a small durable guidance
update in addition to fixing the immediate issue. First distinguish missing, unclear, unreached,
and ignored guidance. Name the generalized lesson and its evidence in the handoff.

## Examples

Bad: the agent fixes only the specific example.

```text
Changed this one bool return into a named error.
```

Good: the agent fixes the instance and records the reusable rule.

```text
Changed this bool return into a named error and added the API pattern that fallible operations
should report the failing condition instead of collapsing it into success/failure.
```

## References

- [OpenAI harness engineering](https://openai.com/index/harness-engineering/): supports making
  recurring failures legible and enforceable in the working environment. The failure classification
  above is a review procedure, not a measured claim that guidance caused a task's outcome.
