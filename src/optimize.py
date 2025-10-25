import numpy as np
import pandas as pd

def greedy_reallocate(current_spend, roi_share, total_budget=None, steps=20):
    """Toy budget optimizer: shifts small chunks toward higher ROI share.
    current_spend: Series of channel -> spend
    roi_share: Series of channel -> [0,1] shares (higher is better)
    """
    s = current_spend.copy().astype(float)
    if total_budget is None:
        total_budget = s.sum()
    chunk = total_budget * 0.02  # 2% chunk
    for _ in range(steps):
        give = s.idxmax()  # simplistic: take from largest spender
        take = roi_share.idxmax()
        if give == take:
            break
        s[give] = max(0.0, s[give] - chunk)
        s[take] += chunk
    # ensure budget conserved
    s *= total_budget / s.sum()
    return s
