import numpy as np
import scipy as sp
from scipy import stats
from numpy.random import default_rng


stats.norm.mean()  # 0.
stats.norm.std()  # 1.
stats.norm.var()  # 1.
rv = stats.norm()
dir(rv)
stats.norm.cdf(0)
stats.norm.cdf(np.array([-1.0, 0, 1]))
stats.norm.pdf(np.array([-1.0, 0, 1]))
stats.norm.ppf(np.array([0.25, 0.5, 0.75]))  # quantile
stats.norm.rvs(loc=1.0, scale=1.0, size=3)  # sample

rng = default_rng(42)
stats.norm.rvs(size=3, random_state=rng)  # reproduciable sample
