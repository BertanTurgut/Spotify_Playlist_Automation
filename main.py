import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secret

# Suitable scope for the purpose
scope = 'playlist-modify-public'
# Authentication and creating Spotipy object
spotipy_object = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secret.client_id, client_secret=secret.client_secret, redirect_uri=secret.redirect_url, scope=scope))

# Collect current user's dictionary
user_dictionary = spotipy_object.current_user()
user_id = user_dictionary['id']


