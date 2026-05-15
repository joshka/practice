# VCS Quote Revsets And Shell Syntax

## Metadata

- ID: `VCS-QUOTE-REVSETS-AND-SHELL-SYNTAX`
- Legacy ID: `R-0705`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Quote revsets and shell-sensitive syntax.

## Why

Revsets and bookmark syntax often contain characters such as `@`, `|`, `&`, `~`, parentheses, or
spaces that shells can interpret. Unquoted syntax can run a different command than intended or fail
in confusing ways.

## Helps

- Prevents shell parsing bugs in jj examples, scripts, and agent commands.

## Limits

Quoting style depends on shell and context. Prefer simple single quotes in shell examples unless
interpolation is needed.

## Agent Instruction

Quote revsets and shell-sensitive syntax because revsets and bookmark syntax often contain characters
such as `@`, `|`, `&`, `~`, parentheses, or spaces that shells can interpret.

## Mechanisms

Supported by quoted examples, script tests, shellcheck where applicable, and checking `jj help` for
revset syntax before publishing commands.

## References

- [Principle: Jj Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
