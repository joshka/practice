# VCS Confirm GitHub Remote Topology

## Metadata

- ID: `VCS-CONFIRM-GITHUB-REMOTE-TOPOLOGY`
- Name: `Confirm GitHub Remote Topology`
- Summary: Inspect `origin`, `upstream`, push remote, PR base, and PR head before publication.
  Fork and owned-repo layouts differ, so defaults can push or target the wrong repository.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Confirm GitHub `origin` and `upstream` topology before publication.

## Why

Forks and GitHub defaults can make `origin` mean the user fork while `upstream` means the canonical
repo, or vice versa in owned repos. Publishing or opening a PR without confirming that topology can
push to the wrong remote or target the wrong base.

## Helps

- Keeps push remote, PR head, PR base, and tracked bookmarks aligned.

## Limits

In a known single-remote personal repo, a quick inspection may be enough. Reconfirm when forks,
organization repos, maintainer access, or renamed remotes are involved.

## Agent Instruction

Confirm GitHub `origin` and `upstream` topology before publication because forks and GitHub defaults
can make `origin` mean the user fork while `upstream` means the canonical repo, or vice versa in
owned repos.

## Mechanisms

Supported by `jj git remote list`, `jj bookmark list`, `gh repo view`, explicit `gh --repo --head
--base`, and dry-run publication.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
