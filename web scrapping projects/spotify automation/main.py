from urllib import response
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
client_id="1e16d9de694c4f10991a2bd376dea0b2"
client_secret="49a9c90778fc4ea48f05e2a7e269c07b"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
print(song_names)
