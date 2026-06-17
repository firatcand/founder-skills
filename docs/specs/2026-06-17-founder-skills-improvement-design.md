# Founder-skills improvement — design (P0/P2/P3)

Date: 2026-06-17 · Branch: `improve-skills-p0-p2-p3`

## Context

These 19 skills are used **primarily inside roster workspaces**, where an orchestrator
(`EXPERT.md`/`agent.md`) injects project context (voice, ICP, stage) and places output.
Skills must stay **pure, self-contained, roster-agnostic** (no hardcoded `guidelines/` or
`pending/` paths) so standalone installs and per-user edits never break.

## Evidence (blind pressure test, 59 agents, all 19 skills)

- 10 won / 9 lost, nearly all margins "slight" (only `seo` won by "moderate").
- **15/19 advantages were "specific curated expertise"**, not generic competence — the
  skills' knowledge is real and defensible.
- **Dominant cause of losses was process leakage**, not weak content: skills emitted
  `§`-citations, "Mode: Generate", "I have everything I need", and skill-handoff chatter
  into the deliverable. Fixing output discipline should flip several slight losses to wins
  without touching knowledge.
- Competitor-naming gaps are **by design** — that's project substrate roster injects, not
  skill content.

## Approved scope

**P0 — Output-discipline rule (all 19 skills).** Deliver only what the user uses; never
leak internal scaffolding (citations the reader can't see, mode/process narration,
handoff chatter). Apply frameworks silently; assume-and-proceed instead of interrogating.

**P2 — Gut `prompt-engineering-patterns`.** Fix shipped defects: `prompt-optimization.md:372`
syntax bug; `model="gpt-5"` + deprecated `openai.ChatCompletion`; hardcoded model-id
strings; naive accuracy/token "best practice". Strip provider-specific runnable code to
language-agnostic technique guidance; defer model-IDs to the `claude-api` skill. Keep
`prompt-architect` (only 35–45% overlap, different altitude).

**P3 — Polish pass (all 19).** Terse triggering-focused `description`s (≤350 chars, lead
with "Use when…", one disambiguation line); remove hard "always ask" gates
(`pricing` stage, `prompt-architect` Markdown/XML); fix `seo` name casing (`SEO`→`seo`);
add roster-agnostic substrate-aware phrasing where output is commercial/brand/content.

## Deferred (not in this pass)

- **P1** — merge `ui-design`+`ux-design`+`graphic-design` → `design-advisor` (80% overlap).
- **P4** — roster repo: fix `design/EXPERT.md` routes; EXPERT injects substrate + writes back.

## Execution

Five parallel subagents, partitioned by disjoint file sets (no edit conflicts). Each agent
does P0+P3 for its skills; the prompt-skills agent also does P2. Verify via `git diff`;
re-run a mini pressure test on previously-leaking skills.

## Validation (leakage fix)

Re-ran the blind pressure test on the skills that originally lost to scaffolding leakage.

- `channel-expert`, `prompt-architect`: clean after the P0 block alone.
- `pricing`, `ui-design`: the generic P0 block was **not** enough — their bodies actively
  named modes ("Builder mode", "Mode 1/2"), cited `§` sections / KB shorthand
  ("a16z anti-pattern"), and (ui-design) scripted a handoff and pointed at a non-existent
  `references/principles.md`. Fixed at the source: marked mode names + `§` refs as internal
  routing, blunted the output-discipline block with the exact offending phrases, removed the
  scripted handoff and the dangling `ui-ux-pro-max`, and made ui-design self-contained on its
  inline numeric defaults.
- After those edits, all **skill-driven** leaks disappeared (verified round over round:
  "Builder mode", "Mode 1/2", KB shorthand, handoff chatter all gone).
- A residual "I read the files / references empty / now producing" preamble still trips the
  leak flag, but it is a **test-harness artifact** of dispatching a subagent with a
  "go read these files" instruction — it persists even when the agent is told not to narrate,
  and does not occur when a skill is loaded as ambient context in real use. Not skill content;
  not fixable by editing the skill.

Conclusion: scaffolding leakage from skill content is resolved.
