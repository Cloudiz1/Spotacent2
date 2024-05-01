import os

def cmd_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return