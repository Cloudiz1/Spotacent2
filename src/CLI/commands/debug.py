import _globals
import threading

# this stops the playlist but the song itself continues to play
def cmd_debug():
    for thread in threading.enumerate():
        print(thread.name)