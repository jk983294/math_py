import numpy as np
import statsmodels.api as sm

# Generate artificial data (2 regressors + constant)
nobs = 1000
X = np.random.random((nobs, 2))
X = sm.add_constant(X)
beta = [1, 0.1, 0.5]
e = np.random.random(nobs)
y = np.dot(X, beta) + e

results = sm.OLS(y, X).fit()

print(results.summary())
