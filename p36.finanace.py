import pandas as pd
import numpy as np

# Load the stock data from CSV file
# Replace 'stock_data.csv' with your actual data file path
data = pd.read_csv('CSV_FILES/stock_data.csv')

# Extract the closing prices
closing_prices = data['closing_price']

# Calculate the daily returns
daily_returns = closing_prices.pct_change()

# Calculate the mean and standard deviation of daily returns
mean_return = np.mean(daily_returns)
std_deviation = np.std(daily_returns)

# Calculate the annualized volatility (assuming 252 trading days in a year)
annualized_volatility = std_deviation * np.sqrt(252)

print(f"Mean Daily Return: {mean_return:.4f}")
print(f"Standard Deviation of Daily Returns: {std_deviation:.4f}")
print(f"Annualized Volatility: {annualized_volatility:.4f}")

# Provide insights into stock price movements
if mean_return > 0:
    print("The stock tends to have positive average daily returns.")
else:
    print("The stock tends to have negative or near-zero average daily returns.")

if annualized_volatility < 0.2:
    print("The stock's volatility is relatively low.")
elif 0.2 <= annualized_volatility < 0.4:
    print("The stock's volatility is moderate.")
else:
    print("The stock's volatility is relatively high.")
