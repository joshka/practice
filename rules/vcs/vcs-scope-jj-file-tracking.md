# VCS Scope JJ File Tracking

## Metadata

- ID: `VCS-SCOPE-JJ-FILE-TRACKING`
- Legacy ID: `R-0710`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Scope jj file track and untrack commands to intended paths.

## Why

`jj file track` and `jj file untrack` can affect more files than intended if paths are omitted or
globbed too broadly. Path-scoping matters when local plans, generated files, or private override
files should stay untracked.

## Helps

- Prevents accidental publication or removal of local-only and unrelated files.

## Limits

Broad tracking is acceptable during an intentional repo import or generated-file policy change. For
normal edits, name the paths.

## Agent Instruction

Scope jj file track and untrack commands to intended paths because `jj file track` and `jj file
untrack` can affect more files than intended if paths are omitted or globbed too broadly.

## Mechanisms

Supported by explicit paths, `.git/info/exclude`, global ignores, `jj status`, and diff review after
track or untrack commands.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
