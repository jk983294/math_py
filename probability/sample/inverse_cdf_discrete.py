import pandas as pd
import numpy as np
from pandas import DataFrame

n = 1000
u = np.random.rand(n)
df = DataFrame(data=u, columns=["u"])

labels = [1, 2, 3, 4, 5, 6]
# map the individual samples to the set {1, 2, . . . , 6} labeled v
df["v"] = pd.cut(df.u, np.linspace(0, 1, 7), include_lowest=True, labels=labels)
df.groupby("v").count()
