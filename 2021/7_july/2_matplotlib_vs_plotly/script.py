import matplotlib.pyplot as plt
import pandas as pd


def plot_scores(mpl=0, px=0):
    """
    A custom function to plot scores in a nice way.
    """
    # Set the ratios to 50% if equal
    if mpl == px:
        mpl_score = 0.5
        px_score = 0.5
    # Set a minimum score of 0.3 if any score is 0
    elif mpl == 0 and px != 0:
        mpl_score = 0.3
        px_score = 0.7
    elif px == 0 and mpl != 0:
        px_score = 0.3
        mpl_score = 0.7
    else:
        mpl_score = round(mpl / (mpl + px), 2)
        px_score = round(px / (mpl + px), 2)

    # Put scores in a DataFrame
    df = pd.DataFrame(
        {"mpl_score": {"lib": mpl_score}, "plotly_score": {"lib": px_score}}
    )
    fig, ax = plt.subplots(figsize=(6.2, 2.5), dpi=140)

    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])

    ax.barh(df.index, df["mpl_score"], color="#CE260C", alpha=0.9, label="Matplotlib")
    ax.barh(
        df.index,
        df["plotly_score"],
        left=df["mpl_score"],
        color="#000F16",
        alpha=0.9,
        label="Plotly",
    )

    for i in df.index:
        ax.annotate(
            mpl,
            xy=(df["mpl_score"][i] / 2, i),
            va="center",
            ha="center",
            fontsize=40,
            fontweight="light",
            fontfamily="serif",
            color="white",
        )

        ax.annotate(
            "Matplotlib",
            xy=(df["mpl_score"][i] / 2, -0.25),
            va="center",
            ha="center",
            fontsize=15,
            fontweight="light",
            fontfamily="serif",
            color="white",
        )

        ax.annotate(
            px,
            xy=(df["mpl_score"][i] + df["plotly_score"][i] / 2, i),
            va="center",
            ha="center",
            fontsize=40,
            fontweight="light",
            fontfamily="serif",
            color="white",
        )
        ax.annotate(
            "Plotly",
            xy=(df["mpl_score"][i] + df["plotly_score"][i] / 2, -0.25),
            va="center",
            ha="center",
            fontsize=15,
            fontweight="light",
            fontfamily="serif",
            color="white",
        )

    for s in ["top", "left", "right", "bottom"]:
        ax.spines[s].set_visible(False)
