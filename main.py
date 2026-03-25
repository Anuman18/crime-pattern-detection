from src.utils.data_loader import load_data
from src.utils.preprocessing import clean_data, select_features


def main():
    file_path = "data/raw/crime_data.csv"

    df = load_data(file_path)

    # Clean data
    df = clean_data(df)

    # Select features for ML
    df_features = select_features(df)

    print("Original Shape:", df.shape)
    print("Feature Shape:", df_features.shape)
    print(df_features.head())


if __name__ == "__main__":
    main()