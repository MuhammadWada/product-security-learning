# Phase 3 — Linux and Computer Architecture

**Months**: 7-9 | **Est. hours**: 130-155 | **Status**: Not started
**Security integration**: OS security, attack surfaces, Linux permissions and process isolation

## Objective

Understand how software executes on hardware and interacts with the operating system. Builds on the electrical engineering background.

## Outline

| Month | Focus | Practical assignment |
|---|---|---|
| 7 | Computer architecture: CPU, ISAs (ARM/x86), caches, virtual memory, assembly, linking | Memory and performance analyzer |
| 8 | Operating systems: processes, threads, scheduling, synchronization, filesystems, system calls | Process monitor; concurrent workers; introduce and fix race conditions |
| 9 | Linux systems programming: Bash, signals, permissions, sockets, systemd, GDB | Linux telemetry monitoring service (runs under systemd, recovers from failure) |

## Major project

C HTTP server (from the original Weeks 3-4): implement a basic server over TCP sockets, test it, identify vulnerabilities, then harden it against buffer overflows.

## Resources

Computer Systems: A Programmer's Perspective, Operating Systems: Three Easy Pieces, Linux man-pages, Linux kernel documentation, Bare Metal C.

## Acceptance criteria

Explain CPU/memory/OS relationships; process and thread behavior; identify and debug a race condition; use Linux utilities; write a multithreaded C++ app; debug with GDB; deploy and operate a Linux service.
