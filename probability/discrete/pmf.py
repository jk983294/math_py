import pandas as pd

# PMF of two dices, one is fair with probability 1/6, one is unfair with probability 1/9 when x <= 3 and 2/9 when x > 3
d = pd.DataFrame(
    index=[(i, j) for i in range(1, 7) for j in range(1, 7)],
    columns=["sm", "d1", "d2", "pd1", "pd2", "p"],
)
d.d1 = [i[0] for i in d.index]
d.d2 = [i[1] for i in d.index]
d.sm = d.index.map(sum)
d.loc[d.d1 <= 3, "pd1"] = 1 / 9.0
d.loc[d.d1 > 3, "pd1"] = 2 / 9.0
d.pd2 = 1 / 6.0
d.p = d.pd1 * d.pd2
d.groupby("sm")["p"].sum()
