class Parsed_Command:
    def __init__(self, input_command):
        self.command = input_command.strip().split()
        self.length = len(self.command)
        self.parent_command = self.command[0]
        
        self.args = []
        for counter, term in enumerate(self.command):
            if counter != 0:
                self.args.append(term)