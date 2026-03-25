# main.py

from src.utils.data_loader import load_data
from src.utils.preprocessing import clean_data, select_features
from src.models.clustering import perform_clustering
from src.models.risk_scoring import calculate_risk_score, categorize_risk


def main():
    file_path = "data/raw/crime_data.csv"

    df = load_data(file_path)

    # Preprocessing
    df = clean_data(df)
    df_features = select_features(df)

    # Clustering
    clusters, _ = perform_clustering(df_features)
    df["Cluster"] = clusters

    # Risk Score
    risk_scores = calculate_risk_score(df_features)
    df["Risk_Score"] = risk_scores

    # Risk Category
    df["Risk_Level"] = df["Risk_Score"].apply(categorize_risk)

    print(df[["STATE/UT", "YEAR", "Risk_Score", "Risk_Level"]].head())


if __name__ == "__main__":
    main()