# GitHub Community Health Baseline

Use this file when deciding the minimum healthy file set for a public GitHub repository.

## Core baseline

Prioritize these files because GitHub surfaces them in Community Profile and contributor flows:

- `README.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `SUPPORT.md`
- issue templates or issue forms
- pull request template

## Baseline rules

- Start from the minimum sustainable set, not the maximum possible paperwork.
- Prefer repository-aware wording over generic boilerplate.
- Distinguish clearly between required maintainer inputs and default template text.
- Use GitHub-supported filenames and locations first.
- If a file would contain policy promises the maintainer cannot keep, scale it down.

## Repository-level expectations

### `README.md`

Must answer:

- what the project is
- who it is for
- current status
- how to install or use it
- how to contribute or get help

### `LICENSE`

Must exist for an open-source repository. Public code without a license is not safely reusable.

### `CONTRIBUTING.md`

Must explain:

- where to ask questions
- how to open issues
- how to submit changes
- any repo-specific guardrails such as tests, docs, or commit expectations

### `CODE_OF_CONDUCT.md`

Keep it short and standard unless the maintainer needs a custom policy. Include an actionable reporting path.

### `SECURITY.md`

State:

- what kinds of reports belong there
- where to report vulnerabilities
- what not to do, such as posting zero-day details in public issues

### `SUPPORT.md`

Clarify:

- where users should ask for help
- where not to ask
- whether support is best-effort only

### Issue and PR templates

Use templates to improve signal quality. Do not demand unnecessary information.

## File placement

Preferred GitHub-recognized locations:

- repository root
- `.github/`
- `docs/` for selected community files when appropriate

For issue forms and template config, prefer:

- `.github/ISSUE_TEMPLATE/*.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/pull_request_template.md`

## Common failure modes

- missing license
- README that explains only vision, not usage
- CONTRIBUTING that says "PRs welcome" but gives no path
- SECURITY that mixes user support and vulnerability reporting
- templates that demand irrelevant fields
- support promises that imply guaranteed response times

## Use with the suite

- `oss-repo-audit` uses this as the baseline checklist.
- `oss-community-files` uses this to decide what to generate.
- `oss-publish-github` uses this to block premature publication when important gaps remain.
