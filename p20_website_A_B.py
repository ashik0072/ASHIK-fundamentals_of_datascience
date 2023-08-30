import numpy as np
from scipy.stats import ttest_ind
design_A_conversion_rates = [0.10, 0.12, 0.09,
                             0.11, 0.13, 0.14, 0.08, 0.10, 0.11, 0.12]
design_B_conversion_rates = [0.13, 0.11, 0.10,
                             0.14, 0.12, 0.11, 0.09, 0.13, 0.10, 0.12]
mean_A = np.mean(design_A_conversion_rates)
mean_B = np.mean(design_B_conversion_rates)
std_A = np.std(design_A_conversion_rates, ddof=1)
std_B = np.std(design_B_conversion_rates, ddof=1)
n_A = len(design_A_conversion_rates)
n_B = len(design_B_conversion_rates)
t_stat, p_value = ttest_ind(
    design_A_conversion_rates, design_B_conversion_rates)
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between website design A and B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between website design A and B.")
