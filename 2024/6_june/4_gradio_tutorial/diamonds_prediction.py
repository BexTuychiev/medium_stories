import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import gradio as gr

# Load the diamonds dataset
diamonds = sns.load_dataset("diamonds")

# Prepare the features and target
X = diamonds.drop("price", axis=1)
y = diamonds["price"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the preprocessing steps
numeric_features = ["carat", "depth", "table", "x", "y", "z"]
categorical_features = ["cut", "color", "clarity"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(drop="first"), categorical_features),
    ]
)


# Create a pipeline with preprocessing and model
model = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
    ]
)

# Fit the model
model.fit(X_train, y_train)


# Create the Gradio interface
def predict_price(carat, cut, color, clarity, depth, table, x, y, z):
    input_data = pd.DataFrame(
        {
            "carat": [carat],
            "cut": [cut],
            "color": [color],
            "clarity": [clarity],
            "depth": [depth],
            "table": [table],
            "x": [x],
            "y": [y],
            "z": [z],
        }
    )
    prediction = model.predict(input_data)[0]
    return f"Predicted Price: ${prediction:.2f}"


iface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Carat"),
        gr.Dropdown(["Fair", "Good", "Very Good", "Premium", "Ideal"], label="Cut"),
        gr.Dropdown(["D", "E", "F", "G", "H", "I", "J"], label="Color"),
        gr.Dropdown(
            ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"], label="Clarity"
        ),
        gr.Number(label="Depth"),
        gr.Number(label="Table"),
        gr.Number(label="X"),
        gr.Number(label="Y"),
        gr.Number(label="Z"),
    ],
    outputs="text",
    title="Diamond Price Predictor",
    description="Enter the characteristics of a diamond to predict its price.",
)

iface.launch(share=True)
