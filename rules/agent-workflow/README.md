# Agent Workflow

Agent workflow rules cover objectives, scoped capabilities, durable context, review packets,
security proof, feedback loops, and concrete next choices.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`AGENT-BUDGET-FOR-FEEDBACK-LOOPS`](agent-budget-for-feedback-loops.md). Budget tokens and time
  for feedback loops. Agent work needs room for reading, editing, running checks, inspecting
  failures, and reporting proof. Helps: Prevents premature handoff and makes validation failures
  part of the planned work instead of a surprise.
- [`AGENT-DEFINE-GOOD-BEFORE-JUDGMENT-HEAVY-WORK`](agent-define-good-before-judgment-heavy-work.md).
  Define good before judgment-heavy work. Agents are weak at guessing taste after the fact. Helps:
  Produces better first-pass output and reduces rewrites caused by hidden taste criteria.
- [`AGENT-DISTILL-FROM-BLESSED-ARTIFACTS`](agent-distill-from-blessed-artifacts.md). Study accepted
  code, docs, tests, and reviews first. Adapt local convention to this task.
- [`AGENT-ENCODE-NONFUNCTIONAL-REQUIREMENTS`](agent-encode-nonfunctional-requirements.md). Encode
  nonfunctional requirements. Requirements such as latency, accessibility, reviewability, security,
  privacy, determinism, and downstream compatibility are easy for agents to miss because they may
  not appear in the immediate diff. Helps: Keeps invisible constraints from being discovered only
  during review or production use.
- [`AGENT-GIVE-OBJECTIVES-WITH-BOUNDARIES`](agent-give-objectives-with-boundaries.md). Give agents
  objectives with boundaries, not brittle step lists. A brittle step list can make an agent follow
  the wrong route even after the codebase shows a better one. Helps: Preserves intent while letting
  the agent adapt to real repo structure and discovered constraints.
- [`AGENT-GRANT-SCOPED-CAPABILITIES`](agent-grant-scoped-capabilities.md). Grant scoped agent
  capabilities. Agents with broad authority can accidentally mutate external systems, publish state,
  delete files, or read secrets unrelated to the task. Helps: Reduces blast radius and makes
  permission boundaries auditable.
- [`AGENT-ISOLATE-WORKSPACES-BY-TASK`](agent-isolate-workspaces-by-task.md). Isolate agent
  workspaces by task. Parallel agent tasks can overwrite each other, mix unrelated diffs, or make
  validation ambiguous when they share one working copy. Helps: Keeps concurrent work reviewable and
  prevents one task from inheriting another task's partial edits.
- [`AGENT-KEEP-DURABLE-CONTEXT-ON-DISK`](agent-keep-durable-context-on-disk.md). Keep durable
  context on disk. Prompt context disappears, compacts, or becomes invisible to future sessions.
  Helps: Prevents accepted guidance from being trapped in one chat and makes long-running work
  resumable.
- [`AGENT-KEEP-SECRETS-OUT-OF-CONTEXT`](agent-keep-secrets-out-of-context.md). Keep secrets out of
  context. Secrets pasted into prompts, docs, logs, or test output can be retained, repeated, or
  committed accidentally. Helps: Reduces credential leakage and keeps shared artifacts safe to
  publish.
- [`AGENT-MAKE-BAD-OUTPUT-HARD`](agent-make-bad-output-hard.md). Make bad output mechanically hard.
  Repeated prompt reminders are weaker than a repo that rejects bad output mechanically. Helps:
  Turns recurring review feedback into enforcement and lowers the cost of good output.
- [`AGENT-PREFER-BUILD-PRESERVING-EDITS`](agent-prefer-build-preserving-edits.md). Prefer
  build-preserving edits when the route stays natural. A long period of broken build state hides
  which edit caused the failure and makes agent recovery harder. Helps: Improves bisectability,
  local recovery, and confidence during multi-step edits.
- [`AGENT-PREFER-IN-DISTRIBUTION-TOOLS`](agent-prefer-in-distribution-tools.md). Prefer
  in-distribution tools for agent-facing work. Agents are more reliable with tools that match their
  trained and tested workflow. Helps: Reduces tool misuse and makes commands easier for humans to
  rerun.
- [`AGENT-PREFER-TOOLS-OVER-PROMPTS`](agent-prefer-tools-over-prompts.md). Prefer tools and checks
  over repeated prompting. If the same instruction must be repeated to every agent, it belongs in a
  tool, check, template, or guide. Helps: Converts repeated steering into durable enforcement and
  frees human attention for ambiguous decisions.
- [`AGENT-PRESENT-CONCRETE-NEXT-OPTIONS`](agent-present-concrete-next-options.md). Present concrete
  next options after validated chunks. After a validated chunk, the maintainer needs to decide what
  happens next, not decode vague choices such as "continue" or "more cleanup." Naming the next chunk
  and why to choose it makes review flow cheap and keeps scope under human control. Helps: Makes
  iterative work easy to steer and prevents agents from silently choosing preference-sensitive
  follow-ups.
- [`AGENT-PRESERVE-HUMAN-WORK`](agent-preserve-human-work.md). Preserve unrelated human work. Agents
  share a working tree with human edits and sometimes other agents. Helps: Protects user work and
  keeps diffs limited to the task the agent owns.
- [`AGENT-PRESERVE-INTENT`](agent-preserve-intent.md). Preserve intent over literalism. Literal
  execution can satisfy the words while missing the goal. Helps: Keeps agent work aligned with the
  user's real objective instead of producing brittle literal compliance.
- [`AGENT-PRODUCE-REVIEW-PACKETS`](agent-produce-review-packets.md). Produce review packets for
  agent output. Agent output often spans code, docs, generated artifacts, and validation logs.
  Helps: Makes agent output reviewable and reduces trust gaps around what was actually checked.
- [`AGENT-PROVE-SECURITY-IMPACT`](agent-prove-security-impact.md). Prove security impact separately
  from hypotheses. Security claims are easy to overstate. Helps: Makes security review concrete and
  keeps mitigations tied to demonstrated risk.
- [`AGENT-REPORT-PROOF-IN-HANDOFFS`](agent-report-proof-in-handoffs.md). Report proof, not
  confidence, in agent handoffs. Confidence language is not evidence. Helps: Improves handoff
  quality and makes residual risk visible.
- [`AGENT-REVIEW-OUTPUT-AS-FUTURE-MAINTAINER`](agent-review-output-as-future-maintainer.md). Review
  agent output from the perspective of a future maintainer who did not see the session. Agent output
  can pass checks while depending on prompt-only context, vague names, hidden state, over-broad
  abstractions, missing tests, or undocumented behavior changes. Helps: Catches agent output that is
  locally plausible but hard to maintain after context disappears. - Turns review from confidence
  assessment into durable artifact inspection.
- [`AGENT-SEPARATE-NOTES-FROM-CORRECTIONS`](agent-separate-notes-from-corrections.md). Separate note
  capture from correction during fast review. During fast review, it is tempting for an agent to fix
  each note immediately. Helps: Preserves review signal and turns clustered feedback into better
  guidance or cleaner edits.
- [`AGENT-SPEND-HUMAN-ATTENTION-ON-AMBIGUITY`](agent-spend-human-attention-on-ambiguity.md). Spend
  human attention on ambiguity. Agents can spend a lot of effort executing through an unresolved
  decision. Helps: Uses human attention where it changes direction and lets agents handle the
  well-bounded work after that.
- [`AGENT-SUGGEST-LOCAL-OVERRIDE-FILES`](agent-suggest-local-override-files.md). Suggest ignored
  agent override files for local-only repo context. Some agent instructions are true only for one
  checkout: local jj topology, ignored plan directories, machine-specific paths, or temporary repo
  notes. Helps: Separates local steering from shared policy and reduces accidental leakage of
  machine-specific state.
- [`AGENT-TURN-FEEDBACK-INTO-GUIDANCE`](agent-turn-feedback-into-guidance.md). Turn repeated
  feedback into durable guidance. Repeated corrections such as "show why," "name the next thing," or
  "do not use abstract rule names" are process bugs. Helps: Converts review friction into durable
  improvement of the workflow.
- [`AGENT-USE-AGENTS-MD-AS-MAP`](agent-use-agents-md-as-map.md). Use `AGENTS.md` as a map, not the
  whole manual. `AGENTS.md` becomes hard to use when it tries to contain every rule, example, and
  exception. Helps: Keeps agent instructions scannable and reduces context bloat without losing
  durable guidance.
- [`AGENT-VERIFY-RISKY-CHANGES-WITH-CANARIES`](agent-verify-risky-changes-with-canaries.md). Verify
  risky changes with canaries before cutover. Some changes can pass local tests and still fail when
  exposed to real traffic, real docs rendering, real provider state, or real users. Helps: Reduces
  blast radius for deployment, integration, migration, and generated-behavior changes.
