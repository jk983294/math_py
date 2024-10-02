import numpy as np
import scipy as sp
from scipy import stats


rv = stats.gamma(1, scale=2.0)
rv.mean()
rv.std()
rv.var()
rv.cdf(0)
rv.cdf(np.array([-1.0, 0, 1]))
rv.pdf(np.array([-1.0, 0, 1]))
rv.ppf(np.array([0.25, 0.5, 0.75]))  # quantile
rv.rvs(size=3)  # sample
