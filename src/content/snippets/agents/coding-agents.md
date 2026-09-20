# Coding Agent Workflow Instructions

## Metadata

- Name: `Coding Agent Workflow Instructions`
- ID: `agent-coding-workflow-instructions`
- Summary: `Compact workflow instructions for repositories that delegate implementation or review
  work to coding agents. The snippet emphasizes objectives, boundaries, durable handoff, repo-owned
  context, and feedback that becomes reusable guidance.`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agent-workflow, delegation, handoff, feedback`
- Tags: `agent-workflow, agent-context, tooling, review-handoff, feedback-loops`
- Related: `guides/coding-agents.md, principles/docs-are-contracts.md`

Use this snippet when a repo wants agent work to be durable, reviewable, and easy to integrate.

```markdown
## Coding-Agent Workflow

Treat agents as workers producing reviewable artifacts, not as magic sessions. Define the objective,
boundaries, acceptance criteria, available tools, and expected proof before delegating or starting a
large edit.

Prefer repo-owned context, tools, checks, and workspaces over repeated prompt steering. Keep
long-running or parallel work isolated by task. Do not overwrite unrelated human or agent changes.

Continue through already-authorized implementation and validation. Ask about unresolved choices
that materially change scope, correctness, or authority; small review units are not permission gates.

Handoff should include the purpose, changed files, validation, skipped checks, known risks, and any
follow-up. If repeated feedback exposes a missing rule, tool, test, or doc, turn that feedback into
durable guidance instead of relying on memory.

Match proof to the user or consumer surface. Separate implemented behavior, observed workflows,
and remaining acceptance work. Before adding another rule, check whether existing guidance was
missing, unclear, unreached, or ignored. Respect task budgets and stop equivalent review passes
once the required gates pass and no new finding warrants another pass.

Canonical guide:

- `guides/coding-agents.md`
```
