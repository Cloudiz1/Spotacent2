# from CLI.imports import *
from CLI.commands.clear import *
from CLI.commands.quit import *
from CLI.commands.help import *
from CLI.commands.add import *
from CLI.commands.play import *
from CLI.commands.get import *
from CLI.commands.set import *
from CLI.commands.pause import *
from CLI.commands.unpause import *
from CLI.commands.debug import *
from CLI.commands.skip import *
from CLI.commands.remove import *

import _globals

def execute_command(Cmd):
    match Cmd.parent_command:
        case "help":
            cmd_help(Cmd)
        case "clear":
            cmd_clear()
        case "quit":
            cmd_quit()
        case "add":
            cmd_add(Cmd)
        case "play":
            cmd_play(Cmd)
        case "get":
            cmd_get(Cmd)
        case "set":
            cmd_set(Cmd, _globals.currently_playing)
        case "pause":
            cmd_pause(_globals.currently_playing)
        case "unpause":
            cmd_unpause(_globals.currently_playing)
        case "skip":
            cmd_skip(_globals.currently_playing)
        case "debug":
            cmd_debug()
        case "remove":
            cmd_remove(Cmd)