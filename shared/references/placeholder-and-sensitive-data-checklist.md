# Placeholder And Sensitive Data Checklist

Use this file before any "ready to publish" claim.

## Placeholder scan

Look for tokens like:

- `{{PROJECT_NAME}}`
- `{{MAINTAINER_NAME}}`
- `{{MAINTAINER_CONTACT}}`
- `{{REPOSITORY_URL}}`
- `{{SUPPORT_CHANNEL}}`
- `{{SECURITY_CONTACT}}`

If placeholders remain, report them explicitly.

## Sensitive data scan

Review for:

- personal email addresses the maintainer did not mean to publish
- internal URLs or private documentation links
- tokens, secrets, `.env` examples with real values
- screenshots containing personal or internal data
- organization-specific policies copied into a public repo without approval

## Publishing rule

Do not say the project is publish-ready when either:

- placeholders remain in visible user-facing files
- sensitive data has not been reviewed

## Use with the suite

- `oss-repo-audit` uses this to flag blockers.
- `oss-community-files` uses this after filling templates.
- `oss-publish-github` uses this as a final local check before push guidance.
