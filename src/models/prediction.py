# src/models/prediction.py

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def train_model(df):
    """
    Train model to predict total crimes
    """

    # Target
    y = df["TOTAL IPC CRIMES"]

    # Features
    X = df.drop(columns=["TOTAL IPC CRIMES", "STATE/UT", "YEAR"])

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    preds = model.predict(X_test)

    # Evaluation
    error = mean_absolute_error(y_test, preds)

    return model, error