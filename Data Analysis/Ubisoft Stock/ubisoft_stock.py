import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Set the start and end date
start_date = '2015-01-01'
end_date = '2022-01-01'
 
# Set the ticker
ticker = 'UBSFY'
 
# Get the data
df = yf.download(ticker, start_date, end_date, progress=False)

# Calculate the 20-day SMA
sma_period = 20
sma_df = df['Close'].rolling(window=sma_period).mean()

# Calculate the standard deviation
std_df = df['Close'].rolling(window=sma_period).std()

# Bollinger Bands
upper_band = sma_df + std_df * 2
lower_band = sma_df - std_df * 2

# Plot the data
plt.plot(df.index, sma_df, label='20-day SMA')
plt.fill_between(df.index, upper_band, lower_band, alpha=0.3, label='Bollinger Band')
plt.xlabel('Year')
plt.ylabel('Price')
plt.title('Closing Price')
plt.legend()
plt.show()

