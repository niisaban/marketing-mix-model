import numpy as np
import pandas as pd

def adstock(x, decay=0.5):
    carry = 0.0
    out = []
    for xi in x:
        carry = xi + decay * carry
        out.append(carry)
    return np.array(out)

def hill_saturation(x, alpha=1.2, k=500.0):
    # S-curve: x^alpha / (x^alpha + k^alpha)
    x = np.asarray(x, dtype=float)
    return (x**alpha) / (x**alpha + k**alpha + 1e-9)
