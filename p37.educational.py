# from scipy.stats import pearsonr
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import seaborn as sns

# study_time = [3, 6, 1, 3, 7, 2, 9, 4, 8]  # List of study time values
# exam_scores = [56, 78, 23, 60, 45, 95, 70, 90, 91]  # List of exam score values

# correlation = np.corrcoef(study_time, exam_scores)  # [0, 1]
# print("Correlation coefficient:", correlation)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
# Replace 'student_data.csv' with your actual data file path
data = pd.read_csv('CSV_FILES/student_data.csv')

# Extract study time and exam scores
study_time = data['study_time']
exam_scores = data['exam_scores']

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(study_time, exam_scores, color='blue', alpha=0.7)
plt.title("Study Time vs Exam Scores")
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Scores")
plt.show()

# Calculate the correlation coefficient
correlation_coefficient = np.corrcoef(study_time, exam_scores)[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")

# Create a scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x=study_time, y=exam_scores, scatter_kws={'alpha': 0.7})
plt.title("Study Time vs Exam Scores with Regression Line")
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Scores")
plt.show()

# Create a joint plot with regression line and histograms
sns.jointplot(x=study_time, y=exam_scores,
              kind='reg', scatter_kws={'alpha': 0.7})
plt.show()

# Create a density plot and histogram
sns.displot(data, x='study_time', y='exam_scores', kind='kde')
plt.show()
