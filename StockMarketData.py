"""Load stock data from CSV or API.
Compute daily returns and cumulative returns.
Plot stock prices and returns over time.
Compare multiple stocks using subplots.
Identify and annotate peaks and drops in stock price."""

import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('stock_data.csv', index_col='Date', parse_dates=True)
x['daily_return'] = x['Close'].pct_change()
x['cumulative_return'] = (1 + x['daily_return']).cumprod()

plt.figure(figsize=(10, 5))
plt.plot(x['Close'], label='Stock Price')
plt.plot(x['daily_return'], label='Daily Return')
plt.plot(x['cumulative_return'], label='Cumulative Return')
plt.legend()
plt.show()

y = pd.read_csv('another_stock_data.csv', index_col='Date', parse_dates=True)
y['daily_return'] = y['Close'].pct_change()
y['cumulative_return'] = (1 + y['daily_return']).cumprod()

fig, axs = plt.subplots(2, 1, figsize=(10, 10))
axs[0].plot(x['Close'], label='Stock 1 Price')
axs[0].plot(y['Close'], label='Stock 2 Price')
axs[0].legend()
axs[1].plot(x['daily_return'], label='Stock 1 Daily Return')
axs[1].plot(y['daily_return'], label='Stock 2 Daily Return')
axs[1].legend()
plt.show()

peaks = x['Close'][x['Close'] == x['Close'].max()]
drops = x['Close'][x['Close'] == x['Close'].min()]

plt.plot(x['Close'], label='Stock Price')
plt.scatter(peaks.index, peaks, color='red', label='Peak')
plt.scatter(drops.index, drops, color='green', label='Drop')
plt.legend()
plt.show()
