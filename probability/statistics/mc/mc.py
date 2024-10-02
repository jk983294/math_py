import numpy as np
import scipy as sp
from scipy import stats

# flip a coin 100 times, what is the probability that the number of heads <= 45
p = 0.5  # probability of flipping heads each flip
n = 100  # number of coin flips per trial
x = 45

# Monte Carlo Approach
N = 100000  # 100000 trials, each with 100 flips
rng = np.random.default_rng()  # use the "new" Generator interface
simulation = rng.random(size=(n, N)) < p  # False for tails, True for heads
counts = np.sum(simulation, axis=0)  # count the number of heads each trial
# estimate the probability as the observed proportion of cases in which the count did not exceed 45
prob = np.sum(counts <= x) / N
print(f"The Monte Carlo approach estimates the probability as {prob:.3f}")
