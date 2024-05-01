defined_commands = ["help", "play", "clear", "quit", "add", "get", "set", "pause", "unpause", "debug", "skip", "remove"]

# (Minimum args, Maximum args)
num_args_allowed = {
    "help": (None, 1),
    "play": (2, 2), # song or playlist
    "clear": (None, 0),
    "quit": (None, None),
    "add": (2, 2),
    "get": (1, 2),
    "set": (2, 2),
    "pause": (0, 0),
    "unpause": (0, 0),
    "skip": (0, 0),
    "debug": (0, 999),
    "remove": (2, 2)
}

help_table = {
    "help": {
        "syntax": 'help <command name>: gives the description as well as the syntax of a desired command || help syntax: lists the syntax of all commands',
        "description": 'gives extra information for commands; use "help syntax" to see syntax of commands'
    },
    
    "play": {
        "syntax": 'play song <song number (found by using get songs)>: plays a song || play playlist <playlist name or number>: plays a playlist',
        "description": "plays a song or a playlist"
    },
    
    "clear": {
        "description": "clears the console"
    },
    
    "quit": {
        "description": "exits the program"
    },
    
    "add": {
        "description": "adds either a song or a playlist",
        "syntax": 'add <song url> <playlist name>: adds a song to a playlist || add playlist <name>: creates a new playlist'
    },
    
    "get": {
        "description": "returns things including: installed songs, named playlists, the songs in a playlist, or more",
        "syntax": "get songs: gets all installed songs || get playlists: gets named playlists || get songs <playlist name>: gets all songs in a playlist || get setting <setting>" 
    },

    "set": {
        "description": "changes a setting",
        "syntax": "set volume <number 1-100 inclusive> || set loop <bool> || set shuffle <bool>"
    },

    "pause": {
        "description": "pauses the current song"
    },

    "unpause": {
        "description": "unpauses the current song"
    },
    
    "stop": {
        "description": "stops playing songs"
    },
    
    "remove": {
        "description": "removes either a song from a playlist or an entire playlist",
        'syntax': 'remove playlist <playlist name> || remove <song number (found with "get songs <playlist name>")> <playlist name>'
    }
}