import numpy as np

# given a rod of unit-length, broken independently and randomly at two places,
# what is the probability that the three pieces can form a triangle?
sim_times = 10000
x, y = np.random.rand(2, sim_times)  # uniform rv
a, b, c = x, (y - x), 1 - y  # 3 sides
s = (a + b + c) / 2
np.mean((s > a) & (s > b) & (s > c) & (y > x))
