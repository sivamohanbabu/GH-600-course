# Lab 6: Capstone Delivery Exercise

**Estimated time:** 120 minutes

## Scenario

A team needs to deliver a safe change through the GitHub platform. Working as an individual or in a team, establish repository controls, automate validation, and document delivery evidence.

## Required deliverables

1. Protected `main` branch or ruleset.
2. Issue and pull request demonstrating a change.
3. GitHub Actions workflow that:
   - Runs on pull requests.
   - Checks out the repository.
   - Executes tests.
   - Uploads test evidence.
4. Security configuration evidence.
5. Release tag and GitHub Release.
6. Short delivery record containing decisions and findings.

## Presentation

Present for 10 minutes:

- Architecture and repository workflow
- Permission model and threat controls
- CI/CD and release process
- Security findings and remediation
- Evidence that a change reached the release state

## Hints

- Require at least one approval.
- Use read-only workflow permissions unless a step needs write access.
- Keep secrets in repository or environment secret stores, never in source.
- Demonstrate one control that would stop an unsafe change.
- Link the pull request, workflow run, and release in the delivery record.
