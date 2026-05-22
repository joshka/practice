# Project Operating Manual

## Metadata

- Name: `Project Operating Manual`
- ID: `project-operating-manual`
- Summary: A project operating manual is a repo-owned document that applies broad software
  guidance to one live codebase. It turns a large catalog of durable rules into an opinionated
  project-specific doctrine, decision surface, and review contract so maintainers and agents do not
  have to reconstruct "the totality of what matters here" from `AGENTS.md` plus many scattered
  guides.
- Status: `draft`
- Audience: `both`
- Topics: `guidance, agent-workflow, review, source-truth, project-context`
- Tags: `documentation, agent-context, source-truth, reviewability, generated-artifacts`
- Related: `coding-agents, software-change-preferences, guidance-generation-and-audit,
  guidance-content-model-stewardship`

## Purpose

Use a project operating manual when a project needs more than a short `AGENTS.md` map but less than
"load the whole guidance catalog into every task." The failure mode is familiar:

- `AGENTS.md` grows into an unreadable wall of instructions.
- Durable guidance stays in many guides, rules, and patterns, but no single artifact explains how
  this project applies them.
- Agents load whichever files happen to look relevant and miss local priorities, active exceptions,
  or current boundaries.
- Review comments repeat because the project has no one place that states its doctrine, proof
  standards, and known tradeoffs in applied form.

The manual fixes that by giving one project-owned artifact a stronger job than `AGENTS.md`: define
the project's software doctrine, current boundary decisions, validation expectations, and active
exceptions in terms that can guide ongoing work.

## Recommended Shape

Keep `AGENTS.md` short and make it point to the manual. The manual should be the first deep artifact
an agent or maintainer reads when starting meaningful work in that repo.

The manual is most useful when it contains these sections:

1. Project doctrine.
   State the few non-negotiable software qualities for this codebase: correctness, compatibility,
   simplicity, operability, upgrade posture, reviewability, and user-surface priorities.
1. System mental model.
   Explain the current architecture, ownership boundaries, major data flows, and which modules own
   which kinds of decisions.
1. Change policy.
   Apply broad guidance to this repo's common work: how to shape changes, when to split refactors
   from behavior, how to treat generated artifacts, and what kinds of changes need prior design
   discussion.
1. Proof matrix.
   State what validation counts as credible proof for common change classes such as parser work,
   API changes, docs-only edits, generated output, UI changes, migrations, and dependency updates.
1. Current decisions and exceptions.
   Record the local exceptions, inherited constraints, known debt, compatibility promises, and
   intentional non-goals that a generic rule pack cannot infer.
1. Operating workflow.
   Explain how issues, plans, review packets, jj changes, release notes, and follow-up work should
   flow in this project.
1. Open questions.
   Keep unresolved architectural or policy questions visible so agents do not silently answer them
   inside implementation diffs.

## How To Build It

Write the manual by distilling from the project's accepted artifacts, not by pasting the entire
guidance catalog:

1. Start from the durable global guidance that should apply here.
1. Inspect accepted code, tests, docs, incidents, reviews, and release problems from this project.
1. Record only the project-specific consequences of those broad rules.
1. Name local exceptions explicitly instead of burying them in examples.
1. Link to deeper guides and rule packs for reference rather than copying long catalogs inline.

This keeps the manual opinionated and applied. It should answer "how do these software values show
up in this codebase?" rather than "what are all possible software rules?"

## Relationship To Other Artifacts

- `AGENTS.md` stays a compact map: local commands, task-start routing, capability limits, and a
  pointer to the operating manual.
- Guides, rules, principles, and patterns remain the durable canonical catalog.
- The project operating manual is the applied interpretation layer for one repository.
- Templates, checks, and generators should support the manual where repeated drift is mechanical.

In other words: the catalog explains the total philosophy, the manual explains the current project,
and `AGENTS.md` tells agents where to start.

## Checks

Review a project operating manual against these questions:

1. Does it explain how broad rules apply here, or merely link to everything?
1. Does it name current exceptions, debts, and boundary decisions?
1. Does it tell a reviewer what proof is expected for each major change class?
1. Would a new maintainer know where to put a change and how to justify it?
1. Would an agent know which unresolved decisions must be escalated instead of guessed?

Lint the manual with normal Markdown checks, and review it whenever the repo's boundaries, release
process, proof expectations, or nonfunctional requirements change materially.

## Limits

The manual is not a substitute for source reading, tests, ADRs, or domain docs. It should stay
specific enough to guide work and short enough to reread. If it becomes a second unstructured rule
catalog, it has failed and should be tightened back to project doctrine, local policy, and applied
exceptions.
