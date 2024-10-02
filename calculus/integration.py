import numpy as np
import scipy as sp


def integrand(x, a, b):
    return a * x**2 + b


a = 2
b = 1
res = sp.integrate.quad(integrand, 0, 1, args=(a, b))


# 二重积分
area = sp.integrate.dblquad(
    lambda x, y: x * y, 0, 0.5, lambda x: 0, lambda x: 1 - 2 * x
)


# n重积分
def f(x, y):
    return x * y


def bounds_y():
    return [0, 0.5]


def bounds_x(y):
    return [0, 1 - 2 * y]


sp.integrate.nquad(f, [bounds_x, bounds_y])
