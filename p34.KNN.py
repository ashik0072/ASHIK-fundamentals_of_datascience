import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Load the medical dataset
# Replace 'medical_data.csv' with your actual data file path
dataset = pd.read_csv('CSV_FILES/medical_data.csv')
'''Gender :
    1 - male
    2 - female
   bp :
    1 - high
    2 - normal
   cholesterol :
    1 - high
    2 - normal
   outcome :
    1 - bad
    2 - good
   '''
# Select features and target
selected_features = ['age', 'gender', 'blood_pressure', 'cholesterol']
target = 'outcome'

X = dataset[selected_features]
y = dataset[target]

# Convert categorical features to numerical using one-hot encoding
X = pd.get_dummies(X, columns=['gender'], drop_first=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Calculate model evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")

# Display confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred, labels=['Good', 'Bad'])
print("Confusion Matrix:")
print(conf_matrix)

# ... (Previous code)

# Map numerical predictions to labels
predicted_labels = ['Good' if pred == 2 else 'Bad' for pred in y_pred]

# Print individual predictions
for i, prediction in enumerate(predicted_labels):
    print(f"Prediction {i+1}: {prediction}")
