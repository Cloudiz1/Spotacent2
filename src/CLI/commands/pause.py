def cmd_pause(current_song):
    if current_song != None:
        current_song.pause()
        return
        
    print("No song currently playing.")