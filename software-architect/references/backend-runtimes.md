# Backend Runtime and Language Selection

## Decision Matrix

| Workload | Recommended | Why |
|----------|------------|-----|
| I/O-bound APIs, gateways, infra tooling | **Go** | Goroutines, simple ops, strong stdlib, healthy hiring |
| Memory-safe hot paths, predictable latency, max throughput | **Rust** | No GC, ownership model, ~15ms at 1K concurrent vs Go ~20ms |
| Complex enterprise logic, rich JVM ecosystem | **Java/Kotlin** | Spring/Hibernate/Kafka ecosystem, Loom virtual threads (21+) |
| I/O APIs by frontend-heavy teams, BFFs | **TypeScript/Node** | Shared language, event loop for I/O concurrency |
| ML inference, data pipelines, scientific computing | **Python** | NumPy/Pandas/PyTorch ecosystem dominance |
| Massive concurrency, soft real-time, fault tolerance | **Elixir/Erlang (BEAM)** | OTP supervision, ~2KB processes, "let it crash" |

---

## Detailed Profiles

### Go
- **Concurrency**: Goroutines (lightweight green threads) handle thousands of connections without thread-per-connection overhead
- **Stdlib**: `net/http`, `encoding/json`, `database/sql` cover most backend needs
- **GC**: Tuned for low-latency server workloads
- **Hiring**: Strong — powers Kubernetes, Docker, cloud infra tooling
- **Trade-off**: Limited expressiveness; intentional simplicity frustrates complex type-level invariants

### Rust
- **Ownership/borrow checker**: Eliminates concurrency bugs at compile time
- **Production use**: AWS Firecracker, Cloudflare Workers
- **Hiring**: Smaller than Go, substantially smaller than Java/TypeScript; expect higher onboarding
- **Polyglot pattern**: Rust for hot paths/proxies/perf-sensitive libs; Go for surrounding services
- **Trade-off**: Higher initial development cost

### Java/Kotlin (JVM)
- **Ecosystem**: Spring, Hibernate, Kafka clients, gRPC, JDBC — richest enterprise library set
- **Project Loom** (Java 21+): Virtual threads narrow concurrency gap vs Go
- **JIT**: Competitive CPU-bound throughput at steady state
- **Cost**: Startup time and memory footprint — painful in serverless/container-dense deploys
- **Kotlin**: Full JVM interop, null-safety in type system, less boilerplate — pragmatic modernization path

### TypeScript/Node.js
- **Strength**: Event loop for high-concurrency I/O; vast ecosystem; deep hiring pool
- **ThoughtWorks Radar warning**: Struggles with compute-intensive workloads — use Go/Rust/JVM instead
- **Risk**: Ecosystem churn (framework rewrites, dependency sprawl) is real long-term maintainability cost
- **Note**: Structural type system provides safety, but runtime is still JavaScript

### Python
- **Dominates**: Data/ML via NumPy, Pandas, PyTorch, scikit-learn
- **GIL**: Historical parallelism limit; Python 3.13 free-threaded mode experimental
- **Async**: FastAPI, async SQLAlchemy mitigate I/O concurrency for data API use cases
- **Not recommended as**: General-purpose high-throughput API server runtime

### Elixir/Erlang (BEAM)
- **OTP supervision**: Processes fail in isolation, supervisors restart — extreme resilience
- **Process weight**: ~2KB vs ~2MB OS threads → millions concurrent on modest hardware
- **Production**: WhatsApp (hundreds of millions of users, small Erlang cluster), SumUp (financial transactions)
- **Correct for**: Real-time collaboration, telecom-grade infra, IoT platforms
- **Wrong for**: General-purpose API server without BEAM expertise
- **Hiring**: Small and specialized market

---

## Polyglot Architecture: When to Introduce a Second Runtime

**Coordination costs** of polyglot: additional build pipelines, observability variance (different tracing clients, log formats), runtime deployment/debugging differences, multi-ecosystem expertise requirement.

### Justified when ALL three hold:
1. A specific service has **demonstrated** production problems on the primary runtime (not anticipated — measured)
2. The service has **stable interfaces** minimizing cross-language coupling
3. The team has **operational capacity** to maintain two stacks

### Innovation token test (McKinley):
A second runtime spends a token. Justified if it provides competitive differentiation or solves an otherwise-intractable problem. NOT justified as a learning exercise or architectural preference.
