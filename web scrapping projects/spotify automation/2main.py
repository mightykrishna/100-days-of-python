from http import client
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
client_id="1e16d9de694c4f10991a2bd376dea0b2"
client_secret="49a9c90778fc4ea48f05e2a7e269c07b"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()[client_id]

OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'

date=input("what date do you want to travel to? in yyyy-mm-dd\n")

response=requests.get(url="https://www.billboard.com/charts/hot-100/"+date)
#print(response.status_code)
songs=BeautifulSoup(response.text, "html.parser")

allSongs=songs.find_all('h3', id="title-of-a-story")

songNames=[x.get_text().replace("\n", "").replace("\t","") for x in allSongs]

songNames=list(dict.fromkeys(songNames))
songNames.remove('Songwriter(s):')
songNames.remove('Producer(s):')
songNames.remove('Imprint/Promotion Label:')

songNames=songNames[3:102]
with open("songs.txt",mode="w") as file:
    for song in songNames:
        file.write(f"{song}\n")
print(songNames)