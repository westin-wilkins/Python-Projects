import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Set the start and end date
start_date = '2000-01-01'
end_date = '2022-01-01'
 
# Set the ticker
ticker = 'NTDOY'
 
# Get the data
df = yf.download(ticker, start_date, end_date, progress=False)

# Set values
x = np.arange(df['Adj Close'].size)
fit = np.polyfit(x, df['Adj Close'], deg=2)
fit_function = np.poly1d(fit)

# Plot the data
plt.figure(figsize=(12,6))

# Plot the adjusted close price with the moving average
plt.subplot(2,1,1)
plt.plot(df['Adj Close'], label='Adjusted Close Price')
plt.plot(df['Adj Close'].rolling(window=10).mean(), label='10-day SMA')
plt.plot(df['Adj Close'].ewm(span=10, adjust=False).mean(), label='10-day EMA')
plt.title('Convolution')
plt.legend()

# Plot the polynomial fit function
plt.subplot(2,1,2)
plt.plot(df['Adj Close'])
plt.plot(df['Adj Close'].index ,fit_function(x))
plt.title('Polynomial Fit Function')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')

# Show the plot
plt.show()