import os
import json

def get_playlist_path(playlist_name):
    return (f"./playlists/{playlist_name}.json")
    
def create_playlist(name):
    playlist_path = get_playlist_path(name)
    
    if os.path.exists(playlist_path):
        print("Playlist already exists")
        
    else:
        with open(playlist_path, "w") as f:
            json.dump({"songs": []}, f, sort_keys=True, indent=4)
            
        print(f'Created playlist with name: "{name}"')
        
def delete_playlist(name):
    os.remove(get_playlist_path(name))
        
def add_song(playlist_name, song):
    playlist_path = get_playlist_path(playlist_name)
    playlist = get_playlist(playlist_path)
    
    formatted_song_name = song.replace("_", " ")
    
    if song in playlist["songs"]:
        print(f"{formatted_song_name} is already in playlist")
        return
    
    with open(playlist_path, "w") as f:
        playlist["songs"].append(song)
        json.dump(playlist, f, sort_keys=True, indent=4)
        
    print(f'Added {formatted_song_name} to {playlist_name}')
        
def get_playlist(playlist_path):
    with open(playlist_path, "r") as f:
        return json.load(f)
    
def get_songs(playlist_name):
    playlist_path = get_playlist_path(playlist_name)
    playlist = get_playlist(playlist_path)
    
    songs_in_playlist = playlist["songs"]
    returned_songs = []
    for song in songs_in_playlist:
        returned_songs.append(song)
        
    return returned_songs
    
# delete_playlist("test")

# create_playlist("test")
# add_song("test", "test5")

# get_songs("test")