import numpy as np
import pandas as pd

def simulate_weekly(n_weeks=104, seed=0):
    rng = np.random.default_rng(seed)
    weeks = np.arange(n_weeks)
    # baseline + slow growth
    trend = 200 + 0.5 * weeks
    season = 10 * np.sin(2 * np.pi * weeks / 52)

    channels = ['search', 'social', 'audio', 'display']
    spends = {ch: rng.gamma(shape=5, scale=200, size=n_weeks) for ch in channels}

    df = pd.DataFrame({'week': weeks, 'trend': trend, 'season': season})
    for ch in channels:
        df[f'spend_{ch}'] = spends[ch]
    # noise term
    df['eps'] = rng.normal(0, 15, size=n_weeks)
    return df
