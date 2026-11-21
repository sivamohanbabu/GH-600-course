# Lab 4: Security and Compliance

**Estimated time:** 60 minutes

## Objectives

- Configure a security policy.
- Enable dependency and secret scanning.
- Review security findings.
- Practice secret exposure response.

## 1. Add a security policy

Create `SECURITY.md`:

```markdown
# Security Policy

## Reporting

Report suspected vulnerabilities privately through GitHub Security Advisories.

## Supported versions

The latest release on the default branch is supported.
```

## 2. Enable repository security features

In **Settings** > **Advanced Security**:

1. Enable Dependabot alerts.
2. Enable Dependabot security updates.
3. Enable secret scanning.
4. Enable push protection.
5. Enable code scanning.

## 3. Add dependency review

Create a pull request workflow that uses `actions/dependency-review-action`.

## 4. Secret response simulation

Do not use a real credential. Add a clearly fake secret to a feature branch and attempt to push it. Observe push protection. If an exposure occurs in an exercise repository, rotate the credential and document remediation.

## 5. Security review

For each finding:

- Assign severity.
- Identify the affected component.
- Decide to fix, accept, or defer.
- Record a remediation owner and due date.

## Success criteria

- Security policy exists.
- Security features are enabled.
- Push protection behavior is demonstrated.
- Learner can describe an incident response sequence.
