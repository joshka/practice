# Agent Define Good Before Judgment Heavy Work

## Metadata

- ID: `AGENT-DEFINE-GOOD-BEFORE-JUDGMENT-HEAVY-WORK`
- Legacy ID: `R-0808`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Define good before judgment-heavy work.

## Why

Agents are weak at guessing taste after the fact. For naming, grouping, documentation voice, review
shape, public API design, or rule IDs, define the quality bar before changing the artifact so the
agent has goal posts instead of inferred preferences.

## Helps

- Produces better first-pass output and reduces rewrites caused by hidden taste criteria.

## Limits

Do not over-plan obvious mechanical edits. Use this rule when judgment, aesthetics, compatibility,
or review expectations determine whether the output is good.

## Agent Instruction

Before naming, grouping, documentation voice, API shape, or rule IDs, define the quality bar so the
agent has concrete goalposts.

## Mechanisms

Supported by upfront acceptance criteria, examples of accepted output, naming rules, review rubrics,
and task prompts that ask what “good” means before execution.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
