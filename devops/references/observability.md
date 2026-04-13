# Observability & Monitoring

## 1. Three Pillars and Integration

**Principle:** Metrics (time-series), logs (event records), traces (request journeys). Power is multiplicative: metrics → *that* something's wrong, traces → *where*, logs → *why*. OpenTelemetry (OTel) is the de facto standard for vendor-neutral instrumentation.

Charity Majors (Honeycomb) challenges three-pillars as outdated: primitive should be the **arbitrarily wide structured event** — rich data blob per operation in columnar DB enabling high-cardinality queries. Eliminates siloed-tool switching during incidents.

Practical advice regardless of model: consistent structured formats (JSON logs, OTel spans), correlate via trace ID propagation.

**Failure pattern — "Observability Paralysis":** Three signals, three vendors, inconsistent formats, no shared correlation IDs. 30% of incident time switching dashboards.

**Corrective heuristic:** OTel as single instrumentation API from day one. Inject/propagate trace ID through all inter-service calls. Trace ID in structured log output. Even with separate backends (Prometheus + Loki + Jaeger), trace ID correlates everything.

## 2. Alerting: SLO-Based and Alert Fatigue

**Principle:** Alert when user experience is at risk, not when infra metrics cross thresholds. SLO-based alerting (Google SRE Workbook): fire on error budget burn rate — when current consumption rate will exhaust budget before window closes.

**Four Golden Signals:** Latency, traffic, errors, saturation. Define SLOs against user-experience signals (availability, success rate, p99 latency) not infra proxies (CPU, memory).

**Failure pattern — "Alert Fatigue Infrastructure":** 47 active alerts, 30 pages/week, majority self-resolve. Engineers stop trusting alerts, real incidents buried.

**Corrective heuristic:** Every alert must answer: "Does this require human action, right now, that can't wait until business hours?" Fails test → delete (noise), route to task queue (ticket), or remove from paging (dashboard). Target <2 pages/shift/day. Multi-window multi-burn-rate alerting (5min + 1hr).

## 3. Observability Pipeline Design and Cost

**Principle:** At scale, telemetry volume = significant cost. OTel-based pipeline optimization: 70-90% data volume reduction, 60-80% storage cost reduction.

**Architecture:** Two-layer OTel Collector: agent collectors (host-level filtering/batching) → gateway collectors (sampling, cardinality reduction, tiered storage routing).

**Tail-based sampling:** Decisions at trace completion → retain 100% error/slow traces, sample 5-10% healthy fast traces. Storage tiering: hot (7d fast query) / warm (30d indexed) / cold (90d+ object storage).

**Failure pattern — "Cardinality Explosion":** Label with user_id/request_id on Prometheus metric. 1M users = 1M series = crashed Prometheus or multi-thousand-dollar Datadog bill in hours.

**Corrective heuristic:** Max label cardinality policy in CI — no high-cardinality labels (user ID, session ID, IP, request ID). Mimirule or remote-write filter to drop. Budget observability at 5-10% of compute spend, alert when exceeded.
