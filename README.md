# Development Preferences

This repository is the standalone home for my durable software-development preferences. It captures
how I prefer code, documentation, tests, version-control workflows, review artifacts, and
coding-agent handoffs to be shaped.

## What This Is For

This repo turns repeated software-review judgment into reusable guidance for humans, coding agents,
and downstream repositories.

Use it to:

- Decide how a change should be shaped.
- Cite a preference in review.
- Give coding agents compact operating rules.
- Copy generated guidance into another project.

Use it in two ways:

- As a human-readable explanation of the development beliefs I want to apply consistently.
- As a canonical source of compact rules that can be copied into other repositories for agents to
  follow.

The repo should support two audiences:

- Humans who want concise principles, tradeoffs, and review language.
- Agents that need compact, reusable guidance for `AGENTS.md`-style instructions.

The goal is not to freeze taste. The guidance should evolve from real development practice, review
feedback, and durable external sources while remaining compact enough to use.

## Why This Exists

The same development preferences come up repeatedly: keep code locally understandable, make public
APIs intentional, prove behavior with useful tests, write docs as contracts, preserve reviewability,
and give agents enough context to do solid work without turning every prompt into a manual.

This repo turns those repeated preferences into named, reviewable artifacts. Humans get the
reasoning, tradeoffs, and review language. Agents get compressed instructions that are specific
enough to shape behavior and small enough to use in real implementation sessions.

The repo is also meant to avoid rediscovery. If a rule is durable enough to matter across projects,
it should live here once, then be copied or generated into downstream repos from this canonical
source.

## Guidance Model

Prefer many small, named Markdown files over a few large essays when an idea needs reuse. Each
referenceable idea should have a stable name or ID so it can be linked, cited in review, or copied
into agent instructions without ambiguity.

A guidance unit should usually include:

- Name: the stable reference name.
- Problem: the pressure or failure mode that makes the guidance relevant.
- Preferred move: the action to take.
- Tradeoff: when the move is limited, risky, or not worth the ceremony.
- Agent instruction: a compact operational form for coding agents that includes enough trigger,
  failure-mode, or constraint context to apply the rule without blindly repeating the human title.
- References: optional durable sources that support, frame, or contrast the guidance.

Guides should assemble and contextualize these units instead of duplicating them. If a guide needs a
rule that is useful across topics, promote that rule into a named guidance file and link to it.

Use these durable layers:

- [Rules](rules/README.md): one-file-per-rule compact instructions grouped by domain.
- [Principles](principles/README.md): reasoning notes for broad beliefs that justify several rules.
- [Patterns](patterns/README.md): repeatable situation-and-move guidance.
- [Mechanisms](mechanisms/README.md): lints, checks, commands, and configuration that support
  rules mechanically.
- [Agent snippets](snippets/agents/README.md): compressed execution packs and profile-style
  guidance for `AGENTS.md` files.

Start new repeatable moves from `templates/pattern.md`. Use the existing principle and mechanism
files as models for deeper reasoning notes and tooling profiles.

## What Is Here

The repo has two related surfaces:

- A detailed reasoning surface for humans: guides, principles, patterns, mechanisms, and references.
- A compact execution surface for agents: reviewed rule files and generated agent snippets.

The detailed surface explains why rules exist and where they stop applying. The compact surface is
what another repo can copy into `AGENTS.md`-style guidance so agents can apply the preferences during
implementation.

## Read This Repo Directly

Task entry points:

| Work area         | Start here                                                            |
| ----------------- | --------------------------------------------------------------------- |
| Change shape      | [Software Change Preferences](guides/software-change-preferences.md)  |
| Rust review       | [Rust Maintainability](guides/rust-maintainability.md)                |
| Code shape        | [Code Shape](guides/code-shape.md)                                    |
| Documentation     | [Markdown And Documentation](guides/markdown-documentation.md)        |
| Coding-agent work | [Coding Agents](guides/coding-agents.md)                              |
| JJ workflow       | [JJ Workflow](guides/jj-workflow.md)                                  |

Guide entry points by decision area:

- [Software Change Preferences](guides/software-change-preferences.md): broad defaults for change
  shape, review, and verification.
- [Rust Maintainability](guides/rust-maintainability.md): Rust reader-locality, APIs, errors,
  tests, dependencies, and performance.
- [Code Shape](guides/code-shape.md): source-level moves that reduce reader burden.
- [Boundary Correctness](guides/boundary-correctness.md): parsing, validation policy, state,
  explicit inputs, side effects, and async boundaries.
- [Observability And Failure](guides/observability-and-failure.md): structured errors, logging
  ownership, telemetry, and privacy-safe diagnostics.
- [Markdown And Documentation](guides/markdown-documentation.md): Markdown style, Rustdoc,
  examples, docs-as-contracts, and source-link policy.
- [Documentation Workflow](guides/documentation-workflow.md): documentation pass depth, evidence,
  local voice, PR narrative, repo maps, and drift remediation.
- [Coding Agents](guides/coding-agents.md): objectives, context, tools, workspaces, review, and
  feedback loops for agent work.
- [JJ Workflow](guides/jj-workflow.md): local jujutsu change shape, descriptions, bookmarks,
  remotes, and recovery.

Use [rules](rules/README.md) when you need a compact instruction with its own reviewable home. Use
[principles](principles/README.md) when you need the reasoning behind a rule. Use
[patterns](patterns/README.md) when you need a stable review term or a compact rule to cite. Use
[mechanisms](mechanisms/README.md) when you need the lint, command, CI, or configuration support
behind a rule. Use [agent snippets](snippets/agents/README.md) when you need copyable `AGENTS.md`
sections or a compressed reviewed-rule pack for another repo. Use
[the guidance plan](references/guidance-plan.md) to see how the current guide set is organized and
where future work belongs.

## Use In Another Project

Use this repo as the canonical source for shared development rules. Downstream repos should copy the
generated adoption template, keep `AGENTS.md` short, and keep the full reviewed rule set in generated
domain files under `docs/development/rules/`.

From this repo, generate or refresh the downstream files into a target repo:

```bash
python3 scripts/generate_downstream_template.py --output /path/to/target-repo
```

This writes:

```text
/path/to/target-repo/
  AGENTS.md
  docs/development/
    README.md
    rules/
      README.md
      <domain>.md
```

After copying, edit only the repo-local parts: validation commands, source-control notes, local
paths, and project-specific constraints. Do not hand-edit copied rule text. If a shared rule is
wrong, change it in this repo, regenerate the downstream template, and copy the refreshed files into
the target repo.

This keeps all reviewed rules represented downstream, including domains that are easy to forget such
as performance, source hygiene, and review artifacts, while still letting agents load only the rule
domain relevant to a task.

The intended downstream shape is:

- `AGENTS.md`: the short repo-local map, local validation commands, and local constraints.
- `docs/development/README.md`: the local development guidance entry point.
- `docs/development/rules/README.md`: the generated index of copied rule domains.
- `docs/development/rules/<domain>.md`: generated compact rules for each domain.

This squares summary and detail: `AGENTS.md` stays readable, while every reviewed rule remains
available in the target repo without making agents or maintainers pull information manually from
this repo.

## Maintaining This Repo

Keep changes small, reviewable, and tied to one clear purpose. Add new files only when they contain
durable content that is ready for review; do not create placeholders to satisfy a planned tree.

Before handing off broad guidance changes, run:

```bash
python3 scripts/audit_guidance.py
python3 scripts/generate_rule_indexes.py --check
python3 scripts/generate_agent_rules.py --check
python3 scripts/generate_downstream_template.py --check
markdownlint-cli2 "**/*.md"
pnpm build
```

The audit checks the guidance architecture directly: rule metadata and references, domain indexes,
generated agent-pack coverage, stale rule IDs, private local context leaks, placeholder text, and
internal Markdown links. Regenerate rule indexes with `python3 scripts/generate_rule_indexes.py`
after changing rule titles, rationale, or summaries. Regenerate `snippets/agents/rules.md` with
`python3 scripts/generate_agent_rules.py` after changing reviewed rule instructions.
Regenerate `templates/downstream/` with `python3 scripts/generate_downstream_template.py` after
changing reviewed rule instructions or downstream adoption shape.

Use `python3 scripts/audit_guidance.py --quality` during rule-deepening passes. That stricter mode
flags rules whose rationale still starts by repeating the rule text, which is a sign that the rule
may need concrete examples, narrower tradeoffs, or stronger explanation before it feels durable.

This repo is principles-first. External sources can support, frame, or challenge the guidance, but
they do not replace the preferences captured here.

When adapting an idea from an external source, record:

- The source link.
- The idea it supports.
- Whether this repo adopts, adapts, or intentionally differs from it.

Private or local source inventories, if useful during development, should stay out of durable docs
and out of pushed public branches.
