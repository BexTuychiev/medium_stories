# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -U -r requirements.txt

COPY . .

# Run the training script to generate model.joblib and scaler.joblib
RUN python src/train.py

# Run the application
CMD ["python", "src/app.py"]