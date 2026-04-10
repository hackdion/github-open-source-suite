# Release And Versioning Guide

Use this file when deciding whether the repository is ready for a first release or a follow-up release.

## Release prerequisites

Check locally before drafting or publishing:

- the repository has a clear README
- the repository has a license
- install or usage steps were checked recently
- placeholders and private references were reviewed
- open-source file set is present or intentionally scoped down

## Versioning guidance

- Use semantic versioning only when the project’s change surface justifies it.
- For very small or early projects, `0.x` is usually the safe default.
- Do not imply strict compatibility guarantees the maintainer is not ready to honor.

## First release guidance

For a first public release, prepare:

- version label
- short release summary
- highlights list
- breaking changes or limitations
- installation or migration notes if needed

## Release notes rules

- Lead with what changed and who should care.
- Keep a short "Known limitations" section when the project is early.
- Link to docs, not to local-only files or private systems.
- Avoid marketing language that overstates maturity.

## Pre-release versus stable

Suggest pre-release when:

- APIs are likely to change
- setup is still fragile
- documentation is incomplete
- maintainer support expectations are still uncertain

Suggest stable only when:

- onboarding was checked
- core workflows are reproducible
- important repository metadata is filled in

## Changelog guidance

A dedicated changelog is useful when:

- the project has repeat releases
- users need a durable change history
- releases are likely to be consumed without opening GitHub UI

For very early repositories, release notes alone can be enough.

## Use with the suite

- `oss-publish-github` uses this to draft first-release preparation.
- `oss-release-management` uses this to choose release style, version framing, and note structure.
