import Song

def cmd_set(Cmd, current_song):
    # updates volume
    if Cmd.args[0] == "volume":
        try:
            global new_volume
            new_volume = float(Cmd.args[1])
        except:
            print("Volume can only be set to an integer.")
            return
        
        if new_volume > 100:
            new_volume = 100
        elif new_volume < 0:
            new_volume = 0

        new_volume /= 100
        
        Song.update_settings_file("volume", new_volume)

        if current_song != None:
            current_song.set_volume(new_volume)
            
        print(f"Volume set to {new_volume * 100}")
        
    # updates boolean settings such as shuffle or loop
    if Cmd.args[0] in ["shuffle", "loop"]:
        updated_setting = Cmd.args[0]
        updated_value = Cmd.args[1].lower()
        
        if updated_value == "true":
            Song.update_settings_file(updated_setting, True)
            
        elif updated_value == "false":
            Song.update_settings_file(updated_setting, False)
            
        else:
            print(f'The setting "{updated_setting}" only accepts the parameters "true" or "false" (case insensitive)')
            return
        
        print(f"Set {updated_setting} to {updated_value}")