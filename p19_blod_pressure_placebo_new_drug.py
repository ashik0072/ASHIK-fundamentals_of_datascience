import scipy.stats as stats
import numpy as np

# Sample data for the drug group
drug_data = [10.2, 9.5, 11.1, 8.8, 9.9, 10.5, 10.8, 11.2, 9.7, 10.3,
             10.6, 10.1, 10.9, 9.4, 10.7, 9.8, 9.2, 10.0, 10.4, 11.0,
             10.3, 10.8, 10.6, 9.3, 10.2, 9.9, 11.3, 10.5, 9.7, 10.8,
             9.6, 11.1, 9.9, 10.4, 10.0, 10.6, 11.2, 10.3, 10.7, 9.8,
             10.2, 9.5, 10.1, 10.8, 10.6, 9.3, 10.0, 10.4, 9.9, 11.0]

# Sample data for the placebo group
placebo_data = [12.5, 13.2, 11.8, 14.1, 13.0, 12.4, 12.1, 11.7, 12.8, 12.2,
                12.9, 12.0, 12.3, 13.8, 12.5, 13.4, 13.0, 12.2, 12.6, 11.7,
                12.4, 12.1, 12.3, 13.6, 12.5, 12.8, 11.4, 12.6, 13.3, 12.2,
                13.7, 11.8, 13.0, 12.5, 12.9, 12.3, 11.7, 12.6, 12.2, 13.1,
                12.5, 13.2, 12.0, 11.3, 11.5, 12.8, 12.4, 12.9, 11.7]

# Calculate mean and standard deviation for each group
mean_drug = np.mean(drug_data)
# Using Bessel's correction for sample std
std_drug = np.std(drug_data, ddof=1)
n_drug = len(drug_data)

mean_placebo = np.mean(placebo_data)
std_placebo = np.std(placebo_data, ddof=1)
n_placebo = len(placebo_data)

# Calculate t-score for 95% confidence level
t_score = stats.t.ppf(0.975, df=min(n_drug - 1, n_placebo - 1))

# Calculate margin of error
margin_of_error_drug = t_score * (std_drug / np.sqrt(n_drug))
margin_of_error_placebo = t_score * (std_placebo / np.sqrt(n_placebo))

# Calculate confidence intervals
confidence_interval_drug = (
    mean_drug - margin_of_error_drug, mean_drug + margin_of_error_drug)
confidence_interval_placebo = (
    mean_placebo - margin_of_error_placebo, mean_placebo + margin_of_error_placebo)

# Print results
print("95% Confidence Interval for Mean Reduction in Blood Pressure (Drug Group):",
      confidence_interval_drug)
print("95% Confidence Interval for Mean Reduction in Blood Pressure (Placebo Group):",
      confidence_interval_placebo)
