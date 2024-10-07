import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x1 = stats.norm.rvs(loc=1.0, scale=1.0, size=10)
kde1 = stats.gaussian_kde(x1)
xs = np.linspace(x1.min() - 1, x1.max() + 1, 200)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x1, np.zeros(x1.shape), "b+", ms=20)  # rug plot
x_eval = np.linspace(-10, 10, num=200)
ax.plot(x_eval, kde1(x_eval), "k-", label="Scott's Rule")
ax.plot(xs, stats.norm.pdf(xs, loc=1.0, scale=1.0), "r--", label="True PDF")
plt.show()
