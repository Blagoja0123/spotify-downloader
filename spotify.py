import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv.main import load_dotenv

load_dotenv()


print(os.environ.get('CLIENT_ID'), os.environ.get('CLIENT_SECRET'))

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id = os.environ.get('CLIENT_ID'),
    client_secret = os.environ.get('CLIENT_SECRET')
))

# song helper datatype
class song:

    title: str
    artist: str

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

# get songs and playlist name using the spotify API

def set_song_list(playlist_link):

    song_list = set()
    playlist_link = playlist_link.split('/')
    playlist_id = playlist_link[len(playlist_link)-1]
    playlist_id = playlist_id.split('?')
    playlist_id = playlist_id[0]
    result = sp.playlist(playlist_id)
    playlist_name = result['name'] # type: ignore
    for item in result['tracks']['items']: # type: ignore
        track = item['track']
        artist = item['track']['artists'][0]['name']
        print(track['name'] + ' - ' + artist)
        song_list.add(song(track['name'], artist))
    return (song_list, playlist_name) 
