import numpy as np
import scipy as sp
from scipy import stats


stats.expon.mean()
stats.expon.std()
stats.expon.var()
stats.expon.cdf(0)
stats.expon.cdf(np.array([-1.0, 0, 1]))
stats.expon.pdf(np.array([-1.0, 0, 1]))
stats.expon.ppf(np.array([0.25, 0.5, 0.75]))  # quantile
stats.expon.rvs(scale=2.0, size=3)  # sample, scale  = 1./lambda
