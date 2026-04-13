# Developer Experience & Platform Engineering

## 1. Internal Developer Platform (IDP) Design

**Principle:** Self-service abstraction between developers and infra complexity. Kelsey Hightower: "forever, people have tried to build a thing where most of the organization doesn't think about servers." DORA 2024: platform engineering is primary driver of delivery performance.

**Canonical IDP layers:**
1. Developer Experience: Backstage portal (catalog, templates, docs)
2. Platform Orchestration: Terraform + GitOps (ArgoCD) for self-service infra
3. Runtime Infrastructure: EKS or equivalent
4. Shared Services: observability, security, secrets, CI templates

**Golden paths:** Pre-built opinionated templates for common patterns. Python microservice golden path encodes: observability instrumentation, secrets injection, health checks, Dockerfile, CI template. Scaffolds new service in minutes with all best practices.

**Failure pattern — "IDP as Ticket System":** Jira board where devs request infra from ops. 2-3 day wait. Not a platform — a bottleneck.

**Corrective heuristic:** Measure: time from "I need a service" to "code in staging" without a ticket. Target <30min via golden path. Track dev satisfaction (SPACE framework: satisfaction, performance, activity, communication, efficiency).

## 2. Platform Team Operating Models

**Principle:** Platform team = product team with developers as customers. Product roadmap from developer pain points, SLOs for platform services, active DX measurement.

**Build vs buy:** Buy SaaS for commodity with high self-host overhead. Build internal for tight integration needs. Backstage often right to self-host (deep internal integration); CI/CD infra buy (GitHub Actions, GitLab, Buildkite) over self-hosted Jenkins.

**Failure pattern — "Platform as Gatekeeper":** Abstractions so opinionated devs can't do non-standard tasks. Shadow infra emerges.

**Corrective heuristic:** Spectrum not fence: golden paths for 80%, escape hatches with audit for 20%, contribution model for extensions. Track "% deploys via golden paths" and "escape hatch uses/quarter."

## 3. DORA Metrics and Developer Feedback Loops

**Elite benchmarks:** Deploy multiple/day, lead time <1hr, restore <1hr, CFR <15%. Most rigorously validated benchmarks (39,000+ professionals, decade of data).

**Feedback loop levers:**
1. Pre-commit hooks: fast local validation, seconds
2. PR-level CI: tests + security scans, <10min
3. Deployment pipeline: staging deploy + smoke, <15min
4. Production feedback: observability alerting surfaces failures within minutes of release

**Failure pattern — "DORA Gaming":** Counting hotfix deploys as deployment frequency.

**Corrective heuristic:** Team-level trends over rolling 90-day windows, not snapshots. Quarterly retros with qualitative dev satisfaction. Degradation → trace to specific process change. Metrics are leading indicators, not goals to optimize directly.
