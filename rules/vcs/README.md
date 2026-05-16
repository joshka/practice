# JJ Topology And Source Control

VCS rules cover jj-first source-control work, remote topology, operation-log recovery, workspaces,
publication safety, and file-tracking decisions.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`VCS-ASK-BEFORE-REPAIRING-JJ-ALIASES`](vcs-ask-before-repairing-jj-aliases.md). Ask before
  changing jj aliases when they disagree with the observed repository topology. Aliases encode
  workflow policy, so silent repairs can alter future user commands.
- [`VCS-AVOID-INTERACTIVE-JJ-IN-AGENT-WORK`](vcs-avoid-interactive-jj-in-agent-work.md). Use
  noninteractive jj commands with explicit messages, targets, and files in agent work. Interactive
  editors, prompts, merge tools, and pagers can hang unattended sessions.
- [`VCS-CONFIGURE-JJ-PAGER`](vcs-configure-jj-pager.md). Scope pager control with `--no-pager`,
  `JJ_PAGER=cat`, or session configuration. Direct output keeps source-control evidence visible
  without changing the user's global pager.
- [`VCS-CONFIRM-BROAD-JJ-OPERATIONS`](vcs-confirm-broad-jj-operations.md). Confirm jj operations
  that abandon, rebase, squash, split, restore, publish, or go broad. Confirmation protects
  unrelated work when a command can reshape history or public state.
- [`VCS-CONFIRM-GITHUB-REMOTE-TOPOLOGY`](vcs-confirm-github-remote-topology.md). Inspect `origin`,
  `upstream`, push remote, PR base, and PR head before publication. Fork and owned-repo layouts
  differ, so defaults can push or target the wrong repository.
- [`VCS-CREATE-OPERATION-LOG-POINT-BEFORE-RESHAPING`](vcs-create-operation-log-point-before-reshaping.md).
  Create a recent jj operation boundary before risky stack reshaping. Recovery is easier when there
  is a known point before rebases, splits, squashes, or repairs.
- [`VCS-DO-NOT-FALL-BACK-TO-GIT-FOR-JJ-ISSUES`](vcs-do-not-fall-back-to-git-for-jj-issues.md).
  Diagnose jj locks, pager issues, and state problems through jj before switching tools. Git
  bypasses jj change-graph semantics, so use it only for transport after jj state is coherent.
- [`VCS-DRY-RUN-SURPRISING-PUBLICATION`](vcs-dry-run-surprising-publication.md). Use dry-run for
  ambiguous or surprising remote publication, not every routine push. Extra verification pays off
  when remotes, bookmarks, force-like updates, or PR bases are unclear.
- [`VCS-DUPLICATE-FOR-ALTERNATIVE-CANDIDATES`](vcs-duplicate-for-alternative-candidates.md). Use `jj
  duplicate` when two plausible fixes or refactors need independent validation. Separate candidate
  changes preserve comparison and recovery without mutating the only option.
- [`VCS-INSPECT-SPARSE-STATE`](vcs-inspect-sparse-state.md). Check sparse checkout state before
  treating a missing path as absent from history. Sparse patterns can hide files, so inspection
  prevents recreating or editing the wrong path.
- [`VCS-INSPECT-STATE-BEFORE-MUTATING`](vcs-inspect-state-before-mutating.md). Inspect working-copy,
  stack, bookmark, conflict, and unowned state before mutation. Current state keeps edits scoped and
  avoids rewriting work the agent did not inspect.
- [`VCS-JJ-AS-SOURCE-OF-TRUTH`](vcs-jj-as-source-of-truth.md). Use jj for local workflow in
  repositories with `.jj` state. This preserves descriptions, stack shape, operation-log recovery,
  and bookmark semantics.
- [`VCS-JJ-NEW-FOR-REVIEW-LANES`](vcs-jj-new-for-review-lanes.md). Start unrelated review units with
  `jj new` before edits accumulate. Separate changes keep review atomic while leaving later squash
  or absorb decisions easy.
- [`VCS-MAKE-GITHUB-HANDOFF-EXPLICIT`](vcs-make-github-handoff-explicit.md). Name bookmark, remote,
  base, head, and repo when handing coherent jj state to GitHub. Explicit publication avoids
  host-tool inference mistakes in forks, stacks, and multi-remote repos.
- [`VCS-MATCH-JJ-TOPOLOGY-TO-REPO-ROLE`](vcs-match-jj-topology-to-repo-role.md). Align fetch
  remotes, push remotes, tracked bookmarks, aliases, and PR bases to repo role. Owned, maintainer,
  and fork-only workflows need different topology assumptions.
- [`VCS-NAME-EXACT-JJ-MUTATION-TARGETS`](vcs-name-exact-jj-mutation-targets.md). Specify revisions,
  filesets, bookmarks, and destinations for mutating jj commands. Explicit targets make intent
  reviewable and prevent defaults from acting on surprising state.
- [`VCS-QUOTE-REVSETS-AND-SHELL-SYNTAX`](vcs-quote-revsets-and-shell-syntax.md). Quote jj revsets,
  bookmark syntax, and other shell-sensitive command fragments. Shell metacharacters can alter
  commands, so examples should prefer simple safe quoting.
- [`VCS-RECOVER-WITH-OPERATION-LOG`](vcs-recover-with-operation-log.md). Use jj operation-log
  recovery before destructive cleanup habits. The operation log preserves recoverable graph states,
  but inspect the target before restoring.
- [`VCS-REPAIR-REMOTE-TOPOLOGY-COHERENTLY`](vcs-repair-remote-topology-coherently.md). Repair fetch,
  push, tracking, trunk alias, PR base, and PR head assumptions together. Remote topology is
  coupled, so partial fixes can leave publication commands half-correct.
- [`VCS-RUN-JJ-MUTATIONS-SEQUENTIALLY`](vcs-run-jj-mutations-sequentially.md). Do not overlap jj
  commands that write repo, working-copy, bookmark, or config state. Sequential mutations avoid
  locks, stale reads, and confusing operation order.
- [`VCS-SCOPE-JJ-FILE-TRACKING`](vcs-scope-jj-file-tracking.md). Pass intended paths to `jj file
  track` and `jj file untrack`. Scoped tracking keeps local-only, generated, or unrelated files out
  of publication state.
- [`VCS-STOP-REPEATED-JJ-RETRIES-AND-LOCALIZE-STATE`](vcs-stop-repeated-jj-retries-and-localize-state.md).
  Stop repeating a failing jj command after a transient retry and inspect relevant state. Diagnosis
  beats command spam when locks, sparse paths, bookmarks, or remotes disagree.
- [`VCS-TRACK-REMOTES-EXPLICITLY`](vcs-track-remotes-explicitly.md). Set explicit remote tracking
  when the same bookmark name exists on multiple remotes. This prevents fetch, rebase, and
  publication ambiguity in fork and upstream workflows.
- [`VCS-TREAT-BOOKMARK-REMOTE-SYNTAX-AS-VERSION-SENSITIVE`](vcs-treat-bookmark-remote-syntax-as-version-sensitive.md).
  Verify `bookmark@remote` and remote-bookmark syntax against the installed jj version. Durable
  guidance should avoid assuming one spelling works across commands and releases.
- [`VCS-USE-EVOLOG-AND-OPERATION-LOG`](vcs-use-evolog-and-operation-log.md). Use `jj evolog` for a
  change's evolution and `jj op log` for repository operations. Picking the right log distinguishes
  rewrite history from workspace, bookmark, and import events.
- [`VCS-USE-GIT-FORMATTED-DIFFS-FOR-AGENTS`](vcs-use-git-formatted-diffs-for-agents.md). Prefer `jj
  diff --git` when agents or patch-oriented tools need diff text. Git patch format preserves hunks
  and paths in a shape those consumers can parse reliably.
- [`VCS-USE-IGNORE-WORKING-COPY-CAREFULLY`](vcs-use-ignore-working-copy-carefully.md). Use
  `--ignore-working-copy` only for understood lock-safe inspection or metadata work. It may read
  stale file state, so do not use it to bypass normal synchronization before edits.
- [`VCS-WORKSPACE-ADD-FOR-SECOND-CHECKOUTS`](vcs-workspace-add-for-second-checkouts.md). Use `jj
  workspace add` only when a task needs another filesystem checkout. Ordinary review separation
  should use `jj new`; workspaces fit clean validation or parallelism.
