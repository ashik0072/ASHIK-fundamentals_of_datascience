from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
def get_user_input():
    sepal_length = float(input("Enter sepal length: "))
    sepal_width = float(input("Enter sepal width: "))
    petal_length = float(input("Enter petal length: "))
    petal_width = float(input("Enter petal width: "))
    return np.array([[sepal_length, sepal_width, petal_length, petal_width]])
def main():
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    new_flower = get_user_input()
    predicted_species = clf.predict(new_flower)
    species_names = iris.target_names
    predicted_species_name = species_names[predicted_species[0]]
    print(f"The predicted species for the new flower is: {predicted_species_name}")
if __name__ == "__main__":
    main()
