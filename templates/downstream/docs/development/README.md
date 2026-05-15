# Development Guidance

This directory carries repo-local development guidance for agents and maintainers.

The generated rule files are copied from the `development-preferences` repo, which is the canonical
source for these shared rules. Update local validation commands and repo-specific notes here, but
refresh copied rule text from upstream instead of editing it by hand.

From the canonical repo, refresh this downstream copy with:

```bash
python3 scripts/generate_downstream_template.py --output /path/to/this-repo
```

## Files

- `rules/README.md`: generated index for the full compressed reviewed-rule pack.
- `rules/*.md`: generated domain files containing every reviewed rule.

## Adoption Notes

Keep `AGENTS.md` short enough to scan. Put the full rule pack in generated domain files so agents
can load only the domains relevant to the task, while still ensuring every reviewed rule is
represented downstream.

Update local validation commands, source-control notes, and project-specific boundaries in
`AGENTS.md` or nearby local docs. If a generated rule is wrong, update the canonical
`development-preferences` repo and recopy the generated files.
