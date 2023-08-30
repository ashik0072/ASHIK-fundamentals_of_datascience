import numpy as np
from sklearn.neighbors import KNeighborsClassifier


data = np.array([
    [30, 120, 200, 80, 150],
    [35, 118, 210, 85, 160],
    [40, 122, 190, 90, 170],
    [45, 123, 190, 75, 130],
    [50, 152, 180, 90, 170],
    [45, 142, 190, 92, 140],
    [23, 112, 140, 70, 120],
    [31, 122, 140, 68, 140],
    [48, 142, 195, 92, 150],
])
target = np.array([0, 0, 1, 1,1,1,0,0,1])  
def predict_medical_condition(features, k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(data, target)
    prediction = knn.predict([features])
    return prediction[0]

age = float(input("Enter the age of the patient: "))
blood_pressure = float(input("Enter the blood pressure of the patient: "))
cholesterol = float(input("Enter the cholesterol level of the patient: "))
weight = float(input("Enter the weight of the patient: "))
blood_sugar = float(input("Enter the blood sugar level of the patient: "))

k = int(input("Enter the value of k (number of neighbors): "))
new_patient_features = [age, blood_pressure, cholesterol, blood_sugar, weight]
prediction = predict_medical_condition(new_patient_features, k)
if prediction == 0:
    print("The patient is not predicted to have the medical condition.")
else:
    print("The patient is predicted to have the medical condition.")
