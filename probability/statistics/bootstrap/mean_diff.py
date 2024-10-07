import numpy as np
from scipy import stats

x = np.array([94, 197, 16, 38, 99, 141, 23])
y = np.array([52, 104, 146, 10, 51, 30, 40, 27, 46])


def statistic(x, y, axis=0):
    return np.mean(x, axis=axis) - np.mean(y, axis=axis)


observed_statistic = statistic(x, y)
res = stats.bootstrap((x, y), statistic, n_resamples=1000, method="percentile")
print(f"Observed Statistic Value: {observed_statistic}")
print(f"Standard Error: {res.standard_error}")
res.confidence_interval
ci_percentile = stats.scoreatpercentile(res.bootstrap_distribution, [2.5, 97.5])
