import seaborn as sns
import numpy as np
import pandas as pd
import time
from tabulate import tabulate  # pip install tabulate

np.random.seed(42)

# Load and prepare data
dataset_size = 20_000
diamonds = sns.load_dataset("diamonds")

# Build feature and target arrays
xy = diamonds[["carat", "price"]].values
np.random.shuffle(xy)
xy = xy[:dataset_size]

# Normalize the data
mean = np.mean(xy, axis=0)
std = np.std(xy, axis=0)
xy_normalized = (xy - mean) / std

# Split the data
train_size = int(0.8 * dataset_size)
train_xy, test_xy = xy_normalized[:train_size], xy_normalized[train_size:]


# Model and loss functions
def model(m, x, b):
    return m * x + b


def loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def stochastic_gradient_descent(
    x, y, epochs=100, learning_rate=0.01, batch_size=32, stopping_threshold=1e-6
):
    """
    SGD with support for mini-batches and gradient clipping.
    """
    # Initialize the model parameters randomly
    m = np.random.randn()
    b = np.random.randn()

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

            # Gradient clipping
            clip_value = 1.0
            m_gradient = np.clip(m_gradient, -clip_value, clip_value)
            b_gradient = np.clip(b_gradient, -clip_value, clip_value)

            # Update the model parameters
            m -= learning_rate * m_gradient
            b -= learning_rate * b_gradient

        # Compute the loss
        y_pred = model(m, x, b)
        current_loss = loss(y, y_pred)

        if abs(previous_loss - current_loss) < stopping_threshold:
            break

        previous_loss = current_loss

    return m, b


def stochastic_gradient_descent_with_momentum(
    x,
    y,
    epochs=100,
    learning_rate=0.01,
    batch_size=32,
    stopping_threshold=1e-6,
    momentum=0.9,
):
    """
    SGD with momentum, support for mini-batches, and gradient clipping.
    """
    # Initialize the model parameters randomly
    m = np.random.randn()
    b = np.random.randn()

    # Initialize velocity terms
    v_m = 0
    v_b = 0

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

            # Gradient clipping
            clip_value = 1.0
            m_gradient = np.clip(m_gradient, -clip_value, clip_value)
            b_gradient = np.clip(b_gradient, -clip_value, clip_value)

            # Update velocity terms
            v_m = momentum * v_m + learning_rate * m_gradient
            v_b = momentum * v_b + learning_rate * b_gradient

            # Update the model parameters using velocity
            m -= v_m
            b -= v_b

        # Compute the loss
        y_pred = model(m, x, b)
        current_loss = loss(y, y_pred)

        if abs(previous_loss - current_loss) < stopping_threshold:
            break

        previous_loss = current_loss

    return m, b


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


def run_optimization(opt_func, x, y, **kwargs):
    start_time = time.time()
    m, b = opt_func(x, y, **kwargs)
    end_time = time.time()

    y_preds = model(m, test_xy[:, 0], b)
    y_preds_denormalized = y_preds * std[1] + mean[1]
    y_true_denormalized = test_xy[:, 1] * std[1] + mean[1]
    actual_mse = np.mean((y_true_denormalized - y_preds_denormalized) ** 2)

    return end_time - start_time, np.sqrt(actual_mse)


# Run all optimization methods
results = []

results.append(
    (
        "SGD",
        *run_optimization(
            stochastic_gradient_descent,
            train_xy[:, 0],
            train_xy[:, 1],
            learning_rate=0.1,
            epochs=10000,
            batch_size=64,
        ),
    )
)

results.append(
    (
        "SGD with Momentum",
        *run_optimization(
            stochastic_gradient_descent_with_momentum,
            train_xy[:, 0],
            train_xy[:, 1],
            learning_rate=0.1,
            epochs=10000,
            batch_size=64,
            momentum=0.9,
        ),
    )
)

results.append(
    (
        "RMSprop",
        *run_optimization(
            rmsprop_optimization,
            train_xy[:, 0],
            train_xy[:, 1],
            learning_rate=0.01,
            epochs=10000,
            batch_size=64,
            beta=0.9,
            epsilon=1e-8,
        ),
    )
)

results.append(
    (
        "ADAM",
        *run_optimization(
            adam_optimization,
            train_xy[:, 0],
            train_xy[:, 1],
            learning_rate=0.01,
            epochs=10000,
            batch_size=64,
            beta1=0.9,
            beta2=0.999,
            epsilon=1e-8,
        ),
    )
)

# Create and print the table
headers = ["Optimization Method", "Runtime (seconds)", "Actual RMSE"]
print(tabulate(results, headers=headers, floatfmt=".4f"))

# If you want to save the results to a CSV file:
pd.DataFrame(results, columns=headers).to_csv("optimization_results.csv", index=False)
