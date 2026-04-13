# Cloud Architecture Patterns

## Table of Contents
1. Multi-Region and Multi-AZ Design
2. Network Topology
3. Cost Optimization and FinOps
4. Cloud-Native Design Patterns
5. Vendor Lock-in vs Portability
6. Landing Zone Design

---

## 1. Multi-Region and Multi-AZ Design

**Principle:** Use multi-AZ as default for production. Reserve multi-region for explicit DR, regulatory data locality, or sub-100ms global latency. AWS Well-Architected Framework lists "implement multi-Region when multi-AZ would suffice" as a named anti-pattern.

3+ AZs protect against power, networking, hardware failures with single-digit ms latency. Multi-AZ does NOT cover complete regional events.

Multi-region options:
- **Active-passive**: Simpler, DNS-level failover (Route 53, GCP Cloud DNS), accepts RPO from replication lag.
- **Active-active**: Aurora Global Database, DynamoDB Global Tables, Cosmos DB multi-region writes — but last-writer-wins conflict complexity.

**Decision rule:** Measure actual RTO/RPO before committing. Most Series A startups → robust multi-AZ + documented runbooks.

**Failure pattern — "Multi-Region as Prestige Architecture":** Deployed for signaling, not requirements. Result: desynchronized deployments, data drift, doubled complexity, often decreased availability.

**Corrective heuristic:** Before multi-region answer: (1) SLA penalty if region goes dark? (2) Data model supports eventual consistency? (3) On-call capacity for two full-stack deployments? If unclear → three-AZ, one region, fast failover runbooks.

---

## 2. Network Topology

**Principle:** Design VPC topology as a product from day one. Hub-and-spoke via Transit Gateway — centralized egress (shared NAT), ingress inspection, blast-radius separation.

**Subnet tiering:** Public (LBs, NAT Gateways) → Private application (compute) → Isolated data (databases, no internet route).

**Sizing:** CIDRs generous — /28s can't accommodate K8s pod CIDR expansion. Transit Gateway or GCP Shared VPC at scale.

**Service mesh:** Istio (~20-30% overhead, richest features) vs Linkerd (~10-15% overhead, CNCF, simpler). CNCF SMI for vendor-neutral APIs.

**Failure pattern — "Service Mesh on Day One":** Full Istio before 5 services.

**Corrective heuristic:** Adopt mesh when ≥2 of: (1) >15 services with mTLS, (2) L7 canary routing needed, (3) dedicated platform team. Otherwise → API gateway mTLS + PrivateLink.

---

## 3. Cost Optimization and FinOps

**Principle:** Cloud cost is engineering, not finance. FinOps stages: Crawl (visibility), Walk (optimization), Run (unit economics — cost per customer/request/inference).

**Levers by effort:**
1. **Right-sizing:** Compute Optimizer/Recommender/Advisor → 20-40% savings, no commitment.
2. **Savings Plans/RIs:** Compute SP (66%), EC2 Instance SP (72%), Convertible RI (54% + family flexibility). 1-3yr for stable baselines.
3. **Spot/Preemptible:** Up to 90% for fault-tolerant work. Diversified Spot Fleets + on-demand fallback.
4. **Tooling:** ProsperOps/Xosphere (commitment automation); CloudZero/Apptio (cost attribution).

**Failure pattern — "RI Lock-in Without Utilization Discipline":** 3yr Standard RIs then migrating families.

**Corrective heuristic:** Prefer Compute SP over EC2 Instance SP. Automate commitment management. Monthly review; <70% utilization over 30d triggers review. Infracost in CI/CD.

---

## 4. Cloud-Native Design Patterns

**Cell-based architecture:** Partition entire stack into independent cells, each serving bounded user partition. Consistent-hashing routing on stable key (user ID, tenant ID).

**Circuit breaker:** Consumer-side — when downstream failures exceed threshold, open and fast-fail. Resilience4j (JVM), Polly (.NET).

**Failure pattern — "Retry Storms":** Synchronized retries flood recovering service.

**Corrective heuristic:** (1) Circuit breakers on all cross-service calls, (2) Jitter on retry intervals, (3) Timeout budgets at every boundary.

---

## 5. Vendor Lock-in vs Portability

**Principle:** Lock-in = switching-cost calculation (Hohpe). Proprietary for commodity (10x leverage), portable for differentiating logic.

K8s strongest portability but cloud extensions erode it. Egress: 100TB from S3 ≈ $8,500; R2 zero-egress.

**Failure pattern — "Multi-Cloud as Portability":** Two security postures, two cost strategies, no actual portability.

**Corrective heuristic:** Evaluate four dimensions independently: technical, contractual, operational, data. Operational lock-in (CI/CD, monitoring, IaC) most persistent.

---

## 6. Landing Zone Design

**Principle:** Pre-configured multi-account structure with guardrails before first workload.

AWS Control Tower: preventive (SCPs), detective (Config Rules), proactive (CFN checks). Structure: management, security/audit, log archive, workload in separate OUs.

**Failure pattern — "Monolithic Account":** All environments in one account.

**Corrective heuristic:** Minimum three accounts: (1) management/billing, (2) security/audit, (3) workload. Automate via AFT.
