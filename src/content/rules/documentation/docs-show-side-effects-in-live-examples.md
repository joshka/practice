# Docs Show Side Effects In Live Examples

## Metadata

- Name: `Show Side Effects in Live Examples`
- ID: `DOCS-SHOW-SIDE-EFFECTS-IN-LIVE-EXAMPLES`
- Summary: `Show setup, visible effects, and cleanup when examples touch live resources or
  persistent state. Gate costly or externally visible actions so examples stay honest and safe to
  adapt.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, examples, side-effects, verification`
- Related: `make-side-effects-visible, DOCS-DOCUMENT-LIFECYCLE-AND-SIDE-EFFECTS`

## Rule

Show side effects and cleanup in live-resource examples.

## Why

Examples that create files, hit networks, write DNS records, open terminals, spawn tasks, or mutate
external services can look harmless while leaving persistent state or requiring cleanup. Showing
setup, side effects, and teardown teaches the operational contract, not just the call syntax.

## Helps

- Reduces unsafe copy-paste behavior and makes live-resource examples honest about their effects.

## Limits

Do not include real credentials, destructive defaults, or noisy cleanup detail in quickstarts. Gate
live examples behind explicit opt-in when the side effect is costly or externally visible.

## Agent Instruction

Show side effects and cleanup in examples that create files, hit networks, write records, open
terminals, spawn tasks, or mutate services.

## Mechanisms

Supported by `no_run` examples with clear setup, sandboxed fixtures, cleanup code,
environment-variable gates, and integration tests for live-example helpers.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
