import os
import playlists as pls
import Song
import _globals

def cmd_get(Cmd): # get songs || get playlists || get songs <playlist> || 
    
    if Cmd.args[0] == "songs" and len(Cmd.args) == 1: # get installed songs
        installed_songs = get_installed_songs()
        formatted_songs = format_song_names(installed_songs)
        for song in formatted_songs:
            print(song)
            
    elif Cmd.args[0] == "songs" and len(Cmd.args) == 2: # get songs in a playlist
        queried_playlist = Cmd.args[1]
        songs = pls.get_songs(queried_playlist)
        
        formatted_songs = format_song_names(songs)
        
        for song in formatted_songs:
            print(song)
            
    elif Cmd.args[0] == "playlists" and len(Cmd.args) == 1: # get playlists
        playlists = get_playlists()
        for iterator, playlist in enumerate(playlists):
            print(str(iterator + 1) + ". " + playlist)
            
    elif Cmd.args[0] == "setting":
        if len(Cmd.args) != 2:
            print("Invalid number of parameters")
            return
        
        settings = Song.read_settings_file(_globals.settings_path)
        try:
            print(f'{Cmd.args[1]}: {settings[Cmd.args[1]]}')
            return
        
        except:
            print(f"{Cmd.args[1]} is not a valid setting")
            
    elif Cmd.args[0] == "settings":
        settings = Song.read_settings_file(_globals.settings_path)
        
        for setting in settings:
            print(f"{setting}: {settings[setting]}")
        
def get_installed_songs():
    returned_songs = []
    installed_songs = os.scandir("./songs")
    for song in installed_songs:
        returned_songs.append(song.name.lower())
        
    returned_songs.sort()
        
    return returned_songs

def format_song_names(songs):
    for iterator, song_name in enumerate(songs):
        songs[iterator] = str(iterator + 1) + ". " + song_name # adds numbers
        songs[iterator] = songs[iterator].replace("_", " ") # removes whitespace
        songs[iterator] = songs[iterator].replace(".wav", "")
        
    return songs
        
def get_playlists():
    playlists = os.scandir("./playlists")
    
    returned_playlists = []
    for playlist in playlists:
        returned_playlists.append(playlist.name)
        
    returned_playlists.sort()
    
    formatted_playlist = []
    
    for playlist in returned_playlists:
        formatted_playlist.append(playlist.replace(".json", ""))
        
    return formatted_playlist