---
name: "Performance issue"
about: Report slowdowns or high resource use and propose a target.
title: "perf: <area> is slow/heavy under <conditions>"
labels: ["performance"]
assignees: []
---

## Impact
- What is slow/heavy? <!-- function, step, script, notebook -->
- Workload size: <!-- rows, features, iterations, etc. -->
- Severity: Low / Medium / High
- User impact: <!-- wall time, memory, cost, UX -->

## Reproduction
1. Steps:
2. Data/sample (or synthetic snippet):
3. Command/script:
```bash
# example
pytest -q -k test_slow_case
