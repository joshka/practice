# Log At Owned Boundaries

## Metadata

- Name: `Log At Owned Boundaries`
- ID: `log-at-owned-boundaries`
- Summary: Logs become noisy and inconsistent when every helper records the same failure from a
  partial viewpoint. Log where the code owns the operation and can attach useful, safe diagnostic
  context.
- Status: `reviewed`
- Audience: `both`
- Topics: `logging, observability, rust`
- Tags: `observability, ownership, boundary-correctness, side-effects`
- Related: `contain-observability-policy, preserve-error-context`

## Problem

Logs become noisy and misleading when every layer logs the same failure. A helper that lacks request,
job, user, retry, or resource context often emits a vague message, and the owning boundary emits
another one later. Operators then see duplicate events without a clear source of truth.

## Preferred Move

Log at the boundary that owns the operation and has the context needed to make the event useful.
Lower layers should return typed errors with enough context for that boundary to log once. Include
stable correlation fields and avoid prose-only messages for operationally important events.

## Tradeoff

Low-level components can log when they own an independent operation, such as connection-pool
maintenance, background compaction, or protocol negotiation. The rule is ownership, not file-system
depth.

## Agent Instruction

Before adding a log, ask which boundary owns the operation and whether another layer will log the
same failure. Prefer one useful log with correlation fields over repeated logs from helpers.

## Examples

Bad: the helper logs without the job context that explains the failure.

```rust
fn write_snapshot(snapshot: Snapshot) -> Result<(), StoreError> {
    fs::write(snapshot.path(), snapshot.bytes()).map_err(|source| {
        error!("failed to write snapshot");
        StoreError::Write { source }
    })
}
```

Good: the helper returns context, and the job boundary logs once with owned fields.

```rust
fn write_snapshot(snapshot: Snapshot) -> Result<(), StoreError> {
    fs::write(snapshot.path(), snapshot.bytes()).map_err(|source| StoreError::Write {
        path: snapshot.path().to_owned(),
        source,
    })
}

fn run_snapshot_job(job_id: JobId, snapshot: Snapshot) -> Result<(), JobError> {
    write_snapshot(snapshot).map_err(|source| {
        error!(%job_id, error = %source, "snapshot job failed");
        JobError::Snapshot { job_id, source }
    })
}
```

## References

| Source                      | Use      | Note                                                    |
| --------------------------- | -------- | ------------------------------------------------------- |
| [OWASP logging][owasp]      | `adapts` | Logs should support investigation without excess noise. |
| [OpenTelemetry logs][logs]  | `adapts` | Structured log records support consistent correlation.  |

[logs]: https://opentelemetry.io/docs/specs/otel/logs/data-model/
[owasp]: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
