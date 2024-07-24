# src/app.py
import os
import joblib
import pandas as pd
import seaborn as sns

from prometheus_client import start_http_server, Gauge
from prometheus_client import make_wsgi_app
from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from data_drift import detect_data_drift
from concept_drift import detect_concept_drift

app = Flask(__name__)

# Load the model pipeline
try:
    model_pipeline = joblib.load("../model_pipeline.joblib")
    print("Model pipeline loaded successfully")
except Exception as e:
    print(f"Error loading model pipeline: {e}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in current directory: {os.listdir('.')}")
    model_pipeline = None

# Create Prometheus metrics
data_drift_gauge = Gauge("data_drift", "Data Drift Score")
concept_drift_gauge = Gauge("concept_drift", "Concept Drift Score")

# Load reference data
diamonds = sns.load_dataset("diamonds")
X_reference = diamonds[["carat", "cut", "color", "clarity", "depth", "table"]]
y_reference = diamonds["price"]


@app.route("/predict", methods=["POST"])
def predict():
    if model_pipeline is None:
        return jsonify({"error": "Model pipeline not loaded properly"}), 500

    data = request.json
    df = pd.DataFrame(data, index=[0])

    prediction = model_pipeline.predict(df)
    return jsonify({"prediction": prediction[0]})


def monitor_drifts():
    # Simulating new data (in a real scenario, this would be actual new data)
    new_diamonds = sns.load_dataset("diamonds").sample(n=1000, replace=True)
    X_current = new_diamonds[["carat", "cut", "color", "clarity", "depth", "table"]]
    y_current = new_diamonds["price"]

    # Data drift detection
    is_data_drift, _, data_drift_score = detect_data_drift(X_reference, X_current)
    data_drift_gauge.set(data_drift_score)

    # Concept drift detection
    is_concept_drift, concept_drift_score = detect_concept_drift(
        model_pipeline,
        X_reference,
        y_reference,
        X_current,
        y_current,
    )
    concept_drift_gauge.set(concept_drift_score)

    if is_data_drift:
        print("Data drift detected!")
    if is_concept_drift:
        print("Concept drift detected!")


app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(8000)

    # Schedule drift monitoring
    scheduler = BackgroundScheduler()
    scheduler.add_job(monitor_drifts, "interval", minutes=1)
    scheduler.start()

    # Run Flask app
    app.run(host="0.0.0.0", port=5000)
