# Agent Guidance

Use this file as the repo-local map. Keep the reviewed shared rule pack in
`docs/development/` so every rule is available without making this file a long manual.

The copied development guidance comes from the `development-preferences` repo. The public reference
site is [Software Practices](https://www.joshka.net/practice/). Use the local compact rules first,
and use the site when a rule, pattern, principle, or guide needs more context.

## Local Rules

- Follow local code, tests, docs, and existing conventions before general preferences.
- Preserve unowned human or agent work.
- Keep changes small, atomic, and reviewable.
- Report validation evidence in handoffs instead of confidence language.
- Use the validation commands listed below before handoff.
- Read `docs/development/snippets/agents/rules.md` for the single-file reviewed rule pack.
- Read `docs/development/rules/README.md` when a task needs only one rule domain.
- Preserve and prioritize repo-specific instructions in this file. Merge shared guidance into the
  local agent map; do not replace local project rules with the template blindly.
- Refresh copied guidance with `python3 docs/development/update.py` when the shared rule set
  changes.
- If a shared rule causes trouble or should be changed for most projects, capture that feedback for
  the `development-preferences` repo.

## Validation

Replace these examples with the repo's real checks:

```bash
cargo fmt --check
cargo test
markdownlint-cli2 "**/*.md"
```

## Deeper Guidance

- `docs/development/snippets/agents/rules.md`: generated single-file reviewed rule pack.
- `docs/development/rules/README.md`: generated index for reviewed rule domains.
- `docs/development/bootstrap-downstream.md`: instructions for refreshing and merging this guidance
  into a downstream repo.
- `docs/development/README.md`: local map for development guidance.
- [Software Practices](https://www.joshka.net/practice/): canonical rendered reference for guides,
  rules, patterns, principles, mechanisms, and tags.
