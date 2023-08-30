import csv
import numpy as np
import scipy.stats

# Load concentration data from CSV file
concentration_data = []
with open("CSV_FILES/rare_elements.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        concentration_data.append(float(row[1]))

# User input
sample_size = int(input("Enter sample size: "))
confidence_level = float(input("Enter confidence level (between 0 and 1): "))
precision = float(input("Enter desired level of precision: "))

# Calculate sample mean and standard deviation
sample_data = np.random.choice(
    concentration_data, size=sample_size, replace=False)
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)

# Calculate critical value based on confidence level
alpha = 1 - confidence_level
critical_value = scipy.stats.t.ppf(1 - alpha / 2, df=sample_size - 1)

# Calculate margin of error
margin_of_error = critical_value * (sample_std / np.sqrt(sample_size))

# Calculate confidence interval
confidence_interval_lower = sample_mean - margin_of_error
confidence_interval_upper = sample_mean + margin_of_error

print("\nPoint Estimate:")
print("Sample Mean:", sample_mean)

print("\nConfidence Interval:")
print(f"{confidence_level * 100:.1f}% Confidence Interval:")
print(f"Lower Bound: {confidence_interval_lower:.4f}")
print(f"Upper Bound: {confidence_interval_upper:.4f}")

print("\nMargin of Error:", margin_of_error)
