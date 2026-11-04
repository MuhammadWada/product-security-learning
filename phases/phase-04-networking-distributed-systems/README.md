# Phase 4 — Networking and Distributed Systems

**Months**: 10-12 | **Est. hours**: 130-155 | **Status**: Not started
**Security integration**: Protocol security, TLS and certificate validation, API authentication, database security

## Objective

Understand how independent software components communicate and cooperate; prerequisite for cloud engineering.

## Outline

| Month | Focus | Practical assignment |
|---|---|---|
| 10 | Networking: TCP/IP, DNS, sockets, HTTP/TLS, REST, JSON, authentication | Socket apps, HTTP client, basic API; packet analysis |
| 11 | Backend and databases: SQL, PostgreSQL, transactions, indexing, FastAPI | Telemetry ingestion service |
| 12 | Distributed systems: async, queues, retries/timeouts, idempotency, consistency | Distributed telemetry platform (ingestion, processing, retrieval) with injected failures |

Also in this window: introduce Rust (ownership, error handling, testing) via the file encryption utility from the original Week 5; deepened in Phase 8. Introduce Redis and a message broker such as RabbitMQ.

## Resources

Computer Networking: A Top-Down Approach, Designing Data-Intensive Applications, FastAPI, PostgreSQL, and Redis documentation, The Rust Programming Language (Ch. 4-6).

## Acceptance criteria

Write a TCP client/server; explain TCP vs UDP; design a REST API and relational schema; understand transactions and isolation; build independently deployable services; handle timeouts and failures; explain eventual consistency and idempotency.

**Gate**: run the application across separate processes and show it handles a service interruption without corrupting stored data.
