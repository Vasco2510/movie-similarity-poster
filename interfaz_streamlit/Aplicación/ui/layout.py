import streamlit as st
from PIL import Image
import requests
from io import BytesIO

from data.loader import load_movies_metadata, load_clustered_data, merge_movies_with_clusters
from logic.clustering_utils import get_movie_info, get_similar_movies
from logic.tmdb_utils import get_poster_url
from config.settings import DATASETS

def app_layout():
    st.title("🎬 Visualizador de Películas Similares por Cluster")

    # --- Selección de dataset ---
    dataset_name = st.selectbox("Selecciona un dataset de clustering:", list(DATASETS.keys()))
    dataset_path = DATASETS[dataset_name]

    # --- Cargar datos ---
    st.info(f"Cargando datos desde: `{dataset_path}`")
    movies_df = load_movies_metadata()
    cluster_df = load_clustered_data(dataset_path)
    full_df = merge_movies_with_clusters(cluster_df, movies_df)

    # --- Selección de película ---
    movie_title = st.selectbox("Selecciona una película:", sorted(full_df["title"].dropna().unique()))
    n_similar = st.slider("Cantidad de películas similares:", 1, 10, 5)

    # --- Filtro por género ---
    genre_cols = [c for c in full_df.columns if full_df[c].isin([0, 1]).any()]
    genre_filter = st.selectbox("Filtrar por género (opcional):", ["Ninguno"] + genre_cols)
    genre_filter = None if genre_filter == "Ninguno" else genre_filter

    # --- Mostrar resultados ---
    movie_row = get_movie_info(full_df, movie_title)
    cluster_col = "cluster" if "cluster" in full_df.columns else "cluster_gmm"
    st.subheader("🎞️ Película seleccionada")
    st.write(movie_row[["title", "genres", cluster_col]])

    # --- Películas similares ---
    similar_movies = get_similar_movies(full_df, movie_row, n_similar, genre_filter)

    st.subheader("🎯 Películas similares")
    cols = st.columns(5)
    for i, (_, row) in enumerate(similar_movies.iterrows()):
        tmdb_id = row.get("tmdbId")
        poster_url = get_poster_url(tmdb_id)

        # Crear nueva fila cada 5 imágenes
        if i % 5 == 0 and i != 0:
            cols = st.columns(5)

        col = cols[i % 5]
        if poster_url:
            response = requests.get(poster_url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                col.image(img, caption=f"{row['title']}\n({row['distance']:.3f})", use_container_width=True)
            else:
                col.write(f"{row['title']}\n({row['distance']:.3f})")
        else:
            col.write(f"{row['title']}\n({row['distance']:.3f})")
