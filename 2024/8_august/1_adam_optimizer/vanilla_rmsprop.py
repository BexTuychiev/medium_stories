import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings

warnings.filterwarnings("ignore")
np.random.seed(42)

# Load the data
dataset_size = 10_000

diamonds = sns.load_dataset("diamonds")

# Extract the target and the feature
xy = diamonds[["carat", "price"]].values
np.random.shuffle(xy)  # Shuffle the data
xy = xy[:dataset_size]

# Normalize the data
mean = np.mean(xy, axis=0)
std = np.std(xy, axis=0)
xy_normalized = (xy - mean) / std

# Split the data
train_size = int(0.8 * dataset_size)
train_xy, test_xy = xy_normalized[:train_size], xy_normalized[train_size:]


def model(m, x, b):
    """Simple linear model"""
    return m * x + b


def loss(y_true, y_pred):
    """Mean squared error"""
    return np.mean((y_true - y_pred) ** 2)


def rmsprop_optimization(
    x,
    y,
    epochs=100,
    learning_rate=0.01,
    batch_size=32,
    stopping_threshold=1e-6,
    beta=0.9,
    epsilon=1e-8,
):
    """
    RMSprop optimization with support for mini-batches.
    """
    # Initialize the model parameters randomly
    m = np.random.randn()
    b = np.random.randn()

    # Initialize accumulators for squared gradients
    s_m = 0
    s_b = 0

    n = len(x)
    previous_loss = np.inf

    for i in range(epochs):
        # Shuffle the data
        indices = np.random.permutation(n)
        x = x[indices]
        y = y[indices]

        for j in range(0, n, batch_size):
            x_batch = x[j : j + batch_size]
            y_batch = y[j : j + batch_size]

            # Compute the gradients
            y_pred = model(m, x_batch, b)
            m_gradient = 2 * np.mean(x_batch * (y_batch - y_pred))
            b_gradient = 2 * np.mean(y_batch - y_pred)

            # Update accumulators
            s_m = beta * s_m + (1 - beta) * (m_gradient**2)
            s_b = beta * s_b + (1 - beta) * (b_gradient**2)

            # Update parameters
            m -= learning_rate * m_gradient / (np.sqrt(s_m) + epsilon)
            b -= learning_rate * b_gradient / (np.sqrt(s_b) + epsilon)

        # Compute the loss
        y_pred = model(m, x, b)
        current_loss = loss(y, y_pred)

        if abs(previous_loss - current_loss) < stopping_threshold:
            break

        previous_loss = current_loss

    return m, b


# Find the optimal parameters m and b with RMSprop
m, b = rmsprop_optimization(
    train_xy[:, 0],
    train_xy[:, 1],
    learning_rate=0.01,
    epochs=10000,
    batch_size=512,
    beta=0.9,
    epsilon=1e-8,
)

# Make predictions
y_preds = model(m, test_xy[:, 0], b)

# Compute and print the loss
mean_squared_error = loss(test_xy[:, 1], y_preds)

print(f"Normalized RMSE: {mean_squared_error**0.5}")

# Denormalize the predictions and compute the actual RMSE
y_preds_denormalized = y_preds * std[1] + mean[1]
y_true_denormalized = test_xy[:, 1] * std[1] + mean[1]
actual_mse = np.mean((y_true_denormalized - y_preds_denormalized) ** 2)

print(f"Actual RMSE: {actual_mse**0.5}")
