# main.py

from src.utils.data_loader import load_data
from src.utils.preprocessing import clean_data, extract_datetime_features, encode_categorical


def main():
    file_path = "data/raw/crime_data.csv"

    df = load_data(file_path)

    # Step 1: Clean
    df = clean_data(df)

    # Step 2: Extract time features
    df = extract_datetime_features(df, date_column="Date")  # ⚠️ change column name if needed

    # Step 3: Encode categorical
    df = encode_categorical(df, columns=["Location", "Crime_Type"])  # ⚠️ adjust names

    print(df.head())


if __name__ == "__main__":
    main()