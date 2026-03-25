# src/utils/preprocessing.py

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataset:
    - Handle missing values
    - Drop duplicates
    """
    
    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values (basic strategy)
    df = df.fillna(method='ffill')

    return df


def extract_datetime_features(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Extract useful time-based features
    """
    
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

    df["year"] = df[date_column].dt.year
    df["month"] = df[date_column].dt.month
    df["day"] = df[date_column].dt.day
    df["hour"] = df[date_column].dt.hour

    return df


def encode_categorical(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Convert categorical columns into numeric
    """
    
    df = pd.get_dummies(df, columns=columns, drop_first=True)
    
    return df