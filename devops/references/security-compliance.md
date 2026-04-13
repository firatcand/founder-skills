# Security & Compliance

Shift-left embeds controls at cheapest fix point. Combined with zero-trust runtime → defense in depth without sacrificing velocity.

## 1. Secrets Management

**Principle:** No static long-lived secret in production. Vault dynamic secrets: unique time-bounded credential on demand, TTL lease, auto-rotate. 1hr TTL prod, 24hr staging.

Cloud-native: AWS Secrets Manager, Azure Key Vault (30d rotation), GCP Secret Manager. No human sees prod secret in plaintext.

K8s: Vault Agent Injector or Secrets Store CSI Driver — tmpfs at pod startup, auto-renewed, never in etcd/image layers.

**Failure pattern — "Secret Sprawl":** Secrets in 5 places.

**Corrective heuristic:** Inventory audit (truffleHog, git-secrets, Gitleaks) including git history. Rotate all discovered immediately. Pre-commit hooks + CI scanning. Track "% from Vault/KMS" → 100%.

## 2. IAM Architecture

**Principle:** Least privilege. RBAC for baseline + ABAC for high-risk. RBAC suffers role creep at scale. ABAC evaluates at request time → JIT time-bounded access.

Identity federation (Okta, Azure AD, Google Workspace) for centralized lifecycle. SPIFFE/SPIRE for workload identity.

**Failure pattern — "Admin Roles for Velocity":** Temp admin becomes permanent.

**Corrective heuristic:** JIT access (IAM Identity Center, Teleport, Boundary). 2-4hr max. Step-up MFA for prod. Quarterly reviews. Target ≥90% JIT.

## 3. Supply Chain Security

**Principle:** Threats via dependencies, tooling, distribution. Three elements: SBOM (inventory), signing (integrity), SLSA (provenance).

SBOM: CycloneDX/SPDX in CI (syft, cdxgen, trivy). Sigstore/Cosign: keyless signing. Kyverno/Gatekeeper: no signature = no deploy.

**Failure pattern — "Dependency Confusion":** Public package with internal name.

**Corrective heuristic:** Private proxy (Artifactory, Nexus, CodeArtifact) with scoping rules. Pin to exact digests. SCA (Snyk, Dependabot) with breaking gates. Signed SBOMs as attestations.

## 4. Zero-Trust Networking

**Principle:** Never trust, always verify. Access on identity/posture/context, never network location.

**Five controls:** (1) Strong identity per request, (2) Device posture, (3) Micro-segmentation, (4) Least-privilege + JIT, (5) Continuous monitoring.

**Failure pattern — "Zero Trust as Just MFA":** Human MFA but unauthenticated service-to-service.

**Corrective heuristic:** Three zones: (1) User (MFA, conditional access), (2) Service (mTLS, SPIFFE, API gateway), (3) Data (ABAC, tokenization). Implement in order.

## 5. Compliance-as-Code and Shift-Left

**Principle:** Executable compliance in CI/CD > periodic audits. OPA (Rego), Sentinel, OPA Gatekeeper.

**30/60/90 plan:**
- 30d: MFA/SSO, branch protection, commit signing, secrets scanning, SCA, Checkov.
- 60d: SAST (Semgrep), container scanning (Trivy, Grype), policy gates on TF plans, mTLS pilot.
- 90d: OPA Gatekeeper prod, SLSA L2, security champions, DORA security KPIs.

**Failure pattern — "Security Theater":** Scanners enabled, findings routinely suppressed.

**Corrective heuristic:** SLA tiers: P0 24hr, P1 7d, P2 30d. Break-glass via security team. Track suppressed:fixed ratio; >20% → tune rules.
