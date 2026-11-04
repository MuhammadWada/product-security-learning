# Phase 1 — Python and Software Foundations

**Months**: 1-3 | **Est. hours**: 130-155 | **Status**: In progress
**Security integration**: Secure coding basics (input validation, secure file handling, failing safely), introductory threat modeling

## Objective

Become independently capable of writing, debugging, testing, and organizing small software applications. Python only; no second language until programming itself is understood.

## Outline

| Month | Focus | Practical assignment |
|---|---|---|
| 1 | Programming fundamentals: types, conditionals, loops, functions, lists/dicts/tuples/sets | Sensor Telemetry Analyzer (CSV stats, thresholds, data quality) |
| 2 | Software construction: modules, classes, file/JSON/CSV handling, unit tests, logging | Telemetry Processing Application v2 (modular, persistent, tested) |
| 3 | Professional practice: Git branches/PRs, type hints, linting, formatting, documentation, a release | Documented, tested, version-controlled release; CLI password manager |

## Projects

- [01-telemetry-analyzer](01-telemetry-analyzer/) — started as the Week 1 Simple Log Parser; its ingest/parse/validate pipeline now feeds the Sensor Telemetry Analyzer.

## Resources

Harvard CS50P, Official Python Tutorial, pytest docs, Pro Git, Automate the Boring Stuff with Python (existing).

## Acceptance criteria

- Write a Python application without following a tutorial.
- Break a problem into functions and modules.
- Work with common data structures.
- Handle invalid inputs and runtime errors.
- Write and run unit tests.
- Use Git branches and commits.
- Explain the application architecture.

**Gate**: build a new small application from a written problem statement in 6-8 hours, including tests and documentation, without a step-by-step tutorial.
