import streamlit as st
from utils.tmdb_api import get_tmdb_poster
from PIL import Image, ImageDraw

def _blank_placeholder(width=150, height=225):
    """Crea un recuadro blanco como placeholder."""
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline="gray", width=2)
    return img

def show_movie_info(movie):
    st.write(f"**🎬 Título:** {movie['title'].iloc[0]}")
    st.write(f"**Géneros:** {movie['genres'].iloc[0]}")
    cluster_col = "cluster_gmm" if "cluster_gmm" in movie.columns else "cluster"
    st.write(f"**Cluster:** {movie[cluster_col].iloc[0]}")

def show_posters(df, n_cols=3):
    cols = st.columns(n_cols)
    for idx, (_, movie) in enumerate(df.iterrows()):
        with cols[idx % n_cols]:
            st.write(f"**{movie['title']}**")

            poster_url = get_tmdb_poster(movie["tmdbId"])
            if poster_url:
                st.image(poster_url, width=150)
            else:
                placeholder = _blank_placeholder()
                st.image(placeholder, width=150)

            st.caption(movie["genres"])
