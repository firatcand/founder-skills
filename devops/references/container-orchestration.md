# Container Orchestration

## 1. Kubernetes Architecture Decisions

**First decision:** K8s at all? ECS/Fargate strong for AWS-native, <20 services, no K8s expertise. Fargate eliminates EC2 cluster management with task-level billing. EKS = full K8s API + control plane fees + node management.

When K8s: use managed control planes (EKS, GKE Autopilot, AKS) unless compliance/scale justifies self-hosted. Kelsey Hightower: K8s "gives you mechanisms — now you need to operate them."

**Cluster topology:** Single large cluster vs multiple purpose clusters (prod/non-prod, per-team). Multi-cluster adds ops complexity but provides hard blast-radius isolation. Namespaces map to team ownership, not environments (separate clusters for prod/non-prod).

**Failure pattern — "Namespace as Environment":** Prod and dev in same cluster via namespaces. Leaked ClusterAdmin token, misconfigured NetworkPolicy, or noisy neighbor → prod impact.

**Corrective heuristic:** Hard cluster boundaries prod/non-prod. Within prod: namespaces for team/service isolation with RBAC. ResourceQuotas + LimitRanges on every namespace. Admission controllers (OPA Gatekeeper, Kyverno) at namespace creation.

## 2. Autoscaling: HPA, VPA, KEDA

**HPA:** Scales replica count on CPU/memory/custom metrics.
**VPA:** Adjusts container resource requests/limits based on observed usage.
**KEDA:** Extends HPA to external event sources, enables scale-to-zero.

KEDA powerful for event-driven: scale on Kafka consumer lag, SQS queue depth, Redis list length (not CPU, which is lagging backpressure indicator). Scale-to-zero eliminates idle cost for bursty workloads.

VPA + HPA conflict on same deployment with default metrics. In-place VPA (K8s 1.35+) adjusts without restarts where node capacity allows.

**Failure pattern — "Fixed Resource Requests":** Generous dev values copied to prod. 80% pods at 5% CPU. 10-15x overspend.

**Corrective heuristic:** VPA recommendation mode for 2-4 weeks. Set requests at p50, limits at p95-p99. Re-evaluate quarterly. KEDA for any queue/event-driven workload.

## 3. Service Mesh Considerations

**When to adopt:** (1) mTLS across all service-to-service, (2) Fine-grained traffic management without app code changes, (3) Unified observability across services.

Linkerd: operationally simpler (Rust micro-proxy, ~10-15%, CNCF graduated). Istio: richer traffic management (~20-30%, more CRDs).

**When to avoid:** <15 services, no platform team, app-level mTLS + API gateway sufficient.

**Failure pattern — "Complexity Explosion":** All Istio features enabled before team understands K8s networking. Six debugging layers.

**Corrective heuristic:** Phased adoption: Phase 1 (mTLS only) → Phase 2 (traffic management for canary) → Phase 3 (full observability). Maintain escape hatch: verify disabling mesh restores expected traffic.
