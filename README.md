# Marketing Mix Modeling (MMM) — Ridge + Adstock + Saturation

**MMM = Marketing Mix Modeling**.  
We simulate weekly KPIs (e.g., subscriptions) and channel spends, transform spends with **adstock** (carry‑over) and **saturation** (diminishing returns), then fit a **ridge regression** to attribute impact and explore **budget reallocation**.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/run_end_to_end.py
pytest -q
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
