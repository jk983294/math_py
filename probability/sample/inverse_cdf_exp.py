import pandas as pd
import numpy as np
import scipy.stats

# generate samples from the exponential distribution

alpha = 1.0  # exponential distribution parameter
n_samp = 1000  # num of samples
u = scipy.stats.uniform(0, 1)  # define uniform random variable
# define inverse function
Finv = lambda u: 1 / alpha * np.log(1 / (1 - u))
# apply inverse function to samples
v = np.array([Finv(v) for v in u.rvs(n_samp)])

np.mean(v)
np.std(v)
