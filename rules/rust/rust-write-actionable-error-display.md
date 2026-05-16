# Rust Write Actionable Error Display

## Metadata

- Name: `Write Actionable Error Display`
- ID: `RUST-WRITE-ACTIONABLE-ERROR-DISPLAY`
- Summary: Write `Display` messages that tell humans what failed and what useful next action or
  context exists. Keep structured state in error fields, sources, diagnostics, or `Debug` instead of
  dumping internals into the user-facing string.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, errors, failure-output, observability`
- Related: `write-actionable-error-messages, rust-preserve-error-context`

## Rule

Write human-oriented and actionable error `Display` output.

## Why

`Display` is often what users, CLIs, logs, and support messages show. It should say what failed and
what the caller can do next without dumping debug internals or hiding the operation that failed.

## Helps

Helps users and agents fix failures from the message they actually see in CLI output, logs, test
diffs, and error reports.

## Limits

Keep `Display` concise and human-facing. Put structured fields on the error type and detailed
developer state in `Debug`, sources, or diagnostics.

## Agent Instruction

Write human-oriented and actionable error `Display` output because `Display` is often what users, CLIs,
logs, and support messages show.

## Mechanisms

Write `Display` messages that name the failed operation, relevant input, expected shape, and next
action. Preserve source errors instead of flattening them into strings.

## References

- [Rust API Guidelines: errors implement standard
  traits](https://rust-lang.github.io/api-guidelines/interoperability.html#c-good-err)
- [Rust API Guidelines: error messages are lowercase without trailing
  punctuation](https://rust-lang.github.io/api-guidelines/interoperability.html#c-good-err)
