# Patterns

Patterns are small, named guidance units. Each pattern should be useful on its own in a review
comment, guide link, or coding-agent instruction.

Use `templates/pattern.md` for new entries.

## Seed Patterns

| ID                                             | Name                                         | Status   |
| ---------------------------------------------- | -------------------------------------------- | -------- |
| `avoid-boolean-flag-parameters`                | Avoid Boolean Flag Parameters                | reviewed |
| `avoid-secret-or-private-log-context`          | Avoid Secret Or Private Log Context          | reviewed |
| `ask-what-were-you-trying-to-achieve`          | Ask What Were You Trying To Achieve          | reviewed |
| `bootstrap-repo-docs`                          | Bootstrap Repo Docs                          | reviewed |
| `budget-tokens-for-feedback-loops`             | Budget Tokens For Feedback Loops             | reviewed |
| `cap-change-radius`                            | Cap Change Radius                            | reviewed |
| `choose-doc-pass-depth`                        | Choose Doc Pass Depth                        | reviewed |
| `choose-doc-type`                              | Choose Doc Type                              | reviewed |
| `choose-good-enough-tools`                     | Choose Good Enough Tools                     | reviewed |
| `close-the-agent-loop`                         | Close The Agent Loop                         | reviewed |
| `chunk-statements`                             | Chunk Statements                             | reviewed |
| `code-is-memory-of-process`                    | Code Is Memory Of Process                    | reviewed |
| `commit-messages-for-history`                  | Commit Messages For History                  | reviewed |
| `contain-observability-policy`                 | Contain Observability Policy                 | reviewed |
| `define-good-before-judgment-heavy-work`       | Define Good Before Judgment-Heavy Work       | reviewed |
| `delete-redundant-comments`                    | Delete Redundant Comments                    | reviewed |
| `deliver-context-just-in-time`                 | Deliver Context Just In Time                 | reviewed |
| `distill-from-blessed-artifacts`               | Distill From Blessed Artifacts               | reviewed |
| `document-errors-panics-safety`                | Document Errors Panics Safety                | reviewed |
| `document-intentional-non-goals`               | Document Intentional Non Goals               | reviewed |
| `document-system-mental-models`                | Document System Mental Models                | reviewed |
| `encode-nonfunctional-requirements`            | Encode Nonfunctional Requirements            | reviewed |
| `follow-local-conventions`                     | Follow Local Conventions                     | reviewed |
| `garbage-collect-agent-drift`                  | Garbage Collect Agent Drift                  | reviewed |
| `give-agents-objectives-with-boundaries`       | Give Agents Objectives With Boundaries       | reviewed |
| `grant-scoped-agent-capabilities`              | Grant Scoped Agent Capabilities              | reviewed |
| `isolate-agent-workspaces`                     | Isolate Agent Workspaces                     | reviewed |
| `inject-time-and-randomness`                   | Inject Time And Randomness                   | reviewed |
| `keep-async-boundaries-explicit`               | Keep Async Boundaries Explicit               | reviewed |
| `keep-automations-repo-owned`                  | Keep Automations Repo Owned                  | reviewed |
| `keep-docs-near-their-subject`                 | Keep Docs Near Their Subject                 | reviewed |
| `keep-name-current`                            | Keep Name Current                            | reviewed |
| `keep-public-dependencies-intentional`         | Keep Public Dependencies Intentional         | reviewed |
| `keep-secrets-out-of-context`                  | Keep Secrets Out Of Context                  | reviewed |
| `keep-structure-reversible`                    | Keep Structure Reversible                    | reviewed |
| `label-doc-claims-by-evidence`                 | Label Doc Claims By Evidence                 | reviewed |
| `limit-live-context`                           | Limit Live Context                           | reviewed |
| `log-at-owned-boundaries`                      | Log At Owned Boundaries                      | reviewed |
| `make-bad-output-mechanically-hard`            | Make Bad Output Mechanically Hard            | reviewed |
| `make-failures-observable`                     | Make Failures Observable                     | reviewed |
| `make-invalid-states-hard-to-express`          | Make Invalid States Hard To Express          | reviewed |
| `make-parameters-explicit`                     | Make Parameters Explicit                     | reviewed |
| `make-plans-versioned-artifacts`               | Make Plans Versioned Artifacts               | reviewed |
| `make-runtime-state-agent-legible`             | Make Runtime State Agent Legible             | reviewed |
| `make-side-effects-visible`                    | Make Side Effects Visible                    | reviewed |
| `make-state-transitions-explicit`              | Make State Transitions Explicit              | reviewed |
| `make-the-change-easy-first`                   | Make The Change Easy First                   | reviewed |
| `make-validation-policy-explicit`              | Make Validation Policy Explicit              | reviewed |
| `manage-agent-work-not-sessions`               | Manage Agent Work Not Sessions               | reviewed |
| `move-declaration-and-initialization-together` | Move Declaration And Initialization Together | reviewed |
| `name-coupling`                                | Name Coupling                                | reviewed |
| `optimize-for-long-term-coherence`             | Optimize For Long Term Coherence             | reviewed |
| `optimize-for-agent-legibility`                | Optimize For Agent Legibility                | reviewed |
| `parse-dont-validate`                          | Parse Dont Validate                          | reviewed |
| `practice-agent-workouts`                      | Practice Agent Workouts                      | reviewed |
| `prefer-100-column-prose-wrap`                 | Prefer 100-Column Prose Wrap                 | draft    |
| `prefer-durable-summaries`                     | Prefer Durable Summaries                     | reviewed |
| `prefer-in-distribution-tools`                 | Prefer In Distribution Tools                 | reviewed |
| `prefer-standard-conversions`                  | Prefer Standard Conversions                  | reviewed |
| `prefer-tools-over-prompts`                    | Prefer Tools Over Prompts                    | reviewed |
| `preserve-agent-context-coherence`             | Preserve Agent Context Coherence             | reviewed |
| `preserve-error-context`                       | Preserve Error Context                       | reviewed |
| `preserve-intent-over-literalism`              | Preserve Intent Over Literalism              | reviewed |
| `preserve-local-doc-voice`                     | Preserve Local Doc Voice                     | reviewed |
| `preserve-unowned-work`                        | Preserve Unowned Work                        | reviewed |
| `produce-review-packets`                       | Produce Review Packets                       | reviewed |
| `prove-security-impact`                        | Prove Security Impact                        | reviewed |
| `reader-locality`                              | Reader Locality                              | reviewed |
| `record-agent-operating-lessons`               | Record Agent Operating Lessons               | reviewed |
| `report-verification-honestly`                 | Report Verification Honestly                 | reviewed |
| `remediate-doc-drift`                          | Remediate Doc Drift                          | reviewed |
| `return-structured-errors`                     | Return Structured Errors                     | reviewed |
| `review-proof-not-just-code`                   | Review Proof Not Just Code                   | reviewed |
| `separate-discovery-from-editing`              | Separate Discovery From Editing              | reviewed |
| `separate-structure-from-behavior`             | Separate Structure From Behavior             | reviewed |
| `shape-tool-output-for-agents`                 | Shape Tool Output For Agents                 | reviewed |
| `small-reviewable-chunks`                      | Small Reviewable Chunks                      | reviewed |
| `smallest-trustworthy-verification`            | Smallest Trustworthy Verification            | reviewed |
| `spend-human-attention-on-ambiguity`           | Spend Human Attention On Ambiguity           | reviewed |
| `strengthen-cohesion`                          | Strengthen Cohesion                          | reviewed |
| `test-observable-behavior`                     | Test Observable Behavior                     | reviewed |
| `teach-agents-through-tools`                   | Teach Agents Through Tools                   | reviewed |
| `turn-feedback-into-guidance`                  | Turn Feedback Into Guidance                  | reviewed |
| `untangle-before-changing`                     | Untangle Before Changing                     | reviewed |
| `use-agents-md-as-map`                         | Use AGENTS.md As Map                         | reviewed |
| `use-disk-as-context-sink`                     | Use Disk As Context Sink                     | reviewed |
| `use-explaining-variable`                      | Use Explaining Variable                      | reviewed |
| `use-guard-clause`                             | Use Guard Clause                             | reviewed |
| `use-narrow-agent-reviewers`                   | Use Narrow Agent Reviewers                   | reviewed |
| `verify-with-canaries-before-cutover`          | Verify With Canaries Before Cutover          | reviewed |
| `write-actionable-error-messages`              | Write Actionable Error Messages              | reviewed |
| `write-docs-as-contracts`                      | Write Docs As Contracts                      | reviewed |
| `write-pr-narrative`                           | Write PR Narrative                           | reviewed |
