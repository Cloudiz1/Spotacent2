import pygame.mixer as mixer
import json
import _globals

class Song:
    def __init__(self, path):
        mixer.init()
        self.song = mixer.Sound(path)
        mixer.fadeout(0)
        
        # reads and applies settings
        settings = read_settings_file(_globals.settings_path)
        self.set_volume(float(settings["volume"]))
        
    def play(self):
        mixer.Sound.play(self.song)
    
    def pause(self):
        mixer.pause()
        print("Song paused")
        
    def unpause(self):
        print("Unpausing song...")
        mixer.unpause()
        
    def set_volume(self, volume):
        mixer.Sound.set_volume(self.song, volume)
        
    def is_playing(self):
        return mixer.get_busy()
    
    def stop(self):
        mixer.stop()
    
def update_settings_file(key, value):
    settings = dict
    with open(_globals.settings_path, "r") as f:
        settings = json.load(f)
        settings[key] = value
        
    with open(_globals.settings_path, "w") as f: 
        json.dump(settings, f, sort_keys=True, indent=4)
        
def read_settings_file(path):
    with open (_globals.settings_path, "r") as f:
        return json.load(f)
    
    
# update_volume_json(0.5)
# song = Song("./songs/Never_Gonna_Give_You_Up_by_Rick_Astley.wav")
# song.play()
# input()
# song.change_volume(.1)
# input()