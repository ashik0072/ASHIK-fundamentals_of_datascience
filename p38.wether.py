import pandas as pd
import numpy as np

# Load the temperature data
# Replace 'temperature_data.csv' with your actual data file path
data = pd.read_csv('CSV_FILES/temperature_data.csv')

# Calculate the mean temperature for each city
mean_temperatures = data.groupby('city')['temperature'].mean()

# Calculate the standard deviation of temperature for each city
std_deviation_temperatures = data.groupby('city')['temperature'].std()

# Determine the city with the highest temperature range
temperature_ranges = data.groupby(
    'city')['temperature'].apply(lambda x: max(x) - min(x))
city_with_highest_range = temperature_ranges.idxmax()

# Find the city with the most consistent temperature (lowest standard deviation)
city_with_lowest_std_deviation = std_deviation_temperatures.idxmin()

print("Mean Temperatures:")
print(mean_temperatures)

print("\nStandard Deviations of Temperatures:")
print(std_deviation_temperatures)

print(f"\nCity with the Highest Temperature Range: {city_with_highest_range}")
print(
    f"City with the Most Consistent Temperature: {city_with_lowest_std_deviation}")
