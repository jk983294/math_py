import numpy as np
from scipy import stats

x = np.array([94, 197, 16, 38, 99, 141, 23])  # treatment group
y = np.array([52, 104, 146, 10, 51, 30, 40, 27, 46])  # control group

stats.ttest_ind(x, y, equal_var=True, alternative="greater")
