# Verify With Canaries Before Cutover

## Metadata

- Name: `Verify With Canaries Before Cutover`
- ID: `verify-with-canaries-before-cutover`
- Summary: Automation is risky when production cutover is the first real proof. Use a canary path,
  rollback plan, and human approval for operations with remote access, credentials, production data,
  or long-lived service impact.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, deployment, verification`
- Tags: `verification, testing, automation`
- Related: `define-good-before-judgment-heavy-work, close-the-agent-loop`

## Problem

Automation is risky when the first real test is the production cutover. Agents can confidently
change a system while missing reachability, rollback, credential, or compatibility problems that
only appear after deployment.

## Preferred Move

For risky operations, create a canary path that proves the important property before production
cutover. Validate the canary, preserve a rollback path, and require human approval when the blast
radius or irreversibility warrants it.

## Tradeoff

Canaries add overhead. Skip them for low-risk local changes with cheap rollback, but prefer them
when the operation touches remote access, credentials, devices, production data, or long-lived
services.

## Agent Instruction

Before cutting over a risky automation, identify the canary signal and rollback path. Do not treat
the cutover as complete until the canary evidence is reported.

## Examples

Bad: the agent replaces the only working access path in one step.

```text
Uploaded the new remote-access binary and restarted the service.
```

Good: the agent tests a separate identity before production cutover.

```text
Deployed the new binary to the canary identity, verified SSH reachability, then cut over the
production identity after the check passed.
```
