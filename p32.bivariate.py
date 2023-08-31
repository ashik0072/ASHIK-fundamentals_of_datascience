import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the house dataset
# Replace 'house_data.csv' with your actual data file path
dataset = pd.read_csv('CSV_FILES/house_data.csv')

'''Location
    1 - Suburban
    2 - urban
    3 - rural
    '''
# Select features and target
selected_feature = 'house_size'
target = 'price'

X = dataset[[selected_feature]]
y = dataset[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate model evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Visualize the regression line and data points
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.xlabel(selected_feature)
plt.ylabel(target)
plt.title(f"Linear Regression: {selected_feature} vs {target}")
plt.legend()
plt.show()
