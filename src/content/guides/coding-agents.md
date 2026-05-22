# Coding Agents

## Metadata

- Name: `Coding Agents`
- ID: `coding-agents`
- Summary: Coding-agent guidance covers task setup, repo-owned context, tools, workspaces,
  verification, handoff proof, feedback loops, and maintainer review flow. It treats agents as
  workers in a system whose output should be reviewable, durable, and easy to integrate.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, workflow, context, tools, validation, review`
- Tags: `agent-workflow, agent-context, tooling, verification, review-handoff`
- Related: `agent-instructions-are-operational-controls, mechanize-repeated-feedback,
  give-agents-objectives-with-boundaries`

This guide covers agent-task setup, `AGENTS.md` guidance, agent-output review, and decisions that
should become tooling instead of another prompt.

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

Define the work before delegating it or starting judgment-heavy execution. The useful setup is not a
step list; it is a clear objective with boundaries, success criteria, available tools, and expected
proof at handoff. For naming, grouping, review-shape, public API, or other taste-heavy work,
establish the quality bar before changing the artifact, then leave room for the agent to choose a
better route inside safe boundaries.

Use [Give Agents Objectives With Boundaries][objectives] when a task should preserve the user's
goal without freezing the implementation route. Use
[Define Good Before Judgment-Heavy Work][define-good] when the acceptance criteria, evidence, or
remaining human judgment need to be explicit.
Use [Agent Give Objectives With Boundaries][agent-objectives] and [Agent Define Good Before
Judgment-Heavy Work][agent-define-good] when this guidance needs compact agent-execution wording.

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
For ongoing projects whose software doctrine no longer fits in a short map, use
[Project Operating Manual][project-operating-manual] as the project-owned interpretation layer
between the broad catalog and the current repo.
Use [Agent Keep Durable Context On Disk][agent-disk-context], [Agent Use AGENTS.md As
Map][agent-agents-map], and [Agent Distill From Blessed Artifacts][agent-blessed-artifacts] when
context should live in repo-owned artifacts rather than transient prompt memory.

## Tools And Guardrails

Prefer tools and checks over heroic prompting. If a mistake is repeatable, move it into the cheapest
enforcement layer: type shape, API design, lint, test, formatter, schema, template, runbook, or
review checklist.

Use [Prefer Tools Over Prompts][tools-over-prompts], [Make Bad Output Mechanically Hard][mechanical],
and [Teach Agents Through Tools][teach-tools] when feedback points to a missing guardrail or
capability.
Use [Agent Prefer Tools Over Prompts][agent-tools-prompts] and [Agent Make Bad Output
Hard][agent-bad-output] when repeated prompt steering should become a tool, check, template, or
schema.

Use [Make The Change Easy First][easy-first] when the requested change is risky because the repo
lacks a harness, test, boundary, or workflow that would make the behavior change straightforward.
Use [Code Is Memory Of Process][code-memory] and [Keep Automations Repo Owned][repo-automation] when
stable process knowledge should become a checked artifact.

For systems that agents can reload, extend, or self-modify, prefer staged changes with validation
and rollback over direct mutation of the live runtime. Generated or guest code should be inspectable
after failure without replacing the last known good behavior.

Use [Agent Prefer Build Preserving Edits][agent-build-preserving] when a long broken state would
make recovery and review harder.

## Workspaces And Capabilities

Keep agent work isolated by task. Each independent edit should have a clear workspace, source-control
change, ownership boundary, logs, and cleanup policy. Do not make a human track five interactive
sessions when the work can be represented as durable tasks.

Use [Manage Agent Work Not Sessions][manage-work], [Isolate Agent Workspaces][workspaces], and
[Preserve Agent Context Coherence][context-coherence] when parallel or long-running work would
otherwise smear state across threads and checkouts.
Use [Agent Isolate Workspaces By Task][agent-workspaces] and [Agent Preserve Human
Work][agent-preserve-work] when multiple edits, agents, or human changes share source-control state.

Grant only the authority the task needs. Use [Grant Scoped Agent Capabilities][scoped-capabilities]
and [Keep Secrets Out Of Context][secrets] when credentials, external systems, or privileged tools
are involved.
Use [Agent Grant Scoped Capabilities][agent-capabilities] and [Agent Keep Secrets Out Of
Context][agent-secrets] when task authority, credentials, or external systems need explicit limits.

## Verification And Review

Agent output should arrive with proof. The right proof depends on the task: failing and passing
tests, logs, screenshots, traces, benchmark output, specialist reviews, canaries, or deployment
notes.

### Review Stance

Review agent output from the perspective of a future maintainer who did not write the code.
Prioritize correctness, edge cases, API clarity, documentation truthfulness, rendering behavior,
terminal-state behavior, and focused tests for the contract.

When code is hard to read, identify the cause precisely: concept mixing, poor ordering, hidden
state, vague names, too much abstraction, or missing tests.

### Edit Preparation

Before editing, identify the owning module, local dependencies, existing tests, and narrowest useful
validation command. While editing, preserve current user behavior unless the task intentionally
changes it. Before handoff, report focused checks, broad checks, skipped checks, residual risk, and
follow-up.

### Handoff Shape

Handoff notes should say what changed, where the important files are, what validation ran, what did
not run, and what risk remains. Avoid long implementation diaries.

Use [Review Proof Not Just Code][review-proof], [Produce Review Packets][review-packets], and
[Report Verification Honestly][honest-verification] when handing work to a maintainer. Use [Review
Agent Output As Future Maintainer][future-maintainer-review] when evaluating whether agent output is
maintainable after the session context disappears.
Use [Agent Produce Review Packets][agent-review-packets] and [Agent Report Proof In
Handoffs][agent-proof] when a handoff needs compact proof-focused wording.

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
Use [Agent Budget For Feedback Loops][agent-loop-budget] and [Agent Turn Feedback Into
Guidance][agent-feedback-guidance] when repeated corrections should become durable guidance or
automation.

## Maintainer Review Loop

After a validated chunk, present concrete next chunks instead of vague continuation prompts. Put
`I've reviewed, do the next thing` first when the expected path is for the maintainer to accept the
current chunk and continue. Name the actual next thing in that option, and do the appropriate
workflow work behind it: mark reviewed material, update the jj description, start a fresh jj change
when the next unit is separate, and then begin that named next chunk.

Explain why each offered path is worth choosing. Include the tradeoff that matters for review:
scope, risk, latency, validation depth, naming, structure, or follow-up cost. If the maintainer gives
feedback instead of choosing the next chunk, address that feedback before continuing.

For fast manual review sessions, separate note capture from correction. Capture reviewer notes in a
durable queue without applying corrections unless asked, then apply corrections later in scoped
batches such as one content type, one page, or one ownership area.

Use [Agent Present Concrete Next Options][agent-next-options] and [Agent Separate Notes From
Corrections][agent-notes-corrections] when maintainer review needs clear next choices or a separate
review-note queue.

## Long-Term Coherence

Agent work should scale to the next many changes. A correct-looking patch can still damage the
system if it adds parallel concepts, hides side effects, weakens tests, or loses the repository's
shape.

Use [Optimize For Long Term Coherence][long-term], [Preserve Intent Over Literalism][intent], and
[Encode Nonfunctional Requirements][nonfunctional] when the prompt is narrower than the actual
quality bar.
Use [Agent Encode Nonfunctional Requirements][agent-nonfunctional] and [Agent Preserve
Intent][agent-preserve-intent] when acceptance depends on compatibility, privacy, performance,
determinism, or the user's real goal.

Use [Ask What Were You Trying To Achieve][achieve] when surprising legacy code may be preserving an
old intent. Use [Choose Good Enough Tools][good-enough-tools] and
[Prefer In Distribution Tools][in-distribution] when selecting tooling for agent-friendly work.

## Agent Snippet

For copyable `AGENTS.md` guidance, use [Coding Agent Workflow Instructions][agent-snippet]. For a
broader repo baseline, use [Core Agent Instructions][core-snippet]. For a compressed execution pack
generated from reviewed rules, use [Reviewed Rule Agent Pack][rule-pack].

## Related Guidance

Use [Agent Workflow Rules][agent-rules] for compact reviewed instructions, and use
[Agent Instructions Are Operational Controls][agent-controls] when deciding how much context belongs
in compressed agent wording. Repeated corrections should move toward scripts, lints, templates, or
generators; use [Mechanize Repeated Feedback][mechanize-feedback] and
[Guidance Generation And Audit][guidance-audit] when agent guidance needs generated surfaces to stay
current.

## Review Questions

### Task Setup

- Is the objective clear without overfitting the implementation path?
- Are boundaries, capabilities, and forbidden actions explicit?
- Is the relevant context on disk or linked from a stable owner?
- Can the agent validate the work with tools it can access?

### Handoff And Loop

- Does the handoff include proof instead of confidence language?
- Did feedback become a reusable improvement where appropriate?
- Does the next-option list include a reviewed-and-continue path when that is the normal flow?
- Does each option explain why that path would be chosen?

### Coherence

- Does this change preserve the repo's long-term concepts and reviewability?

[achieve]: ../patterns/ask-what-were-you-trying-to-achieve.md
[agent-agents-map]: ../rules/agent-workflow/agent-use-agents-md-as-map.md
[agent-bad-output]: ../rules/agent-workflow/agent-make-bad-output-hard.md
[agent-blessed-artifacts]: ../rules/agent-workflow/agent-distill-from-blessed-artifacts.md
[agent-build-preserving]: ../rules/agent-workflow/agent-prefer-build-preserving-edits.md
[agent-capabilities]: ../rules/agent-workflow/agent-grant-scoped-capabilities.md
[agent-controls]: ../principles/agent-instructions-are-operational-controls.md
[agent-define-good]: ../rules/agent-workflow/agent-define-good-before-judgment-heavy-work.md
[agent-disk-context]: ../rules/agent-workflow/agent-keep-durable-context-on-disk.md
[agent-feedback-guidance]: ../rules/agent-workflow/agent-turn-feedback-into-guidance.md
[agent-legibility]: ../patterns/optimize-for-agent-legibility.md
[agent-loop-budget]: ../rules/agent-workflow/agent-budget-for-feedback-loops.md
[agent-next-options]: ../rules/agent-workflow/agent-present-concrete-next-options.md
[agent-nonfunctional]: ../rules/agent-workflow/agent-encode-nonfunctional-requirements.md
[agent-notes-corrections]: ../rules/agent-workflow/agent-separate-notes-from-corrections.md
[agent-objectives]: ../rules/agent-workflow/agent-give-objectives-with-boundaries.md
[agent-preserve-intent]: ../rules/agent-workflow/agent-preserve-intent.md
[agent-preserve-work]: ../rules/agent-workflow/agent-preserve-human-work.md
[agent-proof]: ../rules/agent-workflow/agent-report-proof-in-handoffs.md
[agent-rules]: ../rules/agent-workflow/README.md
[agent-review-packets]: ../rules/agent-workflow/agent-produce-review-packets.md
[agent-secrets]: ../rules/agent-workflow/agent-keep-secrets-out-of-context.md
[agents-map]: ../patterns/use-agents-md-as-map.md
[agent-snippet]: ../snippets/agents/coding-agents.md
[agent-tools-prompts]: ../rules/agent-workflow/agent-prefer-tools-over-prompts.md
[agent-workspaces]: ../rules/agent-workflow/agent-isolate-workspaces-by-task.md
[blessed-artifacts]: ../patterns/distill-from-blessed-artifacts.md
[canaries]: ../patterns/verify-with-canaries-before-cutover.md
[close-loop]: ../patterns/close-the-agent-loop.md
[code-memory]: ../patterns/code-is-memory-of-process.md
[context-coherence]: ../patterns/preserve-agent-context-coherence.md
[core-snippet]: ../snippets/agents/core.md
[define-good]: ../patterns/define-good-before-judgment-heavy-work.md
[disk-context]: ../patterns/use-disk-as-context-sink.md
[drift]: ../patterns/garbage-collect-agent-drift.md
[easy-first]: ../patterns/make-the-change-easy-first.md
[feedback-guidance]: ../patterns/turn-feedback-into-guidance.md
[future-maintainer-review]: ../rules/agent-workflow/agent-review-output-as-future-maintainer.md
[good-enough-tools]: ../patterns/choose-good-enough-tools.md
[guidance-audit]: ../mechanisms/guidance-generation-and-audit.md
[honest-verification]: ../patterns/report-verification-honestly.md
[human-attention]: ../patterns/spend-human-attention-on-ambiguity.md
[in-distribution]: ../patterns/prefer-in-distribution-tools.md
[intent]: ../patterns/preserve-intent-over-literalism.md
[jit-context]: ../patterns/deliver-context-just-in-time.md
[lessons]: ../patterns/record-agent-operating-lessons.md
[long-term]: ../patterns/optimize-for-long-term-coherence.md
[manage-work]: ../patterns/manage-agent-work-not-sessions.md
[mechanize-feedback]: ../principles/mechanize-repeated-feedback.md
[mechanical]: ../patterns/make-bad-output-mechanically-hard.md
[nonfunctional]: ../patterns/encode-nonfunctional-requirements.md
[objectives]: ../patterns/give-agents-objectives-with-boundaries.md
[project-operating-manual]: ../mechanisms/project-operating-manual.md
[repo-automation]: ../patterns/keep-automations-repo-owned.md
[review-packets]: ../patterns/produce-review-packets.md
[review-proof]: ../patterns/review-proof-not-just-code.md
[rule-pack]: ../snippets/agents/rules.md
[scoped-capabilities]: ../patterns/grant-scoped-agent-capabilities.md
[secrets]: ../patterns/keep-secrets-out-of-context.md
[security-impact]: ../patterns/prove-security-impact.md
[teach-tools]: ../patterns/teach-agents-through-tools.md
[token-budget]: ../patterns/budget-tokens-for-feedback-loops.md
[tools-over-prompts]: ../patterns/prefer-tools-over-prompts.md
[workspaces]: ../patterns/isolate-agent-workspaces.md
