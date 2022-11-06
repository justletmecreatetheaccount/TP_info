class Interface:
    def __init__(self, name):
        self.name = name
        self.load_file = ""
        self.work_file = ""
        self.commands = {}
        self.args = {}

    def register_command(self, command_name, command):
        self.commands[command_name] = (command)

    def execute_command(self, entry, param):
        fnct = self.commands[entry]
        fnct(self, param)

    def register_entry(self):
        entry = input(f"What do you want this machine {self.name} to do ? :: ")
        entry = entry.lower()
        entry = entry.split(" ")
        return entry

    def run(self):
        while True:
            try :

                entry = self.register_entry()
                command = entry[0]
                print (command)
                param = entry[1:]
                print (param)
                if command == "exit":
                    exit = input("Do you whish to exit the program [Y/N] :: ")
                    exit.lower()
                    if exit == "y":
                        break
                    else:
                        continue

                if command not in self.commands.keys():
                    print ("Command not found ... ")
                    continue

                self.execute_command(command, param)
            except :
                print ("An unforseen even has happend ... ")
                continue
def help(Interface : Interface, param):
    print("Type 'exit' to exit the program")

def sum_(param):
    sum = 0
    for i in param:
        sum += int (i)
    return sum

def sum(Interface : Interface, param):
    print (sum_(param))

def average(Interface : Interface, param):
    print (sum_(param) / len(param))
    return sum_(param) / len(param)

def file_selection(Interface : Interface, param):
    Interface.load_file = param[0]
    print ("File loaded I hope ... ")

def words(Interface : Interface, param):
    Interface.work_file = Interface.load_file
    print("Work file set ...")


def info(Interface : Interface, param):
    with open(Interface.load_file) as file:
        data = file.read()
        n_c = len(data)
        n_l = len(data.split("\n"))
    print (n_c, "characters")
    print (n_l, "lines")


def search(Interface : Interface, param):
    with open(Interface.work_file) as file:
        data = file.read()
        print(f"{param[0]} is present in dictionnary") if param[0] in data else print ("Not found ... ")
        


Interface_1 = Interface(input("What would you like to call me ? :: "))
Interface_1.register_command("help", help)
Interface_1.register_command("average", average)
Interface_1.register_command("sum", sum)
Interface_1.register_command("file", file_selection)
Interface_1.register_command("words", words)
Interface_1.register_command("info", info)
Interface_1.register_command("search", search)
Interface_1.run()