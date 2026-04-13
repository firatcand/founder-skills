# Incident Management & Reliability Engineering

## 1. SRE Principles: SLOs, SLIs, Error Budgets

**Principle:** Error budget (Google SRE) converts reliability from aspiration to finite, negotiable resource. 99.9% SLO over 30d = 0.1% budget ≈ 43min downtime/month. Failures consume budget; remaining budget spent on risky deploys/experiments. Budget exhausted → reliability takes precedence (Error Budget Policy signed by product, engineering, SRE).

SLI/SLO/SLA hierarchy: SLIs = measurements (99.2% this week), SLOs = targets (99.5% over 30d), SLAs = external contracts with financial consequences.

**Failure pattern — "SLO as Vanity Metric":** 99.99% SLO with no error budget policy. Missed → retroactively adjusted. Meaningless.

**Corrective heuristic:** Before setting SLO, answer: "What happens when we exhaust the budget?" Pre-agreed in Error Budget Policy (feature freeze, reliability sprint, CTO escalation). 30-day rolling window. Start conservative (99.5% not 99.9%) until 3-6 months historical data.

## 2. Incident Response Frameworks

**Principle:** Structure before incident: defined roles (IC, Comms Lead, SMEs), escalation paths, severity classifications, pre-written runbooks.

IC responsible for coordination/communication/decision, not technical debugging. Reduces cognitive load on debugging engineers.

Runbooks must be executable: "Run `kubectl rollout undo deployment/api-service`" not "Consider rolling back." On-call must be sustainable: max alert volume per shift, compensation for night pages, regular rotation.

**Failure pattern — "Heroic Firefighting":** Same 3 engineers every incident, no runbooks, ad-hoc Slack debugging, heroes celebrated not systemic learning.

**Corrective heuristic:** Every new system includes runbook for top 3 failure modes. Measure TTFMA (time to first meaningful action) alongside MTTR — good runbook = TTFMA <5min. Rotate on-call to all team engineers.

## 3. Blameless Postmortems

**Principle:** Structured analysis attributing failures to systemic conditions, not individuals. 48-72 hours while fresh. "What conditions made it easy to make this mistake" → systemic improvements. Google SRE: postmortem when single incident consumes >20% of 4-week budget.

Template: impact metrics, precise timeline, root cause (five-whys), "what went well" + "what went poorly," tracked action items with owners/priorities/dates.

**Failure pattern — "Postmortem Theater":** Document written, action items recorded, no follow-up. Same failure recurs 6 months later.

**Corrective heuristic:** Postmortem action items = P0 work in product backlog. Quarterly review of completion rates. <80% completion → capacity planning failure → dedicated reliability sprint. Cross-team sharing quarterly.

## 4. Chaos Engineering

**Principle:** Deliberately induce failure to build confidence. Hypothesis-driven: define steady-state hypothesis, perturb, observe. Tools: Chaos Monkey (Netflix), Gremlin (commercial), LitmusChaos (CNCF), Harness CE.

Start non-prod, graduate to prod after building blast-radius confidence. Cadence: infra failures (instance termination, network partition) → app failures (latency injection, error injection, resource exhaustion).

**Failure pattern — "Chaos Without Hypothesis":** Random failure injection, no baseline, anxiety not insight.

**Corrective heuristic:** Document before each experiment: (1) Hypothesis with specific thresholds, (2) Blast radius controls, (3) Abort criteria. On-call engineer monitoring during execution.
