import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class AIEngine: 
    def __init__(self, dataset_path=None) -> None:
        if dataset_path:
            self.df = pd.read_csv(dataset_path)
        
        # Select features and target variable
        X = df.drop(["distance"], axis=1)
        y = df["distance"]

        # Split your data into training and testing
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

        # Initialize and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Test & Evaluate the model
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")
