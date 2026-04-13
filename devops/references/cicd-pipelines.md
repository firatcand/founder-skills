# CI/CD Pipeline Design & Automation

DORA elite performers: deploy on-demand (multiple/day), lead time <1hr, restore <1hr, change failure rate 0-15%.

## 1. Trunk-Based Development and Feature Flags

**Principle:** Trunk-based dev — small, integrated changes to main — is prerequisite for true CI. Feature flags decouple deployment from release.

Merge cost scales with branch age. Automate flag lifecycle (Unleash) including archival. Long-lived flags become implicit config debt.

**Failure pattern — "Branch-Based CI Theater":** CI on long-lived branches lasting weeks.

**Corrective heuristic:** Branches <1-2 days. Mandatory CI gates on every PR. Branch protection blocking merge if main diverged >N commits. Feature flags before changing branching model.

## 2. Monorepo vs Polyrepo CI

**Principle:** Monorepos: atomic cross-service changes + shared tooling. Polyrepos: hard boundaries + independent deployment. Depends on organizational coupling.

Critical monorepo capability: **affected-only builds** (git diff analysis). Turborepo, Nx, Bazel. 80% remote cache hit rate with 50 daily PRs saves 20+ hrs/day.

**Failure pattern — "Full Monorepo Build on Every Commit":** All services on every PR.

**Corrective heuristic:** Affected-build tooling from day one. Remote caching. Build time SLO: p95 PR CI <10 min.

## 3. Build Optimization

**Levers:** Layer caching, test parallelization, incremental builds. Cache keys: lockfiles for deps, source hash for builds.

**Failure pattern — "Cache Poisoning by Over-Broad Keys"**

**Corrective heuristic:** Layer caches: OS → runtime → deps (lockfile hash) → app (source hash). Target ≥70% cache hit. Distributed caching for ephemeral runners.

## 4. Deployment Strategies

- **Blue-Green:** Two envs, switch LB. Instant rollback. Stateless + double-capacity budget.
- **Canary:** 1-5% → metric analysis → 25% → 50% → 100%. Flagger integrates Istio/Linkerd.
- **Rolling:** Sequential replacement, no idle env, slower rollback. Default K8s.
- **Multi-region:** Canary in one region, progressive rollout.

Argo Rollouts extends K8s for all strategies.

**Failure pattern — "Big Bang Deployments":** 2 weeks accumulated, maintenance window.

**Corrective heuristic:** If you need a maintenance window, deployment is too large. Track deploy frequency + CFR. CFR >15% → freeze features, invest in automation.

## 5. GitOps Workflows

**Principle:** Git = single source of truth. ArgoCD/Flux reconcile. Declarative, automated, observable, recoverable (rollback = git revert). Operators pull from Git (no K8s API creds in CI).

**Failure pattern — "GitOps + Manual kubectl":** Manual changes overwritten or sync disabled → drift.

**Corrective heuristic:** Hard sync in prod, revoke kubectl from humans. Break-glass with MFA + postmortem. All changes through Git.

## 6. Artifact Management and Pipeline Security

**Principle:** Every artifact: (1) hermetically built, (2) signed provenance, (3) immutable with content-addressable digests.

**SLSA:** L1 (unsigned provenance), L2 (signed, hosted builds), L3 (hermetic, isolated). Sigstore/Cosign: keyless signing via CI OIDC, Rekor transparency log.

**Failure pattern — "Mutable Tags":** `myapp:latest` in prod.

**Corrective heuristic:** Digest pinning. Kyverno/OPA Gatekeeper rejecting unverified images.
