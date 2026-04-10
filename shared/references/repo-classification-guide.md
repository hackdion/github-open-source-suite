# Repository Classification Guide

Use this file to classify the repository before generating open-source files or release guidance.

## Classification order

Inspect local evidence in this order:

1. top-level files and folders
2. package and dependency manifests
3. executable entry points
4. documentation shape
5. tests and examples
6. existing git history and release artifacts

## Common repository types

### Skill repository

Signals:

- one or more `SKILL.md` files
- `agents/openai.yaml`
- shared prompts, references, or templates

Minimum file emphasis:

- README
- LICENSE
- CONTRIBUTING
- SUPPORT
- release notes explaining how to use the skills

### MCP server or integration repo

Signals:

- MCP server manifests
- tool definitions
- transport or server setup docs

Minimum file emphasis:

- README with setup and tool list
- SECURITY
- SUPPORT
- issue templates for bug reports and compatibility issues

### Plugin repository

Signals:

- plugin metadata
- install instructions
- integration points

Minimum file emphasis:

- README with compatibility matrix
- CONTRIBUTING
- release guidance

### Library or package

Signals:

- package manifest
- importable source tree
- test suite

Minimum file emphasis:

- README with install and API quick start
- LICENSE
- changelog or release notes path

### CLI tool

Signals:

- executable entrypoint
- command docs or help output

Minimum file emphasis:

- README with install and examples
- issue template for bug reports
- release notes including platform or binary notes when relevant

### Docs-first repository

Signals:

- large docs tree
- limited executable code

Minimum file emphasis:

- README with navigation
- contribution guidance for docs changes
- support routing

### Small or medium project

Signals:

- application code
- examples or screenshots
- user-facing workflow

Minimum file emphasis:

- README with status and scope
- support routing
- issue forms
- security route when the software is runnable by others

## Readiness states

Score repository readiness separately from repository type.

### Local-only

Signals:

- no commits yet
- most files still untracked
- internal milestone wording such as "local V1 complete"
- local validators or tests may pass, but public-facing community routing is missing

### Repo-foundation-ready

Signals:

- git repo exists
- at least one meaningful commit exists
- basic hygiene such as `.gitignore` is present
- public community surface is still incomplete

### Community-surface-ready

Signals:

- minimum public-facing files are present for the repo type
- maintainer routing for support and security is at least drafted
- obvious placeholders, private references, and secret risks were already checked
- GitHub publication metadata or release work may still be incomplete

### Publish-ready

Signals:

- community surface is in good shape
- blocking publication inputs are known
- the next blockers are mostly GitHub-facing actions or confirmations

### Release-ready

Signals:

- publish prep is complete
- version framing and release notes path are chosen
- remaining blockers are release execution or remote confirmation gates

## Classification rules

- Pick the primary type first, then note secondary traits.
- Score readiness separately from type. A skill repo, plugin, or project can still be only local-only.
- Do not generate every possible file just because a repository could use them.
- If the project is tiny, keep the file set minimal but still legally and operationally clear.
- If the repository exposes runnable software or accepts credentials, prefer including `SECURITY.md`.
- Passing local tests or validators does not mean the repository is publish-ready.
- Having a `README` or `LICENSE` alone does not mean the community surface is complete.
- A repo with no commits yet should not be treated as publish-ready even if the files already exist.

## Use with the suite

- `oss-repo-bootstrap` uses the type to suggest `.gitignore`.
- `oss-repo-audit` uses the type and readiness state to score missing files and route the next handoff.
- `oss-community-files` uses the type and readiness state to choose template emphasis and examples.
- `oss-publish-github` uses readiness state to reject premature publication prep.
