# Agent Keep Secrets Out Of Context

## Metadata

- Name: `Keep Secrets Out of Context`
- ID: `AGENT-KEEP-SECRETS-OUT-OF-CONTEXT`
- Summary: Avoid putting real credentials or sensitive values into prompts, docs, logs, and tests.
  Keeping secrets out of context reduces leakage through retained, repeated, or committed text.
- Related: `keep-secrets-out-of-context, avoid-secret-or-private-log-context,
  grant-scoped-agent-capabilities`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, security-privacy, agent-context`

## Rule

Keep secrets out of context.

## Why

Secrets pasted into prompts, docs, logs, or test output can be retained, repeated, or committed
accidentally. Agents should use credential mechanisms without seeing or restating secret values
unless the task explicitly requires secret handling.

## Helps

- Reduces credential leakage and keeps shared artifacts safe to publish.

## Limits

Some tasks must reason about secret shapes, scopes, or redaction behavior. Use placeholders, scoped
test credentials, or secret managers rather than real sensitive values.

## Agent Instruction

Keep secrets out of context because secrets pasted into prompts, docs, logs, or test output can be
retained, repeated, or committed accidentally.

## Mechanisms

Supported by environment variables, secret managers, redaction checks, ignored local config, test
fixtures with fake values, and review for accidental secret exposure.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
