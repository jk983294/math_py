import numpy as np
from scipy import stats

p = 0.75
dist = stats.bernoulli(p=p)
sample = dist.rvs(size=1000)
vote_for_0 = np.sum(sample == 0)
vote_for_1 = np.sum(sample == 1)
print(f"{vote_for_0} for candidate 0, {vote_for_1} for candidate 1")


def statistic(sample, axis=0):
    return np.sum(sample, axis=axis) / sample.shape[axis]


statistic(sample)

data = (sample,)
# Passing `confidence_level=0.9` produces a 90% confidence interval
res = stats.bootstrap(data, statistic, confidence_level=0.9)
res.confidence_interval
