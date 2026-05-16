# Change Respect Generated Artifact Ownership

## Metadata

- ID: `CHANGE-RESPECT-GENERATED-ARTIFACT-OWNERSHIP`
- Legacy ID: `R-0013`
- Status: `reviewed`
- Domain: `change-shape`
- Depth: `compact`

## Rule

Respect generated artifact ownership instead of hand-editing generated outputs.

## Why

Generated changelogs, lockfiles, code, snapshots, API listings, docs, and release files often have a
source input that owns their contents. A hand edit to the generated output may be overwritten on the
next run, may hide that the generator configuration or source data is wrong, or may make future
regeneration produce a surprising diff.

Respecting ownership keeps fixes at the durable layer: update the source input, generator
configuration, template, release metadata, or generation command when those own the artifact. If a
tool explicitly supports curated edits, make that ownership model visible so reviewers know the edit
will survive the next generation step.

## Helps

- Prevents manual generated-file edits from being lost or fighting the generator.
- Makes generator, template, and release-tooling changes reviewable at the source.

## Limits

Some generated artifacts are designed for post-generation curation. Edit them by hand only when the
tool's workflow says that curation is stable, and report whether the source, generated output, or
both were intentionally changed.

## Agent Instruction

Edit the source input, template, release metadata, or generator config for generated artifacts; hand
edit generated output only for tool workflows that make curation durable.

## Mechanisms

Supported by generated-file headers, generator commands in handoffs, release-tooling PRs, template
tests, generated-output diffs, and checks that compare generated artifacts to their sources.

## References

- [Change Sync Generated Artifacts](change-sync-generated-artifacts.md)
- [IBM: Manual editing of generated artifacts](https://www.ibm.com/docs/en/imdm/11.6?topic=model-manual-editing-generated-artifacts)
- [Release Please: release PRs update changelog files](https://github.com/googleapis/release-please)
