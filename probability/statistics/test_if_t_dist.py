import numpy as np
import scipy as sp
from scipy import stats

x = stats.t.rvs(10, size=1000)
x.min()
x.max()
x.mean()
x.var()
n, (smin, smax), sm, sv, ss, sk = stats.describe(x)
m, v, s, k = stats.t.stats(10, moments="mvsk")  # theoretical mean/variance/skew/kurt
print("KS-statistic D = %6.3f pvalue = %6.4f" % stats.kstest(x, "t", (10,)))
print("t-statistic = %6.3f pvalue = %6.4f" % stats.ttest_1samp(x, m))

# manually calculate t-test
tt = (sm - m) / np.sqrt(sv / float(n))  # t-statistic for mean
pval = stats.t.sf(np.abs(tt), n - 1) * 2  # two-sided pvalue = Prob(abs(t)>tt)
print("t-statistic = %6.3f pvalue = %6.4f" % (tt, pval))

# check tail
crit01, crit05, crit10 = stats.t.ppf([1 - 0.01, 1 - 0.05, 1 - 0.10], 10)
print(
    "critical values from ppf at 1%%, 5%% and 10%% %8.4f %8.4f %8.4f"
    % (crit01, crit05, crit10)
)

freq01 = np.sum(x > crit01) / float(n) * 100
freq05 = np.sum(x > crit05) / float(n) * 100
freq10 = np.sum(x > crit10) / float(n) * 100
print(
    "sample %%-frequency at 1%%, 5%% and 10%% tail %8.4f %8.4f %8.4f"
    % (freq01, freq05, freq10)
)

quantiles = [0.0, 0.01, 0.05, 0.1, 1 - 0.10, 1 - 0.05, 1 - 0.01, 1.0]
crit = stats.t.ppf(quantiles, 10)
n_sample = x.size
freqcount = np.histogram(x, bins=crit)[0]
tdof, tloc, tscale = stats.t.fit(x)
nloc, nscale = stats.norm.fit(x)
tprob = np.diff(stats.t.cdf(crit, tdof, loc=tloc, scale=tscale))
nprob = np.diff(stats.norm.cdf(crit, loc=nloc, scale=nscale))
tch, tpval = stats.chisquare(freqcount, tprob * n_sample)
nch, npval = stats.chisquare(freqcount, nprob * n_sample)
print("chisquare for t:      chi2 = %6.2f pvalue = %6.4f" % (tch, tpval))
print("chisquare for normal: chi2 = %6.2f pvalue = %6.4f" % (nch, npval))
