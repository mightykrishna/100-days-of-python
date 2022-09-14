from http import client
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
client1_id="1e16d9de694c4f10991a2bd376dea0b2"
client1_secret="49a9c90778fc4ea48f05e2a7e269c07b"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback ",
        client_id="1e16d9de694c4f10991a2bd376dea0b2",
        client_secret="49a9c90778fc4ea48f05e2a7e269c07b",
        show_dialog=True,
        cache_path="token.txt"
    )
)
#user_id = sp.current_user()["id"]