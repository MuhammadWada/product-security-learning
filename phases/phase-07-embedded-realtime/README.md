# Phase 7 — Embedded and Real-Time Systems

**Months**: 19-21 | **Est. hours**: 130-155 | **Status**: Not started
**Security integration**: Secure boot chains, firmware signing, firmware update security, debug interface security

## Objective

Develop software that interacts directly with hardware, using an STM32 board first.

## Outline

| Month | Focus | Practical assignment |
|---|---|---|
| 19 | C and microcontrollers: Cortex-M, registers, GPIO, timers, interrupts, UART/SPI/I2C, DMA | Peripheral control; external sensor |
| 20 | RTOS: FreeRTOS tasks, queues, semaphores, priority inversion, watchdogs (Zephyr after) | Concurrent tasks and fault management |
| 21 | Bare metal and embedded Linux: startup code, linker scripts, U-Boot, device trees, Yocto | Minimal startup firmware; boot Linux on a dev board |

## Major projects

- Embedded telemetry acquisition system: STM32 node sending data through a gateway to the AWS platform.
- Simulated secure boot process (original Week 11).
- NXP i.MX embedded Linux gateway as a follow-on if hardware setup is time-consuming.

## Resources

STM32CubeIDE, Mastering the FreeRTOS Real Time Kernel, Zephyr, Yocto, and U-Boot documentation.

## Acceptance criteria

Write and debug embedded C; Cortex-M architecture; configure peripherals; interrupt-driven software; RTOS application; real-time scheduling; bare-metal startup and linking; embedded Linux architecture.

**Gate**: a functioning embedded telemetry node with reliable communication to the cloud application.
