# Lab 3: GitHub Actions

**Estimated time:** 75 minutes

## Objectives

- Create a workflow triggered by pull requests.
- Run tests and publish an artifact.
- Apply least-privilege workflow permissions.
- Troubleshoot a failed workflow.

## 1. Create the workflow

Create `.github/workflows/python-ci.yml`:

```yaml
name: Python CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - name: Run unit tests
        run: python -m unittest -v
```

## 2. Commit and push

```powershell
git switch main
git add .github/workflows/python-ci.yml
git commit -m "Add Python CI workflow"
git push
```

## 3. Open a pull request

Change `main.py`, push a feature branch, and open a pull request. Confirm the workflow runs.

## 4. Troubleshooting challenge

Add a temporary failing test or change the workflow to invoke a missing command. Inspect the logs, correct the workflow, and rerun it.

```powershell
gh run list
gh run view
```

## 5. Add an artifact

Update the workflow to generate `test-results.txt` and upload it with `actions/upload-artifact@v4`.

## Success criteria

- Pull request workflow completes successfully.
- A failed run is diagnosed and corrected.
- Workflow permissions are limited to `contents: read`.
- An artifact is downloadable.
