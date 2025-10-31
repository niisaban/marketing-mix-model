
---

### `.github/ISSUE_TEMPLATE/ci-cd-issue.md`
```markdown
---
name: "CI/CD workflow issue"
about: Report failures or flakiness in GitHub Actions or release pipelines.
title: "ci: <workflow> failing on <event/branch>"
labels: ["ci"]
assignees: []
---

## Workflow details
- Workflow file: <!-- e.g., .github/workflows/ci.yml -->
- Trigger/event: <!-- push, pull_request, schedule, workflow_dispatch -->
- Branch/PR: <!-- main, feature-x, #123 -->
- Failing job/step: <!-- build / test / upload-artifact, etc. -->

## Runs
- Failing run URL: <!-- paste link -->
- Last known green run URL (if any):

## Logs / artifacts
```text
# Paste the most relevant 20–50 lines (scrub secrets).
