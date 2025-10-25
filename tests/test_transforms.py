import numpy as np
from src.transforms import adstock, hill_saturation

def test_adstock_monotone_decay():
    x = [100, 0, 0, 0]
    out = adstock(x, decay=0.5)
    assert out[1] < out[0] and out[2] < out[1]

def test_hill_bounds():
    x = np.linspace(0, 1000, 50)
    y = hill_saturation(x, alpha=1.2, k=500)
    assert (y >= 0).all() and (y <= 1).all()
