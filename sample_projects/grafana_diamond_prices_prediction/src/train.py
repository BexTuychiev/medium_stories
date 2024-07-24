# src/train.py
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import pandas as pd


def train_model():
    # Load the diamonds dataset
    diamonds = sns.load_dataset("diamonds")

    # Prepare the features and target
    X = diamonds[["carat", "cut", "color", "clarity", "depth", "table"]]
    y = diamonds["price"]

    # Encode categorical variables
    X = pd.get_dummies(X, columns=["cut", "color", "clarity"])

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model MSE: {mse}")

    # Save the model and scaler
    joblib.dump(model, "../model.joblib")
    joblib.dump(scaler, "../scaler.joblib")

    print("Model and scaler saved successfully.")


if __name__ == "__main__":
    train_model()
