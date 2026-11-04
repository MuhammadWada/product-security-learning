# Phase 2 — C, C++, and Algorithms

**Months**: 4-6 | **Est. hours**: 130-155 | **Status**: Not started
**Security integration**: Memory safety and secure coding; encrypted password manager using a vetted crypto library

## Objective

Build a computer science foundation and move from scripting to compiled systems programming.

## Outline

| Month | Focus | Practical assignment |
|---|---|---|
| 4 | C: compilation, pointers, arrays, strings, structs, allocation, GDB | Telemetry record library in C |
| 5 | Data structures and algorithms: Big-O, lists, stacks, queues, hash tables, trees, heaps, graphs, sorting | Benchmark searches; implement structures and graph traversal |
| 6 | Modern C++ (C++17+): RAII, smart pointers, STL, templates, CMake, GoogleTest | High-performance telemetry processing library; compare against Python |

Security work: buffer-overflow and memory-safety analysis of the C code; add encryption to the password manager with a vetted library and a key-management strategy. Hand-rolled AES is a separate educational exercise.

## Resources

CS50x, LearnCpp, CMU Principles of Imperative Computation, Computer Systems: A Programmer's Perspective, CMake tutorial, Effective C, Serious Cryptography (Ch. 1-4, 7).

## Acceptance criteria

Explain how source becomes an executable; stack vs heap; pointers and ownership; implement common data structures; analyze complexity; write a modular C++ app; build with CMake; debug memory defects.

**Gate**: independently implement a C++ library, build it with CMake, test it, and explain its memory-management strategy.
