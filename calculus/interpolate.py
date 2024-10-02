import numpy as np
import scipy as sp

# linear interpolation
x = np.linspace(0, 10, num=11)
y = np.cos(-(x**2) / 9.0)
xnew = np.linspace(0, 10, num=1001)
ynew = np.interp(xnew, x, y)

# cubic spline
spl = sp.interpolate.CubicSpline([1, 2, 3, 4, 5, 6], [1, 4, 8, 16, 25, 36])
spl(2.5)

# B-spline
bspl = sp.interpolate.make_interp_spline(x, y, k=3)
bspl(2.5)
