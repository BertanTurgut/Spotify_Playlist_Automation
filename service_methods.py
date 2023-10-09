import spotipy
from spotipy.oauth2 import SpotifyOAuth

def createPlaylist(spotipy_client: spotipy, name, public=True, collaborative=False, description=''):
    user_dictionary = spotipy_client.current_user()
    user_id = user_id = user_dictionary['id']
    spotipy_client.user_playlist_create(user_id, name, public, collaborative, description)
