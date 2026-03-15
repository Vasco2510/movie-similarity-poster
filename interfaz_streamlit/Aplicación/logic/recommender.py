import numpy as np
import pandas as pd

def get_similar_movies(selected_movie, df, n=6, genre_filter=None):
    """Devuelve películas similares del mismo cluster (más cercanas por distancia euclidiana)."""
    cluster_col = "cluster_gmm" if "cluster_gmm" in df.columns else "cluster"
    coords = [col for col in df.columns if "UMAP" in col]

    cluster_id = selected_movie[cluster_col].iloc[0]
    cluster_movies = df[df[cluster_col] == cluster_id].copy()

    if genre_filter:
        cluster_movies = cluster_movies[cluster_movies[genre_filter] == 1]

    selected_coords = selected_movie[coords].values[0]
    cluster_movies["distance"] = np.linalg.norm(cluster_movies[coords].values - selected_coords, axis=1)

    cluster_movies = cluster_movies[cluster_movies["movieId"] != selected_movie["movieId"].iloc[0]]
    return cluster_movies.sort_values("distance").head(n)
