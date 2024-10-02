import numpy as np
import scipy as sp


# 一元函数求根
def func(x):
    return x + 2 * np.cos(x)


sol = sp.optimize.root(func, 0.3)
sol.x
sol.fun


# 二元函数求根
def func2(x):
    f = [x[0] * np.cos(x[1]) - 4, x[1] * x[0] - x[1] - 5]
    jac = np.array([[np.cos(x[1]), -x[0] * np.sin(x[1])], [x[1], x[0] - 1]])
    return f, jac


sol = sp.optimize.root(func2, [1, 1], jac=True, method="lm")
sol.x
