# Lab 5: Packages and Releases

**Estimated time:** 45 minutes

## Objectives

- Package or artifact a release.
- Create a semantic version tag.
- Generate release notes.
- Publish release assets.

## 1. Prepare a version

Use semantic versioning:

- `MAJOR.MINOR.PATCH`
- Increment the patch version for a bug fix.
- Increment the minor version for a backward-compatible feature.
- Increment the major version for a breaking change.

## 2. Create a release

```powershell
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
gh release create v1.0.0 --generate-notes --title "GH-600 v1.0.0"
```

## 3. Attach an artifact

Build a release archive or text artifact and attach it:

```powershell
"Release v1.0.0" | Out-File release.txt -Encoding utf8
gh release upload v1.0.0 release.txt
```

## 4. Review release metadata

Confirm:

- Tag target
- Release name
- Generated notes
- Asset
- Pre-release status
- Latest release state

## Success criteria

- A semantic version tag exists.
- A release includes generated notes.
- A release asset is downloadable.
