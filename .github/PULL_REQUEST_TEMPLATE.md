## What
<!-- Briefly describe the change. -->

## Why
<!-- Why this is needed / what it improves. -->

## Changes
- [ ] Code
- [ ] Docs / README
- [ ] CI / workflow
- [ ] Other: __________

## How to test
1. Create/activate venv
2. Install deps: `pip install -r requirements.txt`
3. Run tests:
   - **PowerShell**  
     ```powershell
     $env:PYTHONPATH = (Get-Location).Path
     pytest -q --maxfail=1 -ra
     ```
   - **bash/zsh**  
     ```bash
     export PYTHONPATH="$PWD"
     pytest -q --maxfail=1 -ra
     ```

## Screenshots / Logs (if relevant)
<!-- paste or attach -->

## Risk / Rollout
- Risk: Low / Medium / High
- Rollback: Revert this PR
- Affects: Docs / Tests / Runtime / CI

## Checklist
- [ ] CI green
- [ ] Branch up-to-date with `main`
- [ ] Tests added/updated where needed
- [ ] Docs updated (README/CHANGELOG as appropriate)
