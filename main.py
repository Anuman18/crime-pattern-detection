# main.py

from src.utils.data_loader import load_data
from src.utils.preprocessing import clean_data, select_features
from src.models.clustering import perform_clustering


def main():
    file_path = "data/raw/crime_data.csv"

    df = load_data(file_path)

    # Preprocessing
    df = clean_data(df)
    df_features = select_features(df)

    # Clustering
    clusters, model = perform_clustering(df_features)

    # Attach clusters to original data
    df["Cluster"] = clusters

    print(df[["STATE/UT", "YEAR", "Cluster"]].head())


if __name__ == "__main__":
    main()