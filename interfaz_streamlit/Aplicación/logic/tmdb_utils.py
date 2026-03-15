import requests
from config.settings import TMDB_API_KEY
import pandas as pd

def get_poster_url(tmdb_id):
    """Devuelve la URL del poster de una película por su TMDB ID"""
    if pd.isna(tmdb_id):
        return None

    url = f"https://api.themoviedb.org/3/movie/{int(tmdb_id)}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}"
    }

    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return None

    data = r.json()
    poster_path = data.get("poster_path")
    if not poster_path:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster_path}"
