[![ci](https://github.com/niisaban/marketing-mix-model/actions/workflows/ci.yml/badge.svg)](https://github.com/niisaban/marketing-mix-model/actions/workflows/ci.yml)


# Marketing Mix Modeling (MMM) — Ridge + Adstock + Saturation

**MMM = Marketing Mix Modeling**.  
We simulate weekly KPIs (e.g., subscriptions) and channel spends, transform spends with **adstock** (carry‑over) and **saturation** (diminishing returns), then fit a **ridge regression** to attribute impact and explore **budget reallocation**.

## Quickstart
```bash
# (Recommended) Python 3.11+
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run a small demo (simulate + analyze)
python scripts/run_demo.py

# Run tests
pytest -q
```
### Run tests locally

#### Windows (PowerShell, current session)
```powershell
# Expose repo root to Python for this shell session
$env:PYTHONPATH = (Get-Location).Path
pytest -q --maxfail=1 -ra
```

#### macOS / Linux (bash/zsh, current session)
```bash
# Expose repo root to Python for this shell session
export PYTHONPATH="$PWD"
pytest -q --maxfail=1 -ra
```

#### (Optional) Windows CMD
```bat
:: Expose repo root to Python for this CMD session
set PYTHONPATH=%CD%

:: Run tests (quiet; stop early; show failure summary)
pytest -q --maxfail=1 -ra
```


## Structure
```
marketing-mix-model/
├─ src/
│  ├─ simulate.py     # synthetic weekly data
│  ├─ transforms.py   # adstock, saturation
│  ├─ features.py     # build design matrix
│  ├─ model.py        # ridge fit + attribution
│  └─ optimize.py     # simple greedy budget optimizer
├─ scripts/
│  └─ run_end_to_end.py
├─ tests/
│  ├─ test_transforms.py
│  └─ test_model.py
├─ data/
│  └─ README.md
├─ requirements.txt
├─ .github/workflows/ci.yml
└─ README.md
```

## Concepts (expanded)
- **Adstock**: advertising effects persist over time; modeled via geometric decay.
- **Saturation**: diminishing returns; we use a Hill function (S‑curve).
- **Ridge regression**: L2 regularization for stable attribution when channels correlate.

## Outputs
- Channel coefficients & normalized **ROAS** proxy.
- A toy **budget optimization** suggestion under a fixed total spend.
- Plots saved to `outputs/` (optional).

> This is intentionally light‑weight (no PyMC/Stan) to keep it interview‑ready.

> Note: run pytest -q locally before pushing.


### Get help / share results

- ❓ Ask a question → [New Q&A](https://github.com/niisaban/marketing-mix-model/discussions/new?category=Q%26A)
- 🎉 Share a result → [New Show & Tell](https://github.com/niisaban/marketing-mix-model/discussions/new?category=Show%20and%20tell)
