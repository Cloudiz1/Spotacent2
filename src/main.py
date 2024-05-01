from playlists import *
from Song import *
import CLI.cli 
from CLI.commands.clear import cmd_clear
import os

try:
    os.mkdir("playlists")
    os.mkdir("songs")
except:
    pass

cmd_clear()
print("Welcome to Spotacent (my ripoff of spotify)!")

while True:
    CLI.cli.process_input(input("> "))