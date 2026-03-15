import streamlit as st
from data.loader import load_clusters, load_movies, merge_movies_with_clusters
from logic.recommender import get_similar_movies
from ui.display import show_movie_info, show_posters

def main():
    st.set_page_config(page_title="Visualizador de Clusters de Películas", layout="wide")
    st.title("🎥 Visualizador de Películas por Clusters")

    st.sidebar.header("⚙️ Configuración")

    algorithm = st.sidebar.selectbox("Algoritmo", ["GMM", "KMEANSPP"])
    method = st.sidebar.selectbox("Método", ["pca", "nmf"])
    dim = st.sidebar.selectbox("Dimensionalidad", ["2d", "3d"])
    n_similar = st.sidebar.slider("Películas similares a mostrar", 3, 10, 6)

    movies_df = load_movies()
    cluster_df = load_clusters(algorithm, method, dim)
    merged_df = merge_movies_with_clusters(cluster_df, movies_df)

    st.sidebar.markdown("---")
    all_titles = merged_df["title"].dropna().unique()
    selected_title = st.selectbox("Selecciona una película:", sorted(all_titles))

    if selected_title:
        selected_movie = merged_df[merged_df["title"] == selected_title]
        if not selected_movie.empty:
            st.subheader("🎭 Película seleccionada")
            col1, col2 = st.columns([1, 2])
            with col1:
                show_posters(selected_movie, n_cols=1)
            with col2:
                show_movie_info(selected_movie)

            st.subheader("🎯 Películas similares")
            # Detectar columnas de géneros (asumiendo que empiezan desde la 6ta)
            possible_genres = movies_df.columns[5:]

            # Filtrar solo las que existen en merged_df
            valid_genres = [g for g in possible_genres if g in merged_df.columns and merged_df[g].sum() > 0]

            # Si no hay columnas válidas, solo mostrar "Ninguno"
            if not valid_genres:
                valid_genres = ["Ninguno"]

            genre_filter = st.sidebar.selectbox(
                "Filtrar por género (opcional):",
                ["Ninguno"] + valid_genres
            )

            if genre_filter == "Ninguno":
                genre_filter = None

            similar_movies = get_similar_movies(selected_movie, merged_df, n=n_similar, genre_filter=genre_filter)
            if similar_movies.empty:
                st.info("No se encontraron películas similares.")
            else:
                show_posters(similar_movies)
        else:
            st.warning("Película no encontrada en este conjunto.")

if __name__ == "__main__":
    main()
