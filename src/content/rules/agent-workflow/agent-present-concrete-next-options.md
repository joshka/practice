# Agent Present Concrete Next Options

## Metadata

- Name: `Present Concrete Next Options`
- ID: `AGENT-PRESENT-CONCRETE-NEXT-OPTIONS`
- Summary: After a validated chunk, offer specific follow-up chunks with their tradeoffs. Concrete
  options let the maintainer steer scope without decoding vague requests to continue.
- Related: `spend-human-attention-on-ambiguity, small-reviewable-chunks,
  manage-agent-work-not-sessions`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, review-handoff, reviewability, change-shape`

## Rule

Present concrete next options after validated chunks.

## Why

After a validated chunk, the maintainer needs to decide what happens next, not decode vague choices
such as "continue" or "more cleanup." Naming the next chunk and why to choose it makes review flow
cheap and keeps scope under human control.

## Helps

- Makes iterative work easy to steer and prevents agents from silently choosing preference-sensitive
  follow-ups.

## Limits

Do not ask for a choice when there is only one safe or obvious next action. Continue directly when
the user has already approved that path.

## Agent Instruction

After a validated chunk, name the next concrete chunk and why to choose it so the maintainer
controls scope cheaply.

## Mechanisms

Supported by numbered next options, explicit tradeoffs, jj descriptions, reviewed-status updates,
and task plans that name the next concrete chunk.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
