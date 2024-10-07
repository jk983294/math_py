import numpy as np
import scipy as sp
from scipy import stats

x = stats.t.rvs(10, size=1000)
print("normal skewtest teststat = %6.3f pvalue = %6.4f" % stats.skewtest(x))
print("normal kurtosistest teststat = %6.3f pvalue = %6.4f" % stats.kurtosistest(x))
print("normaltest teststat = %6.3f pvalue = %6.4f" % stats.normaltest(x))
standarded_x = (x - x.mean()) / x.std()
print("normaltest teststat = %6.3f pvalue = %6.4f" % stats.normaltest(standarded_x))
stat2, _ = stats.jarque_bera(x)
stats.jarque_bera(x).pvalue


def statistic(x):
    # Calculates the Jarque-Bera Statistic
    # Compare against `scipy.stats.jarque_bera`:
    n = len(x)
    mu = np.mean(x, axis=0)
    x = x - mu  # remove the mean from the data
    s = stats.skew(x)  # calculate the sample skewness
    k = stats.kurtosis(x)  # calculate the sample kurtosis
    statistic = n / 6 * (s**2 + k**2 / 4)
    return statistic


statistic(x)
