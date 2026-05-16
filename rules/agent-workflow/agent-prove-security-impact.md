# Agent Prove Security Impact

## Metadata

- ID: `AGENT-PROVE-SECURITY-IMPACT`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Prove security impact separately from hypotheses.

## Why

Security claims are easy to overstate. A hypothesis such as "this might expose data" is not the same
as proof of reachability, exploitability, affected assets, or user impact. Keeping those layers
separate prevents both panic and false reassurance.

## Helps

- Makes security review concrete and keeps mitigations tied to demonstrated risk.

## Limits

Do not require exploit proof before fixing an obvious low-cost hardening issue. Use the stronger
proof standard when prioritization, disclosure, or risk claims depend on impact.

## Agent Instruction

Prove security impact separately from hypotheses because security claims are easy to overstate.

## Mechanisms

Supported by threat models, reproduction steps, reachability analysis, logs, test cases, redaction
checks, and security review packets that separate hypothesis from evidence.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
