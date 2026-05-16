# Docs Verify Commands Paths And Links

## Metadata

- ID: `DOCS-VERIFY-COMMANDS-PATHS-AND-LINKS`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Verify example commands, file paths, and linked references.

## Why

Commands, paths, and links are executable instructions in disguise. A stale `cargo` command, moved
file path, or broken reference sends readers and agents down a false path even when the surrounding
prose is well written.

## Helps

- Keeps docs operationally accurate and reduces repair time for readers following examples.

## Limits

Some commands require credentials, services, or platforms that cannot be run locally. Mark those
assumptions and verify the parts that can be checked.

## Agent Instruction

Verify example commands, file paths, and linked references because they act like executable
instructions.

## Mechanisms

Supported by shell checks, link checkers, doctests, `cargo doc`, rendered-preview review, and
explicit skipped-check notes when a command cannot be run.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
