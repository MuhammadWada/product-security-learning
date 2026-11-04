# Phase 6 — Cloud Engineering and DevOps

**Months**: 16-18 | **Est. hours**: 130-155 | **Status**: Not started
**Security integration**: AWS IAM and cloud security architecture, container security, CI/CD security, secrets management, vulnerability scanning

## Objective

Deploy, secure, monitor, and maintain software in cloud environments. AWS is the single cloud provider.

## Outline

| Month | Focus | Practical assignment |
|---|---|---|
| 16 | Cloud fundamentals and AWS: EC2, IAM, VPC, S3, RDS, load balancing | Secured cloud environment; harden an EC2 instance and write a security guide (original Week 16) |
| 17 | Containers: Docker, Compose, registries, Kubernetes fundamentals; ECS before EKS | Containerize and deploy the full application securely (original Week 15) |
| 18 | IaC and DevOps: Terraform, GitHub Actions, CloudWatch, OpenTelemetry | Cloud-deployed telemetry platform |

## Resources

AWS Getting Started and Skill Builder, Docker Getting Started, Terraform and Kubernetes tutorials, OpenTelemetry docs.

## Acceptance criteria

Provision AWS independently; explain EC2/ECS/EKS/Lambda; containerize and deploy; Terraform; CI/CD; monitoring; identify and fix common cloud misconfigurations; estimate costs.

**Gate**: a clean deployment from a fresh environment recreates the application without manual server configuration.
