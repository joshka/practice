# Agent Verify Risky Changes With Canaries

## Metadata

- ID: `AGENT-VERIFY-RISKY-CHANGES-WITH-CANARIES`
- Legacy ID: `R-0817`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Verify risky changes with canaries before cutover.

## Why

Some changes can pass local tests and still fail when exposed to real traffic, real docs rendering,
real provider state, or real users. Canaries and staged rollout make the change reversible while
evidence accumulates.

## Helps

- Reduces blast radius for deployment, integration, migration, and generated-behavior changes.

## Limits

Do not add canary ceremony to changes whose failure mode is local and cheap to revert. Use canaries
when external state, users, data, or production behavior are at risk.

## Agent Instruction

Use canaries for changes that can pass local tests but fail under real traffic, docs rendering,
provider state, or users.

## Mechanisms

Supported by feature flags, staged rollout, shadow reads, dry-run modes, partial publication,
metrics, logs, rollback plans, and explicit cutover criteria.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
