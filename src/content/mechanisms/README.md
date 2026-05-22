# Mechanisms

Mechanisms are mechanical supports for the guidance in this repo: lints, formatter settings, CI
checks, command recipes, local tool configuration, templates, and generated artifacts. They do not
replace judgment, but they make preferred behavior cheaper and repeated mistakes harder.

## Draft Mechanisms

- [`project-operating-manual`](project-operating-manual.md): A project-owned operating manual
  applies the broader guidance catalog to one live codebase so `AGENTS.md` can stay a map instead
  of becoming the whole doctrine.

## Reviewed Mechanisms

- [`guidance-generation-and-audit`](guidance-generation-and-audit.md): Generators and audits keep
  rule indexes, compressed agent snippets, templates, and Markdown synchronized.
- [`guidance-content-model-stewardship`](guidance-content-model-stewardship.md): Content-model
  stewardship keeps guidance families distinct while recording subjective review queues.
- [`jj-agent-workflow`](jj-agent-workflow.md): Noninteractive jj defaults, topology checks, and
  local override conventions make agent VCS work safer.
- [`rust-api-and-release-checks`](rust-api-and-release-checks.md): Cargo release, semver, feature,
  packaging, and minimum-version checks protect downstream users.
- [`rust-docs-validation`](rust-docs-validation.md): Doctests, Rustdoc warnings, rendered docs, and
  docs.rs-style builds prove documentation surfaces.
- [`rust-lints-and-formatting`](rust-lints-and-formatting.md): Rust and Markdown formatting plus
  project lints encode stable mechanical preferences.
- [`rust-tooling-profile`](rust-tooling-profile.md): The broad Rust tooling profile gathers lints,
  docs, release, CI, performance, and agent tooling.
- [`testing-and-benchmarking`](testing-and-benchmarking.md): Test, feature-matrix, fuzzing,
  property, and benchmark tools are chosen by risk and feedback cost.
