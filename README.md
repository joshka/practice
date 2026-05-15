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

## How To Use This Repo

Start with the guide that matches the decision you are making:

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
- [Jj Workflow](guides/jj-workflow.md): local jujutsu change shape, descriptions, bookmarks,
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

## Repository Shape

The first reviewed version uses this shape:

```text
README.md
AGENTS.md
guides/
  software-change-preferences.md
  rust-maintainability.md
  code-shape.md
  boundary-correctness.md
  observability-and-failure.md
  markdown-documentation.md
  documentation-workflow.md
  jj-workflow.md
  coding-agents.md
rules/
  README.md
  <domain>/
    README.md
    <rule-id>.md
principles/
  README.md
  <stable-principle-id>.md
patterns/
  README.md
  <stable-guidance-id>.md
mechanisms/
  README.md
  <stable-mechanism-id>.md
snippets/
  agents/
    <copyable-agent-section>.md
    rules.md
references/
  guidance-plan.md
  external-source-ledger.md
templates/
  rule.md
  pattern.md
  principle.md
  mechanism.md
  downstream/
    AGENTS.md
    docs/development/
      README.md
      rules/
        README.md
        <domain>.md
```

Do not add placeholder files just to match the planned structure. Create files when they contain
durable content that is ready for review.

## Delivery Approach

Build this repo in small, reviewable chunks. Each chunk should have one clear purpose and be
validated locally before handoff.

## Validation

Run both checks before handing off broad guidance changes:

```bash
python3 scripts/audit_guidance.py
python3 scripts/generate_rule_indexes.py --check
python3 scripts/generate_agent_rules.py --check
python3 scripts/generate_downstream_template.py --check
markdownlint-cli2 "**/*.md"
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

Completed first-version sequence:

1. Establish the repo charter and guidance architecture.
1. Add the first pattern/principle template and a small seed batch of named guidance units.
1. Add a broad software-change guide that links to the seed units.
1. Add Rust maintainability guidance and Rust-specific units.
1. Add Markdown, documentation, and coding-agent guides.
1. Add jj workflow guidance and copy/paste agent snippets.

Possible later work:

- Extract sharper examples from real review comments.
- Add project-specific snippet variants after reuse exposes repeated adaptation work.
- Add narrower mechanism profiles when repeated rule clusters expose a command, lint, CI job, or
  generated artifact that should be named directly.

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
