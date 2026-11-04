# AI Usage Rules

The objective is to learn to engineer software with AI, not to delegate engineering judgment to AI.

## Five rules

1. Never accept code that I cannot explain.
2. Never accept a test suite as proof of correctness without examining what it actually tests.
3. Never deploy infrastructure I cannot independently audit.
4. Never allow an agent to make unreviewed architectural decisions.
5. Require agents to explain assumptions, tradeoffs, failure modes, and security implications.

## Agent and learner responsibilities by period

| Months | Agent responsibility | My responsibility |
|---|---|---|
| 1-3 | Explain concepts, generate exercises | Write the code |
| 4-6 | Review algorithms and implementations | Understand memory and correctness |
| 7-9 | Assist with debugging | Diagnose system behavior |
| 10-12 | Generate API and service scaffolding | Design interfaces and failure handling |
| 13-15 | Implement application components | Own architecture |
| 16-18 | Generate infrastructure and pipelines | Audit deployment and security |
| 19-21 | Assist with embedded development | Verify hardware behavior |
| 22-24 | Implement and critique specialized components | Verify performance and correctness |
| 25-30 | Adversarial review, test generation | Own security and architecture decisions |

## AI engineering log

For every substantial project, add an entry to `ai-engineering-log.md`:

- What I asked the agent to implement.
- What assumptions it made.
- What architectural decisions it proposed.
- What defects I discovered.
- What tests I used to validate it.
- What I changed and why.

## Cryptography

Production code uses vetted cryptographic libraries. Hand-written algorithms (e.g., AES) are educational exercises kept in a separate directory and never used in an application.
