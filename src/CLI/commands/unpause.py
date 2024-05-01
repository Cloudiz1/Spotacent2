def cmd_unpause(current_song):
    if current_song != None:
        current_song.unpause()
        return
        
    print("No song currently playing.")