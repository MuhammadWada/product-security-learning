# Phase 9 — GPU, FPGA, and Hardware Security

**Months**: 25-27 | **Est. hours**: 130-155 | **Status**: Not started
**Security integration**: Side channels, hardware trust, FPGA bitstream security, hardware roots of trust

## Objective

Move from introductory exposure (Phase 8) to implementation and security analysis of specialized compute.

## Focus areas

- GPU: CUDA programming, memory hierarchy, CPU vs GPU benchmarking, heterogeneous work allocation.
- FPGA: SystemVerilog, synthesis, timing, AXI, Vivado/Vitis; secure protocol on FPGA (original Week 12).
- Hardware security: side-channel attack fundamentals, hardware attack case study (original Week 13), bitstream security, debug-interface security, hardware/software interface security.
- Fleet key management: design a key hierarchy, provisioning, rotation, and revocation for edge devices that are disconnected or physically exposed; the role of a TPM or secure element.
- Tamper and data-at-rest protection: zeroization triggers, hardware-bound keys, tamper-evident and tamper-responsive design, and how to verify these protections work.
- Edge ML security: protect model weights on a deployed device, adversarial inputs to perception, and integrity of the model update pipeline.

## Resources

NVIDIA CUDA Programming Guide, AMD Vitis Developer Hub, side-channel attack overview material.

## Acceptance criteria

- Write a basic CUDA kernel and compare CPU and GPU performance, including memory-transfer overhead.
- Simulate an FPGA design and explain which work belongs on a CPU, GPU, or FPGA.
- Explain how at least one side-channel attack works and how to mitigate it.
- Design a key hierarchy with provisioning, rotation, and revocation for disconnected devices.
- Design tamper detection, zeroization triggers, and hardware-bound data-at-rest protection.
- Describe threats to a deployed ML model and how to protect its weights and update path.

**Gate**: design and review a fielded device from the DECTP capstone. Produce a key-management design, a tamper and zeroization plan, and a side-channel analysis, then defend them in a design review.

## Notes

The gate was chosen on 2026-11-04 and can be adjusted as the phase approaches.
