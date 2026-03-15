import os
import pandas as pd

# Determinar la ruta base automáticamente (sin hardcodear)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # => /Aplicación
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))           # => /visualizador_p2_ml

BASE_PATH_GMM = os.path.join(PROJECT_ROOT, "GMM_clusters")
BASE_PATH_KMEANS = os.path.join(PROJECT_ROOT, "KMEANSPP_Clusters")
MOVIES_PATH = os.path.join(PROJECT_ROOT, "unified_movies_clean.csv")

def load_clusters(algorithm="GMM", method="pca", dim="2d"):
    """Carga el CSV correspondiente al algoritmo, método y dimensión."""
    folder = BASE_PATH_GMM if algorithm == "GMM" else BASE_PATH_KMEANS
    file_prefix = "movies_clustered" if algorithm == "GMM" else "kmeanspp_clustered"
    filename = f"{file_prefix}_{method}_umap_{dim}.csv"
    path = os.path.join(folder, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    return pd.read_csv(path)

def load_movies():
    """Carga el archivo base con la metadata de las películas."""
    if not os.path.exists(MOVIES_PATH):
        raise FileNotFoundError(f"No se encontró el archivo: {MOVIES_PATH}")
    df = pd.read_csv(MOVIES_PATH)
    df["movieId"] = df["movieId"].astype(str)
    df["tmdbId"] = pd.to_numeric(df["tmdbId"], errors="coerce")
    return df

def merge_movies_with_clusters(cluster_df, movies_df):
    """Une los datos del clustering con los metadatos de películas."""
    cluster_df["movieId"] = cluster_df["movieId"].astype(str)
    return pd.merge(cluster_df, movies_df, on="movieId", how="left")
