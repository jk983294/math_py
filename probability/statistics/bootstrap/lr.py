import numpy as np
from scipy import stats

x = np.array(
    [
        99,
        152,
        293,
        155,
        196,
        53,
        184,
        171,
        52,
        376,
        385,
        402,
        29,
        76,
        296,
        151,
        177,
        209,
        119,
        188,
        115,
        88,
        58,
        49,
        150,
        107,
        125,
    ]
)
y = np.array(
    [
        25.8,
        20.5,
        14.3,
        23.2,
        20.6,
        31.1,
        20.9,
        20.9,
        30.4,
        16.3,
        11.6,
        11.8,
        32.5,
        32.0,
        18.0,
        24.1,
        26.5,
        25.8,
        28.8,
        22.0,
        29.7,
        28.9,
        32.8,
        32.5,
        25.4,
        31.7,
        28.5,
    ]
)

res_lr = stats.linregress(x, y)

resid = y - res_lr.intercept + res_lr.slope * x
stats.shapiro(resid)  # test if resid normal dist


def statistic(x, y):
    res = stats.linregress(x, y)
    return res.slope, res.intercept


res = stats.bootstrap((x, y), statistic, vectorized=False, paired=True)

print(f"The slope standard error is: {res.standard_error[0]}")
print(f"The intercept standard error is: {res.standard_error[1]}")
print(
    f"The confidence interval on the slope is: {res.confidence_interval.low[0], res.confidence_interval.high[0]}"
)
print(
    f"The confidence interval on the intercept is: {res.confidence_interval.low[1], res.confidence_interval.high[1]}"
)
