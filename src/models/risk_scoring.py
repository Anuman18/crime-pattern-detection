# src/models/risk_scoring.py

import numpy as np
from sklearn.preprocessing import MinMaxScaler


def calculate_risk_score(data):
    """
    Calculate normalized crime risk score (0 to 1)
    """

    scaler = MinMaxScaler()
    normalized = scaler.fit_transform(data)

    # Mean of all crime features = overall risk
    risk_score = np.mean(normalized, axis=1)

    return risk_score


def categorize_risk(score):
    """
    Convert score into human-readable category
    """

    if score < 0.3:
        return "LOW"
    elif score < 0.6:
        return "MEDIUM"
    else:
        return "HIGH"