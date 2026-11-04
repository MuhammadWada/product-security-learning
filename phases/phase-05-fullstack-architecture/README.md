# Phase 5 — Full-Stack Development and Software Architecture

**Months**: 13-15 | **Est. hours**: 130-155 | **Status**: Not started
**Security integration**: OWASP Top 10, authentication and authorization (JWT, OAuth 2.0/OIDC, RBAC), secure sessions, threat modeling

## Objective

Design and implement a complete application from UI through backend and persistence, and formalize software architecture.

## Outline

| Month | Focus | Practical assignment |
|---|---|---|
| 13 | Frontend: HTML/CSS, JavaScript, TypeScript, React | Telemetry dashboard components |
| 14 | Full stack: React-FastAPI integration, authentication, RBAC, WebSockets, Playwright | Authenticated live telemetry with UI tests |
| 15 | Architecture: SOLID, layering, hexagonal, modular monolith vs microservices, ADRs | Document and refactor the system; produce ADRs |

Security work: build an intentionally vulnerable web app, test and remediate against the OWASP Top 10 (original Week 7); secure API with JWT and rate limiting (original Weeks 10, 14).

Optional specialization: Go REST API (original Week 6), if time allows.

## Resources

Full Stack Open, TypeScript, React, and Playwright docs, Fundamentals of Software Architecture, OWASP documentation.

## Acceptance criteria

Build a React/TypeScript frontend; integrate frontend and backend; implement authN/authZ; design a maintainable architecture; document decisions; explain when microservices are appropriate; test the whole application.

**Gate**: deliver an application another developer can install, configure, test, and operate from the documentation alone.
