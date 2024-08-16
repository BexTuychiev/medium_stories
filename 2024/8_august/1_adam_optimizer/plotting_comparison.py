import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Read the CSV file
data = pd.read_csv("optimization_results.csv")

# Create the bar chart with double y-axis
fig, ax1 = plt.subplots(figsize=(9, 7))  # Increased height for more space

x = np.arange(len(data["Optimization Method"]))
bar_width = 0.35

# Plot runtime bars
rects1 = ax1.bar(
    x - bar_width / 2,
    data["Runtime (seconds)"],
    bar_width,
    label="Runtime",
    color="b",
    alpha=0.7,
)
ax1.set_ylabel("Runtime (seconds)", color="b", fontsize=12)
ax1.tick_params(axis="y", labelcolor="b")
ax1.set_ylim(0, 65)  # Set y-axis range for runtime

# Create the second y-axis with log scale
ax2 = ax1.twinx()
ax2.set_yscale("log")
ax2.yaxis.set_major_formatter(ScalarFormatter())
ax2.yaxis.get_major_formatter().set_scientific(False)
ax2.yaxis.get_major_formatter().set_useOffset(False)

# Plot RMSE bars
rects2 = ax2.bar(
    x + bar_width / 2,
    data["Actual RMSE"],
    bar_width,
    label="RMSE",
    color="r",
    alpha=0.7,
)
ax2.set_ylabel("Actual RMSE (log scale)", color="r", fontsize=12)
ax2.tick_params(axis="y", labelcolor="r")

# Set x-axis ticks
ax1.set_xticks(x)
ax1.set_xticklabels(data["Optimization Method"], ha="center", fontsize=10)

# Add a legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", fontsize=14)


# Add value labels on the bars
def autolabel(rects, ax, is_log=False):
    for rect in rects:
        height = rect.get_height()
        if is_log:
            label = f"${height:.0f}"  # Added dollar sign for RMSE
        else:
            label = f"{height:.2f}"
        ax.annotate(
            label,
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=8,
        )


autolabel(rects1, ax1)
autolabel(rects2, ax2, is_log=True)

plt.title(
    "Comparison of Optimization Methods: Runtime vs RMSE (Log Scale)", fontsize=14
)
plt.tight_layout()

# Adjust the top of the plot to make room for labels
plt.subplots_adjust(top=0.9)

# plt.show()

# If you want to save the plot
plt.savefig("images/optimization_comparison_log.png", dpi=300, bbox_inches="tight")
