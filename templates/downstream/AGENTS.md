# Agent Guidance

Use this file as the repo-local map. Keep the full reviewed rule pack in
`docs/development/rules/` so every rule is available without making this file a long manual.

The copied rule files come from the `development-preferences` repo, which is the canonical source
for these rules. Refresh those files from that repo when the shared rule set changes.

## Local Rules

- Follow local code, tests, docs, and existing conventions before general preferences.
- Preserve unowned human or agent work.
- Keep changes small, atomic, and reviewable.
- Report validation evidence in handoffs instead of confidence language.
- Use the validation commands listed below before handoff.
- Read `docs/development/rules/README.md` for the full reviewed development rule pack.

## Validation

Replace these examples with the repo's real checks:

```bash
cargo fmt --check
cargo test
markdownlint-cli2 "**/*.md"
```

## Deeper Guidance

- `docs/development/rules/README.md`: generated index for all reviewed rule domains.
- `docs/development/README.md`: local map for development guidance.
