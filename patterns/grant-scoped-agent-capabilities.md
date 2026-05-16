# Grant Scoped Agent Capabilities

## Metadata

- Name: `Grant Scoped Agent Capabilities`
- ID: `grant-scoped-agent-capabilities`
- Summary: Broad tool access increases the blast radius of agent mistakes and makes review harder.
  Grant the smallest capabilities needed for the current task, then expand deliberately when the
  work proves it needs more reach.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, security, tools`
- Related: `keep-secrets-out-of-context, make-bad-output-mechanically-hard`

## Problem

Broad credentials and host-level access make agent mistakes more dangerous than necessary. A task
that needs read access to one system should not receive an ambient credential that can mutate many
systems.

## Preferred Move

Give agents the narrowest capability that can do the job. Prefer read-only identities, repo-scoped
filesystems, tool-specific APIs, egress controls, and short-lived tokens. Make the capability easy
to revoke and easy to audit.

## Tradeoff

Too many tiny capabilities can slow work and hide the real workflow. Scope access around coherent
jobs, not every individual operation, and expand only when the validation evidence shows it is
necessary.

## Agent Instruction

Before using a privileged tool or credential, check whether a narrower capability exists. Report the
scope of authority used for the task and avoid requesting broader access as a first move.

## Examples

Bad: a read-only accounting task receives a full account credential.

```text
Use my main brokerage login to download monthly statements.
```

Good: the task gets a narrow, revocable identity.

```text
Use the read-only statement-export identity. It can list and download statements but cannot trade or
transfer assets.
```
