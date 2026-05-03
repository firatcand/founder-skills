![Banner]([./assets/banner.png](https://github.com/firatcand/founder-skills/blob/fe2173718aa6ba1ba4723dc703f4649bd38d1231/founder-skills-banner%402x.png))
# Founder Skills

Claude Code skills for founders building B2B SaaS — covering GTM, product, engineering, design, and content.

Built by a three-time founder who scaled an open-source authorization platform to enterprise customers (Adobe, MasterCard, P&G) and acquisition. These skills encode hard-won playbooks into reusable Claude Code instructions.

## Install

```bash
# Browse available skills
npx skills add firatcand/founder-skills --list

# Install a specific skill
npx skills add firatcand/founder-skills --skill copywriter-skill -a claude-code

# Install multiple skills
npx skills add firatcand/founder-skills --skill sales-skill --skill product-position -a claude-code

# Install all skills
npx skills add firatcand/founder-skills --all -a claude-code

# Install globally (available in every project)
npx skills add firatcand/founder-skills --skill copywriter-skill -g -a claude-code
```

Alternative installer (cross-agent — works with Cursor, Windsurf, Aider, Codex too):

```bash
npx openskills install firatcand/founder-skills
```

## Skills

### Go-To-Market

| Skill | What it does |
|-------|-------------|
| **[sales-skill](./sales-skill)** | B2B SaaS sales execution — discovery, demos, objection handling, MEDDPICC, deal reviews, negotiation |
| **[prospecting](./prospecting)** | ICP definition, account tiering, cadence design, cold calling, LinkedIn outreach, signal-based selling |
| **[channel-expert](./channel-expert)** | Acquisition channel strategy — CAC benchmarks, channel selection, outbound vs inbound, budget allocation |
| **[product-position](./product-position)** | Positioning, messaging hierarchy, competitive framing, category design, strategic narratives |
| **[copywriter-skill](./copywriter-skill)** | Clarity-first commercial copy — landing pages, emails, CTAs, headlines. Grounded in Ogilvy, Zinsser, Hopkins |
| **[seo](./seo)** | SEO & AEO for early-stage startups — keyword strategy, technical audits, schema markup, AI citation optimization |
| **[plg-skill](./plg-skill)** | Product-Led Growth — freemium/trial design, activation metrics, PQL definitions, viral loops, PLG readiness |
| **[pricing](./pricing)** | SaaS pricing strategy — value metrics, tier design, packaging, WTP research, pricing page optimization |

### Product & Engineering

| Skill | What it does |
|-------|-------------|
| **[product-spec](./product-spec)** | PRDs, feature specs, user stories, acceptance criteria. Includes spec audit mode |
| **[software-architect](./software-architect)** | Architecture decisions — monolith vs micro, database selection, CQRS, tech stack tradeoffs. Fowler, Richardson, Kleppmann |
| **[devops](./devops)** | Cloud architecture, CI/CD, Kubernetes, IaC, observability, SRE, platform engineering |
| **[data-analysis](./data-analysis)** | Product and GTM analytics — funnels, cohort retention, A/B testing, dashboards, metric design |

### Design

| Skill | What it does |
|-------|-------------|
| **[ui-design](./ui-design)** | UI design principles — spacing, visual hierarchy, typography, color systems, accessibility |
| **[ux-design](./ux-design)** | UX audit and design specs — Gestalt principles, progressive disclosure, affordance, feedback |
| **[graphic-design](./graphic-design)** | Color, typography, layout, branding, WCAG accessibility, design systems for non-designers |

### Content & Prompting

| Skill | What it does |
|-------|-------------|
| **[script-writer-skill](./script-writer-skill)** | Video and podcast scripts — TikTok, Reels, YouTube Shorts/long-form, hooks, retention, CTAs |
| **[motion-picture](./motion-picture)** | Video production planning — storyboards, shot lists, color scripts, pacing, animation principles |
| **[prompt-architect](./prompt-architect)** | Write, critique, rewrite, compare, and template LLM prompts. Prompt Architect 3.0 methodology |
| **[prompt-engineering-patterns](./prompt-engineering-patterns)** | Advanced prompt engineering — chain-of-thought, few-shot, system prompts, optimization techniques |

## How Skills Work

Each skill is a `SKILL.md` file with optional `references/` for deep knowledge bases. Claude Code loads the skill description into context at all times (for triggering), then reads the full `SKILL.md` + references only when the skill activates.

```
skill-name/
├── SKILL.md              # Orchestration layer (frontmatter + instructions)
└── references/           # Deep knowledge bases loaded on demand
    └── knowledge-base.md
```

Skills follow Anthropic's [Agent Skills specification](https://www.npmjs.com/package/skills).

## Manual Install

If you prefer not to use the CLI:

```bash
# Clone the repo
git clone https://github.com/firatcand/founder-skills.git

# Symlink a skill into Claude Code
mkdir -p ~/.claude/skills
ln -s $(pwd)/founder-skills/copywriter-skill ~/.claude/skills/copywriter-skill
```

Or for project-level:

```bash
mkdir -p .claude/skills
ln -s /path/to/founder-skills/copywriter-skill .claude/skills/copywriter-skill
```

## License

MIT
