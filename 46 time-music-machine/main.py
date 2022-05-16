import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = "YOUR SPOTIFY CLIENT ID"
CLIENT_SECRET = "YOUR SPOTIFY CLIENT SECRET"

# Scrapping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
response = requests.get(f"{BILLBOARD_URL}/{date}")
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(name="h3", class_="a-no-trucate")
song_names = [" ".join(title.getText().split()) for title in titles]

# Spotify Auth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
songs_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song}, year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a private playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Adding songs found to the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)
