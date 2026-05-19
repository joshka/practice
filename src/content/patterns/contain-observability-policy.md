# Contain Observability Policy

## Metadata

- Name: `Contain Observability Policy`
- ID: `contain-observability-policy`
- Summary: Logging, metrics, tracing, and privacy choices become inconsistent when every call site
  invents its own policy. Put observability decisions at owned boundaries so lower layers expose
  facts without duplicating policy.
- Status: `reviewed`
- Audience: `both`
- Topics: `observability, architecture, rust`
- Tags: `observability, security-privacy, side-effects, ownership`
- Related: `make-failures-observable, make-side-effects-visible`

## Problem

Logging, metrics, tracing, sampling, redaction, severity, and correlation rules become hard to
change when every helper invents its own observability policy. The code may emit many signals, but
the signals are inconsistent and difficult to interpret together.

## Preferred Move

Keep observability policy at owned boundaries: request handlers, job runners, CLI commands,
workflow steps, persistence adapters, or domain services that own an operation. Lower helpers should
return structured errors or events; the boundary decides how to log, count, trace, redact, or sample
them.

## Tradeoff

Some low-level code owns a real boundary, such as a database adapter or protocol parser. It can emit
signals when it owns the operation being observed. Do not force all observability upward if doing so
would lose the only useful context.

## Agent Instruction

When adding logs, metrics, or spans, identify the boundary that owns the operation. Put policy there
and keep lower helpers focused on structured return values unless the helper owns an external
boundary.

## Examples

Bad: a parser decides severity, wording, and metrics policy for an import workflow.

```rust
fn parse_record(row: CsvRow) -> Result<Record, ParseError> {
    if row.id().is_empty() {
        warn!("import row skipped: missing id");
        metrics::increment!("import.row.skipped");
        return Err(ParseError::MissingId);
    }

    Ok(Record::from(row))
}
```

Good: the parser returns meaning, and the import boundary owns observability policy.

```rust
fn parse_record(row: CsvRow) -> Result<Record, ParseError> {
    if row.id().is_empty() {
        return Err(ParseError::MissingId);
    }

    Ok(Record::from(row))
}

fn import_row(row: CsvRow, batch_id: BatchId) -> Result<(), ImportError> {
    let record = parse_record(row).map_err(|source| {
        warn!(%batch_id, error = %source, "import row rejected");
        metrics::increment!("import.row.rejected");
        ImportError::Rejected { batch_id, source }
    })?;

    save(record).map_err(|source| ImportError::Store { batch_id, source })
}
```

## References

| Source                           | Use      | Note                                                     |
| -------------------------------- | -------- | -------------------------------------------------------- |
| [OpenTelemetry concepts][otel]   | `adapts` | Signals should be modeled consistently across telemetry. |
| [OpenTelemetry log model][logs]  | `adapts` | Log records have structured fields and severity.         |

[logs]: https://opentelemetry.io/docs/specs/otel/logs/data-model/
[otel]: https://opentelemetry.io/docs/concepts/semantic-conventions/
