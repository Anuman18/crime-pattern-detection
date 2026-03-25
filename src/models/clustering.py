# src/models/clustering.py

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def perform_clustering(data, n_clusters=3):
    """
    Perform KMeans clustering on crime data
    """

    # Scale data (VERY IMPORTANT for ML)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # KMeans model
    model = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = model.fit_predict(scaled_data)

    return clusters, model