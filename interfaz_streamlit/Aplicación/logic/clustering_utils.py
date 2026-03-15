import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

def get_movie_info(df, title):
    """Obtiene la fila de una película por su título"""
    return df[df["title"] == title].iloc[0]

def get_similar_movies(df, movie_row, n=5, genre_filter=None):
    """Obtiene las N películas más cercanas en el mismo cluster"""
    cluster_col = "cluster" if "cluster" in df.columns else "cluster_gmm"
    cluster = movie_row[cluster_col]
    cluster_df = df[df[cluster_col] == cluster]

    # Filtrado por género
    if genre_filter:
        cluster_df = cluster_df[cluster_df[genre_filter] == 1]

    # Determinar columnas de coordenadas
    umap_cols = [c for c in df.columns if "UMAP" in c]
    coords = cluster_df[umap_cols].values
    movie_coords = movie_row[umap_cols].values.reshape(1, -1)

    # Calcular distancias euclidianas
    distances = euclidean_distances(movie_coords, coords).flatten()
    cluster_df = cluster_df.assign(distance=distances)

    # Excluir la película base
    cluster_df = cluster_df[cluster_df["movieId"] != movie_row["movieId"]]

    return cluster_df.nsmallest(n, "distance")
