# Telemetry Analyzer

**Phase 1, Months 1-3** | **Status**: In progress

## Problem statement

Read telemetry and log data from files, parse and validate it, and report useful summaries. The project began as the Week 1 Simple Log Parser; its ingest, parse, and validate pipeline is now the first stage of the Sensor Telemetry Analyzer, and the data source expands from a text log to CSV sensor data.

## Current state

- Design spec for the original log parser: [designSpec_LogParser.md](designSpec_LogParser.md)
- Working building blocks in [sample_file_open.py](sample_file_open.py): safe file opening, EOF-safe `readline()` loop, keyword matching with a match counter. Verified against the `foo` test file.
- Original week-level write-up: [README_Week_1.md](README_Week_1.md) (the "What I Learned" section is still unfilled).
- Session notes are in [notes/](notes/).
- Sample data: Windows System Event Log exports in `data/` (local only, gitignored because they contain machine and user identifiers). Use a sanitized sample if a public test file is needed.

## Next steps

1. Run the keyword search against the Windows Event Log export (multi-line records will stress the line-by-line approach).
2. Read CSV sensor data and compute minimum, maximum, average, and standard deviation.
3. Add threshold detection and data-quality metrics.
4. Handle malformed and missing data without crashing.
5. Write automated tests (pytest) and a `docs/` folder per [../../../docs/project-template.md](../../../docs/project-template.md).

## Security extension

Input validation and secure file handling: no assumptions about file contents, fail safely on bad input, clear boundaries between input, processing, and output.

## Known limitation

Keyword search is case-sensitive (`str.find()`); deferred on purpose.

## Scoring

Scored against [../../../docs/rubric.md](../../../docs/rubric.md) before advancing. Not yet scored.
