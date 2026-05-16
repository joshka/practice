# VCS Make GitHub Handoff Explicit

## Metadata

- ID: `VCS-MAKE-GITHUB-HANDOFF-EXPLICIT`
- Name: `Make GitHub Handoff Explicit`
- Summary: Name bookmark, remote, base, head, and repo when handing coherent jj state to GitHub.
  Explicit publication avoids host-tool inference mistakes in forks, stacks, and multi-remote repos.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Make GitHub handoff explicit after jj state is coherent.

## Why

JJ state and GitHub state are related but not identical. Before opening or updating a PR, the
handoff should name the bookmark, remote, base branch, head branch, and repository so host tooling
does not infer the wrong target.

## Helps

- Makes PR publication reproducible and avoids confusing branch or fork inference.

## Limits

In a simple known repo, defaults may work. Be explicit when forks, stacks, multiple remotes, or
nonstandard bookmark names are involved.

## Agent Instruction

Make GitHub handoff explicit after jj state is coherent because jj state and GitHub state are related
but not identical.

## Mechanisms

Supported by `jj bookmark list`, `jj git push`, `gh pr create --repo --head --base`, and publication
notes that name local and remote refs.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
