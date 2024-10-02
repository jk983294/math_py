import sympy as S
import numpy as np
from sympy import stats
from sympy.stats import density, E, Die

x = Die("D1", 6)  # 1st
y = Die("D2", 6)  # 2nd
a = S.symbols("a")
z = x + y
J = E((x - a * (x + y)) ** 2)  # expectation
print(S.simplify(J))

(sol,) = S.solve(S.diff(J, a), a)  # using calculus to minimize
print(sol)

# here 6 is ten times more probable than any other outcome
x = stats.FiniteRV(
    "D3", {1: 1 / 15.0, 2: 1 / 15.0, 3: 1 / 15.0, 4: 1 / 15.0, 5: 1 / 15.0, 6: 2 / 3.0}
)

E(x, S.Eq(z, 7))  # conditional expectation E(x|z=7)
