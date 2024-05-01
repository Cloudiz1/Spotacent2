import CLI.lookup_tables as tbl 

def is_command_valid(Command):    
    if Command.parent_command not in tbl.defined_commands:
        print("Command not found")
        return False
        
    # return tuple of (min # args, max # args)
    num_args_allowed = tbl.num_args_allowed[Command.parent_command]
    min_args = num_args_allowed[0]
    max_args = num_args_allowed[1]
      
    if min_args == None: # too few args
        pass
    elif len(Command.args) < min_args:
        print(f'Too few arguements.')
        return False
        
    if max_args == None: # too many args
        pass
    elif len(Command.args) > max_args:
        print(f'Too many arguements.')
        return False
        