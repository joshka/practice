# Docs Readme As Entry Point

## Metadata

- Name: `README as Entry Point`
- ID: `DOCS-README-AS-ENTRY-POINT`
- Summary: `Use README files to orient readers to purpose, setup, first useful use, and deeper docs.
  Split out manual-level detail when it hides the starting path.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, reader-locality, source-truth`
- Related: `bootstrap-repo-docs, keep-docs-near-their-subject`

## Rule

Keep README files as entry points.

## Why

A README is usually the first page for humans and agents. It should orient the reader to purpose,
install or setup path, first useful example, and where deeper material lives. If it becomes a full
manual or a link dump, the entry point stops helping readers start.

## Helps

- Gives new readers a reliable starting path without duplicating every reference detail.

## Limits

A small project can keep more detail in the README. Split out deeper guides when the README starts
hiding the first useful path.

## Agent Instruction

Keep README files as entry points because a README is usually the first page for humans and agents.

## Mechanisms

Supported by README outlines, quickstart examples, doc maps, link checks, and review that asks
whether the first screen helps a new reader begin.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
