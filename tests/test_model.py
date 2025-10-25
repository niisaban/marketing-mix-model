from src.simulate import simulate_weekly
from src.features import design_matrix
from src.model import fit_mmm

def test_fit_runs():
    df = simulate_weekly(n_weeks=60, seed=1)
    # simple KPI
    from src.features import design_matrix
    X = design_matrix(df)
    df['kpi'] = X.sum(axis=1)  # toy
    model, Xmat, coef = fit_mmm(df, y_col='kpi')
    assert len(coef) == Xmat.shape[1]
