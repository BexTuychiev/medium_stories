# src/train.py
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import pandas as pd
import seaborn as sns


def train_model():
    # Load the diamonds dataset
    diamonds = sns.load_dataset("diamonds")

    # Separate features and target
    X = diamonds[["carat", "cut", "color", "clarity", "depth", "table"]]
    y = diamonds["price"]

    # Create preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), ["carat", "depth", "table"]),
            (
                "cat",
                OneHotEncoder(drop="first", sparse=False),
                ["cut", "color", "clarity"],
            ),
        ]
    )

    # Create a pipeline that includes preprocessing and the model
    model_pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
        ]
    )

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Fit the pipeline
    model_pipeline.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model_pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model MSE: {mse}")

    # Save the entire pipeline
    joblib.dump(model_pipeline, "../model_pipeline.joblib")

    print("Model pipeline saved successfully.")


if __name__ == "__main__":
    train_model()
