import numpy as np
import pandas as pd
import finance.factor as al
import matplotlib.pyplot as plt

# Number of assets and time periods
n_assets = 10
n_periods = 100

# Generate random factor data
np.random.seed(0)
factor_data = pd.DataFrame(np.random.randn(n_periods, n_assets),
                           index=pd.date_range('2023-01-01', periods=n_periods, freq='D'),
                           columns=[f'asset_{i}' for i in range(n_assets)])

# Generate random pricing data
pricing_data = pd.DataFrame(np.cumsum(np.random.randn(n_periods, n_assets), axis=0),
                            index=pd.date_range('2023-01-01', periods=n_periods, freq='D'),
                            columns=[f'asset_{i}' for i in range(n_assets)])

# Align factor data with pricing data
factor_data = factor_data.stack().reset_index()
factor_data.columns = ['date', 'asset', 'factor']
factor_data = factor_data.set_index(['date', 'asset'])

factor_data = al.utils.get_clean_factor_and_forward_returns(factor_data, pricing_data)

# # Calculate factor returns
# perf = al.performance.factor_returns(factor_data)
# perf.plot(title='Factor Returns')
# plt.show()

# # Calculate information coefficient (IC)
# ic = al.performance.factor_information_coefficient(factor_data)
# ic.plot(title='Information Coefficient (IC)')
# plt.show()

# # Calculate quantile returns, 不同quantile的平均return
# qtl_mean_ret, qtl_ret_std_error = al.performance.mean_return_by_quantile(factor_data)
# al.plotting.plot_quantile_returns_bar(qtl_mean_ret)
# plt.show()

# Plot cumulative returns by quantile
# qtl_rets = al.performance.factor_cumulative_returns(factor_data, "1D")
# al.plotting.plot_cumulative_returns_by_quantile(qtl_rets, "1D")
# plt.show()
al.tears.create_full_tear_sheet(factor_data)