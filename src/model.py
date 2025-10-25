import numpy as np
import pandas as pd
from sklearn.linear_model import RidgeCV
from .features import design_matrix

def fit_mmm(df, y_col='kpi', alphas=(0.1, 1.0, 10.0)):
    X = design_matrix(df)
    y = df[y_col].values
    model = RidgeCV(alphas=list(alphas), cv=5).fit(X, y)
    coef = pd.Series(model.coef_, index=X.columns).sort_values(ascending=False)
    return model, X, coef

def attribute_roi(model, X, channel_cols=None):
    if channel_cols is None:
        channel_cols = [c for c in X.columns if c.endswith('_x')]
    # normalize coefficients to sum of positive impacts
    contrib = X[channel_cols].mul(model.coef_[[X.columns.get_loc(c) for c in channel_cols]], axis=1)
    channel_contrib = contrib.mean(axis=0)
    share = (channel_contrib - channel_contrib.min()).clip(lower=0)
    if share.sum() > 0:
        share = share / share.sum()
    return channel_contrib.sort_values(ascending=False), share
