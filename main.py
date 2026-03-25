from src.utils.data_loader import load_data


def main():
    file_path = "data/raw/crime_data.csv"

    df = load_data(file_path)

    print(df.head())


if __name__ == "__main__":
    main()