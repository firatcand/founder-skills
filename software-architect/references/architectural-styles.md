# Architectural Styles: Trade-offs and Decision Framework

## Quick Decision Matrix

| Factor | Modular Monolith | Microservices | Serverless | Event-Driven |
|--------|-----------------|---------------|------------|-------------|
| Team size | Any | 50+ engineers minimum | Any | Varies |
| Domain stability | Evolving | Stable, well-understood boundaries | N/A | Varies |
| Operational maturity | Basic CI/CD | Mature CI/CD, distributed tracing, on-call | Cloud-native | Message broker ops |
| Default? | **Yes** — correct default for <100 engineers | No — earn it | Narrow use cases | Complement, not primary |

---

## 1. Modular Monolith (The Underrated Default)

**What it is**: Single deployable unit with strong internal boundaries — bounded contexts, strict module APIs, no shared mutable state across modules.

**Why it's the default**: Retains refactoring flexibility that microservices eliminate. Wrong service boundary in microservices = cross-team migration. Wrong module boundary in monolith = a refactoring.

**Correct for**: Most systems under 100 engineers with a not-yet-stable domain model.

**Migration path**: Strangler Fig Pattern (Newman) — extract services incrementally at edges where boundaries are clearest. Triggered by **demonstrated** scaling bottlenecks, not anticipated ones. Follow domain model, not technical layers.

**Primary risk**: Distributed monolith anti-pattern — deployed as services but coupled so tightly they can't deploy independently. All microservice costs, none of the benefits. Happens when service extraction precedes domain modeling.

---

## 2. Microservices: Where They Excel

**Genuine strengths**: Independent deployability, targeted scalability, runtime-per-workload optimization.

**Design philosophy** (Vogels): "Everything fails all the time" — design for isolated failure, not prevention.

### Prerequisites (Newman)
- Comprehensive test coverage (prerequisite for independent deployment)
- Mature CI/CD automation (optional for monolith, mandatory for dozens of services)
- Distributed tracing infrastructure
- Teams large enough to own services end-to-end
- On-call rotations need ~8 people minimum (Larson) — sets org size lower bound

### Accidental Complexity
- Network partitions, partial failures, split-brain, eventual consistency lag
- Cross-service transactions require Saga pattern (Richardson) — shifts consistency from DB layer (mature tools) to application code (hard to test)
- Richardson himself noted coupling event sourcing + Sagas compounds complexity beyond what many teams handle
- Inter-service calls are not free: network egress, load balancers, NAT gateways, per-service autoscaling, cache duplication, sidecars
- Amazon Prime Video 2023: consolidated microservice monitoring → monolithic architecture → substantial cost reduction

### When NOT to use
- Domain model not yet stable (boundaries will be wrong)
- Team too small for independent service ownership
- No demonstrated scaling need beyond single-process capacity
- Fowler's key insight: "almost all successful microservices stories started with a monolith that was split up"

---

## 3. Serverless: Narrow But Real Value

**Excels when**: Bursty event-driven workloads, unpredictable traffic, idle time wastes provisioned capacity, operational overhead is binding constraint.

**Good fits**: Image processing pipelines on upload, webhook handlers, periodic batch jobs.

### Failure Modes
- Cold start latency: Python Lambda 250–600ms — breaches SLAs for synchronous user-facing APIs
- Cost crossover: per-invocation pricing exceeds reserved container capacity at lower traffic than teams anticipate
- Debugging opacity: correlating Lambda logs + API Gateway metrics + third-party statuses across distributed trace (67% of teams struggle per Gartner 2024)

### NOT appropriate for
- Latency-sensitive paths with cold-start intolerance
- Long-running compute jobs
- Persistent connection workloads
- Host-level customization needs
- Vendor lock-in exposure is high (coupled to provider-specific event sources)

---

## 4. Event-Driven Architecture

**Core value**: Temporal decoupling — producers and consumers operate independently across time. Scales well for high-throughput ingestion.

**Vocabulary** (Hohpe, Enterprise Integration Patterns): channels, messages, pipes-and-filters, correlation IDs, message brokers, dead letter queues.

### Choreography vs Orchestration
- **Choreography** (services react to each other's events): emergent behavior, difficult to reason about
- **Orchestration** (central coordinator issues commands): more explicit, but creates coupling and new failure domain

### Critical Requirements
- Idempotency in consumers
- At-least-once delivery semantics handling
- Understanding broker ordering guarantees (or lack thereof)

### Practical Migration Sequence
1. Introduce message broker at service boundaries where synchronous coupling causes operational problems
2. Model events from domain operations before attempting event sourcing
3. Adopt CQRS at specific read-heavy endpoints before applying system-wide
4. **Do not attempt all three simultaneously** — common failure mode
