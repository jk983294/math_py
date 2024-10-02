import numpy as np
import scipy as sp


def objective_function(x):
    return 3 * x**4 - 2 * x + 1


# 一元函数优化求解
sp.optimize.minimize_scalar(
    objective_function, bracket=(-1, 0)  # bracket provide start point to search
)
sp.optimize.minimize_scalar(
    objective_function, method="bounded", bounds=(-1, 0)
)  # with constrain


# 多元函数优化求解
n_buyers = 10
n_shares = 15
prices = np.random.random(n_buyers)
money_available = np.random.randint(1, 4, n_buyers)
n_shares_per_buyer = money_available / prices
constraint = sp.optimize.LinearConstraint(np.ones(n_buyers), lb=n_shares, ub=n_shares)
bounds = [(0, n) for n in n_shares_per_buyer]
res = sp.optimize.minimize(
    lambda x, prices: -x.dot(prices),
    x0=10 * np.random.random(n_buyers),
    args=(prices,),
    constraints=constraint,
    bounds=bounds,
)
print("The total number of shares is:", sum(res.x))
print("Leftover money for each buyer:", money_available - res.x * prices)
