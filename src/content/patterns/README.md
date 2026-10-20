# Patterns

Patterns are small, named guidance units. Each pattern should be useful on its own in a review
comment, guide link, or coding-agent instruction.

Use `templates/pattern.md` for new entries.

## Seed Patterns

| ID                                             | Name                                         | Status   |
| ---------------------------------------------- | -------------------------------------------- | -------- |
| `avoid-boolean-flag-parameters`                | Avoid boolean flag parameters                | reviewed |
| `avoid-secret-or-private-log-context`          | Avoid secret or private log context          | reviewed |
| `ask-what-were-you-trying-to-achieve`          | Ask what were you trying to achieve          | reviewed |
| `bootstrap-repo-docs`                          | Bootstrap repo docs                          | reviewed |
| `budget-tokens-for-feedback-loops`             | Budget tokens for feedback loops             | reviewed |
| `cap-change-radius`                            | Cap change radius                            | reviewed |
| `characterize-then-fix`                        | Characterize then fix                        | draft    |
| `choose-doc-pass-depth`                        | Choose doc pass depth                        | reviewed |
| `choose-doc-type`                              | Choose doc type                              | reviewed |
| `choose-good-enough-tools`                     | Choose good enough tools                     | reviewed |
| `close-the-agent-loop`                         | Close the agent loop                         | reviewed |
| `chunk-statements`                             | Chunk statements                             | reviewed |
| `code-is-memory-of-process`                    | Code is memory of process                    | reviewed |
| `commit-messages-for-history`                  | Commit messages for history                  | reviewed |
| `contain-observability-policy`                 | Contain observability policy                 | reviewed |
| `define-good-before-judgment-heavy-work`       | Define good before judgment-heavy work       | reviewed |
| `delete-redundant-comments`                    | Delete redundant comments                    | reviewed |
| `deliver-context-just-in-time`                 | Deliver context just in time                 | reviewed |
| `distill-from-blessed-artifacts`               | Distill from blessed artifacts               | reviewed |
| `document-errors-panics-safety`                | Document errors panics safety                | reviewed |
| `document-intentional-non-goals`               | Document intentional non goals               | reviewed |
| `document-system-mental-models`                | Document system mental models                | reviewed |
| `encode-nonfunctional-requirements`            | Encode nonfunctional requirements            | reviewed |
| `follow-local-conventions`                     | Follow local conventions                     | reviewed |
| `garbage-collect-agent-drift`                  | Garbage collect agent drift                  | reviewed |
| `give-agents-objectives-with-boundaries`       | Give agents objectives with boundaries       | reviewed |
| `grant-scoped-agent-capabilities`              | Grant scoped agent capabilities              | reviewed |
| `isolate-agent-workspaces`                     | Isolate agent workspaces                     | reviewed |
| `inject-time-and-randomness`                   | Inject time and randomness                   | reviewed |
| `keep-async-boundaries-explicit`               | Keep async boundaries explicit               | reviewed |
| `keep-automations-repo-owned`                  | Keep automations repo owned                  | reviewed |
| `keep-docs-near-their-subject`                 | Keep docs near their subject                 | reviewed |
| `keep-name-current`                            | Keep name current                            | reviewed |
| `keep-public-dependencies-intentional`         | Keep public dependencies intentional         | reviewed |
| `keep-secrets-out-of-context`                  | Keep secrets out of context                  | reviewed |
| `keep-structure-reversible`                    | Keep structure reversible                    | reviewed |
| `label-doc-claims-by-evidence`                 | Label doc claims by evidence                 | reviewed |
| `limit-live-context`                           | Limit live context                           | reviewed |
| `log-at-owned-boundaries`                      | Log at owned boundaries                      | reviewed |
| `make-bad-output-mechanically-hard`            | Make bad output mechanically hard            | reviewed |
| `make-failures-observable`                     | Make failures observable                     | reviewed |
| `make-invalid-states-hard-to-express`          | Make invalid states hard to express          | reviewed |
| `make-parameters-explicit`                     | Make parameters explicit                     | reviewed |
| `make-plans-versioned-artifacts`               | Make plans versioned artifacts               | reviewed |
| `make-runtime-state-agent-legible`             | Make runtime state agent legible             | reviewed |
| `make-side-effects-visible`                    | Make side effects visible                    | reviewed |
| `make-state-transitions-explicit`              | Make state transitions explicit              | reviewed |
| `make-the-change-easy-first`                   | Make the change easy first                   | reviewed |
| `make-validation-policy-explicit`              | Make validation policy explicit              | reviewed |
| `manage-agent-work-not-sessions`               | Manage agent work not sessions               | reviewed |
| `move-declaration-and-initialization-together` | Move declaration and initialization together | reviewed |
| `name-coupling`                                | Name coupling                                | reviewed |
| `optimize-for-long-term-coherence`             | Optimize for long term coherence             | reviewed |
| `optimize-for-agent-legibility`                | Optimize for agent legibility                | reviewed |
| `parse-dont-validate`                          | Parse dont validate                          | reviewed |
| `practice-agent-workouts`                      | Practice agent workouts                      | reviewed |
| `prefer-100-column-prose-wrap`                 | Prefer 100-column prose wrap                 | draft    |
| `prefer-durable-summaries`                     | Prefer durable summaries                     | reviewed |
| `prefer-in-distribution-tools`                 | Prefer in distribution tools                 | reviewed |
| `prefer-standard-conversions`                  | Prefer standard conversions                  | reviewed |
| `prefer-tools-over-prompts`                    | Prefer tools over prompts                    | reviewed |
| `preserve-agent-context-coherence`             | Preserve agent context coherence             | reviewed |
| `preserve-error-context`                       | Preserve error context                       | reviewed |
| `preserve-intent-over-literalism`              | Preserve intent over literalism              | reviewed |
| `preserve-local-doc-voice`                     | Preserve local doc voice                     | reviewed |
| `preserve-unowned-work`                        | Preserve unowned work                        | reviewed |
| `produce-review-packets`                       | Produce review packets                       | reviewed |
| `prove-security-impact`                        | Prove security impact                        | reviewed |
| `reader-locality`                              | Reader locality                              | reviewed |
| `reconstruct-rationale-before-writing`         | Reconstruct rationale before writing         | reviewed |
| `record-agent-operating-lessons`               | Record agent operating lessons               | reviewed |
| `report-verification-honestly`                 | Report verification honestly                 | reviewed |
| `remediate-doc-drift`                          | Remediate doc drift                          | reviewed |
| `return-structured-errors`                     | Return structured errors                     | reviewed |
| `review-proof-not-just-code`                   | Review proof not just code                   | reviewed |
| `run-rustdoc-quality-pass`                     | Run rustdoc quality pass                     | reviewed |
| `run-source-explanation-pass`                  | Run source explanation pass                  | reviewed |
| `separate-discovery-from-editing`              | Separate discovery from editing              | reviewed |
| `separate-structure-from-behavior`             | Separate structure from behavior             | reviewed |
| `shape-tool-output-for-agents`                 | Shape tool output for agents                 | reviewed |
| `small-reviewable-chunks`                      | Small reviewable chunks                      | reviewed |
| `smallest-trustworthy-verification`            | Smallest trustworthy verification            | reviewed |
| `spend-human-attention-on-ambiguity`           | Spend human attention on ambiguity           | reviewed |
| `strengthen-cohesion`                          | Strengthen cohesion                          | reviewed |
| `test-observable-behavior`                     | Test observable behavior                     | reviewed |
| `teach-agents-through-tools`                   | Teach agents through tools                   | reviewed |
| `turn-feedback-into-guidance`                  | Turn feedback into guidance                  | reviewed |
| `untangle-before-changing`                     | Untangle before changing                     | reviewed |
| `use-agents-md-as-map`                         | Use AGENTS.md as map                         | reviewed |
| `use-disk-as-context-sink`                     | Use disk as context sink                     | reviewed |
| `use-explaining-variable`                      | Use explaining variable                      | reviewed |
| `use-guard-clause`                             | Use guard clause                             | reviewed |
| `use-narrow-agent-reviewers`                   | Use narrow agent reviewers                   | reviewed |
| `verify-with-canaries-before-cutover`          | Verify with canaries before cutover          | reviewed |
| `write-actionable-error-messages`              | Write actionable error messages              | reviewed |
| `write-docs-as-contracts`                      | Write docs as contracts                      | reviewed |
| `write-pr-narrative`                           | Write PR narrative                           | reviewed |
