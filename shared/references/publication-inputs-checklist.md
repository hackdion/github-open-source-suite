# Publication Inputs Checklist

Use this file before generating high-signal community files or attempting GitHub publication steps.

## Core rule

Collect all blocking inputs in one pass before starting execution. Do not ask one question at a time when the required inputs are already knowable upfront.

## Required upfront inputs

Capture these before drafting or remote actions:

- project display title
- GitHub `owner`
- GitHub `repo` slug
- license choice
- documentation language
- support channel
- security reporting route
- whether GitHub Discussions should be enabled
- whether the agent may attempt browser-based GitHub settings changes
- whether a first release should be drafted

## License choices

At minimum, offer:

- `MIT`
- `Apache-2.0`
- `BSD-3-Clause`
- `GPL-3.0`

Do not skip the license question. If the maintainer has a stable default, apply it explicitly and report that default.

## Support channel choices

At minimum, clarify whether support should go to:

- `GitHub Issues`
- `GitHub Discussions + Issues`
- another explicit channel

## Security route choices

Clarify:

- whether `SECURITY.md` should be created locally before publication
- whether the published repo should enable GitHub private vulnerability reporting
- what fallback path exists if the private reporting entry is not yet available

## Execution model

- Reuse known maintainer defaults instead of re-asking mid-work.
- If a value is unknown but non-blocking, keep it as a visible placeholder.
- If a value is blocking for a high-impact action, stop once, ask for the full missing set, then continue.

## Use with the suite

- `oss-community-files` uses this before generating user-facing root files.
- `oss-publish-github` uses this before any remote or publication prep.
- `oss-release-management` uses this before release drafting when repo metadata is still incomplete.
