# Phase 8 — Rust and Advanced Systems

**Months**: 22-24 | **Est. hours**: 130-155 | **Status**: Not started
**Security integration**: Memory safety, software assurance (static/dynamic analysis, fuzzing, threat modeling)

## Objective

Deepen Rust proficiency and establish software assurance practices. Rust is introduced earlier (Phase 4); this phase builds the full project.

## Outline

| Month | Focus | Practical assignment |
|---|---|---|
| 22 | Rust: ownership, lifetimes, traits, error handling, concurrency, Cargo, FFI | Telemetry processing component in Rust; compare with Python and C++ |
| 23 | GPU and FPGA introduction: CUDA basics; digital logic and SystemVerilog in simulation | Simple GPU kernel; FSM and a simulated accelerator (no FPGA purchase needed) |
| 24 | Software assurance: static analysis, fuzzing, property-based testing, fault injection, traceability | Assurance package for the telemetry platform |

Compliance frameworks (NIST SP 800-53 and 800-171, Cyber Survivability) are covered here: translate framework requirements into specific technical controls, trace them to tests, and record the tradeoffs between compliance and engineering velocity.

Formal methods (state machines, invariants, temporal logic, model checking) are introduced after programming and systems fundamentals are solid.

## Assurance package contents

System and software requirements, architecture documentation, interface specifications, threat model, test strategy, test and static-analysis results, performance benchmarks, failure analysis, deployment documentation.

## Acceptance criteria

Build and test a Rust app; explain ownership and borrowing; write a basic CUDA kernel; explain GPU memory hierarchy; simulate a SystemVerilog design; explain FPGA synthesis vs software compilation; define a verification strategy; conduct an architecture and security review.

**Gate**: present the system as a principal-engineer design review, defending architecture, implementation, security, performance, and reliability.
