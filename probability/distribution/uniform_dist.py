import numpy as np
import scipy as sp
from scipy import stats


stats.uniform.mean()
stats.uniform.std()
stats.uniform.var()
stats.uniform.cdf(0)
stats.uniform.cdf(np.array([-1.0, 0, 1]))
stats.uniform.pdf(np.array([-1.0, 0, 1]))
stats.uniform.ppf(np.array([0.25, 0.5, 0.75]))  # quantile
stats.uniform.rvs(scale=2.0, size=3)  # sample
