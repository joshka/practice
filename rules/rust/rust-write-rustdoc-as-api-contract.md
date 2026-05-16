# Rust Write Rustdoc As API Contract

## Metadata

- Name: `Write Rustdoc As API Contract`
- ID: `RUST-WRITE-RUSTDOC-AS-API-CONTRACT`
- Summary: Use Rustdoc to state caller-facing behavior, invariants, failures, side effects, and
  compatibility promises. Leave private implementation detail in comments unless it helps maintain
  the public contract.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, rustdoc, documentation, public-api`
- Related: `write-docs-as-contracts, rust-write-public-docs-for-caller-tasks`

## Rule

Write Rustdoc as an API contract.

## Why

Rustdoc is often the first and most durable public view of a crate. Public docs should explain what
an item represents, how callers use it, what can fail, what side effects happen, and which
compatibility promises callers may rely on. Vague prose and generic examples leave the real
contract in source code.

The Rust API Guidelines explicitly call for crate-level docs, examples, and documentation of error,
panic, and safety considerations. This rule extends that stance to the whole caller-facing contract:
ownership, invariants, lifecycle, concurrency, feature gates, and supported use should be written
where users will read them.

## Helps

- Helps downstream users understand behavior without reading private implementation details.

## Limits

Do not duplicate every implementation detail in Rustdoc. Document caller-facing contracts,
invariants, failure modes, side effects, examples, and meaningful tradeoffs. Private implementation
details belong in source comments only when they help maintainers preserve the contract.

## Agent Instruction

Write Rustdoc as caller-facing contract text, not decoration or generic prose.

## Mechanisms

Supported by `cargo doc`, doctests, broken-link checks, examples, and review that checks public
items for contract-level documentation.

## References

- [Rust API Guidelines: Documentation](https://rust-lang.github.io/api-guidelines/documentation.html)
- [rustdoc book: How to write documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
