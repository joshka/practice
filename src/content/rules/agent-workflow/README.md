# Agent Workflow

Agent workflow rules cover objectives, scoped capabilities, durable context, review packets,
security proof, feedback loops, and concrete next choices.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`AGENT-BUDGET-FOR-FEEDBACK-LOOPS`](agent-budget-for-feedback-loops.md). Reserve enough time and
  tokens for checks, failure inspection, and handoff proof. Planning for the feedback loop keeps
  validation from being squeezed out after the first edit.
- [`AGENT-DEFINE-GOOD-BEFORE-JUDGMENT-HEAVY-WORK`](agent-define-good-before-judgment-heavy-work.md).
  State the quality bar before work where taste, naming, API shape, or review expectations matter.
  Clear criteria give the agent goalposts before it creates a large speculative diff.
- [`AGENT-DISTILL-FROM-BLESSED-ARTIFACTS`](agent-distill-from-blessed-artifacts.md). Study accepted
  code, docs, tests, and reviews first. Adapt local convention to this task.
- [`AGENT-ENCODE-NONFUNCTIONAL-REQUIREMENTS`](agent-encode-nonfunctional-requirements.md). Put
  invisible constraints such as security, accessibility, latency, and compatibility near the task.
  Encoding them upfront makes those requirements part of the implementation target.
- [`AGENT-GIVE-OBJECTIVES-WITH-BOUNDARIES`](agent-give-objectives-with-boundaries.md). Describe the
  outcome, scope, non-goals, forbidden moves, and proof instead of handing over brittle steps.
  Boundaries preserve intent while leaving room for local implementation choices.
- [`AGENT-GRANT-SCOPED-CAPABILITIES`](agent-grant-scoped-capabilities.md). Give agents only the
  permissions and external authority the task actually needs. Scoped capability keeps progress
  possible while reducing accidental mutation, publication, or exposure.
- [`AGENT-ISOLATE-WORKSPACES-BY-TASK`](agent-isolate-workspaces-by-task.md). Put separable or
  parallel agent work in its own workspace or source-control lane. Isolation keeps diffs,
  validation, and ownership clear when multiple changes are in flight.
- [`AGENT-KEEP-DURABLE-CONTEXT-ON-DISK`](agent-keep-durable-context-on-disk.md). Store project
  facts, accepted decisions, and long-lived operating notes in files instead of relying on chat
  context. Durable context makes future sessions and reviews resumable.
- [`AGENT-KEEP-SECRETS-OUT-OF-CONTEXT`](agent-keep-secrets-out-of-context.md). Avoid putting real
  credentials or sensitive values into prompts, docs, logs, and tests. Keeping secrets out of
  context reduces leakage through retained, repeated, or committed text.
- [`AGENT-MAKE-BAD-OUTPUT-HARD`](agent-make-bad-output-hard.md). Turn recurring bad agent output
  into scripts, templates, lint, or checks that fail fast. Mechanical enforcement lowers review cost
  more reliably than repeated prompt reminders.
- [`AGENT-PREFER-BUILD-PRESERVING-EDITS`](agent-prefer-build-preserving-edits.md). Make multi-step
  edits in slices that keep compilation or tests close to green when the route allows it.
  Build-preserving work keeps failures close to the edit that caused them.
- [`AGENT-PREFER-IN-DISTRIBUTION-TOOLS`](agent-prefer-in-distribution-tools.md). Use standard
  project commands, supported CLIs, and documented workflows before inventing ad hoc tool paths.
  Familiar tools reduce misuse and make agent output easier to rerun.
- [`AGENT-PREFER-TOOLS-OVER-PROMPTS`](agent-prefer-tools-over-prompts.md). Move repeated
  instructions into tools, checks, templates, or durable guides. Tooling catches failures even when
  prompts are short, compacted, or interpreted differently.
- [`AGENT-PRESENT-CONCRETE-NEXT-OPTIONS`](agent-present-concrete-next-options.md). After a validated
  chunk, offer specific follow-up chunks with their tradeoffs. Concrete options let the maintainer
  steer scope without decoding vague requests to continue.
- [`AGENT-PRESERVE-HUMAN-WORK`](agent-preserve-human-work.md). Inspect and protect unrelated local
  edits before changing files. Preserving human work keeps the task diff focused and avoids
  destroying unfinished or intentional changes.
- [`AGENT-PRESERVE-INTENT`](agent-preserve-intent.md). Optimize for the user's underlying objective
  when literal wording would miss the point. Intent-preserving work keeps changes aligned with the
  real readability, review, or behavior goal.
- [`AGENT-PRODUCE-REVIEW-PACKETS`](agent-produce-review-packets.md). Hand off agent work with
  purpose, changed files, evidence, skipped checks, risks, and follow-ups. A review packet lets
  maintainers inspect the output without replaying the session.
- [`AGENT-PROVE-SECURITY-IMPACT`](agent-prove-security-impact.md). Separate security hypotheses from
  proof of reachability, exploitability, assets, and user impact. This keeps prioritization and
  mitigation tied to demonstrated risk.
- [`AGENT-REPORT-PROOF-IN-HANDOFFS`](agent-report-proof-in-handoffs.md). Replace confidence language
  with the exact checks, inspection, screenshots, and skipped validation behind a handoff. Proof
  lets reviewers decide what to trust and what remains risky.
- [`AGENT-REVIEW-OUTPUT-AS-FUTURE-MAINTAINER`](agent-review-output-as-future-maintainer.md). Review
  agent output as someone who will not have the chat transcript. This keeps attention on durable
  code, docs, tests, validation proof, and residual risk.
- [`AGENT-SEPARATE-NOTES-FROM-CORRECTIONS`](agent-separate-notes-from-corrections.md). Capture
  fast-review notes before fixing them when there are multiple comments or unclear patterns.
  Separating capture from correction preserves signal and supports coherent follow-up.
- [`AGENT-SPEND-HUMAN-ATTENTION-ON-AMBIGUITY`](agent-spend-human-attention-on-ambiguity.md). Ask for
  human judgment where product behavior, API compatibility, naming, or security posture is still
  ambiguous. Resolving direction early prevents large speculative diffs.
- [`AGENT-SUGGEST-LOCAL-OVERRIDE-FILES`](agent-suggest-local-override-files.md). Put checkout-only
  facts in ignored override files instead of shared guidance. Local overrides keep machine-specific
  steering useful without leaking it to every contributor.
- [`AGENT-TURN-FEEDBACK-INTO-GUIDANCE`](agent-turn-feedback-into-guidance.md). Convert repeated
  review corrections into rules, templates, snippets, or checks. Durable guidance fixes the workflow
  problem instead of requiring the same steering again.
- [`AGENT-USE-AGENTS-MD-AS-MAP`](agent-use-agents-md-as-map.md). Keep `AGENTS.md` compact by using
  it to route agents to deeper guides and mechanisms. Treating it as a map preserves startup context
  without losing durable project guidance.
- [`AGENT-VERIFY-RISKY-CHANGES-WITH-CANARIES`](agent-verify-risky-changes-with-canaries.md). Use
  staged rollout, shadowing, dry runs, or partial publication for changes that can fail only under
  real conditions. Canaries reduce blast radius while evidence accumulates.
