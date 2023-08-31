from sklearn.linear_model import LogisticRegression
import numpy as np

def get_user_input():
    usage_minutes = float(input("Enter usage minutes: "))
    contract_duration = int(input("Enter contract duration (in months): "))
    return np.array([[usage_minutes, contract_duration]])

def main():
    X = np.array([[100, 12], [200, 6], [50, 24], [300, 3]])  
    y = np.array([0, 1, 0, 1])  
    clf = LogisticRegression()
    clf.fit(X, y)
    new_customer_features = get_user_input()
    predicted_churn = clf.predict(new_customer_features)
    if predicted_churn[0] == 0:        print("The new customer is predicted not to churn.")
    else:
        print("The new customer is predicted to churn.")

if __name__ == "__main__":
    main()
