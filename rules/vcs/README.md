# JJ Topology And Source Control

VCS rules cover jj-first source-control work, remote topology, operation-log recovery, workspaces,
publication safety, and file-tracking decisions.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`VCS-ASK-BEFORE-REPAIRING-JJ-ALIASES`](vcs-ask-before-repairing-jj-aliases.md). Ask the user to
  repair jj aliases when topology and aliases disagree. Aliases such as `trunk()` or publish helpers
  encode assumptions about remotes and bookmarks. Helps: Keeps user-level jj configuration
  deliberate and prevents agents from rewriting source-control policy unexpectedly.
- [`VCS-AVOID-INTERACTIVE-JJ-IN-AGENT-WORK`](vcs-avoid-interactive-jj-in-agent-work.md). Avoid
  interactive-by-default jj commands in unattended agent work. Interactive jj commands can open
  editors, prompts, merge tools, or pagers that unattended agents cannot handle reliably. Helps:
  Keeps agent source-control operations repeatable and reviewable.
- [`VCS-CONFIGURE-JJ-PAGER`](vcs-configure-jj-pager.md). Configure `JJ_PAGER` for agent tooling when
  available. Paged output can block or truncate agent command results. Helps: Prevents stuck
  commands and makes source-control evidence visible in handoffs.
- [`VCS-CONFIRM-BROAD-JJ-OPERATIONS`](vcs-confirm-broad-jj-operations.md). Treat broad jj operations
  as confirmation-worthy. Commands that abandon, rebase, squash, split, restore, publish, or affect
  many revisions can rewrite a large part of the graph. Helps: Reduces accidental history reshaping
  and publication mistakes.
- [`VCS-CONFIRM-GITHUB-REMOTE-TOPOLOGY`](vcs-confirm-github-remote-topology.md). Confirm GitHub
  `origin` and `upstream` topology before publication. Forks and GitHub defaults can make `origin`
  mean the user fork while `upstream` means the canonical repo, or vice versa in owned repos. Helps:
  Keeps push remote, PR head, PR base, and tracked bookmarks aligned.
- [`VCS-CREATE-OPERATION-LOG-POINT-BEFORE-RESHAPING`](vcs-create-operation-log-point-before-reshaping.md).
  Use harmless jj inspection to create an operation-log point before risky reshaping. JJ can recover
  through the operation log, but recovery is easier when there is a recent known point before a
  risky stack reshape. Helps: Makes recovery from a bad reshape faster and easier to explain.
- [`VCS-DO-NOT-FALL-BACK-TO-GIT-FOR-JJ-ISSUES`](vcs-do-not-fall-back-to-git-for-jj-issues.md). Do
  not switch to Git because a jj command hits a transient lock or sandbox issue. In a jj repo, Git
  does not represent the full working-copy and change graph semantics. Helps: Keeps jj as the source
  of truth and avoids mixed-tool corruption or confusion.
- [`VCS-DRY-RUN-SURPRISING-PUBLICATION`](vcs-dry-run-surprising-publication.md). Use dry-run for
  surprising or ambiguous remote publication, not routine latency. Dry-run is most valuable when
  publication would be surprising: ambiguous remote, new bookmark, force-like update, fork topology,
  or unclear PR base. Helps: Applies extra verification where publication risk is real.
- [`VCS-DUPLICATE-FOR-ALTERNATIVE-CANDIDATES`](vcs-duplicate-for-alternative-candidates.md). Use `jj
  duplicate` for safe alternative candidates. When comparing two possible fixes or refactor shapes,
  mutating the only candidate makes it hard to return to the original. Helps: Makes experiments
  reversible and keeps competing designs reviewable.
- [`VCS-INSPECT-SPARSE-STATE`](vcs-inspect-sparse-state.md). Inspect sparse state before treating a
  missing path as missing history. In sparse checkouts, a missing file may be outside the sparse
  patterns rather than deleted from history. Helps: Prevents false conclusions about repository
  contents in sparse workspaces.
- [`VCS-INSPECT-STATE-BEFORE-MUTATING`](vcs-inspect-state-before-mutating.md). Inspect working-copy
  and stack state before mutating. Before creating, squashing, rebasing, publishing, or editing
  files, the agent needs to know the current working copy, parent, bookmarks, conflicts, and unowned
  changes. Helps: Keeps changes scoped and avoids surprises from hidden graph or working-copy state.
- [`VCS-JJ-AS-SOURCE-OF-TRUTH`](vcs-jj-as-source-of-truth.md). Use `jj` as the source of truth in
  `.jj` repositories. A `.jj` repo has jj changes, operation log, working-copy state, and bookmarks
  layered over Git storage. Helps: Prevents Git commands from bypassing jj semantics and confusing
  the change graph.
- [`VCS-JJ-NEW-FOR-REVIEW-LANES`](vcs-jj-new-for-review-lanes.md). Use `jj new` for separate review
  lanes. A new task needs a separate review lane before unrelated edits accumulate. Helps: Keeps
  review units atomic and prevents unrelated work from piling into one change.
- [`VCS-MAKE-GITHUB-HANDOFF-EXPLICIT`](vcs-make-github-handoff-explicit.md). Make GitHub handoff
  explicit after jj state is coherent. JJ state and GitHub state are related but not identical.
  Helps: Makes PR publication reproducible and avoids confusing branch or fork inference.
- [`VCS-MATCH-JJ-TOPOLOGY-TO-REPO-ROLE`](vcs-match-jj-topology-to-repo-role.md). Match jj remote
  topology to the repository role. Owned repos, maintainer-access repos, and fork-only contributor
  repos need different remote and bookmark topology. Helps: Keeps local jj aliases and publication
  behavior aligned with the actual collaboration model.
- [`VCS-NAME-EXACT-JJ-MUTATION-TARGETS`](vcs-name-exact-jj-mutation-targets.md). Name exact targets
  for mutating jj commands. Mutating commands that rely on defaults can target the wrong revision,
  fileset, bookmark, or destination when the stack is not what the agent assumes. Helps: Reduces
  accidental rewrites and makes command effects easier to audit.
- [`VCS-QUOTE-REVSETS-AND-SHELL-SYNTAX`](vcs-quote-revsets-and-shell-syntax.md). Quote revsets and
  shell-sensitive syntax. Revsets and bookmark syntax often contain characters such as `@`, `|`,
  `&`, `~`, parentheses, or spaces that shells can interpret. Helps: Prevents shell parsing bugs in
  jj examples, scripts, and agent commands.
- [`VCS-RECOVER-WITH-OPERATION-LOG`](vcs-recover-with-operation-log.md). Use operation-log recovery
  instead of destructive cleanup. JJ records repository operations so many mistakes are recoverable
  without destructive Git reset or stash habits. Helps: Makes recovery safer and avoids destroying
  unrelated local work.
- [`VCS-REPAIR-REMOTE-TOPOLOGY-COHERENTLY`](vcs-repair-remote-topology-coherently.md). Repair remote
  topology coherently. Remote topology has several coupled pieces: fetch remote, push remote,
  tracked bookmark, trunk alias, PR base, and PR head. Helps: Keeps jj, GitHub, and local aliases
  consistent after topology drift.
- [`VCS-RUN-JJ-MUTATIONS-SEQUENTIALLY`](vcs-run-jj-mutations-sequentially.md). Run jj mutations
  sequentially. JJ mutating commands update working-copy and operation state. Helps: Keeps
  source-control state coherent and avoids avoidable lock contention.
- [`VCS-SCOPE-JJ-FILE-TRACKING`](vcs-scope-jj-file-tracking.md). Scope jj file track and untrack
  commands to intended paths. `jj file track` and `jj file untrack` can affect more files than
  intended if paths are omitted or globbed too broadly. Helps: Prevents accidental publication or
  removal of local-only and unrelated files.
- [`VCS-STOP-REPEATED-JJ-RETRIES-AND-LOCALIZE-STATE`](vcs-stop-repeated-jj-retries-and-localize-state.md).
  Stop repeated jj retries and localize state. Repeating a failing jj command without new
  information usually compounds confusion. Helps: Turns source-control failures into diagnosis
  instead of command spam.
- [`VCS-TRACK-REMOTES-EXPLICITLY`](vcs-track-remotes-explicitly.md). Track remotes explicitly when
  bookmark names exist on multiple remotes. When the same bookmark name exists on multiple remotes,
  implicit tracking can choose the wrong source or make publication ambiguous. Helps: Prevents
  fetch, rebase, and publication confusion in fork and upstream workflows.
- [`VCS-TREAT-BOOKMARK-REMOTE-SYNTAX-AS-VERSION-SENSITIVE`](vcs-treat-bookmark-remote-syntax-as-version-sensitive.md).
  Treat `bookmark@remote` command syntax as version-sensitive. JJ command syntax around
  `bookmark@remote` and remote bookmark handling can vary by version and command. Helps: Keeps jj
  guidance accurate across version differences and reduces command-shape failures.
- [`VCS-USE-EVOLOG-AND-OPERATION-LOG`](vcs-use-evolog-and-operation-log.md). Use `jj evolog` for one
  change's evolution and `jj op log` for repository operations. `jj evolog` answers how one change
  evolved; `jj op log` answers how the repository state changed. Helps: Makes diagnosis faster by
  choosing the log that matches the question.
- [`VCS-USE-GIT-FORMATTED-DIFFS-FOR-AGENTS`](vcs-use-git-formatted-diffs-for-agents.md). Prefer
  Git-formatted diffs when agents need to interpret patch text. Many agents and review tools
  understand Git patch format better than native jj summaries. Helps: Makes diffs easier for agents
  and humans to inspect, quote, and apply.
- [`VCS-USE-IGNORE-WORKING-COPY-CAREFULLY`](vcs-use-ignore-working-copy-carefully.md). Use
  `--ignore-working-copy` only for lock-safe inspection or intended metadata updates.
  `--ignore-working-copy` can be useful when the working copy is locked or when only metadata is
  needed, but it also means jj may not snapshot current file changes before answering. Helps: Avoids
  stale reads and accidental metadata changes during lock recovery.
- [`VCS-WORKSPACE-ADD-FOR-SECOND-CHECKOUTS`](vcs-workspace-add-for-second-checkouts.md). Use `jj
  workspace add` only when a second filesystem checkout is needed. `jj new` creates another change
  in the current checkout; `jj workspace add` creates another filesystem checkout. Helps: Avoids
  unnecessary checkout proliferation while preserving isolation when filesystem state matters.
