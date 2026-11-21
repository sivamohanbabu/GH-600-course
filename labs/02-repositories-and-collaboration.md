# Lab 2: Repositories and Collaboration

**Estimated time:** 60 minutes

## Objectives

- Create a feature branch.
- Open and review a pull request.
- Configure protected branch rules.
- Demonstrate required review and status behavior.

## 1. Create a feature branch

```powershell
git switch -c feature/readme-update
"## Team workflow" | Add-Content README.md
git add README.md
git commit -m "Document team workflow"
git push -u origin feature/readme-update
```

## 2. Open a pull request

```powershell
gh pr create --base main --head feature/readme-update --title "Document team workflow" --body "Adds team workflow documentation."
```

## 3. Review the change

1. Open the pull request.
2. Add a comment.
3. Request or make a formal approval.
4. Merge only after review requirements are satisfied.

## 4. Add branch protection

In repository settings:

1. Open **Rules** > **Rulesets**.
2. Target the `main` branch.
3. Require a pull request before merging.
4. Require at least one approval.
5. Require conversation resolution before merging.
6. Require a status check once Lab 3 is completed.

## 5. Test enforcement

Attempt to push directly to `main`.

```powershell
git switch main
"direct change" | Add-Content README.md
git add README.md
git commit -m "Test direct push protection"
git push
```

If rules are configured correctly, the push should be rejected or require an alternate rule bypass.

## Success criteria

- A pull request is linked to an issue or milestone.
- Required approval behavior is documented.
- Direct push protection is verified.
