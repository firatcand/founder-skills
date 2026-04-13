# Database and Data Layer

## Selection Framework (Kleppmann)

Characterize access patterns first, then match storage engine. Ask:

1. Read-to-write ratio?
2. Cardinality and structure of primary access key?
3. Do queries require cross-entity joins or single-entity lookups?
4. What consistency guarantees does business logic require?
5. Write volume and dataset size growth projections?

**CAP Theorem** (Brewer/Gilbert-Lynch): Partition tolerance is non-negotiable in networked systems. Real trade-off is consistency vs availability. Brewer's 2012 refinement: designers can tune consistency/availability independently within the partition window — not a binary choice.

---

## Relational: PostgreSQL (The Default)

**PostgreSQL is the correct default for the large majority of new systems.**

- ACID transactions with row-level locking
- Extensions: PostGIS (geospatial), TimescaleDB (time-series), pgvector (vector search)
- JSONB document storage with indexing
- Full-text search built in
- MVCC: concurrent read-write without read locks
- Scaling: PgBouncer (connection pooling), read replicas, logical replication, Citus (horizontal sharding)

### Where PostgreSQL strains
- Write workloads >~100K writes/sec on single node → application-layer sharding or different engine
- Multi-region writes with strong consistency → CockroachDB or Spanner

### Schema evolution pattern
1. All changes are backward-compatible additions before deployment
2. Column/table removal follows two-phase process separated by a release cycle
3. Migration tooling (Flyway, Liquibase) versioned and applied idempotently
4. Large migrations under traffic without shadow deployment = production incident risk

**MySQL**: Large install base, good for simpler query patterns with high read throughput. PostgreSQL preferred for new systems due to richer features and standards compliance.

---

## Document: MongoDB and DynamoDB

### MongoDB
- **Appropriate when**: Domain model is naturally hierarchical, primary access by entity ID or few indexed fields, infrequent cross-entity joins
- **Genuine advantage**: Flexible schema during early product development with unstable domain model
- **Anti-patterns**: Using as relational DB without FK support (integrity moves to app code, frequently incomplete); designing for cross-document transactions (supported but expensive — signals relational model is more natural)

### DynamoDB
- **Appropriate for**: Single-digit ms latency at any scale with predictable performance
- **Programming model**: Partition key + optional sort key + secondary indexes
- **Critical constraint**: Access patterns must be known upfront and encoded in key design
- **Anti-pattern**: Designing schema relationally then retrofitting to key-value access → query limitations requiring rebuild

### Design principle (Helland)
Entities should be self-contained consistency units. Cross-entity consistency via messaging, not transactions. Embed data accessed together; reference data accessed independently.

---

## Wide-Column: Cassandra / ScyllaDB

- **Appropriate for**: Write-heavy massive scale, geographic distribution, acceptable eventual consistency
- **Data model**: Query-driven — tables designed around specific queries, denormalized, multiple tables for same entities
- **CAP**: AP — favors availability + partition tolerance. Tunable consistency (ONE, QUORUM, ALL) per operation
- **Scaling**: Write throughput scales linearly with nodes
- **Good for**: Time-series, event logs

### Anti-patterns
- Complex relational queries (no joins, limited aggregation)
- Low-volume workloads (operational complexity not justified)
- Strong cross-partition consistency requirements
- Operational burden: compaction strategies, tombstone accumulation, cluster rebalancing need dedicated expertise

---

## Search Engines

### Elasticsearch
- Full-text search, complex query DSL, log aggregation (ELK), analytics
- Lucene-based: fuzzy matching, faceting, aggregations, geospatial
- Operational overhead: cluster management, shard allocation, heap sizing
- Often adopted where PostgreSQL full-text search would suffice

### Meilisearch / Typesense
- Product search: relevance quality + sub-100ms latency + operational simplicity
- Not general-purpose Elasticsearch replacement — fills search-as-a-feature use case

---

## Time-Series and Graph

### Time-Series
- **TimescaleDB** (recommended if already on PostgreSQL): time-partitioned hypertables, continuous aggregations, retention policies, full SQL
- **InfluxDB / Prometheus**: Monitoring and metrics; Prometheus is de facto for Kubernetes (pull-based scraping)

### Graph (Neo4j, Neptune)
- **Justified when**: Primary value is in relationships, not entities — recommendations, fraud detection, knowledge graphs, network topology
- **Kleppmann signal**: Many-hop JOINs on relational schema = data is graph-shaped
- **Poor choice for**: Simple entity storage with occasional relationship queries

---

## Caching: Redis (The Default)

**Redis is the correct default for new systems.**

- Beyond caching: pub/sub, sorted sets (leaderboards, rate limiting), streams (event log), distributed locks
- Single-threaded command processing → predictable sub-ms latency
- Redis Cluster for horizontal scaling
- **Risk**: Data loss if persistence misconfigured — understand AOF vs RDB trade-offs

**Memcached**: Only when requirement is strictly simple key-value cache with multi-threaded perf, no data structures/persistence/pub-sub.

### Cache invalidation strategies
- **Write-through**: Update cache on write
- **Write-behind**: Async update
- **Cache-aside**: Read on miss, write explicitly
- **Cache stampede**: Many concurrent misses for same key hitting DB — mitigate with probabilistic early expiration or distributed locking

---

## CQRS and Event Sourcing

### CQRS
- Separates write model (commands) from read model (optimized queries)
- **Legitimate use case**: High-read-volume where query model must be denormalized differently, read-write consistency can tolerate eventual replication lag
- **Not a default**: Adds two models, sync logic, eventual consistency — not justified for most CRUD systems

### Event Sourcing
- Persists state as immutable event sequence
- **Advantages**: Built-in audit log, event replay, temporal queries, natural EDA alignment
- **Costs**: Event schema versioning complexity (events are permanent), snapshotting needed for long-lived aggregates, paradigm shift
- Richardson's evolution: initially recommended coupling event sourcing + Sagas as default; later acknowledged compounding complexity many teams underestimated
