# Docs Keep Markdown Lintable

## Metadata

- Name: `Keep Markdown Lintable`
- ID: `DOCS-KEEP-MARKDOWN-LINTABLE`
- Summary: `Use project Markdown style so formatting stays enforceable and review noise stays low.
  Treat lint exceptions as intentional local choices, not accumulated drift.`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Keep Markdown lintable.

## Why

Formatting drift adds review noise and makes generated or agent-edited docs harder to maintain.
Lintable Markdown catches line length, heading spacing, fenced code blocks, ordered-list style, and
table alignment before those details become repeated review comments.

## Helps

- Keeps documentation diffs clean and makes style expectations enforceable by tools.

## Limits

Project configs can intentionally override defaults. Follow the repo config when it differs, and
avoid manual formatting fights that a formatter or lint config should settle.

## Agent Instruction

Keep Markdown lintable because formatting drift adds review noise and makes generated or agent-edited
docs harder to maintain.

## Mechanisms

Supported by `markdownlint-cli2`, repo markdownlint config, CI docs checks, editor formatting, and
review that treats lint failures as fixable mechanics.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
