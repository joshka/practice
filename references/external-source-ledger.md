# External Source Ledger

This ledger records durable external sources that inform the guidance in this repo. Rule and
principle files should link directly to the most relevant sources, but this file explains the broad
role each source family plays so the repo can be understood without rereading the original mining
material.

## Source Families

- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/): Rust API shape, traits,
  errors, features, and docs. Adopt where aligned and adapt to maintainer use.
- [Microsoft Pragmatic Rust Guidelines][ms-rust-guidelines]: Agent-facing Rust defaults and safety
  guidance. Adapt while keeping this repo's voice and local priorities.
- [epage Rust Style](https://epage.github.io/dev/rust-style/): Rust module layout, imports,
  naming, and style. Mostly adopt, with local module preferences.
- [epage PR Style](https://epage.github.io/dev/pr-style/): PR narrative and reviewer-oriented
  communication. Adapt into review artifact guidance.
- [The Rust Book](https://doc.rust-lang.org/book/) and official Rust docs: language behavior,
  ownership, traits, and cargo. Use as primary technical reference.
- [Cargo Book](https://doc.rust-lang.org/cargo/): Cargo metadata, features, packaging, and
  dependency behavior. Use as primary tooling reference.
- [rustdoc docs](https://doc.rust-lang.org/rustdoc/): Rustdoc, doctests, and docs.rs-style builds.
  Use as primary documentation tooling reference.
- [Jujutsu docs](https://docs.jj-vcs.dev/): jj commands, revsets, bookmarks, remotes, and recovery.
  Use as primary VCS reference.
- [Diataxis](https://diataxis.fr/): documentation type distinctions. Adapt for repo docs and
  guides.
- [OpenTelemetry](https://opentelemetry.io/docs/): logs, traces, metrics, and observability
  concepts. Use for observability vocabulary.
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/): secret handling, logging safety, and
  security review. Use for security-sensitive limits.
- [Martin Fowler](https://martinfowler.com/) and [Refactoring](https://refactoring.com/):
  refactoring, change shape, and design vocabulary. Adapt without copying prose.
- [Parse, don't validate][parse-dont-validate]: boundary correctness and typed validation. Adapt as
  a core boundary principle.
- [OpenAI docs](https://platform.openai.com/docs/): agent and model behavior where product-specific.
  Use only for current OpenAI-specific claims.

## Use Rules

- Prefer direct links from each rule or principle to the narrowest relevant source.
- Use this ledger when adding a new source family or explaining why a source appears repeatedly.
- Do not copy or closely paraphrase source wording into this repo.
- Treat source links as support, contrast, or provenance; the guidance should still stand in this
  repo's own reasoning.
- Omit references when no durable source clarifies the idea.

[ms-rust-guidelines]: https://microsoft.github.io/rust-guidelines/agents/index.html
[parse-dont-validate]: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
