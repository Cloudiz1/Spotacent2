import CLI.cli_filter as cli_filter
from CLI.parse_input import *
from CLI.execute_command import *

def process_input(input_command):
    
    # empty string
    if input_command.replace(" ", "") == "":
        return
    
    Command = Parsed_Command(input_command)
    
    if cli_filter.is_command_valid(Command) == False:
        return
    
    execute_command(Command)