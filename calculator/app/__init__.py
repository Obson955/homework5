from calculator.commands import CommandHandler
#from calculator.commands.discord import DiscordCommand
from calculator.commands.exit import ExitCommand
from calculator.commands.goodbye import GoodbyeCommand
from calculator.commands.greet import GreetCommand
from calculator.commands.menu import MenuCommand
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand 

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()


    def start(self):
        # Register commands here
        print("Welcome to the calculator!")
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        #self.command_handler.register_command("discord", DiscordCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
       
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command("menu")
            self.command_handler.execute_command(input(">>> ").strip())


