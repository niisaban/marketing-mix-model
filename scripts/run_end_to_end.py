import numpy as np
import pandas as pd
from src.simulate import simulate_weekly
from src.features import design_matrix
from src.model import fit_mmm, attribute_roi
from src.optimize import greedy_reallocate

def main():
    df = simulate_weekly(n_weeks=104, seed=42)

    # Build a synthetic KPI with known effects
    X = design_matrix(df)
    beta = {
        'search_x': 120.0, 'social_x': 80.0, 'audio_x': 50.0, 'display_x': 30.0,
        'trend': 0.8, 'season': 1.5
    }
    y = sum(beta.get(c,0)*X[c].values for c in X.columns) + df['eps'].values
    df['kpi'] = y

    model, Xmat, coef = fit_mmm(df, y_col='kpi')
    contrib, share = attribute_roi(model, Xmat)

    print("Coefficients:\n", coef)
    print("\nMean contribution by channel:\n", contrib)
    print("\nNormalized ROI share proxy:\n", share)

    current_spend = df[[c for c in df.columns if c.startswith('spend_')]].iloc[-1]
    # Map share index (search_x -> search) to spend columns
    share_simple = share.copy()
    share_simple.index = [i.replace('_x','') for i in share.index]
    # Make sure we align with spend_<channel>
    spend_series = current_spend.copy()
    spend_series.index = [i.replace('spend_','') for i in spend_series.index]
    new_alloc = greedy_reallocate(spend_series, share_simple, total_budget=spend_series.sum(), steps=30)
    print("\nSuggested reallocation (toy):\n", new_alloc.sort_values(ascending=False))

if __name__ == "__main__":
    main()
