# Infrastructure as Code

## 1. Tool Selection: Terraform vs Pulumi vs CDK

| Dimension | Terraform/OpenTofu | Pulumi | AWS CDK |
|---|---|---|---|
| Language | HCL (declarative) | Python, TS, Go, etc. | TS, Python, Java |
| State | State file (local/remote) | Pulumi Cloud or self-hosted | CloudFormation (AWS-managed) |
| Multi-cloud | 100+ providers | 80+ providers | AWS-only natively |
| Policy-as-code | Sentinel (enterprise), OPA | CrossGuard (built-in) | CDK Aspects + CFN Guard |
| Hiring pool | Largest | Growing | AWS-specialist |
| Lock-in | Low (OpenTofu fork) | Moderate | High (AWS + CFN) |
| Best for | Multi-cloud, compliance | General-purpose langs, complex logic | AWS-native, tight constructs |

Terraform: declarative HCL, plan/apply + state tracking surfaces drift. HashiCorp BSL → OpenTofu fork (Linux Foundation).
Pulumi: general-purpose languages for complex conditionals/loops/reuse. CrossGuard reduces external tooling.
CDK: richest AWS abstractions (L2/L3 constructs) but CFN state management limits change observability.

**Failure pattern — "IaC as Shell Scripts":** Monolithic, non-modular, hardcoded values, copy-pasted across envs.

**Corrective heuristic:** Module library from day one: one module per component (VPC, EKS, RDS), parameterized. Remote state with locking (S3+DynamoDB, Pulumi Cloud). Pin module versions.

## 2. State Management and Drift Detection

**Principle:** Drift (actual ≠ declared) occurs in 80%+ of orgs. Sources: manual console changes during incidents, automated remediation, partial apply failures.

Terraform detects drift on every `plan`. Automated drift detection: scheduled `terraform plan` alerting on unexpected changes.

**Failure pattern — "Abandoned State Files":** Local apply with personal creds, state committed to Git, overwritten by another engineer.

**Corrective heuristic:** Remote state with locking before any shared apply. Never commit state to VCS. Restrict `apply` to CI/CD; humans only `plan` locally.

## 3. Policy-as-Code and IaC Testing

**Principle:** Governance as executable, version-controlled rules in every pipeline.

**Evaluation chain:** Static analysis (Checkov, tfsec) on raw HCL → OPA/Sentinel on TF plan → Config Rules on actual state → drift detection over time.

Checkov/tfsec: catch misconfigs before any cloud API call (cheapest prevention). OPA on JSON plan: reason about resource relationships.

**Failure pattern — "Policy Exceptions as Default":** Exception approval too slow → everything excepted.

**Corrective heuristic:** Graduated enforcement: warning 30d → blocking. Self-service exception with business justification, auto-expires 30d. Exception rate >10% → policy miscalibrated.
