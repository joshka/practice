# Apply Practice Guidance

## Metadata

- Name: `Apply Practice Guidance`
- ID: `agent-apply-practice-guidance`
- Summary: `Compact instructions for Codex sessions that need to use the shared practice catalog
  from another repository. The snippet turns broad standards into a task-local application loop
  without loading the whole catalog or treating preferences as automatic churn.`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agent-workflow, guidance-selection, review`
- Tags: `agent-workflow, agent-context, reviewability, source-truth`
- Related: `snippets/agents/rules.md, snippets/agents/core.md,
  mechanisms/project-operating-manual.md, guides/coding-agents.md`

## Usage

Use this snippet when a repo wants future Codex sessions to incorporate the shared practice
standards during ordinary implementation, review, and documentation work.

```markdown
## Applying Shared Practice Guidance

Use shared guidance as an input to the current task, not as permission to rewrite unrelated code.
Local repo instructions, accepted code, tests, public contracts, and user goals take priority over
generic preferences.

Fast path for agent sessions:

- Load this snippet first when the user asks to apply shared practice guidance.
- Load one domain file from `docs/development/rules/` when the task is narrow.
- Load `docs/development/snippets/agents/rules.md` when the task crosses several domains and a
  single searchable pack is cheaper than several file reads.
- Open the rendered site or source repo only when rationale, examples, or conflict resolution would
  change the implementation.
- Avoid full doctrine packs during ordinary edits; use them only for broad audits, rewrites,
  operating-manual work, or long-running sessions where coherence matters more than token cost and
  round trips.

Application loop:

1. Start with the task and the local repo map.
1. Load the smallest relevant shared guidance surface:
   `docs/development/rules/README.md` for rule domains,
   `docs/development/snippets/agents/rules.md` for the compact rule pack, or
   https://www.joshka.net/practice/ for deeper rationale.
1. Pick the rules that actually affect this change and ignore rules that do not apply.
1. If two preferences pull in different directions, name the tradeoff explicitly and choose the
   option that best preserves correctness, reviewability, local coherence, and future maintenance.
1. When the right choice is genuinely ambiguous, summarize the options and ask at that boundary
   before burying the decision in a large diff.
1. During handoff, report which local checks ran and, when useful, which shared guidance shaped the
   change.

Decision defaults:

- Prefer local convention over shared preference unless the convention is clearly broken or the
  user asked to revise it.
- Prefer small direct code over a new abstraction unless the abstraction removes real repeated
  complexity or encodes a stable boundary.
- Prefer separate changes for behavior and structural cleanup unless the behavior change needs a
  tiny preparatory refactor to be made safely.
- Prefer enough context to avoid predictable mistakes unless the task is trivial and the repo
  already answers the choice.
- Prefer proceeding with evidence unless the unresolved choice affects product behavior, public API,
  security, or architecture.

Do not cite shared guidance as a substitute for proof. Tests, builds, screenshots, sample output,
source links, and reviewable diffs are the evidence that the change works.
```
