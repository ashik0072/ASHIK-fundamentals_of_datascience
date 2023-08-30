import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import csv
with open("names.csv", mode="w", newline='') as csvfile:
    fieldnames = ["Group", "Value"]  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Group": "Control", "Value": 10.2})  
    writer.writerow({"Group": "Control", "Value": 9.8})
    writer.writerow({"Group": "Control", "Value": 7.2})
    writer.writerow({"Group": "Control", "Value": 6.9})
    writer.writerow({"Group": "Control", "Value": 11.8})
    writer.writerow({"Group": "Treatment", "Value": 12.1}) 
    writer.writerow({"Group": "Treatment", "Value": 11.4})
    writer.writerow({"Group": "Treatment", "Value": 13.4})
    writer.writerow({"Group": "Treatment", "Value": 11.8})
    writer.writerow({"Group": "Treatment", "Value": 12.2})
if __name__ == "__main__":
    file_name =("names.csv")

    data = pd.read_csv(file_name)
    control_group = data[data["Group"] == "Control"]["Value"]
    treatment_group = data[data["Group"] == "Treatment"]["Value"]
plt.boxplot([control_group, treatment_group], labels=["Control Group", "Treatment Group"])
plt.ylabel("Values")
plt.title("Box Plot of Control Group vs. Treatment Group")
plt.show()
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)
print("P-value:", p_value)
alpha = 0.05 
if p_value < alpha:
    print("The new treatment has a statistically significant effect compared to the placebo.")
else:
    print("There is no statistically significant effect of the new treatment compared to the placebo.")
