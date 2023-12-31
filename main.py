import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secret
import service_methods

# Suitable scope for the purpose
scope = "playlist-modify-public"
# Authentication and creating Spotipy object
spotipy_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secret.client_id, client_secret=secret.client_secret, redirect_uri=secret.redirect_url, scope=scope))

service_methods.createPlaylist(spotipy_client, "Test Playlist")
hashtag_id = service_methods.getPlaylistID(spotipy_client, "#")
test_id = service_methods.getPlaylistID(spotipy_client, "Test Playlist")
extracted_ids = service_methods.extractTracksByArtistGenre(spotipy_client, hashtag_id, "rock")
service_methods.addTracksToPlaylist(spotipy_client, test_id, extracted_ids)