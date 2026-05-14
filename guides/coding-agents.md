# Coding Agents

This guide organizes the repo's agent-workflow preferences. Use it when setting up agent tasks,
writing `AGENTS.md` guidance, reviewing agent output, or deciding what should become tooling
instead of another prompt.

Use this guide with [Software Change Preferences](software-change-preferences.md). Agent work still
needs small reviewable chunks, honest verification, and careful working-copy ownership.

## Core Preference

Treat agents as productive workers in a system, not as magic sessions to supervise line by line. A
good agent workflow gives the agent enough objective, context, tools, authority, and validation to
produce a reviewable artifact while preserving human attention for ambiguity and judgment.

Optimize for:

- Objectives with boundaries over brittle step lists.
- Durable repo-owned context over transient prompt memory.
- Tools, checks, and workspaces over repeated human steering.
- Review evidence over confidence language.
- Long-term coherence over one prompt's local success.

## Objectives And Acceptance

Define the work before delegating it. Name the objective, boundaries, success criteria, available
tools, and the proof expected at handoff. Avoid over-specifying the route when the agent can choose
a better path inside safe boundaries.

Use [Give Agents Objectives With Boundaries][objectives] when a task should preserve the user's
goal without freezing the implementation route. Use [Define Good Before Delegating][define-good]
when the acceptance criteria, evidence, or remaining human judgment need to be explicit.

For ambiguous work, spend human attention at the ambiguity boundary. Use
[Spend Human Attention On Ambiguity][human-attention] before asking an agent to bury product,
architecture, security, or public API decisions inside a large diff.

## Context And Knowledge

Agents work best when the repo is legible and the relevant context arrives at the point of use. Keep
large or reusable context on disk, keep `AGENTS.md` as a map, and make accepted artifacts part of
the discovery path.

Use [Distill From Blessed Artifacts][blessed-artifacts] when existing code, tests, docs, or reviews
are denser than the prompt. Use [Deliver Context Just In Time][jit-context] and
[Use Disk As Context Sink][disk-context] when the context is too large or too specialized for one
static instruction block.

Use [Use AGENTS.md As Map][agents-map] to keep top-level instructions compact and linked. Use
[Optimize For Agent Legibility][agent-legibility] when repo structure, docs, commands, and runtime
signals should help future agents find and validate the right thing.

## Tools And Guardrails

Prefer tools and checks over heroic prompting. If a mistake is repeatable, move it into the cheapest
enforcement layer: type shape, API design, lint, test, formatter, schema, template, runbook, or
review checklist.

Use [Prefer Tools Over Prompts][tools-over-prompts], [Make Bad Output Mechanically Hard][mechanical],
and [Teach Agents Through Tools][teach-tools] when feedback points to a missing guardrail or
capability.

Use [Make The Change Easy First][easy-first] when the requested change is risky because the repo
lacks a harness, test, boundary, or workflow that would make the behavior change straightforward.
Use [Code Is Memory Of Process][code-memory] and [Keep Automations Repo Owned][repo-automation] when
stable process knowledge should become a checked artifact.

## Workspaces And Capabilities

Keep agent work isolated by task. Each independent edit should have a clear workspace, source-control
change, ownership boundary, logs, and cleanup policy. Do not make a human track five interactive
sessions when the work can be represented as durable tasks.

Use [Manage Agent Work Not Sessions][manage-work], [Isolate Agent Workspaces][workspaces], and
[Preserve Agent Context Coherence][context-coherence] when parallel or long-running work would
otherwise smear state across threads and checkouts.

Grant only the authority the task needs. Use [Grant Scoped Agent Capabilities][scoped-capabilities]
and [Keep Secrets Out Of Context][secrets] when credentials, external systems, or privileged tools
are involved.

## Verification And Review

Agent output should arrive with proof. The right proof depends on the task: failing and passing
tests, logs, screenshots, traces, benchmark output, specialist reviews, canaries, or deployment
notes.

Use [Review Proof Not Just Code][review-proof], [Produce Review Packets][review-packets], and
[Report Verification Honestly][honest-verification] when handing work to a maintainer.

For risky operations, use [Verify With Canaries Before Cutover][canaries]. For security work, use
[Prove Security Impact][security-impact] so hypotheses, reachability, and concrete impact stay
separate.

## Feedback Loops

Every repeated correction is a chance to improve the system. Capture reusable feedback in patterns,
guides, tools, tests, templates, or runbooks so future sessions do not need the same steering.

Use [Turn Feedback Into Guidance][feedback-guidance], [Record Agent Operating Lessons][lessons],
[Close The Agent Loop][close-loop], and [Garbage Collect Agent Drift][drift] when agent work exposes
a repeated failure mode.

Budget time and tokens for loops that reduce human attention and improve outcomes. Use
[Budget Tokens For Feedback Loops][token-budget] when evaluating review agents, cleanup loops,
security scans, docs checks, or harness evals.

## Long-Term Coherence

Agent work should scale to the next many changes. A correct-looking patch can still damage the
system if it adds parallel concepts, hides side effects, weakens tests, or loses the repository's
shape.

Use [Optimize For Long Term Coherence][long-term], [Preserve Intent Over Literalism][intent], and
[Encode Nonfunctional Requirements][nonfunctional] when the prompt is narrower than the actual
quality bar.

Use [Ask What Were You Trying To Achieve][achieve] when surprising legacy code may be preserving an
old intent. Use [Choose Good Enough Tools][good-enough-tools] and
[Prefer In Distribution Tools][in-distribution] when selecting tooling for agent-friendly work.

## Agent Snippet

For copyable `AGENTS.md` guidance, use [Coding Agent Workflow Instructions][agent-snippet]. For a
broader repo baseline, use [Core Agent Instructions][core-snippet].

## Review Questions

- Is the objective clear without overfitting the implementation path?
- Are boundaries, capabilities, and forbidden actions explicit?
- Is the relevant context on disk or linked from a stable owner?
- Can the agent validate the work with tools it can access?
- Does the handoff include proof instead of confidence language?
- Did feedback become a reusable improvement where appropriate?
- Does this change preserve the repo's long-term concepts and reviewability?

[achieve]: ../patterns/ask-what-were-you-trying-to-achieve.md
[agent-legibility]: ../patterns/optimize-for-agent-legibility.md
[agents-map]: ../patterns/use-agents-md-as-map.md
[agent-snippet]: ../snippets/agents/coding-agents.md
[blessed-artifacts]: ../patterns/distill-from-blessed-artifacts.md
[canaries]: ../patterns/verify-with-canaries-before-cutover.md
[close-loop]: ../patterns/close-the-agent-loop.md
[code-memory]: ../patterns/code-is-memory-of-process.md
[context-coherence]: ../patterns/preserve-agent-context-coherence.md
[core-snippet]: ../snippets/agents/core.md
[define-good]: ../patterns/define-good-before-delegating.md
[disk-context]: ../patterns/use-disk-as-context-sink.md
[drift]: ../patterns/garbage-collect-agent-drift.md
[easy-first]: ../patterns/make-the-change-easy-first.md
[feedback-guidance]: ../patterns/turn-feedback-into-guidance.md
[good-enough-tools]: ../patterns/choose-good-enough-tools.md
[honest-verification]: ../patterns/report-verification-honestly.md
[human-attention]: ../patterns/spend-human-attention-on-ambiguity.md
[in-distribution]: ../patterns/prefer-in-distribution-tools.md
[intent]: ../patterns/preserve-intent-over-literalism.md
[jit-context]: ../patterns/deliver-context-just-in-time.md
[lessons]: ../patterns/record-agent-operating-lessons.md
[long-term]: ../patterns/optimize-for-long-term-coherence.md
[manage-work]: ../patterns/manage-agent-work-not-sessions.md
[mechanical]: ../patterns/make-bad-output-mechanically-hard.md
[nonfunctional]: ../patterns/encode-nonfunctional-requirements.md
[objectives]: ../patterns/give-agents-objectives-with-boundaries.md
[repo-automation]: ../patterns/keep-automations-repo-owned.md
[review-packets]: ../patterns/produce-review-packets.md
[review-proof]: ../patterns/review-proof-not-just-code.md
[scoped-capabilities]: ../patterns/grant-scoped-agent-capabilities.md
[secrets]: ../patterns/keep-secrets-out-of-context.md
[security-impact]: ../patterns/prove-security-impact.md
[teach-tools]: ../patterns/teach-agents-through-tools.md
[token-budget]: ../patterns/budget-tokens-for-feedback-loops.md
[tools-over-prompts]: ../patterns/prefer-tools-over-prompts.md
[workspaces]: ../patterns/isolate-agent-workspaces.md
