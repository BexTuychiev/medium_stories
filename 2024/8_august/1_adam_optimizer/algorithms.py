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

# Split the data
np.random.shuffle(xy)

train_size = int(0.8 * dataset_size)
train_xy, test_xy = xy[:train_size], xy[train_size:]


def model(m, x, b):
    """Simple linear model"""
    return m * x + b


def loss(y_true, y_pred):
    """Mean squared error"""
    return np.mean((y_true - y_pred) ** 2)


def stochastic_gradient_descent(
    x, y, epochs=100, learning_rate=0.01, batch_size=32, stopping_threshold=1e-6
):
    """
    SGD with support for mini-batches.
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

            # Compute the negative gradients
            y_pred = model(m, x_batch, b)
            m_gradient = -2 * np.mean(x_batch * (y_batch - y_pred))
            b_gradient = -2 * np.mean(y_batch - y_pred)

            # Update the model parameters
            m -= learning_rate * m_gradient
            b -= learning_rate * b_gradient

        # Compute the loss
        y_pred = model(m, x, b)
        current_loss = loss(y, y_pred)

        if previous_loss - current_loss < stopping_threshold:
            break

        previous_loss = current_loss

    return m, b


def sgd_with_momentum(
    x,
    y,
    epochs=100,
    learning_rate=0.01,
    batch_size=32,
    stopping_threshold=1e-6,
    momentum=0.9,
):
    """
    SGD with momentum and support for mini-batches.
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

            # Compute the negative gradients
            y_pred = model(m, x_batch, b)
            m_gradient = -2 * np.mean(x_batch * (y_batch - y_pred))
            b_gradient = -2 * np.mean(y_batch - y_pred)

            # Update velocity terms
            v_m = momentum * v_m + learning_rate * m_gradient
            v_b = momentum * v_b + learning_rate * b_gradient

            # Update the model parameters using velocity
            m -= v_m
            b -= v_b

        # Compute the loss
        y_pred = model(m, x, b)
        current_loss = loss(y, y_pred)

        if previous_loss - current_loss < stopping_threshold:
            break

        previous_loss = current_loss

    return m, b
