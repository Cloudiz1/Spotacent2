import json
import playlists

def cmd_remove(Cmd):
    if Cmd.args[0] == "playlist":
        playlists.delete_playlist(Cmd.args[1])
        return
    
    try:
        path = playlists.get_playlist_path(Cmd.args[1])
        songs = playlists.get_playlist(path)

        del(songs["songs"][int(Cmd.args[0]) - 1])
        
        with open(path, "w") as f:
            json.dump(songs, f, sort_keys=True, indent=4)
                
    except:
        print("don't do that man :(")