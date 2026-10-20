# Reviewed Rule Domains

These generated files contain every reviewed rule from the `joshka/practice` repo,
which is the canonical source for this shared rule set. Keep them synchronized from that
repo instead of editing copied rule text by hand.

Use the domain file that matches the current task. Load more than one domain when work crosses
boundaries such as Rust API changes, tests, docs, performance, and source control.

## Domains

- [Agent workflow](agent-workflow.md): 26 rules.
- [Explicit boundaries preserve correctness](boundary.md): 26 rules.
- [Change shape](change-shape.md): 13 rules.
- [Docs are contracts](documentation.md): 33 rules.
- [Observability and failure](observability.md): 5 rules.
- [Measure before optimizing](performance.md): 7 rules.
- [Local reasoning and refactoring](refactoring.md): 9 rules.
- [Private context and review artifacts](review.md): 11 rules.
- [Rust API and crate shape](rust.md): 90 rules.
- [Source and context hygiene](source.md): 4 rules.
- [Tests should explain failures](test-failures.md): 3 rules.
- [Testing and verification](testing.md): 22 rules.
- [JJ topology and source control](vcs.md): 28 rules.
