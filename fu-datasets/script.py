import seaborn as sns
import pandas as pd

diamonds = sns.load_dataset("diamonds")
diamonds.to_csv("diamonds.csv", index=False)
