import CLI.lookup_tables as tbl

def cmd_help(Cmd):    
    
    if len(Cmd.args) == 0 or "syntax" in Cmd.args: # help || help syntax
        
        # sorts keys
        sorted_keys = []
        for key, value in tbl.help_table.items():
            sorted_keys.append(key)

        sorted_keys.sort()
    
        for key in sorted_keys:
            print(f"{key}: {tbl.help_table[str(key)]["description"]}")
            
            if "syntax" in Cmd.args and "syntax" not in tbl.help_table[str(key)]:
                print("")
            
            if "syntax" in Cmd.args and "syntax" in tbl.help_table[str(key)]: # if we are printing syntax as well as definition
                if print_syntax(key) == False:
                    return False
                print("")
                
        return True
            
            
    elif len(Cmd.args) == 1: # help <name>
        
        if Cmd.args[0] not in tbl.defined_commands:
            print("Command does not exist.")
            return False
        
        key = Cmd.args[0]
        print(tbl.help_table[key]["description"])
        if print_syntax(key) == False:
            return False
            
        return True
        
def print_syntax(key):
    if key not in tbl.defined_commands:
        print(f'"{key}" command does not exist')
        return False
    
    syntax_list = tbl.help_table[str(key)]["syntax"].split(" || ")
    
    for cmd in syntax_list:
        print(cmd)
        
        