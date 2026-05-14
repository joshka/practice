# Development Preferences

This repository is the standalone home for practical software-development preferences. It captures
how I prefer code, documentation, tests, version-control workflows, and coding-agent handoffs to be
shaped.

The repo should support two audiences:

- Humans who want concise principles, tradeoffs, and review language.
- Agents that need compact, reusable guidance for `AGENTS.md`-style instructions.

The goal is not to freeze taste. The guidance should evolve from real development practice, review
feedback, and durable external sources while remaining compact enough to use.

## Guidance Model

Prefer many small, named Markdown files over a few large essays when an idea needs reuse. Each
referenceable idea should have a stable name or ID so it can be linked, cited in review, or copied
into agent instructions without ambiguity.

A guidance unit should usually include:

- Name: the stable reference name.
- Problem: the pressure or failure mode that makes the guidance relevant.
- Preferred move: the action to take.
- Tradeoff: when the move is limited, risky, or not worth the ceremony.
- Agent instruction: a compact operational form for coding agents.
- References: optional durable sources that support, frame, or contrast the guidance.

Guides should assemble and contextualize these units instead of duplicating them. If a guide needs a
rule that is useful across topics, promote that rule into a named guidance file and link to it.
Start new reusable guidance units from `templates/pattern.md`.

## Planned Structure

The first version should grow incrementally toward this shape:

```text
README.md
AGENTS.md
guides/
  software-change-preferences.md
  rust-maintainability.md
  markdown-documentation.md
  jj-workflow.md
  coding-agents.md
patterns/
  README.md
  <stable-guidance-id>.md
snippets/
  agents/
    <copyable-agent-section>.md
references/
  README.md
  external-sources.md
templates/
  pattern.md
  guide.md
  agents-section.md
```

Do not add placeholder files just to match the planned structure. Create files when they contain
durable content that is ready for review.

Start with the broad software-change guide at `guides/software-change-preferences.md`.
Rust-specific guidance begins at `guides/rust-maintainability.md`.
Code-shape guidance begins at `guides/code-shape.md`.
Boundary-correctness guidance begins at `guides/boundary-correctness.md`.
Observability and failure guidance begins at `guides/observability-and-failure.md`.
Markdown and documentation guidance begins at `guides/markdown-documentation.md`.
Documentation workflow guidance begins at `guides/documentation-workflow.md`.
Coding-agent workflow guidance begins at `guides/coding-agents.md`.
Jujutsu workflow guidance begins at `guides/jj-workflow.md`.
Reusable agent snippets begin at `snippets/agents/`.

## Delivery Approach

Build this repo in small, reviewable chunks. Each chunk should have one clear purpose and be
validated locally before handoff.

Use a local review loop that optimizes for maintainer attention:

1. After each validated chunk, offer a numbered list of concrete next chunks.
1. Put the recommended next chunk first and explain the tradeoff for each option.
1. Treat a numbered choice as approval to move forward with that chunk.
1. Wait for confirmation before implementing a chunk when the next choice is preference-sensitive.
1. If review feedback arrives instead of a next-choice number, address that feedback before moving
   on.
1. Implement only the confirmed chunk.
1. Validate locally and summarize the actual checks that ran.
1. Ask whether to push the reviewed chunk before publishing it.
1. Move to the next chunk only after the current chunk is accepted or redirected.

Expected sequence:

1. Establish the repo charter and guidance architecture.
1. Add the first pattern/principle template and a small seed batch of named guidance units.
1. Add a broad software-change guide that links to the seed units.
1. Add Rust maintainability guidance and Rust-specific units.
1. Add Markdown, documentation, and coding-agent guides.
1. Add jj workflow guidance and copy/paste agent snippets.
1. Add an external references ledger once the guide and pattern shape shows what is useful.

A later discovery milestone should review private and local agent-instruction material for reusable
guidance, contradictions, and missing named units. Durable public-facing docs in this repo should
not depend on those local source names.

## Source And Reference Policy

This repo is principles-first. External sources can support, frame, or challenge the guidance, but
they do not replace the preferences captured here.

When adapting an idea from an external source, record:

- The source link.
- The idea it supports.
- Whether this repo adopts, adapts, or intentionally differs from it.

Private or local source inventories, if useful during development, should stay out of durable docs
and out of pushed public branches.
