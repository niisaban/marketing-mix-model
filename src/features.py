import numpy as np
import pandas as pd
from .transforms import adstock, hill_saturation

def design_matrix(df, channels=('search','social','audio','display'),
                  decay=0.6, alpha=1.2, k=500.0):
    X = {}
    for ch in channels:
        col = f'spend_{ch}'
        a = adstock(df[col].values, decay=decay)
        s = hill_saturation(a, alpha=alpha, k=k)
        X[f'{ch}_x'] = s
    X_df = pd.DataFrame(X, index=df.index)
    X_df['trend'] = df['trend'].values
    X_df['season'] = df['season'].values
    return X_df
