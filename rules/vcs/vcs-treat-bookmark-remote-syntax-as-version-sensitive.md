# VCS Treat Bookmark Remote Syntax As Version Sensitive

## Metadata

- ID: `VCS-TREAT-BOOKMARK-REMOTE-SYNTAX-AS-VERSION-SENSITIVE`
- Legacy ID: `R-0719`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Treat `bookmark@remote` command syntax as version-sensitive.

## Why

JJ command syntax around `bookmark@remote` and remote bookmark handling can vary by version and
command. Assuming one spelling everywhere makes docs and agent commands fragile across installed jj
versions.

## Helps

- Keeps jj guidance accurate across version differences and reduces command-shape failures.

## Limits

Prefer the current repo's installed jj behavior when writing commands for that checkout. For durable
docs, verify syntax against `jj help` or phrase guidance conceptually.

## Agent Instruction

Treat `bookmark@remote` command syntax as version-sensitive because jj command syntax around
`bookmark@remote` and remote bookmark handling can vary by version and command.

## Mechanisms

Supported by `jj --version`, `jj help bookmark`, tested command snippets, and docs that avoid
unverified shorthand.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
