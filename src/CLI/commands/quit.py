import _globals

def cmd_quit():
    _globals.playing_playlist = False
    exit(0)