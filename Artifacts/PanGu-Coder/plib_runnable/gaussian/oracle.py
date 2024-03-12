import numpy as np
def gaussian(x):
    """
    Gaussian centered around 0.2 with a sigma of 0.1.
    """
    mu = 0.2
    sigma = 0.1
    return np.exp(-(x-mu)**2/sigma**2)
