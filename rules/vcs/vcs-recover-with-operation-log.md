# VCS Recover With Operation Log

## Metadata

- ID: `VCS-RECOVER-WITH-OPERATION-LOG`
- Name: `Recover with Operation Log`
- Summary: Use jj operation-log recovery before destructive cleanup habits.
  The operation log preserves recoverable graph states, but inspect the target before restoring.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`
- Related: `vcs-use-evolog-and-operation-log, preserve-unowned-work`

## Rule

Use operation-log recovery instead of destructive cleanup.

## Why

JJ records repository operations so many mistakes are recoverable without destructive Git reset or
stash habits. Using the operation log preserves the ability to inspect, undo, or restore specific
graph states.

## Helps

- Makes recovery safer and avoids destroying unrelated local work.

## Limits

Do not blindly restore old operations without inspecting what changed since then. Recovery can also
undo useful later work if the target operation is wrong.

## Agent Instruction

Use operation-log recovery instead of destructive cleanup because jj records repository operations so
many mistakes are recoverable without destructive Git reset or stash habits.

## Mechanisms

Supported by `jj op log`, `jj op show`, `jj undo`, `jj op restore`, `jj evolog`, and recovery notes
before broad repair.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
