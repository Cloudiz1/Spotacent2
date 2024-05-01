import _globals

def cmd_skip(current_song):
    _globals.currently_playing = None
    current_song.stop()