import numpy as np
from scipy import stats


def statistic(x):
    # Calculates the Jarque-Bera Statistic
    n = len(x)
    mu = np.mean(x, axis=0)
    x = x - mu  # remove the mean from the data
    s = stats.skew(x)  # calculate the sample skewness
    k = stats.kurtosis(x)  # calculate the sample kurtosis
    statistic = n / 6 * (s**2 + k**2 / 4)
    return statistic


def statistic_vectorized(x, axis=0):
    # fast for monte_carlo_test
    n = x.shape[axis]
    mu = np.mean(x, axis=axis, keepdims=True)
    x = x - mu  # remove the mean from the data
    s = stats.skew(x, axis=axis)  # calculate the sample skewness
    k = stats.kurtosis(x, axis=axis)  # calculate the sample kurtosis
    statistic = n / 6 * (s**2 + k**2 / 4)
    return statistic


x = np.array([148, 154, 158, 160, 161, 162, 166, 170, 182, 195, 236])
norm_dist = stats.norm()
res = stats.monte_carlo_test(
    sample=x,
    rvs=norm_dist.rvs,
    statistic=statistic,
    n_resamples=10000,
    alternative="greater",
)
print(f"Observed values of the statistic: {res.statistic}")
print(f"Monte Carlo p-value: {res.pvalue}")
print(f"Empirical null distribution shape: {res.null_distribution.shape}")
