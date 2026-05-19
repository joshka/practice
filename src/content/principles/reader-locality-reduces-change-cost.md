# Reader Locality Reduces Change Cost

## Metadata

- Name: `Reader Locality Reduces Change Cost`
- ID: `reader-locality-reduces-change-cost`
- Summary: `Code is cheaper to change when the reader can understand the local decision without
  distant facts. Keep related state, inputs, side effects, and policy close enough to inspect
  together.`
- Status: `reviewed`
- Audience: `both`
- Topics: `code-shape, refactoring, cognition, maintainability`
- Tags: `reader-locality, change-shape, reviewability`
- Related: `change-shape-controls-review-cost`

## Claim

Code is cheaper to change when the reader can understand the local part without carrying unrelated
state, distant setup, hidden side effects, or scattered policy in their head.

## Why This Exists

Long functions and broad modules often make early state feel relevant to every later line. A reader
who wants to inspect one block must ask which variables, earlier calculations, guards, mutation,
feature flags, or implicit inputs still matter. As the live context grows, the number of possible
interactions grows faster than the line count.

Reader-local code reduces that search space. It puts declarations near use, names intermediate
concepts, groups coupled behavior, separates unrelated policy, and makes inputs explicit.

## Good Uses

- Move declaration and initialization together.
- Extract an explaining variable or small helper when it reduces live context.
- Use guard clauses to remove irrelevant branches from the main path.
- Group coupled code and move unrelated code away.
- Prefer explicit parameters over hidden ambient input.

## Bad Smells

- A later block depends on setup far above it.
- A variable exists for many lines before it has a meaningful value.
- A helper hides more context than it names.
- Reading one function requires jumping through several weak abstractions.
- State transitions are implied by scattered booleans or ad hoc mutation.

## Limits

Locality is not the same as making everything tiny. A helper is useful when its name and boundary
reduce what the reader must track. If extraction creates more jumps, more parameters, or weaker
names, putting code back in one place may be clearer.

## Agent Consequences

Optimize code shape for the smallest useful live context. Prefer moves that reduce distant facts,
hidden inputs, and scattered policy over moves that merely create more structure.
