# Boundary Make Exec Tools Noninteractive

## Metadata

- ID: `BOUNDARY-MAKE-EXEC-TOOLS-NONINTERACTIVE`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Make exec-like tools noninteractive by default.

## Why

Exec-like tools called by agents, CI, or background tasks cannot safely wait for prompts, editors,
pagers, or credential UI. Noninteractive defaults make commands fail or complete predictably instead
of hanging in unattended workflows.

## Helps

- Prevents stuck jobs and makes tool execution reproducible in automation.

## Limits

Interactive modes are fine for explicit human commands. Keep them opt-in and separate from
automation defaults.

## Agent Instruction

Make exec-like tools noninteractive by default because exec-like tools called by agents, CI, or
background tasks cannot safely wait for prompts, editors, pagers, or credential UI.

## Mechanisms

Supported by `--no-pager`, `--yes` or dry-run flags, disabled editors, timeouts, stdin policy,
environment overrides, and tests for unattended execution.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
