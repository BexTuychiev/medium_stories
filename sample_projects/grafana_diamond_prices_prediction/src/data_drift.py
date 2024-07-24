# src/monitoring/data_drift.py
import numpy as np
from scipy.stats import ks_2samp


def detect_data_drift(reference_data, current_data, threshold=0.1):
    drift_scores = {}
    for column in reference_data.columns:
        ks_statistic, p_value = ks_2samp(reference_data[column], current_data[column])
        drift_scores[column] = ks_statistic

    overall_drift_score = np.mean(list(drift_scores.values()))
    is_drift = overall_drift_score > threshold

    return is_drift, drift_scores, overall_drift_score
