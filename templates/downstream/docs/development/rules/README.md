# Reviewed Rule Domains

These generated files contain every reviewed rule from the `development-preferences` repo,
which is the canonical source for this shared rule set. Keep them synchronized from that
repo instead of editing copied rule text by hand.

Use the domain file that matches the current task. Load more than one domain when work crosses
boundaries such as Rust API changes, tests, docs, performance, and source control.

## Domains

- [Agent Workflow](agent-workflow.md): 25 rules.
- [Explicit Boundaries Preserve Correctness](boundary.md): 25 rules.
- [Change Shape](change-shape.md): 11 rules.
- [Docs Are Contracts](documentation.md): 25 rules.
- [Observability And Failure](observability.md): 5 rules.
- [Measure Before Optimizing](performance.md): 7 rules.
- [Local Reasoning And Refactoring](refactoring.md): 8 rules.
- [Private Context And Review Artifacts](review.md): 6 rules.
- [Rust API And Crate Shape](rust.md): 46 rules.
- [Source And Context Hygiene](source.md): 4 rules.
- [Tests Should Explain Failures](test-failures.md): 3 rules.
- [Testing And Verification](testing.md): 22 rules.
- [Jj Topology And Source Control](vcs.md): 28 rules.
