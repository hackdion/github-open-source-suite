# GitHub Open Source Suite Design

## Goal

Build a reusable skill suite for Codex that standardizes the path from:

1. development-nearly-complete local work
2. open-source readiness
3. GitHub publishing and first release
4. long-term maintainer operations

The suite is intended for global reuse, not just this repository. It must reduce repeated rediscovery of GitHub open source practices, encode sustainable defaults, and avoid improvised boilerplate.

## Scope

Cover these repository types:

- skills
- MCP servers
- plugins
- small and medium projects
- libraries
- CLI tools
- docs-first repositories
- automation or script repositories

Cover the full lifecycle with a default automation posture of:

- auto-execute low-risk local edits and low-risk GitHub drafting work
- require confirmation before high-impact GitHub actions such as repository creation, push, visibility changes, destructive edits, publishing a release, or changing repository structure

## Product Shape

Use a skill suite rather than a single large skill.

Rationale:

- the workflows are related but not identical
- different moments in the lifecycle need different triggers
- the suite can keep each SKILL.md smaller and more reusable
- templates and reference material can be shared without bloating every invocation

## Proposed Skills

### 1. `oss-repo-bootstrap`

Purpose:
Bootstrap the current local directory into a repository that is ready for the rest of the open-source workflow.

Primary responsibilities:

- detect whether the current directory is already a git repository
- run `git init` when needed
- recommend or create a minimal `.gitignore` based on repository type
- check whether a first commit is needed
- suggest default branch naming and initial repository hygiene
- prepare the workspace for later audit and publishing steps
- stop for confirmation before creating remotes, pushing, or performing high-impact git actions

Typical triggers:

- "Initialize this project for GitHub"
- "This folder is not a git repo yet"
- "Turn this local project into a publishable repository"

### 2. `oss-repo-audit`

Purpose:
Inspect a local repository, classify it, identify readiness gaps, and produce a prioritized open-source checklist.

Primary responsibilities:

- inspect local files, configuration, dependency manifests, docs, git state, and release signals first
- classify repository type
- map missing items against GitHub community health expectations
- detect blockers, placeholders, secrets risk, and unsustainable promises
- decide whether the repository is ready for community-file generation or needs upstream fixes first

Typical triggers:

- "Help me open source this repo"
- "Check whether this project is ready for GitHub"
- "Audit this project before publishing"

### 3. `oss-community-files`

Purpose:
Generate or improve the minimum healthy set of community and governance files using repository-aware templates.

Primary responsibilities:

- README hardening
- LICENSE guidance and fill-in support
- CONTRIBUTING
- CODE_OF_CONDUCT
- SECURITY
- SUPPORT
- issue forms or issue templates
- PR template
- `.github/` layout normalization
- placeholder inventory and replacement instructions

Typical triggers:

- "Add standard community files"
- "Set up GitHub health files"
- "Create issue and PR templates"

### 4. `oss-publish-github`

Purpose:
Prepare the repository for GitHub publication and assist with low-risk publishing steps.

Primary responsibilities:

- verify publish prerequisites locally
- prepare repository metadata suggestions
- prepare topics, description, homepage, and support links
- draft release checklist
- draft first release notes
- assist with repository settings guidance
- stop for confirmation before push, create-repo, visibility, or other high-impact actions

Typical triggers:

- "Publish this to GitHub"
- "Make this GitHub-ready"
- "Help me push this project publicly"

### 5. `oss-release-management`

Purpose:
Standardize first-release and ongoing release operations.

Primary responsibilities:

- release readiness checks
- changelog and version-note conventions
- draft tag and release note content
- pre-release versus stable release guidance
- asset attachment checklist
- post-release verification checklist

Typical triggers:

- "Prepare the first release"
- "Draft release notes"
- "Cut a release for this project"

### 6. `oss-maintainer-operations`

Purpose:
Standardize post-publication maintenance, triage, and contribution handling.

Primary responsibilities:

- issue triage rules
- PR review intake and contributor expectations
- support-channel boundaries
- security-reporting routing
- maintenance-status signaling
- backlog hygiene
- sustainable response promises

Typical triggers:

- "Set up maintainer workflow"
- "How should I maintain this repo"
- "Add long-term contribution and support rules"

## Shared Resources

The suite should share common references and templates from one suite root.

### `references/`

Create references that are loaded on demand:

- `github-community-health-baseline.md`
  - GitHub community profile expectations
  - README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT
  - issue and PR template expectations
- `repo-classification-guide.md`
  - rules for classifying skills, MCPs, plugins, libraries, CLIs, apps, docs repos
  - minimum viable file set by repository type
- `release-and-versioning-guide.md`
  - when to suggest changelog, semantic versioning, release notes, pre-release labels
- `maintainer-ops-guide.md`
  - triage, support, boundaries, stale policies, sustainability guidelines
- `placeholder-and-sensitive-data-checklist.md`
  - placeholders, private URLs, emails, tokens, internal references, accidental disclosure checks
- `publication-inputs-checklist.md`
  - one-shot collection of blocking inputs before file generation or GitHub publication actions
  - license options, owner and repo slug, documentation language, support channel, security route, and GitHub settings automation choices
- `official-sources.md`
  - curated list of GitHub Docs, Open Source Guides, and license sources used by the suite

### `assets/`

Provide reusable templates with explicit placeholders:

- `assets/community/README-template.md`
- `assets/community/CONTRIBUTING-template.md`
- `assets/community/CODE_OF_CONDUCT-template.md`
- `assets/community/SECURITY-template.md`
- `assets/community/SUPPORT-template.md`
- `assets/community/pull_request_template.md`
- `assets/community/ISSUE_TEMPLATE/bug_report.yml`
- `assets/community/ISSUE_TEMPLATE/feature_request.yml`
- `assets/community/ISSUE_TEMPLATE/config.yml`
- `assets/releases/release-checklist.md`
- `assets/releases/release-notes-template.md`
- `assets/maintenance/triage-playbook.md`

Template rules:

- use placeholders only where repository-specific data is required
- clearly mark placeholders with a consistent token format
- avoid making promises maintainers cannot sustain
- keep wording neutral and adaptable

### Optional `scripts/`

Only add scripts where deterministic repeatability materially helps:

- community-profile gap scanner
- placeholder scanner
- release-readiness checker

Scripts are optional in v1. The first version can ship with only SKILL files, references, and templates if that keeps delivery simpler and more maintainable.

## Suite Layout

Recommended filesystem layout:

```text
github-open-source-suite/
├── shared/
│   ├── references/
│   └── assets/
├── oss-repo-bootstrap/
│   ├── SKILL.md
│   └── agents/openai.yaml
├── oss-repo-audit/
│   ├── SKILL.md
│   └── agents/openai.yaml
├── oss-community-files/
│   ├── SKILL.md
│   └── agents/openai.yaml
├── oss-publish-github/
│   ├── SKILL.md
│   └── agents/openai.yaml
├── oss-release-management/
│   ├── SKILL.md
│   └── agents/openai.yaml
└── oss-maintainer-operations/
    ├── SKILL.md
    └── agents/openai.yaml
```

Alternative:

- keep the suite root as the current repository
- place each skill folder at the repository root
- place shared references and assets in a shared top-level folder

This alternative is likely easier for this project.

## Workflow Design

### Expected flow across the suite

1. `oss-repo-audit`
2. `oss-repo-audit`
3. `oss-community-files`
4. `oss-publish-github`
5. `oss-release-management`
6. `oss-maintainer-operations`

The suite must also support partial entry points:

- users may start directly at community files
- users may start directly at release management
- users may ask only for maintenance setup

Each skill should:

- check whether earlier prerequisites are missing
- recommend the previous skill when needed
- still do useful bounded work when safe

## Automation Boundaries

Default behavior:

- allow automatic local analysis
- allow automatic drafting of local files
- allow automatic preparation of GitHub-facing text such as release drafts, issue forms, or metadata suggestions
- require user confirmation before push, create repository, change visibility, publish release, overwrite existing high-signal docs, or perform destructive GitHub actions

This matches the user's requested default posture.

## Upfront Input Collection

The suite should not ask for blocking publication inputs one by one during execution when they can be identified upfront.

Before generating user-facing root files or starting GitHub publication work, the suite should gather the blocking set in one pass:

- project display title
- GitHub `owner`
- GitHub `repo` slug
- license choice
- documentation language
- support channel
- security reporting route
- whether GitHub Discussions should be enabled
- whether browser-based GitHub settings changes are allowed
- whether the first release should be drafted

License selection is mandatory and should offer at least:

- `MIT`
- `Apache-2.0`
- `BSD-3-Clause`
- `GPL-3.0`

If a maintainer has known defaults, the suite should reuse them explicitly instead of re-asking mid-flow.

## Quality Rules

Every skill in the suite should enforce:

- local-first inspection before remote assumptions
- no "publish-ready" or "done" claim without fresh verification evidence
- explicit distinction between placeholders and final values
- minimal sustainable standards over bloated policy files
- repository-type-aware output rather than generic boilerplate
- clear escalation when license choice or policy wording has legal or organizational implications

## Required Superpowers And Related Skills

Use these process skills with the suite:

- `brainstorming`
  - required for suite design and major evolution
- `skill-creator`
  - required for creating and validating each skill
- `verification-before-completion`
  - required before claiming the suite or any generated output is complete

Useful companion skills:

- `writing-plans`
  - for implementation planning after this design is approved
- `requesting-code-review`
  - for final review of the suite before broader reuse

Do not require `SpecForge` by default for v1.

Reason:

- this is a reusable skill-suite product and workflow package, not a product-feature spec pipeline
- `SpecForge` can be used later if the project grows into a larger maintained system with roadmap, FRD, TDD, and implementation task decomposition needs

## Source Of Truth

Base the suite primarily on GitHub official documentation and GitHub-adjacent primary sources, then layer community best practices where they do not conflict.

Initial authoritative source set:

- GitHub Docs on community profile and healthy contributions
- GitHub Docs on code of conduct, security policy, support resources, and issue or PR templates
- GitHub Docs on releases
- Choose a License
- Open Source Guides

The suite should prefer official GitHub requirements when there is a conflict between blog advice and platform behavior.

## Non-Goals For V1

Do not include in v1:

- automatic repository creation and push without confirmation
- opinionated CI setup for every repository type
- full legal advice on license compatibility
- heavy automation scripts unless the need becomes obvious during iteration
- repository-type-specific sub-skills beyond the 5 core suite skills

## Implementation Plan Preview

After this design is approved, the next phase should:

1. initialize the repository structure for the suite
2. initialize git for the current directory if it is not already a repository
3. create shared references and shared template assets
4. initialize all 6 skills with `skill-creator` conventions
5. write each `SKILL.md` with concise triggers and workflow boundaries
6. generate `agents/openai.yaml` for each skill
7. validate every skill
8. forward-test at least representative skills on realistic prompts

## Self-Review

This design is intentionally constrained:

- 6 skills instead of a larger fragmented set
- shared references and templates instead of duplicated instructions
- official GitHub baseline first, community practice second
- confirmation gate before high-impact GitHub actions

Open future extension points remain available for:

- scripts
- repository-type-specific overlays
- GitHub Actions recommendations
- maintainer metrics and stale automation
