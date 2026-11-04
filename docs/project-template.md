# Project Template

Every major project lives in its own directory (not one large shared codebase) and contains:

| Artifact | File |
|---|---|
| Problem statement | `README.md` |
| Functional and non-functional requirements | `docs/requirements.md` |
| Architecture diagram | `docs/architecture.md` |
| Design decisions (ADRs) | `docs/decisions/` |
| Source code | `src/` |
| Unit and integration tests | `tests/` |
| Threat model and security assessment | `docs/security.md` |
| Performance measurements | `docs/performance.md` |
| Build and run (and deploy, when applicable) instructions | `README.md` |
| Lessons learned | `docs/lessons-learned.md` |
| Rubric score | `SCORECARD.md` (see `rubric.md`) |
| Session notes | `notes/session-notes-YYYY-MM-DD.md` |

Early projects start with a subset (README, tests, security notes); the full set is expected from Phase 2 onward.

## Security extension

Each project names one security extension (for example input validation, secure storage, memory-safety analysis, or an authentication review) and documents it in `docs/security.md`.
