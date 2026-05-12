# Repository Guidelines

## Project Purpose

This repository is the durable home for practical development preferences. Keep the docs standalone:
they should make sense without naming private source repos, local prototypes, or temporary discovery
paths.

## Documentation Style

- Use Markdown that is friendly to `markdownlint-cli2` defaults.
- Wrap prose around 100 columns unless a project config says otherwise.
- Put a blank line after headings.
- Put a blank line before and after lists, blockquotes, and fenced code blocks.
- Use fenced code blocks with triple backticks and a language tag.
- Use `1.` markers for numbered lists.
- Format Markdown tables so columns line up; this repo configures MD060 with `style: aligned`.
- Prefer concise, named guidance files over large monolithic docs when an idea needs reuse.
- Give referenceable guidance stable names or IDs so it can be linked from guides, review comments,
  and agent snippets.

## Guidance Content

Each reusable guidance unit should usually state:

- The problem or failure mode.
- The preferred move.
- The tradeoff or limit.
- A compact agent instruction.
- Durable references when they clarify the idea.

Guides should link to named guidance units instead of duplicating large sections. Add new files only
when they contain real durable content; avoid empty placeholders.

## Version Control

Use jujutsu (`jj`) for local version-control workflow.

- In this repo, do not use Git for normal local source-control operations.
- Keep changes small, atomic, and reviewable.
- Set a clear jj description early when making real edits.
- Use `--no-pager` for jj commands that produce output.
- Do not run destructive commands.
- Do not rewrite unrelated work.
- Write jj descriptions and published commit messages in the Chris Beams and Tim Pope style: short
  imperative subject, blank line before any body, body wrapped at 72 columns, and body text focused
  on why and what changed rather than restating the diff.
- Use Conventional Commits only when the repository already follows that spec; otherwise use the
  canonical unprefixed Chris Beams and Tim Pope style.

Current publication policy: validate locally and ask before pushing. This policy may change as the
repo workflow matures.

## Local Review Loop

Optimize for small chunks and easy maintainer confirmation.

- After each validated chunk, offer a numbered list of concrete next chunks.
- Put the recommended next chunk first and explain the tradeoff behind each option.
- Treat a numbered choice as approval to move forward with that chunk.
- Explain the tradeoff behind each option, especially when the choice affects structure, naming, or
  future guidance shape.
- If the maintainer responds with review feedback instead of a next-choice number, address that
  feedback before moving on.
- Implement only the confirmed chunk.
- Keep each change small enough to review locally before moving on.
- After validation, ask whether to push before publishing remote state.
- If the maintainer redirects the sequence, update the next chunk instead of defending the old plan.

## Validation

Before handing off documentation changes, run:

```bash
markdownlint-cli2 "**/*.md"
```

If the command is unavailable, report that it was not run. Also report the relevant `jj` status and
diff summary.
