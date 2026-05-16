# Agent Separate Notes From Corrections

## Metadata

- Name: `Separate Notes From Corrections`
- ID: `AGENT-SEPARATE-NOTES-FROM-CORRECTIONS`
- Summary: Capture fast-review notes before fixing them when there are multiple comments or unclear
  patterns. Separating capture from correction preserves signal and supports coherent follow-up.
- Related: `separate-discovery-from-editing, preserve-agent-context-coherence,
  produce-review-packets`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, agent-context, reviewability, change-shape`

## Rule

Separate note capture from correction during fast review.

## Why

During fast review, it is tempting for an agent to fix each note immediately. That can lose the
broader pattern, mix unrelated corrections, or miss that several notes point to one deeper rule.
Capture notes first, then correct in a coherent pass.

## Helps

- Preserves review signal and turns clustered feedback into better guidance or cleaner edits.

## Limits

For a single obvious typo or broken link, fix directly. Separate capture from correction when there
are multiple comments, uncertain intent, or possible rule changes.

## Agent Instruction

Separate note capture from correction during fast review so clustered feedback becomes cleaner edits
or durable guidance.

## Mechanisms

Supported by review-note files, issue checklists, batch correction passes, before/after summaries,
and follow-up rules when feedback repeats.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
