import playlists
import os

from yttwav import *

def cmd_add(Cmd): # add playlist <name> || add <song (url)> <playlist>
    
    if Cmd.args[0] == "playlist": # creating playlist
        playlist_name = Cmd.args[1]
        playlists.create_playlist(playlist_name)
        
    # add <song> <playlist>
    
    else:
        
        existing_playlists = []
        for playlist in os.scandir("./playlists"):
            existing_playlists.append(playlist.name) 
            
        target_playlist = Cmd.args[1]
            
        if target_playlist + ".json" in existing_playlists: 
            added_song = convert_to_wav(Cmd.args[0])
            
            if added_song == None:
                return

            playlists.add_song(target_playlist, added_song)
            
        else:
            print("Playlist does not exist.")
            return 
    
    