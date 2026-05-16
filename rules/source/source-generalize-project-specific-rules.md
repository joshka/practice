# Source Generalize Project Specific Rules

## Metadata

- Name: `Generalize Project-Specific Rules`
- ID: `SOURCE-GENERALIZE-PROJECT-SPECIFIC-RULES`
- Summary: Extract the portable failure mode before promoting local lessons into shared guidance.
  Provider, repo, or tool details should stay local unless they clarify the durable rule.
- Status: `reviewed`
- Domain: `source`
- Depth: `compact`

## Rule

Generalize project-specific rules before promotion.

## Why

Local mining often starts from one repository, tool, provider, or incident. Before a lesson becomes
shared guidance, extract the portable failure mode. A DNS-provider workaround, a terminal backend
quirk, or a repo-specific jj alias may become a general rule only after the provider-specific parts
are separated from the durable preference.

## Helps

- Keeps public guidance broadly reusable while preserving narrow lessons for the places where they
  actually apply.

## Limits

Some lessons remain project-specific and should stay out of shared guidance. Promote the underlying
failure mode only when it applies beyond the original repository or toolchain.

## Agent Instruction

Generalize project-specific rules before promotion because local mining often starts from one
repository, tool, provider, or incident.

## Mechanisms

Supported by source review, local-only planning files, domain labels, explicit limits, and
promotion passes that ask whether the rule applies outside the original repository.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Rust API Guidelines: public APIs are stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
- [Microsoft Pragmatic Rust Guidelines: prefer simple abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
