import requests
import streamlit as st
import math

TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYWE2ZWRjNmFhY2I3YmRmYmY5ZmIzZTQwNTA1NzVhMiIsIm5iZiI6MTc2MTE2NzM3OS4xODksInN1YiI6IjY4Zjk0ODEzMmQ4MjliNDI0MzUzNjNmZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8qNpyp-wtM85ZsTmrESFRwlizPY5cbe_Jyv5N2yef2Q"

def get_tmdb_poster(tmdb_id):
    """Obtiene el poster desde TMDb usando Bearer Token."""
    # Validar ID
    if tmdb_id is None or (isinstance(tmdb_id, float) and math.isnan(tmdb_id)):
        return None

    try:
        tmdb_id = int(tmdb_id)
    except (ValueError, TypeError):
        return None

    try:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?language=en-US"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_KEY}"
        }
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
        # Si la película no tiene poster
        return None
    except Exception as e:
        st.warning(f"Error obteniendo poster TMDb ({tmdb_id}): {e}")
        return None
