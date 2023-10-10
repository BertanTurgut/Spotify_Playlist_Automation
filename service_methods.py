import spotipy

def createPlaylist(spotipy_client: spotipy, name, public=True, collaborative=False, description=''):
    user_dictionary = spotipy_client.current_user()
    user_id = user_dictionary["id"]
    spotipy_client.user_playlist_create(user_id, name, public, collaborative, description)
    print("Playlist \"" + name + "\" is created.")

def extractTracksByArtistGenre(spotipy_client: spotipy, playlist_id, genre):
    extracted_ids = []
    playlist_dictionary = spotipy_client.playlist(playlist_id)
    for item in playlist_dictionary["tracks"]["items"]:
        track = item["track"]
        for artist in track["artists"]:
            artist_genres = spotipy_client.artist(artist["id"])["genres"]
            for genre_ in artist_genres:
                if genre_ == genre:
                    extracted_ids.append(track["id"])
    print("Extraction completed.")
    return extracted_ids

def getPlaylistID(spotipy_client: spotipy, playlist_name):
    user_playlists = spotipy_client.current_user_playlists()["items"]
    for playlist in user_playlists:
        if playlist["name"] == playlist_name:
            print(playlist["id"] + " -> " + "Playlist: \"" + playlist_name + "\"")
            return playlist["id"]

def getPlaylistName(spotipy_client: spotipy, playlist_id):
    user_playlists = spotipy_client.current_user_playlists()["items"]
    for playlist in user_playlists:
        if playlist["id"] == playlist_id:
            print("Playlist: \"" + playlist["name"] + "\"" + " <- " + playlist_id)
            return playlist["name"]

def addTracksToPlaylist(spotipy_client: spotipy, playlist_id, track_id_list):
    track_uri_list = []
    for id_ in track_id_list:
        track_uri_list.append(spotipy_client.track(id_)["uri"])
    spotipy_client.playlist_add_items(playlist_id, track_id_list)
    print("Tracks are added to playlist \"" + getPlaylistName(spotipy_client, playlist_id) + "\".")