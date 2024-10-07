import numpy as np
from scipy import stats

x = np.array([7.1, 7.1, 7.2, 8.3, 9.4, 10.5, 11.4])
y = np.array([2.8, 2.9, 2.8, 2.6, 3.5, 4.6, 5.0])

res_asymptotic = stats.spearmanr(x, y, alternative="greater")
res_asymptotic


def statistic(x, y):
    return stats.kendalltau(x, y).correlation


res = stats.permutation_test(
    (x, y),
    statistic,
    alternative="two-sided",
    permutation_type="pairings",
)
res.pvalue
