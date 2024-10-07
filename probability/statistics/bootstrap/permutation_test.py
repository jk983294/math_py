import numpy as np
from scipy import stats

x = np.array([94, 197, 16, 38, 99, 141, 23])  # treatment group
y = np.array([52, 104, 146, 10, 51, 30, 40, 27, 46])  # control group


def statistic(x, y):
    return np.mean(x) - np.mean(y)


print(statistic(x, y))
res = stats.permutation_test(
    (x, y), statistic, alternative="greater", n_resamples=np.inf
)
res.pvalue
