# Docs Prove Real Use With Examples

## Metadata

- Name: `Prove Real Use With Examples`
- ID: `DOCS-PROVE-REAL-USE-WITH-EXAMPLES`
- Summary: `Use examples that show realistic ownership, errors, lifecycle, configuration, or
  integration shape. Keep them focused, but make them strong enough to prove the contract.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, examples, verification, public-api`
- Related: `test-observable-behavior, DOCS-DISTINGUISH-EXAMPLE-ROLES`

## Rule

Prove real use with examples.

## Why

Examples that only construct a type or call the happy-path function do not prove that the API works
in the way users need. A useful example shows ownership, errors, feature flags, lifecycle,
input/output, or integration shape close enough to real use that readers can adapt it safely.

## Helps

- Turns examples into contract evidence and prevents shallow examples from hiding missing
  integration details.

## Limits

Keep examples focused. Do not build a full app when a smaller realistic slice proves the contract
that matters.

## Agent Instruction

Prove real use with examples because examples that only construct a type or call the happy-path
function do not prove that the API works in the way users need.

## Mechanisms

Supported by doctests, integration examples, example binaries, fixtures, snapshots, and review that
asks what real user question the example answers.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
