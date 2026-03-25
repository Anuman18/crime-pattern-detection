import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values with 0 (important for crime counts)
    df = df.fillna(0)

    return df


def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select only numerical crime columns for ML
    """

    # Drop non-numeric columns
    df_numeric = df.drop(columns=["STATE/UT", "YEAR"])

    return df_numeric