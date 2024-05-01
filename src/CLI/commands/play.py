from Song import *
import playlists as pls
import CLI.commands.get as get
import numpy as np
import _globals
import threading

def cmd_play(Cmd): # play <song name or number> || play <playlist name>
    
    if Cmd.args[0] == "song":
        play_specific_song(Cmd)
    elif Cmd.args[0] == "playlist":
        for thread in threading.enumerate():
            if thread.name == "playlist_thread":
                print("A playlist is already playing, stop it first.")
                return
        
        playlist_thread = threading.Thread(target=play_playlist, name="playlist_thread", args=[Cmd])
        playlist_thread.start()

def get_song_filepath(name):
    filepath = "./songs/" + name
    return filepath

def play_song(path):
    current_song = Song(path)
    current_song.play()
    return current_song

def play_specific_song(Cmd):
    songid = int(Cmd.args[1]) # tests if args[0] can be int, if it can, it means to play a specific song
    
    installed_songs = get.get_installed_songs()
    
    if songid < 1:
        print("index too small")
        return None
    
    if songid > len(installed_songs):
        print("index too large")
        return None
    
    queried_song_name = installed_songs[songid - 1] # gets song name and path
    queried_song_path = get_song_filepath(queried_song_name)
    
    _globals.currently_playing = play_song(queried_song_path)

# this needs to be redone to allow threading
def play_playlist(Cmd):
    # check if playlist exists
    playlist_name = Cmd.args[1]
    if playlist_name not in get.get_playlists():
        
        try:
            playlist_name = get.get_playlists()[int(Cmd.args[1]) - 1]
        except:
            print("Playlist does not exist.")
            return None
    
    _globals.playing_playlist = True
    settings = read_settings_file(_globals.settings_path)

    queued_songs = populate_queue(playlist_name, settings)     
    
    while _globals.playing_playlist == True: 
        if _globals.currently_playing == None or _globals.currently_playing.is_playing() == False: # when a song is not playing
            
            # if queue is empty
            if len(queued_songs) == 0:
                if settings["loop"] == True:
                    queued_songs = populate_queue(playlist_name, settings)
                else:
                    break
            
            song_path = get_song_filepath(queued_songs.pop())
            _globals.currently_playing = play_song(song_path + ".wav")
    
    _globals.playing_playlist = False
            
def populate_queue(playlist_name, settings):
    queued_songs = pls.get_songs(playlist_name)
    
    if settings["shuffle"] == True:
        np.random.shuffle(queued_songs)       
        
    return queued_songs 