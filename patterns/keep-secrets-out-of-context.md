# Keep Secrets Out Of Context

## Metadata

- Name: `Keep Secrets Out Of Context`
- ID: `keep-secrets-out-of-context`
- Summary: Secrets and private data can leak through prompts, transcripts, logs, and generated
  artifacts even when the code change is harmless. Redact or replace sensitive values before they
  enter shared context, and use controlled channels when real secrets are required.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, security, secrets`
- Related: `grant-scoped-agent-capabilities, prefer-tools-over-prompts`

## Problem

Secrets in prompts, repo files, logs, or tool output can enter model context and become hard to
reason about or contain. Once a token is visible to the agent as text, prompt injection and accidental
disclosure risks get worse.

## Preferred Move

Keep secrets outside the repository and outside model-visible context. Prefer harness-managed
capabilities, scoped tool calls, environment injection that is not echoed, and revocable identities.
Expose the ability to perform the task, not the raw credential text.

## Tradeoff

Local development sometimes needs explicit credentials. Use the narrowest viable secret, keep it out
of checked files and transcripts, and rotate it if exposure is uncertain.

## Agent Instruction

Do not ask for or print raw secrets. If a task needs credentials, use the repo's configured secret
mechanism or ask for a scoped capability that keeps the secret out of model-visible text.

## Examples

Bad: the runbook asks the user to paste a token into the thread.

```text
Paste HOME_ASSISTANT_TOKEN here so I can call the API.
```

Good: the runbook uses a preconfigured capability.

```text
Use the `home-assistant-auditor` tool. It exposes read-only device state without printing the
underlying token.
```
