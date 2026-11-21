# Lab 1: GitHub Foundations

**Estimated time:** 45 minutes

## Objectives

- Create and configure a repository.
- Use issues and project conventions.
- Configure a repository through the UI and GitHub CLI.

## Prerequisites

- GitHub account
- GitHub CLI authenticated
- Git installed

## 1. Create the repository

Create a private repository named `gh-600-lab-01`.

```powershell
gh repo create gh-600-lab-01 --private --clone
cd gh-600-lab-01
```

## 2. Add repository files

Create a README and a LICENSE, then commit and push:

```powershell
"# GH-600 Lab 1" | Out-File -FilePath README.md -Encoding utf8
git add README.md
git -c user.name="Learner" -c user.email="learner@example.com" commit -m "Initialize repository"
git branch -M main
git push -u origin main
```

## 3. Create delivery conventions

In the GitHub UI:

1. Create labels: `bug`, `enhancement`, `needs-review`, and `security`.
2. Create an issue named `Prepare repository quality baseline`.
3. Add a milestone named `Course completion`.
4. Add the issue to the milestone and assign it to yourself.

## 4. Use the GitHub CLI

```powershell
gh issue list
gh issue view 1
gh repo view --web
```

## Success criteria

- Repository exists on GitHub.
- README and commit are visible on the default branch.
- Issue and milestone are configured.
- Learner can identify repository owner, visibility, and default branch.
