import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings

warnings.filterwarnings("ignore")
np.random.seed(42)

# Load the data
dataset_size = 20_000

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


def adam_optimization(
    x,
    y,
    epochs=100,
    learning_rate=0.001,
    batch_size=32,
    stopping_threshold=1e-6,
    beta1=0.9,
    beta2=0.999,
    epsilon=1e-8,
):
    """
    ADAM optimization with support for mini-batches.
    """
    # Initialize the model parameters
    m = np.random.randn()
    b = np.random.randn()

    # Initialize first and second moment vectors
    m_m, v_m = 0, 0
    m_b, v_b = 0, 0

    n = len(x)
    previous_loss = np.inf
    t = 0  # Initialize timestep

    for i in range(epochs):
        # Shuffle the data
        indices = np.random.permutation(n)
        x = x[indices]
        y = y[indices]

        for j in range(0, n, batch_size):
            t += 1  # Increment timestep
            x_batch = x[j : j + batch_size]
            y_batch = y[j : j + batch_size]

            # Compute the gradients
            y_pred = model(m, x_batch, b)
            m_gradient = 2 * np.mean(x_batch * (y_pred - y_batch))
            b_gradient = 2 * np.mean(y_pred - y_batch)

            # Update biased first moment estimate
            m_m = beta1 * m_m + (1 - beta1) * m_gradient
            m_b = beta1 * m_b + (1 - beta1) * b_gradient

            # Update biased second raw moment estimate
            v_m = beta2 * v_m + (1 - beta2) * (m_gradient**2)
            v_b = beta2 * v_b + (1 - beta2) * (b_gradient**2)

            # Compute bias-corrected first moment estimate
            m_m_hat = m_m / (1 - beta1**t)
            m_b_hat = m_b / (1 - beta1**t)

            # Compute bias-corrected second raw moment estimate
            v_m_hat = v_m / (1 - beta2**t)
            v_b_hat = v_b / (1 - beta2**t)

            # Update parameters
            m -= learning_rate * m_m_hat / (np.sqrt(v_m_hat) + epsilon)
            b -= learning_rate * m_b_hat / (np.sqrt(v_b_hat) + epsilon)

        # Compute the loss
        y_pred = model(m, x, b)
        current_loss = loss(y, y_pred)

        if abs(previous_loss - current_loss) < stopping_threshold:
            break

        previous_loss = current_loss

    return m, b


# Find the optimal parameters m and b with ADAM
m, b = adam_optimization(
    train_xy[:, 0],
    train_xy[:, 1],
    learning_rate=0.01,
    epochs=10000,
    batch_size=32,
    beta1=0.9,
    beta2=0.999,
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
