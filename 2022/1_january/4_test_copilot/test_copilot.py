import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import *
from sklearn.metrics import *
from sklearn.linear_model import *
from sklearn.ensemble import *
from sklearn.tree import *
from sklearn.neighbors import *
from sklearn.svm import *
from sklearn.naive_bayes import *
from sklearn.discriminant_analysis import *
from sklearn.model_selection import *
from sklearn.pipeline import *
from sklearn.compose import *


import umap

# A function to project data to 2D with UMAP and plot it
def plot_umap(data, labels, title):
    # Project the data to 2D
    reducer = umap.UMAP(n_neighbors=10, min_dist=0.1, n_components=2)
    embedding = reducer.fit_transform(data)

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap='tab10')
    ax.set_title(title)
    plt.show()



















