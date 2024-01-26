import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import matplotlib.pyplot as plt
import json

"""
MSE: average of the squares of errors; average squared difference between estimated and actual values
-quality of the estimator (closer to 0 the better)

MAE: average of the absolute errors; measues the magnitude of errors
-same units as the data, so gives clearer idea relative to dataset

R^2: variance in dependent variable

"""

def train_model(dataset_path, model_name):
    df = pd.read_csv(dataset_path)
            
    # Select features and target variable
    X = df.drop(["distance"], axis=1)
    y = df["distance"]

    # Split your data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5) # original: 3

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Test & Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R^2 Error: {r2}")
    print(f"Test Subjects: {X_test}")
    print(f"Predictions: {y_pred}")

    # Actual vs Predicted Scatter Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, color="blue")

    plt.title("Actual vs Predicted")
    plt.xlabel("Actual Distance")
    plt.ylabel("Predicted Distance")
    plt.grid(True)
    plt.show()

    # Save a model
    joblib.dump(model, model_name)

    max_sequence_len = X_train.shape[1]
    with open("max_sequence_len.json", "w") as f:
        json.dump({"max_sequence_len": max_sequence_len}, f)

    column_names = X_train.columns.tolist()
    with open("column_names.json", "w") as f:
        json.dump(column_names, f)
    
# Load the model
# joblib.load("model_v1.pkl")

