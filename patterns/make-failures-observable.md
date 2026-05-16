# Make Failures Observable

## Metadata

- Name: `Make Failures Observable`
- ID: `make-failures-observable`
- Summary: Errors without diagnostic context force future readers and operators to rediscover what
  failed. Preserve typed errors while adding operation context, correlation, metrics, or logs at the
  boundary that owns the meaning.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, errors, observability`
- Related: `preserve-error-context, write-actionable-error-messages`

## Problem

A failure that returns an error but leaves no useful diagnostic trail pushes the next maintainer,
operator, or caller into rediscovery. They may know that work failed, but not which operation failed,
which boundary was involved, what input class was affected, or how to correlate the failure with
logs, traces, metrics, or support reports.

## Preferred Move

Make important failures observable at the boundary that can add meaning. Preserve the typed error
for callers, and add operation context, correlation identifiers, span fields, metrics, or logs where
that boundary owns enough information to make the failure diagnosable.

## Tradeoff

Do not log every propagated error at every layer. Repeated logging creates noise and can leak private
context. Add observability where the code owns the operation, not where it merely forwards a result.

## Agent Instruction

When adding or changing a failure path, identify who needs to diagnose it and where the owning
boundary is. Preserve the error for callers and add observability only where the boundary can attach
useful operation context.

## Examples

Bad: the boundary drops the operation context and leaves callers with a generic failure.

```rust
pub fn refresh_catalog(store: &Store) -> Result<(), RefreshError> {
    store.write_snapshot()?;
    Ok(())
}
```

Good: the boundary preserves the source error and attaches the operation identity once.

```rust
pub fn refresh_catalog(store: &Store, catalog_id: CatalogId) -> Result<(), RefreshError> {
    store
        .write_snapshot(catalog_id)
        .map_err(|source| RefreshError::SnapshotWrite { catalog_id, source })?;

    metrics::increment!("catalog.refresh.snapshot_written");
    Ok(())
}
```

## References

| Source                             | Use        | Note                                                   |
| ---------------------------------- | ---------- | ------------------------------------------------------ |
| [C-FAILURE][rustdoc-failure]       | `supports` | Public docs should describe failure conditions.        |
| [OpenTelemetry errors][otel-error] | `adapts`   | Error signals should use consistent operation context. |

[otel-error]: https://opentelemetry.io/docs/specs/semconv/general/recording-errors/
[rustdoc-failure]: https://rust-lang.github.io/api-guidelines/documentation.html#c-failure
