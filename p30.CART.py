from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import numpy as np

def get_user_input(feature_names):
    features = []
    for feature_name in feature_names:
        feature_value = float(input(f"Enter the {feature_name}: "))
        features.append(feature_value)
    return np.array([features])

def main():
    X = np.array([[10000, 5, 1, 0], [20000, 3, 2, 1], [15000, 4, 0, 0]])  # Sample feature data
    y = np.array([25000, 30000, 20000])  # Sample target data (car prices)
    feature_names = ["mileage", "age", "brand", "engine_type"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    regressor = DecisionTreeRegressor()
    regressor.fit(X_train, y_train)
    new_car_features = get_user_input(feature_names)
    predicted_price = regressor.predict(new_car_features)

    print(f"The predicted price of the new car is: {predicted_price[0]:.2f}")

if __name__ == "__main__":
    main()
