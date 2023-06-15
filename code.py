# Importing required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Settings to produce nice plots in a Jupyter notebook
plt.style.use('fivethirtyeight')

# Reading in the data
stock_data = pd.read_csv('datasets/stock_data.csv', parse_dates = ['Date'], index_col = ['Date']).dropna()
benchmark_data = pd.read_csv('datasets/benchmark_data.csv', parse_dates = ['Date'], index_col = ['Date']).dropna()


#----- A first glance at the data -----
# Display summary for stock_data
print('Stocks\n')
print(stock_data.info())
print(stock_data.head())

# Display summary for benchmark_data
print('\nBenchmarks\n')
print(benchmark_data.info())
print(benchmark_data.head())


#----- Plot & summarize daily prices for Amazon and Facebook -----
# visualize the stock_data
stock_data.plot(title='Stock Data',subplots=True)

# summarize the stock_data
stock_data.describe()


#----- Visualize & summarize daily values for the S&P 500 -----
# plot the benchmark_data
stock_data.plot(title='S&P 500')

# summarize the benchmark_data
benchmark_data.describe()


#----- The inputs for the Sharpe Ratio: Starting with Daily Stock Returns -----
# calculate daily stock_data returns
stock_returns = stock_data.pct_change()

# plot the daily returns
stock_returns.plot()

# summarize the daily returns
stock_returns.describe()


#----- Daily S&P 500 returns -----
# calculate daily benchmark_data returns
sp_returns = benchmark_data['S&P 500'].pct_change()

# plot the daily returns
sp_returns.plot()

# summarize the daily returns
sp_returns.describe()


#----- Calculating Excess Returns for Amazon and Facebook vs. S&P 500 -----
# calculate the difference in daily returns
excess_returns = stock_returns.sub(sp_returns, axis=0)

# plot the excess_returns
excess_returns.plot()

# summarize the excess_returns
excess_returns.describe()


#----- The Sharpe Ratio, Step 1: The Average Difference in Daily Returns Stocks vs S&P 500 -----
# calculate the mean of excess_returns 
avg_excess_return = excess_returns.mean()

# plot avg_excess_returns
avg_excess_return.plot.bar(title = 'Mean of the Return Difference')


#----- The Sharpe Ratio, Step 2: Standard Deviation of the Return Difference -----
# calculate the standard deviations
sd_excess_return = excess_returns.std()

# plot the standard deviations
sd_excess_return.plot.bar(title = 'Mean of the Return Difference')

#----- Putting it all together -----
# calculate the daily sharpe ratio
daily_sharpe_ratio = avg_excess_return.div(sd_excess_return)

# annualize the sharpe ratio
annual_factor = np.sqrt(252)
annual_sharpe_ratio = daily_sharpe_ratio.mul(annual_factor)

# plot the annualized sharpe ratio
annual_sharpe_ratio.plot.bar(title = 'Annualized Sharpe Ratio: Stocks vs S&P 500')

#----- Conclusion -----
# Uncomment your choice.
buy_amazon = True
# buy_facebook = True