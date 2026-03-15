import os

# API de TMDB
#"eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYWE2ZWRjNmFhY2I3YmRmYmY5ZmIzZTQwNTA1NzVhMiIsIm5iZiI6MTc2MTE2NzM3OS4xODksInN1YiI6IjY4Zjk0ODEzMmQ4MjliNDI0MzUzNjNmZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8qNpyp-wtM85ZsTmrESFRwlizPY5cbe_Jyv5N2yef2Q"
TMDB_API_KEY = os.getenv("eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYWE2ZWRjNmFhY2I3YmRmYmY5ZmIzZTQwNTA1NzVhMiIsIm5iZiI6MTc2MTE2NzM3OS4xODksInN1YiI6IjY4Zjk0ODEzMmQ4MjliNDI0MzUzNjNmZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8qNpyp-wtM85ZsTmrESFRwlizPY5cbe_Jyv5N2yef2Q")


# Resto igual...
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

KMEANS_PATH = os.path.join(BASE_DIR, "KMEANSPP_Clusters")
GMM_PATH = os.path.join(BASE_DIR, "GMM_clusters")
MOVIES_FILE = os.path.join(BASE_DIR, "unified_movies_clean.csv")

DATASETS = {
    "KMEANS++ PCA UMAP 2D": os.path.join(KMEANS_PATH, "kmeanspp_clustered_pca_umap_2d.csv"),
    "KMEANS++ PCA UMAP 3D": os.path.join(KMEANS_PATH, "kmeanspp_clustered_pca_umap_3d.csv"),
    "KMEANS++ NMF UMAP 2D": os.path.join(KMEANS_PATH, "kmeanspp_clustered_nmf_umap_2d.csv"),
    "KMEANS++ NMF UMAP 3D": os.path.join(KMEANS_PATH, "kmeanspp_clustered_nmf_umap_3d.csv"),
    "GMM PCA UMAP 2D": os.path.join(GMM_PATH, "movies_clustered_pca_umap_2d.csv"),
    "GMM PCA UMAP 3D": os.path.join(GMM_PATH, "movies_clustered_pca_umap_3d.csv"),
    "GMM NMF UMAP 2D": os.path.join(GMM_PATH, "movies_clustered_nmf_umap_2d.csv"),
    "GMM NMF UMAP 3D": os.path.join(GMM_PATH, "movies_clustered_nmf_umap_3d.csv"),
}
