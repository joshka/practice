# VCS Configure JJ Pager

## Metadata

- ID: `VCS-CONFIGURE-JJ-PAGER`
- Name: `Configure JJ Pager`
- Summary: Scope pager control with `--no-pager`, `JJ_PAGER=cat`, or session configuration.
  Direct output keeps source-control evidence visible without changing the user's global pager.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`
- Related: `vcs-avoid-interactive-jj-in-agent-work, shape-tool-output-for-agents`

## Rule

Configure `JJ_PAGER` for agent tooling when available.

## Why

Paged output can block or truncate agent command results. Setting `JJ_PAGER=cat` or using
`--no-pager` ensures status, log, and diff output returns directly to the tool where the agent can
inspect it.

## Helps

- Prevents stuck commands and makes source-control evidence visible in handoffs.

## Limits

Do not change a user's global pager unless asked. Prefer per-command `--no-pager` or environment
configuration scoped to the agent session.

## Agent Instruction

Configure `JJ_PAGER` for agent tooling so paged output does not block or truncate command results.

## Mechanisms

Supported by `jj --no-pager`, `JJ_PAGER=cat`, repo-local command wrappers, and agent instructions
that require non-paged jj output.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
