# Agent Spend Human Attention On Ambiguity

## Metadata

- Name: `Spend Human Attention on Ambiguity`
- ID: `AGENT-SPEND-HUMAN-ATTENTION-ON-AMBIGUITY`
- Summary: Ask for human judgment where product behavior, API compatibility, naming, or security
  posture is still ambiguous. Resolving direction early prevents large speculative diffs.
- Related: `spend-human-attention-on-ambiguity, define-good-before-judgment-heavy-work,
  manage-agent-work-not-sessions`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, agent-context, reviewability, public-api`

## Rule

Spend human attention on ambiguity.

## Why

Agents can spend a lot of effort executing through an unresolved decision. Product behavior, public
API compatibility, security posture, naming taste, and repo structure often need human judgment
before implementation, not after a large speculative diff.

## Helps

- Uses human attention where it changes direction and lets agents handle the well-bounded work after
  that.

## Limits

Do not ask humans to decide details the repo already answers. Research and summarize enough context
that the ambiguity is real and the choice is meaningful.

## Agent Instruction

Spend human attention on ambiguity because agents can spend a lot of effort executing through an
unresolved decision.

## Mechanisms

Supported by focused decision prompts, option tradeoffs, prototypes, small spike branches, and
review notes that identify the exact ambiguity boundary.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
